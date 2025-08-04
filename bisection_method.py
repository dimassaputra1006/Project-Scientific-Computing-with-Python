# Fungsi untuk mencari akar kuadrat menggunakan metode bisection
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Kalau angkanya negatif, langsung raise error
    if square_target < 0:
        raise ValueError('Akar kuadrat dari bilangan negatif tidak didefinisikan di bilangan real.')

    # Kasus khusus: kalau target = 1
    if square_target == 1:
        root = 1
        print(f'Akar kuadrat dari {square_target} adalah 1')

    # Kasus khusus: kalau target = 0
    elif square_target == 0:
        root = 0
        print(f'Akar kuadrat dari {square_target} adalah 0')

    else:
        # Batas awal (low) dimulai dari 0
        # Batas atas (high) pakai max(1, square_target) untuk menangani angka < 1
        low = 0
        high = max(1, square_target)

        root = None  # Ini tempat menyimpan akar jika ketemu nanti

        # Loop hingga max_iterations kali
        for _ in range(max_iterations):
            mid = (low + high) / 2               # Ambil titik tengah dari low dan high
            square_mid = mid ** 2                # Kuadratkan mid, ini tebakan akar

            # Kalau tebakan sudah cukup dekat (dalam toleransi), selesai
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break  # Keluar dari loop karena sudah ketemu

            # Kalau hasil kuadrat lebih kecil dari target, geser batas bawah ke mid
            elif square_mid < square_target:
                low = mid

            # Kalau terlalu besar, geser batas atas ke mid
            else:
                high = mid

        # Kalau root masih None setelah semua percobaan, berarti gagal konvergen
        if root is None:
            print(f"Gagal konvergen dalam {max_iterations} iterasi.")

        # Kalau berhasil, tampilkan hasilnya
        else:
            print(f'Akar kuadrat dari {square_target} diperkirakan {root}')

    return root  # Kembalikan nilai akar yang ditemukan

while True:
    user_input = input("\nMasukkan angka yang ingin dicari akar kuadratnya (atau ketik 'exit' untuk keluar): ")

    if user_input.lower() == 'exit':  # Jika user ketik "exit", keluar dari loop
        print("Sampai jumpa!")
        break

    try:
        number = float(user_input)  # Ubah input string menjadi angka float
        square_root_bisection(number)  # Panggil fungsi utama
    except ValueError as e:
        # Tangkap error kalau input bukan angka atau negatif
        print(f"Input tidak valid: {e}")
