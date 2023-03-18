# QR Code Generator

This project allows you to generate a QR code of any valid URL by using Python's Flask library and the Qrcode library.

## Installation

### Setup a virtual environment

First you need to setup a virtual environment for this project. To do that, run:

```
python3 -m venv venv
```

This will create a new directory called `venv` in your current directory. After that, activate the virtual environment by running:

```
source venv/bin/activate
```

### Install dependencies

To install the required libraries, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the script, open your terminal and run:

```
python app.py
```

The application will start a Flask server listening on a default port (usually 5000).

Now, you can send GET request to generate a QR code based on a URL parameter. Here's a sample request:

```
http://localhost:5000/generate_qr_code?url=https://www.example.com
```

Replace `https://www.example.com` with the URL you want to generate a QR code for, and the server will return an image in PNG format representing the QR code.