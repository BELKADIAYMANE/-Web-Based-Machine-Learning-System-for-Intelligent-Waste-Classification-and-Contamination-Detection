import os
import requests

# Your URLs
urls = [
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

# Create folder
folder = 'your_images'
os.makedirs(folder, exist_ok=True)

# Download each image
for url in urls:
    filename = os.path.join(folder, url.split("/")[-1])
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

print("All images downloaded into 'your_images/' folder!")
