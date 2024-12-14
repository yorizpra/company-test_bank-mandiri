# Buatlah program bahasa Java/lainnya dengan ketentuan terdapat Input dan 2 case Output sebagai berikut :

# Input : 

# 116, 88, 20, 90, 30, 77, 54, 37

# Output : 

# case 1 = 20, 30, 37, 54, 77, 88, 90, 116 // mengurutkan dari yang Angka Terkecil ke Angka Terbesar 

# case 2 = 30, 54, 90 // mencetak angka yang merupakan kelipatan angka 6

 

# *Note : 

# Jika menggunakan inputan by user akan menjadi nilai plus.
# Hasil output silahkan di screenshot dan dilampirkan ke Lembar Jawaban setelah memasukan code sederhananya.

import numbers


input_str = input("Masukan angka, pisahkan dengan koma (contoh: 1,2,3): ")

numbers = list(map(int,
input_str.split(',')))

sorted_numbers = sorted(numbers)

multiple_of_six = [num for num in sorted_numbers if num % 6 == 0]

print(f"Case 1: {sorted_numbers}")
print(f"Case 2: {multiple_of_six}")