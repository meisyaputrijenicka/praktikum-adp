B = int(input("Masukan jumlah baris: "))
K = int(input("Masukan jumlah kolom: "))

for m in range(B):
    for j in range(K):
        if (m + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()