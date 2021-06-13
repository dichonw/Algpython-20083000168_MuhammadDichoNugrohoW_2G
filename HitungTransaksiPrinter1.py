jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("===================================================")
    print(" HITUNG TOTAL TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
    print ("===================================================")
    
    hrgPrinter = 660000
    
    n = input(">> Masukkan Jumlah = ")
    
    totalHarga = int(n) * int(hrgPrinter)
    
    print(">> Total Harga  = Rp. " + str(totalHarga))

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break