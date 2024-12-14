# Buatlah program bahasa Java/lainnya menggunakan looping dengan ketentuan sebagai berikut :

# Inputan : {11,22,33,44,55,66,77,88,99}

# Output yang diharapkan : -*22*44*66*88*-

# *Note : 

# Jika menggunakan inputan by user akan menjadi nilai plus.
# Hasil output silahkan di screenshot dan dilampirkan ke Lembar Jawaban setelah memasukan code sederhananya. 

input_str = input("Masukan angka, pisahkan dengan koma (contoh: 1,2,3): ")
numbers = list(map(int, input_str.split(',')))
result = "-*"
for num in numbers:
  if num % 2 == 0:
    result += f"{num}*"
result += "-"
print(result)