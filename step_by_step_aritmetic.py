Oke, ini dia **penjelasan langkah-langkah pembuatan fungsi `arithmetic_arranger` secara runtut dari awal sampai akhir**, dalam format rapi dan siap kamu simpan ke `.txt`:

---

# 📘 Penjelasan Lengkap `arithmetic_arranger`

Fungsi `arithmetic_arranger` menyusun soal penjumlahan dan pengurangan secara terformat rapi secara vertikal, maksimal 5 soal.

---

## 🔢 **Langkah 1: Validasi Jumlah Soal**

```python
if len(problems) > 5:
    return "Error: Too many problems."
```

➡ Maksimal hanya boleh 5 soal. Kalau lebih, kembalikan pesan error.

---

## ➕➖ **Langkah 2: Validasi Operator**

```python
operator = problem.split()[1]
if operator not in ['+', '-']:
    return "Error: Operator must be '+' or '-'."
```

➡ Operator harus `+` atau `-`. Kalau bukan, kembalikan error.

---

## 🔤 **Langkah 3: Validasi Format Angka**

```python
if not operand1.isdigit() or not operand2.isdigit():
    return "Error: Numbers must only contain digits."
if len(operand1) > 4 or len(operand2) > 4:
    return "Error: Numbers cannot be more than four digits."
```

➡ Angka harus digit murni (tanpa huruf/simbol), dan maksimal 4 digit tiap angka.

---

## 📏 **Langkah 4: Menyusun Baris Soal**

### 4.1 Pisahkan komponen tiap soal

```python
operand1, operator, operand2 = problem.split()
```

### 4.2 Hitung lebar kolom

```python
width = max(len(operand1), len(operand2)) + 2
```

➡ Ambil angka terpanjang, tambah 2 (1 spasi + 1 operator).

### 4.3 Susun tiap baris

```python
top_row.append(operand1.rjust(width))
bottom_row.append(operator + operand2.rjust(width - 1))
lines.append("-" * width)
```

➡ Gunakan `rjust()` agar semua baris rata kanan. Garis `-` disesuaikan dengan lebar kolom.

---

## ✅ **Langkah 5 (Opsional): Hitung Jawaban**

```python
if show_answers:
    if operator == '+':
        result = str(int(operand1) + int(operand2))
    else:
        result = str(int(operand1) - int(operand2))
    results.append(result.rjust(width))
```

➡ Jika `show_answers == True`, hitung hasilnya dan ratakan kanan.

---

## 🧩 **Langkah 6: Gabungkan Semua Baris**

```python
arranged_top = '    '.join(top_row)
arranged_bottom = '    '.join(bottom_row)
arranged_lines = '    '.join(lines)
```

➡ Gabungkan semua baris dengan 4 spasi antar soal.

Jika `show_answers == True`:

```python
arranged_results = '    '.join(results)
return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}\n{arranged_results}"
```

Jika `False`:

```python
return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}"
```

---

## 🧪 Contoh Output:

Input:

```python
["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
```

Output (tanpa hasil):

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Output (dengan hasil):

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

---

Kalau kamu mau versi kode final Python-nya juga, bilang saja, nanti aku sertakan juga dalam format rapi untuk `.txt`.
