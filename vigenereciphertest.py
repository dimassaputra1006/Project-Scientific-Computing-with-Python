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

def encrypt(message, key):
    return vigenere(message, key, direction=1)

def decrypt(message, key):
    return vigenere(message, key, direction=-1)

def main():
    print("=== Program Vigenère Cipher ===")

    while True:
        text = input("Masukkan teks: ")
        key = input("Masukkan kunci enkripsi (key): ")

        while True:
            print("\nPilih aksi:")
            print("1. Enkripsi")
            print("2. Dekripsi")
            print("3. Input baru")
            print("4. Keluar\n")

            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

            if pilihan == '1':
                hasil = encrypt(text, key)
                print("Hasil Enkripsi:", hasil)

            elif pilihan == '2':
                hasil = decrypt(text, key)
                print("Hasil Dekripsi:", hasil)

            elif pilihan == '3':
                print("Mengulang input teks & key...\n")
                break  # keluar dari loop dalam, input ulang teks & key

            elif pilihan == '4':
                print("Terima kasih! Program selesai.")
                return

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
main()
