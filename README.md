This is a simple Flask web app that lets users generate downloadable QR codes for any URL. Just paste a link, click a button, and get a QR code image instantly. Perfect for quick sharing, mobile scanning, and learning Flask + QR code generation!

---

## 🚀 Features

- Enter a URL to generate a QR code
- One-click download of the QR code as a PNG
- Mobile-friendly — scan with your phone to open the link
- Minimal, clean interface using Flask and the `qrcode` library

---

## 🛠️ Prerequisites

- Python 3.x
- pip (Python package manager)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-qr-code-generator.git
cd flask-qr-code-generator
````

2. Install dependencies:

```bash
pip install Flask qrcode pillow
```

---

## ▶️ Run the App

```bash
python app.py
```

Then go to `http://127.0.0.1:5000/` in your browser.

---

## 📂 Project Structure

```
.
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # HTML interface for user input
```

---

## 📸 How It Works

1. User enters a URL into the form.
2. Clicks “Generate QR Code”.
3. QR code is generated and served as a downloadable image.
4. Scanning the QR opens the URL in the browser.

---

## ✅ Libraries Used

* **Flask** – Web framework
* **qrcode** – QR code generation
* **Pillow** – Image processing backend used by `qrcode`

---

## 📖 License

This project is open-source and free to use for learning or building personal projects.

---



