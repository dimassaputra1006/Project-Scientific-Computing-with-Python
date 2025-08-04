def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Akar kuadrat dari bilangan negatif tidak didefinisikan di bilangan real.')

    if square_target == 1:
        root = 1
        print(f'Akar kuadrat dari {square_target} adalah 1')
    elif square_target == 0:
        root = 0
        print(f'Akar kuadrat dari {square_target} adalah 0')
    else:
        low = 0
        high = max(1, square_target)
        root = None

        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid ** 2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Gagal konvergen dalam {max_iterations} iterasi.")
        else:
            print(f'Akar kuadrat dari {square_target} diperkirakan {root}')
    
    return root

while True:
    user_input = input("\nMasukkan angka yang ingin dicari akar kuadratnya (atau ketik 'exit' untuk keluar): ")

    if user_input.lower() == 'exit':
        print("Sampai jumpa!")
        break

    try:
        number = float(user_input)
        square_root_bisection(number)
    except ValueError as e:
        print(f"Input tidak valid: {e}")
