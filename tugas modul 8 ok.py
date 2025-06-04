# tulis file
file = open("OrPSB22.txt", "w")
file.write(
"Meisya Putri Jenicka,2410431011,KBI,Anggota Acara,97,Acara\n" 
"Naila Farizka,2410431016,KBI,Koordinator Pubdok,96,Acara\n"
"Fauzi Taufiqur,2410431036,KBI,Koordinator Perlengkapan,94,Perlengkapan\n"
"Maul Java,2410431021,KBI,Anggota Pubdok,90,Pubdok\n" 
"Nailul Athiyyah,2410432046,KBI,Koordinator Danus,95,Perlengkapan\n"
"Desy Fadhillah,2410431038,KBI,Anggota Acara,97,Danus\n" 
"Mutiara Aviva,2410432045,KBI,Anggota Pubdok,92,Danus\n"
"Nur Azizah,2410432011,A,Anggota Acara,89,Pubdok\n"
"Lala Abdillah,2410431031,A,Koordinator Perlengkapan,90,Perlengkapan\n"
"Sari Ramadhani,2410431029,A,Koordinator Acara,85,Danus\n"
"Nazla Raudhatul,2410431004,B,Anggota Pubdok,87,Pubdok\n"
"Dinda Rahma,2410431034,B,Koordinator Pubdok,96,Pubdok\n"
"Angggya Fadhilla,2410431028,B,Koordinator Acara,96,Acara\n"
"Sarah Asyifa,2410431018,B,Anggota Perlengkapan,95,Perlengkapan\n"
"Deeya Ishmah,2410432006,C,Anggota Danus,87,Danus\n"
"Lexania Nazila,2410431019,A,Anggota Acara,90,Acara")
file.close()

file = open("OrPSB22.txt", "r")
print(file.read())
file.close()


# Fungsi skor
def skor(pengalaman, wawancara, bidang):
    pengalaman = pengalaman.lower()
    bidang = bidang.lower()

    poin = 0
    if "koordinator" in pengalaman:
        poin += 2
    if bidang in pengalaman:
        poin += 3
    return (wawancara + poin)*100/100

# Dictionary cakoor per bidang
cakoor_perbidang = {
    "Acara": [],
    "Pubdok": [],
    "Perlengkapan": [],
    "Danus": []
}

# Fungsi baca data
def baca_data():
    file = open("OrPSB22.txt", "r")
    data = file.readlines()
    file.close()

    for dta in data:
        bagian = dta.strip().split(",")
        if len(bagian) != 6:
            continue  # skip jika datanya tidak lengkap

        nama = bagian[0]
        nim = bagian[1]
        kelas = bagian[2]
        pengalaman = bagian[3]
        wawancara = int(bagian[4])
        bidang = bagian[5]

        nilai = skor(pengalaman, wawancara, bidang)
        cakoor_perbidang[bidang].append([nama, nilai])

# Panggil fungsi baca_data()
baca_data()

# Urutkan & tampilkan 2 terbaik per bidang
for bidang in cakoor_perbidang:
    daftar = cakoor_perbidang[bidang]

    # Pengurutan
    for i in range(len(daftar)):
        for j in range(i + 1, len(daftar)):
            if daftar[i][1] < daftar[j][1]:
                sementara = daftar[i]
                daftar[i] = daftar[j]
                daftar[j] = sementara

    print("\nKoordinator Terpilih Bidang", bidang + ":")
    for i in range(min(2, len(daftar))):
        print(str(i+1) + ". " + daftar[i][0] + " - Nilai: " + str(daftar[i][1]))
