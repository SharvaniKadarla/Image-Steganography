import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import random
from PIL import ImageTk, Image

# Encode the secret text into the cover image
def encode_text(cover_img, secret_text):
    secret_text_binary = ''.join(format(ord(c), '08b') for c in secret_text)
    secret_text_binary += '1111111111111110'  # End of Text marker
    text_index = 0
    for i in range(cover_img.shape[0]):
        for j in range(cover_img.shape[1]):
            for k in range(cover_img.shape[2]):
                if text_index < len(secret_text_binary):
                    # Modify the last bit of the cover image pixel value
                    binary_value = format(cover_img[i][j][k], '08b')
                    modified_binary_value = binary_value[:-1] + secret_text_binary[text_index]
                    cover_img[i][j][k] = int(modified_binary_value, 2)
                    text_index += 1
                else:
                    break
            if text_index >= len(secret_text_binary):
                break
    if text_index < len(secret_text_binary):
        messagebox.showwarning("Steganography", "Insufficient cover image capacity to hide the entire message")

def resize_images(cover_img, secret_img):
    # Get the dimensions of the cover image
    cover_height, cover_width, _ = cover_img.shape
    # Resize the secret image to match the dimensions of the cover image
    secret_img = cv2.resize(secret_img, (cover_width, cover_height))
    return cover_img, secret_img

# Encode the secret image into the cover image
def encode_image(cover_img, secret_img):
    # Check if the dimensions of cover_img and secret_img are the same
    if cover_img.shape != secret_img.shape:
        messagebox.showerror("Error", "Cover image and secret image dimensions do not match")
        return
    for i in range(secret_img.shape[0]):
        for j in range(secret_img.shape[1]):
            for l in range(3):
                if i >= cover_img.shape[0] or j >= cover_img.shape[1]:
                    # Skip if the indices are out of bounds for cover_img
                    continue
                # v1 and v2 are 8-bit pixel values of img1 and img2 respectively
                v1 = format(cover_img[i][j][l], '08b')
                v2 = format(secret_img[i][j][l], '08b')
                # Taking 4 MSBs of each image
                v3 = v1[:4] + v2[:4]
                cover_img[i][j][l] = int(v3, 2)


# Decode the secret message from the steganographic image-text
def decode_text():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
    if filepath:
        img = cv2.imread(filepath)
        binary_message = ""
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                for k in range(img.shape[2]):
                    binary_value = format(img[i][j][k], '08b')
                    binary_message += binary_value[-1]
        end_index = binary_message.find('1111111111111110')
        if end_index != -1:
            secret_text_binary = binary_message[:end_index]
            secret_text = ""
            for i in range(0, len(secret_text_binary), 8):
                byte = secret_text_binary[i:i + 8]
                secret_text += chr(int(byte, 2))
            messagebox.showinfo("Decoded Message", "Secret Message:\n" + secret_text)
        else:
            messagebox.showwarning("Decoding Error", "No hidden message found in the image")

# Decode the secret message from the steganographic image image
def decode_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
    if filepath:
        img = cv2.imread(filepath)
        width = img.shape[0]
        height = img.shape[1]
    # img2 is blank image
        img2 = np.zeros((width, height, 3), np.uint8)
        for i in range(width):
            for j in range(height):
                for l in range(3):
                    v1 = format(img[i][j][l], '08b')
                    v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                    # Appending data to img2
                    img2[i][j][l]= int(v3, 2)
    # This is the image produced from the encrypted image
        cv2.imwrite('pic3_re.png', img2)
        img = Image.open('pic3_re.png')
        img.show() # Shows the image in a new window

# Create the main window
window = tk.Tk()
window.title("STEGANOGRAPHY")
window.geometry("500x300")
window.resizable(False, False)
window.configure(padx=20, pady=20)

# Text in Image Steganography
def text_in_image():
    # Create a new top-level window for text in image steganography
    text_in_image_window = tk.Toplevel(window)
    text_in_image_window.title("TEXT IN IMAGE - Steganography")
    text_in_image_window.geometry("500x300")
    # Function to select the cover image and secret text
    def select_images():
        # Open file dialogs to select the cover image and secret text file
        cover_filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        text_filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if cover_filepath and text_filepath:
            # Read the cover image and secret text
            cover_img = cv2.imread(cover_filepath)
            with open(text_filepath, 'r') as file:
                secret_text = file.read()
            # Embed the secret text into the cover image
            stego_img = np.copy(cover_img)
            encode_text(stego_img, secret_text)
            # Save the steganographic image
            save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if save_filepath:
                cv2.imwrite(save_filepath, stego_img)
                messagebox.showinfo("Steganography", "Image encrypted and saved successfully")
    # Create a button to select the cover image and secret text
    select_images_button = tk.Button(text_in_image_window, text="Select Image and Text File", command=select_images )
    select_images_button.place(x=170,y=120)

# Image in Image Steganography
def image_in_image():
    # Create a new top-level window for image in image steganography
    image_in_image_window = tk.Toplevel(window)
    image_in_image_window.title("IMAGE IN IMAGE - Steganography")
    image_in_image_window.geometry("500x300")
    # Function to select the cover image and secret image
    def select_images():
        # Open file dialogs to select the cover image and secret image
        cover_filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        secret_filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        if cover_filepath and secret_filepath:
            # Read the cover image and secret image
            cover_img = cv2.imread(cover_filepath)
            secret_img = cv2.imread(secret_filepath)
            # Resize the images to have the same dimensions
            cover_img, secret_img = resize_images(cover_img, secret_img)
            # Embed the secret image into the cover image
            stego_img = np.copy(cover_img)
            encode_image(stego_img, secret_img)
            # Save the steganographic image
            save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if save_filepath:
                cv2.imwrite(save_filepath, stego_img)
                messagebox.showinfo("Steganography", "Image encrypted and saved successfully")
    # Create a button to select the cover image and secret image
    select_images_button = tk.Button(image_in_image_window, text="Select Images: Cover and Secret", command=select_images)
    select_images_button.place(x=170,y=120)

# Create buttons for selecting steganography method
text_in_image_button = tk.Button(window, text="Text In Image", command=text_in_image)
text_in_image_button.pack(pady=10)
image_in_image_button = tk.Button(window, text="Image In Image", command=image_in_image)
image_in_image_button.pack(pady=10)

# Create a button for decoding the secret message from the steganographic image 
decode_button = tk.Button(window, text="Decode - Text", command=decode_text)
decode_button.pack(pady=10)
# Create a button for decoding the secret image from the steganographic image
decode_button = tk.Button(window, text="Decode - Image", command=decode_image)
decode_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
