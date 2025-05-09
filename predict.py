import tensorflow as tf
import numpy as np
from PIL import Image
import os

class WasteClassifier:
    def __init__(self, model_path='waste_classifier.h5'):
        self.model = tf.keras.models.load_model(model_path)
        self.material_classes = ['plastic', 'paper', 'glass', 'metal', 'organic', 'hazardous']
        self.contam_classes = ['clean', 'food_residue', 'chemical_stains']
    
    def preprocess_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) / 255.0
        return img_array
    
    def predict(self, image_path):
        img_array = self.preprocess_image(image_path)
        material_pred, contam_pred = self.model.predict(img_array)
        
        material_class = self.material_classes[np.argmax(material_pred)]
        material_conf = np.max(material_pred)
        contam_class = self.contam_classes[np.argmax(contam_pred)]
        contam_conf = np.max(contam_pred)
        
        return {
            'material': material_class,
            'material_confidence': float(material_conf),
            'contamination': contam_class,
            'contamination_confidence': float(contam_conf)
        }

# Example usage
if __name__ == '__main__':
    classifier = WasteClassifier()
    
    # Test on a sample image
    test_image = 'data/train/plastic/clean/image_001.jpg'  # Replace with your image
    if os.path.exists(test_image):
        prediction = classifier.predict(test_image)
        print("\nPrediction Results:")
        print(f"Material: {prediction['material']} ({prediction['material_confidence']:.2%})")
        print(f"Contamination: {prediction['contamination']} ({prediction['contamination_confidence']:.2%})")
    else:
        print(f"Test image not found at {test_image}")