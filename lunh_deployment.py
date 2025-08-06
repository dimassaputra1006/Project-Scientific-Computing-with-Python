def verify_card_number(card_number):
    """Memverifikasi nomor kartu menggunakan Algoritma Luhn."""
    # 1. Bersihkan input: hilangkan semua karakter non-digit
    clean_number = ''.join(filter(str.isdigit, card_number))
    if not clean_number:
        return False, "Nomor kartu tidak boleh kosong atau hanya simbol."

    # 2. Balik urutan digit agar mudah diproses dari kanan
    reversed_digits = clean_number[::-1]

    # 3. Hitung digit ganjil (posisi 1,3,5,... dari kanan)
    sum_odd = sum(int(d) for d in reversed_digits[::2])

    # 4. Hitung digit genap (posisi 2,4,6,... dari kanan)
    sum_even = 0
    for digit in reversed_digits[1::2]:
        doubled = int(digit) * 2
        # Jika hasil ≥10, jumlahkan digit-digitnya (contoh: 14 → 1+4)
        sum_even += (doubled // 10) + (doubled % 10)

    # 5. Total harus habis dibagi 10
    total = sum_odd + sum_even
    is_valid = total % 10 == 0
    return is_valid, total

def main():
    print("=== Verifikasi Kartu Kredit (Algoritma Luhn) ===")
    while True:
        card = input("\nMasukkan nomor kartu (ketik 'q' untuk keluar): ").strip()
        if card.lower() == 'q':
            print("Terima kasih! Program selesai.")
            break
        
        valid, total = verify_card_number(card)
        if valid:
            print("✅ VALID! Nomor kartu lulus algoritma Luhn.")
        else:
            print("❌ INVALID! Total Luhn =", total, "→ bukan kelipatan 10.")

if __name__ == "__main__":
    main()


#note kartu valid jika hasil itu sama dengan 0
