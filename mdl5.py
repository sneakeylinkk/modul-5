n = int(input("Masukkan jumlah mahasiswa pratikum ADP : "))
data = []

for i in range(n):
    print(f"Mahasiswa ke-{i+1}")
    nama = str(input("Nama          : "))
    pretest = float(input("Nilai Pretest : "))
    posttest = float(input("Nilai Postest : "))
    makalah = float(input("Nilai Makalah : "))
    nilai_akhir = (0.4 * pretest) + (0.4 * posttest) + (0.2 * makalah)
    data.append([nama, nilai_akhir])

print("\n----------------------------------------")
print("|      TABEL NILAI AKHIR MAHASISWA     |")
print("----------------------------------------")
print("|    Nama Mahasiswa    |  Nilai Akhir  |")
print("----------------------------------------")
for j in data:
    print(f"| {j [0]:<20} | {j[1]:>9.2f}     |")
print("----------------------------------------")

jumlah = 0
for m in data : 
    jumlah += m[1]
rata_rata = jumlah / n
print (f"Rata-rata nilai akhir kelas : adalah {rata_rata:.2f}")

nilai_akhir = []
for m in data :
    nilai_akhir.append(m[1])

tertinggi = nilai_akhir[0]
terendah = nilai_akhir[0]

for nilai in nilai_akhir:
    if nilai > tertinggi:
        tertinggi = nilai
    if nilai < terendah:
        terendah = nilai

print("\nMahasiswa dengan nilai tertinggi:")
for m in data:
    if m[1] == tertinggi:
        print(f"{m[0]} dengan nilai {m[1]:.2f}")

print("\nMahasiswa dengan nilai terendah:")
for m in data:
    if m[1] == terendah :
        print(f"{m[0]} dengan nilai {m[1]:.2f}")

print("\nMahasiswa dengan nilai di atas rata-rata:")
for m in data:
    if m[1] > rata_rata:
        print(f"{m[0]} dengan nilai {m[1]:.2f}")
