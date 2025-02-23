import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Global variables
img = None
password = "mysecret"  # Default passcode

def load_image():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        messagebox.showinfo("Image Loaded", "Image loaded successfully!")
def decrypt_message():
    global img, password
    if img is None:
        messagebox.showerror("Error", "Please load an image first!")
        return

    pas = pass_entry.get()
    if password != pas:
        messagebox.showerror("Error", "Incorrect passcode!")
        return

    message = ""
    n, m, z = 0, 0, 0
    for _ in range(len(msg_entry.get("1.0", tk.END).strip())):
        message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3

    output_entry.delete(0, tk.END)
    output_entry.insert(0, message)
    messagebox.showinfo("Decrypted Message", f"Decrypted message: {message}")

# Create GUI
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("600x500")
root.configure(bg="#f4f4f4")

# Title
header = tk.Label(root, text="Steganography Tool", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)
subheader = tk.Label(root, text="Secure Data Hiding in Images", font=("Arial", 14), bg="#2c3e50", fg="white")
subheader.pack(fill=tk.X)

# Load Image Button
load_label = tk.Label(root, text="Load Image", font=("Arial", 12), bg="#f4f4f4")
load_label.pack(pady=5)
load_button = tk.Button(root, text="Choose File", command=load_image)
load_button.pack()

# Message Entry
msg_label = tk.Label(root, text="Enter Message", font=("Arial", 12), bg="#f4f4f4")
msg_label.pack(pady=5)
msg_entry = tk.Text(root, height=3, width=50)
msg_entry.pack()

# Passcode Entry
pass_label = tk.Label(root, text="Enter Passcode", font=("Arial", 12), bg="#f4f4f4")
pass_label.pack(pady=5)
pass_entry = tk.Entry(root, show='*', width=50)
pass_entry.pack()

# Encrypt & Decrypt Buttons
encrypt_button = tk.Button(root, text="Encrypt", bg="#2c3e50", fg="white", command=encrypt_message)
encrypt_button.pack(pady=5)
decrypt_button = tk.Button(root, text="Decrypt", bg="#2c3e50", fg="white", command=decrypt_message)
decrypt_button.pack(pady=5)

# Output Entry
output_label = tk.Label(root, text="Output", font=("Arial", 12), bg="#f4f4f4")
output_label.pack(pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.pack()

root.mainloop()

