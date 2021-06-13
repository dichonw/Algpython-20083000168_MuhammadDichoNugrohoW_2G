jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("===========================================")
    print(" PENILAIAN MAHASISWA AKAN MENDAPAT HURUF 'X' ")
    print ("===========================================")
    
    n = input(">> Masukkan Nilai = ")
    
    if int(n)>100:
        sts = "BATAS INPUTAN HANYA SAMPAI 100"
    elif int(n)>=91 and int(n)<100:
        sts = "A"
    elif int(n)>=81 and int(n)<91:
        sts = "B"
    elif int(n)>=71 and int(n)<81:
        sts = "C"
    elif int(n) < 40:
        sts = "D"
    else:
        sts="INPUTAN TIDAK TERDEFINISI"
    print(">> Nilai Anda = " + str(sts))

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break