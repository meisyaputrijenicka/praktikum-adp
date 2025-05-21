ip = [("A",4.00),("A-",3.75),("B+",3.50),("B",3.00),("B-",2.75),
      ("C+",2.50),("C",2.00),("D",1.00),("E",0.00)]
data_mhs=[]
jmlhmhs = int(input("jumlah mahasiswa : "))
for i in range (jmlhmhs):
    print(f"\nMahasiswa ke-{1+i}")
    nama = input("Nama mahasiswa : ")
    while True:
        nilai = input(f"Masukkan nilai ip anda (A,A-,B+,B,B-,C+,C,D,E): ").upper()
        valid = False
        ip_mhs = 0.00
        for huruf,ip_nilai in ip:
            if nilai==huruf:
                valid = True
                ip_mhs = ip_nilai
                break
        if valid:
            data_mhs.append([nama, nilai, ip_mhs])
            break
        else:
            print("Nilai tidak valid! Inputkan kembali!")
for i in range(len(data_mhs)):
        for j in range(i+1, len(data_mhs)):
            if data_mhs[i][2] < data_mhs[j][2]:
                data_mhs[i], data_mhs[j] = data_mhs[j], data_mhs[i]

print("\nHasil IP Mahasiswa:")
print("-"*40)
print("No.  Nama         Nilai   IP")
print("-"*40)

for i in range(len(data_mhs)):
        print(f"{i+1:<4}{data_mhs[i][0]:<14}{data_mhs[i][1]:<6} {data_mhs[i][2]:.2f}")
print("-"*40)