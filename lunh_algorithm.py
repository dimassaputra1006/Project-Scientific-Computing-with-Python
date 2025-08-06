# Fungsi untuk memverifikasi nomor kartu kredit menggunakan Algoritma Luhn
def verify_card_number(card_number):
    # Langkah 1: Hitung jumlah digit pada posisi ganjil (dari kanan)
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]          # Balik urutan digit
    odd_digits = card_number_reversed[::2]            # Ambil digit ganjil (indeks 0,2,4,...)

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)                # Konversi string ke int lalu jumlahkan

    # Langkah 2: Hitung jumlah digit pada posisi genap (dari kanan)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]           # Ambil digit genap (indeks 1,3,5,...)

    for digit in even_digits:
        number = int(digit) * 2                        # Kalikan digit dengan 2
        if number >= 10:                               # Jika hasil ≥ 10, jumlahkan digitnya
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number                   # Tambahkan ke total genap

    # Langkah 3: Hitung total dan cek validitas
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0                             # Valid jika total habis dibagi 10

# Fungsi utama: membersihkan input dan menjalankan verifikasi
def main():
    card_number = '4111-1111-4555-1142' 
    # Hapus karakter non-digit seperti '-' atau spasi
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Tampilkan hasil verifikasi
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Jalankan program
main()
