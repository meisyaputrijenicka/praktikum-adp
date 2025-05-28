def hitung_kecepatan_akhir(v0, a, t):
    return v0 + a * t

def hitung_jarak(v0, a, t):
    return v0 * t + 0.5 * a * (t ** 2)

n = int(input("Input jumlah data: "))

kecepatan_awal = []
percepatan = []
waktu = []
kecepatan_akhir = []
j_arak = []

i = 0
for i in range(n):
    print(f"\nInput ke-{i+1}")
    v0 = float(input("Masukan kecepatan awal (m/s): "))
    a = float(input("Masukan percepatan (m/s^2): "))
    t = float(input("Masukan waktu (s): "))

    kecepatan_awal.append(v0)
    percepatan.append(a)
    waktu.append(t)

    v_akhir = hitung_kecepatan_akhir(v0, a, t)
    jarak = hitung_jarak(v0, a, t)

    kecepatan_akhir.append(v_akhir)
    j_arak.append(jarak)

print("\nHasil Perhitungan:")
print("-" * 98)
print("| No | Kecepatan Awal (m/s) | Percepatan (m/s^2) | Waktu (s) | Kecepatan Akhir (m/s) | Jarak (m) |")
print("-" * 98)
i = 0
# menggunakan ^angka agar nilai nya berada di tengah tabel serta .2f artinya untuk penganmbilan 2 angka dibelakang koma (data float)
for i in range(n):
    print(f"| {i+1:^2} | {kecepatan_awal[i]:^20.2f} | {percepatan[i]:^19.2f} | {waktu[i]:^9.2f} | {kecepatan_akhir[i]:^20.2f} | {j_arak[i]:^9.2f} |")
print("-" * 98)