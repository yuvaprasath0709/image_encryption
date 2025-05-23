# 🔐 Image Encryption Tool 
Secure Your Visual Data with Advanced AES Encryption

## 🌟 Project Overview

The **Image Encryption Tool** is a robust cybersecurity project meticulously crafted to safeguard your visual data. It employs the industry-standard **Advanced Encryption Standard (AES) algorithm in CBC (Cipher Block Chaining) mode** to encrypt and decrypt image files, effectively protecting them from unauthorized access and tampering.

## ✨ Key Features

* **🛡️ AES Encryption**: Implements the secure AES algorithm with CBC mode and a **unique Initialization Vector (IV)** for each encryption, ensuring strong cryptographic protection.
* **🖼️ Intelligent Image Validation**: Automatically detects and verifies if a file is a legitimate image format (e.g., JPEG, PNG) before proceeding with encryption, preventing erroneous operations.
* **🔗 Secure File Handling**: Enforces **`.enc` file extension validation** for decryption, ensuring only correctly formatted encrypted files are processed.
* **🚀 Enhanced User Experience (UX)**:
    * **Clear & Colorized Feedback**: Provides intuitive, color-coded success messages, error alerts, and informational banners for immediate visual feedback (supports ANSI escape codes in compatible terminals).
    * **Interactive Mode**: Offers a user-friendly interactive prompt for encryption/decryption, making the tool accessible even without complex command-line arguments.
* **📝 Comprehensive Session Logging**: Automatically logs all encryption and decryption operations, including timestamps and any errors, to dedicated log files. This feature is crucial for auditing and troubleshooting.
* **🚫 Robust Error Handling**: Implements clear and informative error messages for scenarios such as file not found, invalid image types, or decryption failures.

## 🛠️ Technologies Used

* **Python 3**: The core programming language.
* **PyCryptodome**: A powerful and well-maintained cryptographic library for Python, providing the AES implementation.
* **Pillow (PIL Fork)**: Essential for image file manipulation and format verification.

---

### 🖥️ Run Locally 

If you prefer to run this project on your local machine:

1.  **Prerequisites**: Ensure you have **Python 3** installed.
2.  **Install Dependencies**:

    ```bash
    pip install pycryptodome Pillow
    ```

---

## 📝 Usage

The tool offers both a direct **Command-Line Mode** and an **Interactive Mode** for convenience.

### Command-Line Mode 🚀

Execute operations directly by providing arguments.

* **Encrypt an Image**:

    ```bash
    python image_encryptor.py encrypt <path/to/your/image.jpg>
    ```

    **Example**:

    ```bash
    python image_encryptor.py encrypt secret_photo.png
    ```

    **Output**: An encrypted file (e.g., `secret_photo.png.enc`) will be created in the same directory.

* **Decrypt an Encrypted Image**:

    ```bash
    python image_encryptor.py decrypt <path/to/your/image.jpg.enc>
    ```

    **Example**:

    ```bash
    python image_encryptor.py decrypt secret_photo.png.enc
    ```

    **Output**: A decrypted file (e.g., `secret_photo.decrypted.jpg`) will be created in the same directory.

### Interactive Mode 💬

Run the script without arguments for a guided experience.

```bash
python image_encryptor.py
```

The tool will prompt you to choose between encryption/decryption and then ask for the file path.

---

## 🧠 How It Works

This tool leverages the **AES (Advanced Encryption Standard) symmetric-key algorithm** in **CBC (Cipher Block Chaining) mode**.

* **Padding**: Image data is first padded using **PKCS#7 padding** to ensure its length is a multiple of the AES block size (16 bytes).
* **Initialization Vector (IV)**: A unique, cryptographically random **16-byte IV** is generated for each encryption. This IV is crucial for CBC mode as it helps to randomize the encryption process, ensuring that identical plaintexts produce different ciphertexts.
* **Encryption**: The padded image data is encrypted using the AES key and the generated IV.
* **Output Format**: The encrypted file consists of the **IV concatenated with the ciphertext**. Both are necessary for successful decryption.
* **Decryption**: Upon decryption, the IV is extracted from the beginning of the encrypted file, and the ciphertext is decrypted using the AES key and this IV. Finally, the padding is removed to restore the original image data.

---

## 💡 Future Enhancements

We are continuously looking to improve the tool's security, usability, and features:

* **🔑 Password-Based Key Derivation (PBKDF2)**: Implement PBKDF2 to derive the AES key from a user-provided password, eliminating the need for a hardcoded key and significantly enhancing security.
* **🖥️ Graphical User Interface (GUI)**: Develop a user-friendly GUI (e.g., using Tkinter) to make the tool accessible to users less familiar with command-line interfaces.
* **📁 Batch Processing**: Add functionality for encrypting or decrypting entire folders of images, boosting efficiency for large collections.
* **🔄 Support for Multiple Algorithms**: Incorporate other encryption algorithms (e.g., DES, RSA) to provide more options, although AES is generally preferred for bulk data encryption.

---

## 🔒 Security Considerations

* **Key Management**: The current version uses a **hardcoded AES key**. This is for demonstration and educational purposes only. For any real-world application, a robust and secure key management system (e.g., using environment variables, key vaults, or PBKDF2 as mentioned above) is absolutely critical.
* **Ethical Use**: This tool is intended for educational and ethical cybersecurity research. **Misuse of this tool for malicious activities is strictly prohibited.**

---

## 🧑‍💻 Author

Developed by Yuva Prasath
