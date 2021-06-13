jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("===================================================")
    print(" HITUNG TOTAL TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
    print ("===================================================")
    
    hrgPrinter = 660000
    
    n = input(">> Masukkan Jumlah Printer = ")
    
    totalHarga = int(n) * float(hrgPrinter)
    
    print(">> Total Harga Printer = Rp. " + str(totalHarga))
    
    if int(totalHarga) > 1500000:
        diskon = 0.15
    else:
        diskon = 0
    
    totalDikson = totalHarga * diskon
    
    print(">> Total Diskon = Rp. " + str(totalDikson))
    
    totalTransaksi = totalHarga - totalDikson
    
    print(">> Total Transaksi = Rp. " + str(totalTransaksi))

    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break