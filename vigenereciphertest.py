# Minta input dari pengguna
text = input("Masukkan teks yang ingin dienkripsi atau didekripsi: ")
custom_key = input("Masukkan kunci enkripsi (key): ")
mode = input("Ketik 'e' untuk Enkripsi atau 'd' untuk Dekripsi: ").lower()

# Fungsi utama: Vigenere Cipher
def vigenere(message, key, direction=1):
    key_index = 0                                # Melacak posisi karakter dalam kunci
    alphabet = 'abcdefghijklmnopqrstuvwxyz'      # Alfabet untuk referensi
    final_message = ''                           # Hasil akhir (cipher/plain)

    for char in message.lower():                 # Per karakter dalam pesan
        if not char.isalpha():                   # Jika bukan huruf, langsung tambahkan
            final_message += char
        else:
            key_char = key[key_index % len(key)] # Huruf kunci saat ini
            key_index += 1

            offset = alphabet.index(key_char)    # Offset berdasarkan huruf kunci
            index = alphabet.find(char)          # Posisi huruf di alfabet
            new_index = (index + offset * direction) % len(alphabet)  # Hitung posisi baru
            final_message += alphabet[new_index] # Tambahkan hasilnya ke pesan akhir
    
    return final_message

# Fungsi enkripsi
def encrypt(message, key):
    return vigenere(message, key)

# Fungsi dekripsi
def decrypt(message, key):
    return vigenere(message, key, -1)

# Menjalankan sesuai mode
if mode == 'e':
    encrypted = encrypt(text, custom_key)
    print(f"\nHasil Enkripsi: {encrypted}")
elif mode == 'd':
    decrypted = decrypt(text, custom_key)
    print(f"\nHasil Dekripsi: {decrypted}")
else:
    print("Mode tidak dikenali. Harus 'e' atau 'd'.")
