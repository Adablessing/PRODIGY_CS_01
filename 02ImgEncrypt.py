from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path).convert("RGB")  # Ensure RGB format
    img_array = np.array(image, dtype=np.uint8)  # Convert to numpy array
    np.random.seed(key)  # Seed random generator with key
    indices = np.arange(img_array.size)
    np.random.shuffle(indices)  # Shuffle indices
    encrypted_array = img_array.flatten()[indices].reshape(img_array.shape)
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, key, output_path):
    encrypted_image = Image.open(encrypted_path).convert("RGB")
    encrypted_array = np.array(encrypted_image, dtype=np.uint8)
    np.random.seed(key)
    indices = np.arange(encrypted_array.size)
    np.random.shuffle(indices)
    reverse_indices = np.argsort(indices)  # Get reverse mapping
    decrypted_array = encrypted_array.flatten()[reverse_indices].reshape(encrypted_array.shape)
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    file_path = input("Enter the image file path: ")
    key = int(input("Enter an encryption key (integer): "))  # Key for shuffling
    output_file = input("Enter output file name: ")

    if choice == 'E':
        encrypt_image(file_path, key, output_file)
    elif choice == 'D':
        decrypt_image(file_path, key, output_file)
    else:
        print("Invalid choice!")
