import tkinter as tk
from tkinter import messagebox

# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            encrypted_text += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            encrypted_text += chr((ord(char) + shift - 32) % 95 + 32)

    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():
            decrypted_text += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            decrypted_text += chr((ord(char) - shift - 32) % 95 + 32)

    return decrypted_text

# Function to handle encryption action
def handle_encrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        encrypted_message = encrypt(text, shift)
        result_label.config(text=f"Encrypted Message: {encrypted_message}")
        result_frame.pack()
        input_frame.pack_forget()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Function to handle decryption action
def handle_decrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        decrypted_message = decrypt(text, shift)
        result_label.config(text=f"Decrypted Message: {decrypted_message}")
        result_frame.pack()
        input_frame.pack_forget()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Function to switch back to input screen
def switch_to_input_screen():
    result_frame.pack_forget()
    input_frame.pack()

# Function to exit the application
def exit_app():
    root.quit()

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Input Screen
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)
import tkinter as tk
from tkinter import messagebox

# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            encrypted_text += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            encrypted_text += chr((ord(char) + shift - 32) % 95 + 32)

    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():
            decrypted_text += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            decrypted_text += chr((ord(char) - shift - 32) % 95 + 32)

    return decrypted_text

# Function to handle encryption action
def handle_encrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        encrypted_message = encrypt(text, shift)
        result_label.config(text=f"Encrypted Message: {encrypted_message}")
        result_frame.pack()
        input_frame.pack_forget()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Function to handle decryption action
def handle_decrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        decrypted_message = decrypt(text, shift)
        result_label.config(text=f"Decrypted Message: {decrypted_message}")
        result_frame.pack()
        input_frame.pack_forget()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Function to switch back to input screen
def switch_to_input_screen():
    result_frame.pack_forget()
    input_frame.pack()

# Function to exit the application
def exit_app():
    root.quit()

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Input Screen
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)

input_label = tk.Label(input_frame, text="Enter your text:")
input_label.pack()

input_text = tk.Text(input_frame, height=6, width=40)
input_text.pack()

shift_label = tk.Label(input_frame, text="Enter shift value:")
shift_label.pack()

shift_entry = tk.Entry(input_frame)
shift_entry.pack()

encrypt_button = tk.Button(input_frame, text="Encrypt", command=handle_encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(input_frame, text="Decrypt", command=handle_decrypt)
decrypt_button.pack(pady=5)

# Result Screen
result_frame = tk.Frame(root)

result_label = tk.Label(result_frame, text="", justify="left")
result_label.pack()

back_button = tk.Button(result_frame, text="Back to Input", command=switch_to_input_screen)
back_button.pack(pady=10)

exit_button = tk.Button(result_frame, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
input_label = tk.Label(input_frame, text="Enter your text:")
input_label.pack()

input_text = tk.Text(input_frame, height=6, width=40)
input_text.pack()

shift_label = tk.Label(input_frame, text="Enter shift value:")
shift_label.pack()

shift_entry = tk.Entry(input_frame)
shift_entry.pack()

encrypt_button = tk.Button(input_frame, text="Encrypt", command=handle_encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(input_frame, text="Decrypt", command=handle_decrypt)
decrypt_button.pack(pady=5)

# Result Screen
#result_frame = tk.Frame(root)

result_label = tk.Label(result_frame, text="", justify="left")
result_label.pack()

back_button = tk.Button(result_frame, text="Back to Input", command=switch_to_input_screen)
back_button.pack(pady=10)

exit_button = tk.Button(result_frame, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()