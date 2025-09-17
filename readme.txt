down load tesseract: https://github.com/UB-Mannheim/tesseract/wiki


Follow the instructions on the page to install Tesseract for your operating system.


pytesseract is just a wrapper; you also need the actual Tesseract OCR engine.

🖥️ On Windows:

Download installer from: Tesseract at UB Mannheim

Install it (default path usually C:\Program Files\Tesseract-OCR\).

Add Tesseract to PATH, or set it in code:

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
