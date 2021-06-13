jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("===================")
    print(" CEK TINGKAT USIA ")
    print ("===================")
    
    n = input(">> Masukkan Usia = ")
    
    if int(n)>60:
        sts = "LANSIA"
    elif int(n) >= 35 and int(n) <= 59:
        sts = "DEWASA"
    elif int(n) >= 18 and int(n) <= 34:
        sts = "PEMUDA"
    elif int(n) >= 15 and int(n) <= 17:
        sts = "REMAJA"
    else:
        sts="ANAK ANAK"
    print(sts)

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break