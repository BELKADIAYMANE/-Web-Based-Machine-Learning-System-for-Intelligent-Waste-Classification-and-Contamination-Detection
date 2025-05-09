import os
import requests
from PIL import Image
from io import BytesIO

# Create directory structure for all possible combinations
material_types = ['plastic', 'paper', 'glass', 'metal', 'organic', 'hazardous']
contamination_levels = ['clean', 'food_residue', 'chemical_stains']

for material in material_types:
    for contamination in contamination_levels:
        os.makedirs(f'data/train/{material}/{contamination}', exist_ok=True)

# All image URLs
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

# Download all images to a temporary directory first
os.makedirs('data/temp', exist_ok=True)

for i, url in enumerate(image_urls):
    try:
        # Fix URL format if needed
        if url.startswith('https:/'):  # Some URLs had incorrect format
            url = url.replace('https:/', 'https://')
            
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        
        # Save with sequential numbering
        file_extension = os.path.splitext(url)[1] or '.jpg'  # Get extension or default to jpg
        img.save(f'data/temp/image_{i:03d}{file_extension}')
        print(f"Downloaded: {url}")
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("\nAll images downloaded to data/temp directory.")
print("Now you need to manually move each image to the appropriate subfolder:")
print("Example: mv data/temp/image_001.jpg data/train/plastic/clean/")
print("Based on the actual material type and contamination level of each image.")

# Create a CSV file template for labeling
import csv

with open('data/image_labels.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'material', 'contamination'])
    
    for i in range(len(image_urls)):
        writer.writerow([f'image_{i:03d}.jpg', '', ''])

print("\nCreated a labeling template at data/image_labels.csv")
print("Fill in the material and contamination columns for each image:")
print("- Material: plastic, paper, glass, metal, organic, hazardous")
print("- Contamination: clean, food_residue, chemical_stains")