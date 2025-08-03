# Minta input dari pengguna
text = input("Masukkan teks yang ingin dienkripsi atau didekripsi: ")
custom_key = input("Masukkan kunci enkripsi (key): ")

# Fungsi utama: Vigenere Cipher
def vigenere(message, key, direction=1):
    key_index = 0                                # Untuk melacak posisi karakter dalam kunci
    alphabet = 'abcdefghijklmnopqrstuvwxyz'      # Daftar alfabet untuk referensi indeks
    final_message = ''                           # Hasil akhir (plaintext atau ciphertext)

    for char in message.lower():                 # Iterasi setiap karakter di teks
        if not char.isalpha():                   # Jika bukan huruf (spasi, simbol), langsung tambahkan
            final_message += char
        else:
            key_char = key[key_index % len(key)] # Ambil huruf dari kunci secara berulang
            key_index += 1

            offset = alphabet.index(key_char)    # Temukan offset dari huruf kunci
            index = alphabet.find(char)          # Temukan posisi huruf di pesan
            new_index = (index + offset * direction) % len(alphabet)  # Hitung indeks baru (maju atau mundur)
            final_message += alphabet[new_index] # Tambahkan huruf baru ke hasil akhir
    
    return final_message                         # Kembalikan hasil akhir

# Fungsi untuk enkripsi
def encrypt(message, key):
    return vigenere(message, key)

# Fungsi untuk dekripsi
def decrypt(message, key):
    return vigenere(message, key, -1)            # Gunakan arah -1 untuk mundur (dekripsi)

# Proses dekripsi dan cetak hasil
print(f'\nEncrypted text (input): {text}')
print(f'Key: {custom_key}')

decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
