# QR Code Generator

**Description:**
A simple Python project that generates QR codes from any website URL or text input. The generated QR code is saved as a PNG image in your Documents folder and can be automatically opened on macOS. Ideal for quickly creating QR codes for sharing links, Wi-Fi credentials, or any text.

---

## Features

* Generate QR codes from user input (URL or text)
* Save QR codes as PNG images
* Automatically add `.png` extension if missing
* Open the QR code image automatically on macOS
* Save images in the user's `Documents` folder by default

---

## Requirements

* Python 3.7 or higher
* [qrcode](https://pypi.org/project/qrcode/) library
* [Pillow](https://pypi.org/project/Pillow/) library

Install dependencies using pip:

```bash
python3 -m pip install qrcode pillow
```

---

## How to Use

1.  Clone or download this project.

2.  Open a terminal and navigate to the project folder.

3.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  Run the script:

    ```bash
    python3 qr_code.py
