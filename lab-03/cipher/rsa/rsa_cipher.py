# rsa_cipher.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open('cipher/rsa/keys/privateKey.pem', "wb") as priv_file:
            priv_file.write(private_key)

        with open('cipher/rsa/keys/publicKey.pem', "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        with open('cipher/rsa/keys/privateKey.pem', "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())

        with open('cipher/rsa/keys/publicKey.pem', "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())

        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        return encrypted_message

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext)
        return decrypted_message.decode('utf-8')

    def sign(self, message, private_key):
        h = SHA256.new(message.encode('utf-8'))
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode('utf-8'))
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
