from PIL import Image
import tkinter as tk
from tkinter import filedialog

def load_image(image_path):
    img = Image.open(image_path)
    return img

def encrypt_image(img):
    pixels = img.load()  # Get pixel data
    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
                pixels[x, y] = ((r + 50) % 256, (g + 50) % 256, (b + 50) % 256)
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                pixels[x, y] = ((r + 50) % 256, (g + 50) % 256, (b + 50) % 256, a)  # Keep alpha

    return img

def decrypt_image(img):
    pixels = img.load()  # Get pixel data
    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
                pixels[x, y] = ((r - 50) % 256, (g - 50) % 256, (b - 50) % 256)
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                pixels[x, y] = ((r - 50) % 256, (g - 50) % 256, (b - 50) % 256, a)  # Keep alpha

    return img

def save_image(img, output_path):
    img.save(output_path)

def open_file():
    file_path = filedialog.askopenfilename()
    img = load_image(file_path)
    return img

def encrypt_and_save():
    img = open_file()
    encrypted_img = encrypt_image(img)
    save_image(encrypted_img, "encrypted_image.png")

def decrypt_and_save():
    img = open_file()
    decrypted_img = decrypt_image(img)
    save_image(decrypted_img, "decrypted_image.png")

# Create user interface
root = tk.Tk()
root.title("Image Encryption Tool")

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_and_save)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_and_save)
decrypt_button.pack()

root.mainloop()
