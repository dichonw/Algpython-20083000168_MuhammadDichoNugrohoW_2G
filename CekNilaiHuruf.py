jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("========================")
    print(" MENAMPILKAN NILAI HURUF ")
    print ("========================")
    
    n = input(">> Masukkan Nilai = ")
    
    if int(n)>100:
        sts = "BATAS INPUTAN HANYA SAMPAI 100"
    elif int(n)>80:
        sts = "BAIK SEKALI"
    elif int(n) >= 65:
        sts = "BAIK"
    elif int(n) >= 55:
        sts = "CUKUP"
    elif int(n) >= 40:
        sts = "KURANG"
    elif int(n) < 40:
        sts = "KURANG SEKALI"
    else:
        sts="INPUTAN TIDAK TERDEFINISI"
    print(sts)

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break