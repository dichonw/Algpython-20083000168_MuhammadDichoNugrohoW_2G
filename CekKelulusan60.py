jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("=========================")
    print(" CEK KELULUSAN DIATAS 60 ")
    print ("=========================")
    
    n = input(">> Masukkan Nilai = ")
    
    if int(n)>60:
        sts = "LULUS"
    else:
        sts="TIDAK LULUS"
    print(sts)

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break