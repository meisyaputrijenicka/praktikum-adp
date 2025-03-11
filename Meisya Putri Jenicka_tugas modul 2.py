print("""==========================DAFTAR FILM BIOSKOP MEI'S CINEMA==================================            
      |---------------------------------------------------------------------|
      ||KODE|   JUDUL FILM BIOSKOP YANG TAYANG BULAN INI       |HARGA|      |
      |---------------------------------------------------------------------|
      ||01|      Harry Potter & The Chamber Of Secret        |Rp.60.000|    |
      ||02|                   Enchanted                      |Rp.55.000|    |
      ||03|        Jurassic World: Fallen Kingdom            |Rp.60.000|    |
      ||04|                    Frozen 2                      |Rp.60.000|    |
      ||05|                Pengabdi Setan                    |Rp.50.000|    |
      ||06|               Avengers: Endgame                  |Rp.60.000|    |
      ||07|               Mr.Bean's Holiday                  |Rp.55.000|    |
      |---------------------------------------------------------------------|""")

name= str(input("masukan nama anda: "))
codee =(input("kode film yang akan anda tonton : "))
add =int(input("jumlah tiket yang anda pesan: "))


if codee=="01":
    judul = "Harry Potter & The Chamber Of Secret"
    harsa = "Rp.60000"
    harga = int(60000*add,)
    print("Total Harga: Rp.",harga)
elif codee=="02":
    judul = "Enchanted"
    harsa = "Rp.55000"
    harga = int(55000*add)
    print("Total Harga: Rp.",harga)
elif codee=="03":
    judul = "Jurassic World: Fallen Kingdom"
    harsa = "Rp.60000"
    harga = int(60000*add)
    print("Total Harga: Rp.",harga)
elif codee=="04":
    judul = "Frozen 2 "
    harsa = "Rp.60000"
    harga = int(60000*add)
    print("Total Harga: Rp.",harga)
elif codee=="05":
    judul = "Pengabdi Setan"
    harsa = "Rp.50000"
    harga = int(50000*add)
    print("Total Harga: Rp.",harga)
elif codee=="06":
    judul = "Avengers: Endgame"
    harsa = "Rp.60000"
    harga = int(60000*add)
    print("Total Harga: Rp.",harga)
elif codee=="07":
    judul = "Mr.Bean's Holiday"
    harsa = "Rp.55000"
    harga = int(55000*add)
    print("Total Harga: Rp.",harga)
else  :
    judul = "Tidak tersedia"
    harsa = "Rp.0"
    harga = int(0*add)
    print("Total Harga: Rp.",harga)
    print ("kode film tidak tersedia, mohon memilih kode film yang tersedia")


if 100000< harga <=250000:
    diskon = int((15/100)*(harga))
    print("diskon:", diskon)
    total_harga = int(harga-diskon)
    print("harga setelah diskon:", total_harga)
elif harga>250000:
    diskon = int((35/100)*(harga))
    print("diskon:", diskon)
    total_harga = int(harga-diskon)
    print("harga setelah diskon:", total_harga)
else:
    diskon = 0
    print("diskon:",diskon)
    total_harga = int(harga-diskon)
    print("harga setelah diskon:", total_harga)


print("\n \nSTRUK PEMESANAN TIKET MEI'S CINEMA")


print(f"""
      \n==========================STRUK PEMESANAN TIKET MEI'S CINEMA=================================
      \n-----------------------------------------------------------------------
      \nNAMA PEMESAN                 : {name}                                       
      \nJUDUL FILM                   : {judul}                                       
      \nJUMLAH TIKET                 : {add}                                      
      \nHARGA SATUAN                 : {harsa}                                      
      \nDISKON                       : {diskon}                                      
      \nTOTAL HARGA (SETELAH DISKON) : {total_harga}
      \n                     ~~~ENJOY YOUR MOVIE<3~~~                         
      \n-----------------------------------------------------------------------
      """)