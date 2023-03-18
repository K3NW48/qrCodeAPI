from flask import Flask, request, send_file
import qrcode
from io import BytesIO
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/generate_qr_code", methods=["GET"])
def generate_qr_code():
    url = request.args.get("url")
    if url and urlparse(url).scheme:
        qr_image = qrcode.make(url)
        binary_stream = BytesIO()
        qr_image.save(binary_stream, "PNG")
        binary_stream.seek(0)
        return send_file(binary_stream, mimetype="image/png")
    else:
        return "Invalid or missing URL parameter", 400

if __name__ == "__main__":
    app.run(debug=True)