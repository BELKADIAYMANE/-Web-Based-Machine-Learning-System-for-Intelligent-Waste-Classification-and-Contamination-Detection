import os
import requests
import random
from PIL import Image
from io import BytesIO

# Define categories
material_types = ['plastic', 'paper', 'glass', 'metal', 'organic', 'hazardous']
contamination_levels = ['clean', 'food_residue', 'chemical_stains']

# Create directory structure
for material in material_types:
    for contamination in contamination_levels:
        os.makedirs(f'data/train/{material}/{contamination}', exist_ok=True)

# Image URLs (fixed format)
image_urls = [
    "https://farm66.staticflickr.com/65535/33978196618_632623b4fc_z.jpg",
    "https://farm66.staticflickr.com/65535/33978196618_e30a59e0a8_o.png",
    "https://farm66.staticflickr.com/65535/47803331152_19beae025a_z.jpg",
    "https://farm66.staticflickr.com/65535/47803331152_ee00755a2e_o.png",
    "https://farm66.staticflickr.com/65535/40888872753_631ab0f441_z.jpg",
    "https://farm66.staticflickr.com/65535/40888872753_08ffb24902_o.png",
    "https://farm66.staticflickr.com/65535/47803331492_b8c0e5aafe_z.jpg",
    "https://farm66.staticflickr.com/65535/47803331492_0e1085ca55_o.png",
    "https://farm66.staticflickr.com/65535/33978199868_1bc379170a_z.jpg",
    "https://farm66.staticflickr.com/65535/33978199868_88ee160849_o.png",
    "https://farm66.staticflickr.com/65535/33978200068_9cd0d8f6a2_z.jpg",
    "https://farm66.staticflickr.com/65535/33978200068_c6eed416ac_o.png",
    "https://farm66.staticflickr.com/65535/47803332212_0ff13e5eb1_z.jpg",
    "https://farm66.staticflickr.com/65535/47803332212_af8cfa9704_o.png",
    "https://farm66.staticflickr.com/65535/33978202498_ef6d507616_z.jpg",
    "https://farm66.staticflickr.com/65535/33978202498_effbca58ef_o.png",
    "https://farm66.staticflickr.com/65535/47803335992_ebcc4e3932_z.jpg",
    "https://farm66.staticflickr.com/65535/47803335992_9c58683430_o.png",
    "https://farm66.staticflickr.com/65535/47855505601_a81c3ba8de_z.jpg",
    "https://farm66.staticflickr.com/65535/47855505601_f75a430abc_o.png",
    "https://farm66.staticflickr.com/65535/40888877173_734cec88e1_z.jpg",
    "https://farm66.staticflickr.com/65535/40888877173_855795c875_o.png"
]

# Create CSV file for tracking labels
csv_file = open('data/random_labels.csv', 'w')
csv_file.write("filename,material,contamination\n")

for i, url in enumerate(image_urls):
    try:
        # Fix URL format if needed
        if url.startswith('https:/') and not url.startswith('https://'):
            url = url.replace('https:/', 'https://')
        
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        
        # Get random labels
        material = random.choice(material_types)
        contamination = random.choice(contamination_levels)
        
        # Save with appropriate naming
        ext = os.path.splitext(url)[1] or '.jpg'
        filename = f"image_{i:03d}{ext}"
        save_path = f"data/train/{material}/{contamination}/{filename}"
        
        img.save(save_path)
        csv_file.write(f"{filename},{material},{contamination}\n")
        
        print(f"Saved {filename} as {material} with {contamination}")
        
    except Exception as e:
        print(f"Error processing {url}: {e}")

csv_file.close()
print("\nAll images downloaded and randomly labeled!")
print("Label information saved to data/random_labels.csv")