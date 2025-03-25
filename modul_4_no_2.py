while True:
    password = input("Masukan password: ")
    if len(password) < 8:
        print("Password harus minimal 8 karakter")
    else:
        huruf_kapital = False
        huruf_kecil = False
        angka = False
        karakter_khusus = False
        for i in password:
            if  'A'<= i <= 'Z':
                huruf_kapital = True
            elif 'a'<= i <= 'z':
                huruf_kecil = True
            elif '0'<= i <= '9':
                angka = True
            elif i in """!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~""":
                karakter_khusus = True
        if huruf_kapital == False:
            print("Password harus memuat setidaknya 1 huruf kapital.")
        if huruf_kecil == False:
            print("Password harus memuat setidaknya 1 huruf kecil.")
        if angka == False:
            print("Password harus memuat setidaknya 1 angka.")
        if karakter_khusus == False:
            print("Password harus memuat setidaknya 1 karakter khusus.")
        if huruf_kecil and huruf_kapital and angka and karakter_khusus:
            print("Password valid")
            break