M = int(input("Modal awal investasi: Rp."))
r = int(input("Suku bunga tahunan (%): "))
T = int(input("Target investasi yang ingin dicapai: Rp."))
tahun = 0
while M<T:
    P = M * (r / 100)
    M = M + P 
    tahun = tahun+1
    print(f""" 
         Tahun ke-{tahun}: Rp. {M}""")
print(f"Target tercapai dalam {tahun} tahun!")