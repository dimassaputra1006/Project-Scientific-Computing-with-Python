# Fungsi utama Vigenere Cipher
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)].lower()
            offset = alphabet.index(key_char.lower())
            char_lower = char.lower()
            index = alphabet.find(char_lower)
            new_index = (index + offset * direction) % len(alphabet)
            final_char = alphabet[new_index]
            # Jaga kapitalisasi
            if char.isupper():
                final_char = final_char.upper()
            final_message += final_char
            key_index += 1

    return final_message

# Fungsi enkripsi dan dekripsi
def encrypt(message, key):
    return vigenere(message, key, direction=1)

def decrypt(message, key):
    return vigenere(message, key, direction=-1)

# Fungsi utama program
def main():
    print("=== Program Vigenère Cipher ===")
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci enkripsi (key): ")
    encrypted_text = ''

    while True:
        print("\nPilih aksi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Input baru")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4): ").strip()

        if choice == '1':
            encrypted_text = encrypt(text, key)
            print("Hasil Enkripsi:", encrypted_text)
        elif choice == '2':
            if encrypted_text == '':
                print("Belum ada hasil enkripsi untuk didekripsi.")
            else:
                decrypted_text = decrypt(encrypted_text, key)
                print("Hasil Dekripsi:", decrypted_text)
        elif choice == '3':
            text = input("Masukkan teks baru: ")
            key = input("Masukkan kunci baru: ")
            encrypted_text = ''
        elif choice == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()