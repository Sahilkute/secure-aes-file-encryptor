from flask import Flask, request, send_file, render_template
from app_utils import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    file = request.files["file"]
    file_data = file.read()
    encrypted = encrypt_file(file_data)

    with open("encrypted_file.bin", "wb") as f:
        f.write(encrypted)

    return send_file("encrypted_file.bin", as_attachment=True, download_name="encrypted.bin")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    file = request.files["file"]
    file_data = file.read()
    decrypted = decrypt_file(file_data)

    with open("decrypted_file.txt", "wb") as f:
        f.write(decrypted)

    return send_file("decrypted_file.txt", as_attachment=True, download_name="decrypted.txt")

if __name__ == "__main__":
    app.run(debug=True)
