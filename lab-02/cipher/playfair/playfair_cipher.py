class PlayfairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển 'J' thành 'I' trong khóa
        key = key.upper()
        key_set = set()
        matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = ""
        for letter in key:
            if letter not in key_set:
                key_set.add(letter)

        for letter in alphabet:
            if letter not in key_set:
                remaining_letters += letter

        key += remaining_letters
        playfair_matrix = [key[i:i + 5] for i in range(0, len(key), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.upper()
        plain_text = plain_text.replace("J", "I")
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            pair = plain_text[i:i + 2]
            if len(pair) < 2:
                pair += "X"
            elif pair[0] == pair[1]:
                pair = pair[0] + "X"
                i -= 1

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

            i += 2
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        banro = ""
        # Loại bỏ ký tự 'X' nếu nó là ký tự cuối cùng và là ký tự được thêm vào
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i + 2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]

        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2] + decrypted_text[-1]

        return banro
