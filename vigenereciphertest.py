# Fungsi utama Vigenere Cipher
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

# Fungsi enkripsi
def encrypt(message, key):
    return vigenere(message, key, direction=1)

# Fungsi dekripsi
def decrypt(message, key):
    return vigenere(message, key, direction=-1)

# Fungsi utama program (loop until exit)
def main():
    print("=== Program Vigenère Cipher ===")
    while True:
        text = input("Masukkan teks yang ingin dienkripsi atau didekripsi: ")
        custom_key = input("Masukkan kunci enkripsi (key): ")
        mode = input("Ketik 'e' untuk Enkripsi atau 'd' untuk Dekripsi: ").strip().lower()

        if mode == 'e':
            result = encrypt(text, key)
            print("Hasil Enkripsi:", result)
        elif mode == 'd':
            result = decrypt(text, key)
            print("Hasil Dekripsi:", result)
        elif mode == 'x':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Mode tidak dikenali. Silakan ulangi.")

# Jalankan program
main()
