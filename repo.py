user = [
    {"nama": "arsene lupin", "nik": 1234, "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
    {"nama": "sherlock holmes", "nik": 4321, "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
    {"nama": "irene adler", "nik": 6789, "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}
]

# Menerima input dari user
nama = input("Masukkan nama: ")
nik = int(input("Masukkan NIK: "))
jenis_kelamin = input("Masukkan jenis kelamin: ")
tanggal_lahir = input("Masukkan tanggal lahir (yyyy-mm-dd): ")

# Menambahkan data baru ke dalam list user
user.append({"nama": nama, "nik": nik, "jenis_kelamin": jenis_kelamin, "tanggal_lahir": tanggal_lahir})

# Mencetak hasil
print("Data user terbaru:")
for data in user:
    print(data)