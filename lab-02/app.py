from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenerCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    result = ""
    error = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        if not key.isdigit():
            error = "Khóa phải là một số nguyên."
        else:
            key = int(key)
            cipher = CaesarCipher()
            if "encrypt" in request.form:
                result = cipher.encrypt_text(text, key)
            elif "decrypt" in request.form:
                result = cipher.decrypt_text(text, key)
    return render_template("caesar.html", result=result, error=error)

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = ""
    error = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        cipher = VigenerCipher()

        if not key.isalpha():
            error = "Khóa phải chứa các ký tự chữ cái (A–Z)."
        else:
            if "encrypt" in request.form:
                result = cipher.vigener_encrypt(text, key)
            elif "decrypt" in request.form:
                result = cipher.vigener_decrypt(text, key)

    return render_template("vigenere.html", result=result, error=error)


@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    result = ""
    error = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        if not key.isdigit() or int(key) < 2:
            error = "khóa phải là một số nguyên ≥ 2."
        else:
            key = int(key)
            cipher = RailFenceCipher()
            if "encrypt" in request.form:
                result = cipher.rail_fence_encrypt(text, key)
            elif "decrypt" in request.form:
                result = cipher.rail_fence_decrypt(text, key)
    return render_template("railfence.html", result=result, error=error)

@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = ""
    error = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        if not key.isalpha():
            error = "Khóa phải chứa các ký tự chữ cái (A–Z)."
        else:
            cipher = PlayfairCipher()
            matrix = cipher.create_playfair_matrix(key)
            if "encrypt" in request.form:
                result = cipher.playfair_encrypt(text, matrix)
            elif "decrypt" in request.form:
                result = cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html", result=result, error=error)

@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    result = ""
    error = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        if not key.isdigit() or int(key) < 2:
            error = "Khóa phải là một số nguyên ≥ 2."
        else:
            key = int(key)
            cipher = TranspositionCipher()
            if "encrypt" in request.form:
                result = cipher.encrypt(text, key)
            elif "decrypt" in request.form:
                result = cipher.decrypt(text, key)
    return render_template("transposition.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
