print("""
            f(x) = 4x^3 + 7x - 5,  x >= 0
                 = 3x^2 - 5x +1,   x < 0
                g(x) = (f(x))^2 - f(x)
                  h(x) = f(x) * g(x) """)

n = int(input("masukan nilai n: "))

x  = []
f  = []
g  = []
h  = []
no = []

for i in range(n):
    nomor = i+1
    x_ = int(input(f"masukan nilai x ke-{i+1} : "))
    x.append(x_)
    if x_ >= 0:
        fx = 4*(x_**3) + 7*x_ - 5
    else:
        fx = 3*(x_**2) - 5*x_ +1

    f.append(fx)
    gx = (fx**2) - fx
    g.append(gx)
    hx = fx * gx
    h.append(hx)
    no.append(nomor)

print("\nOutput:")
print("|No.|\t|x|\t|f(x)|\t|g(x)|\t|h(x)|")

for i in range(n):
    print(f"| {i+1} |\t|{x[i]}|\t|{f[i]}|\t|{g[i]}|\t|{h[i]}|")

while True:
    lagi = input("Input nilai x lagi? (Y/N): ").strip().upper()
    if lagi == 'Y':
        x_ = int(input("masukan nilai x : "))
        x.append(x_)
        f.append(fx)
        gx = (fx**2) - fx
        g.append(gx)
        hx = fx * gx
        h.append(hx)
        
        print("\nOutput:")
        print(f"f({x_}) = {fx}, g({x_}) = {gx}, h({x_}) = {hx}")
    elif lagi == 'N':
        print("Terima kasih!")
        break
    else:
        print("Input tidak valid, silakan masukkan Y atau N.")