tampungan_barang = []

# Tambah barang
def tambah_barang():
    print(' TAMBAH BARANG ')
    while True :
        barang = input('Masukkan barang : ')
        if barang in tampungan_barang:
            print('Barang sudah tersedia')
            pass
        elif barang not in tampungan_barang:
            tampungan_barang.append(barang)
            pilihan = input("Tambahkan barang lagi? (y/n) : ")
            print("LIST BARANG".center(44,'='))
       
            if pilihan == 'y' :
                print("|","Kode".center(12, ' '),"|", "Nama Barang".center(15, ' '),"|","\n")
                for i in tampungan_barang :
                    print("+     ",(tampungan_barang.index(i)+1) ,"      |", (i).center(16, ' '),"+")        
            else : 
                break
                        
# Menghapus barang
def hapus_barang():
    print('Hapus barang'.center(44,'='))
    while True :
        hapus = input('Masukkan nama barang yang akan dihapus : ')
        if hapus in tampungan_barang :
            tampungan_barang.remove(hapus)
            lanjut = input('Tekan y jika lanjut : ').upper()
            if lanjut == "y" :
                hapus_barang()
            else :
                break
      
        else :
            print('Barang tidak tersedia')
            hapus_barang()

# mengedit barang :
def edit_barang() :
    print("LIST BARANG".center(44,'='))
    for i in tampungan_barang :
        print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
    while True :
        print('MENU EDIT BARANG'.center(44,'='))
        caribarang = input('Masukkan nama barang yang mau di edit : ')
        if caribarang in tampungan_barang :
            ubah_ke = input('Ubah ke : ')
            tampungan_barang[tampungan_barang.index(caribarang)] = ubah_ke
            for i in tampungan_barang :
                print("+ Kode Barang ".center(28," "),(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
            print("\n",'-'*50)
        else :
            print('Barang tidak ditemukan!')
            pass
        lanjut()
        
# lanjut
def lanjut():
    lanjut = input('Lanjut (y/n) : ')
    if lanjut == 'y' :
        pass
    else :
        menu()

# Cek Nama Barang
def nama_barang():
    print("LIST BARANG".center(44,'='))
    for i in tampungan_barang :
        print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
        
    exit = input('Tekan enter untuk keluar : ')
    if exit == ' ':
        menu()
    else :
        menu()

# Lihat barang
def daftar_barang():
    while True :
        print('MENU CEK BARANG'.center(44,'='))
        cek = input('Nama barang  : ')
        if cek in tampungan_barang :
            print(cek,'Tersedia!')
        else :
            print(cek,'Tidak tersedia!')
        lanjut = input('Cek lagi? (y/n) :')
        if lanjut == 'y' :
            daftar_barang()
        else :
            break
            
# Cek indeks
def cek_indeks():
        while True :
            print('MENU CEK INDEKS BARANG'.center(44,'='))
            cek = input('Masukkan nama barang  : ')
            if cek in tampungan_barang :
                print('Barang berada pada indeks :', tampungan_barang.index(cek))
            else :
                print('Barang tidak ada!')
            lanjut = input('Cek lagi? (y/n) :').upper()
            if lanjut == 'y' :
                pass
            else :
                break


# menu
def menu():
    while True :
        print('-'*44)
        print("PROGRAM BARANG".center(44,'='))
        print('''
        1. Tambah Barang
        2. Hapus Barang
        3. Edit Barang
        4. Cek Nama Barang
        5. Daftar Barang
        6. Indeks Barang ''')
        print('-'*44)
        
        pilihan = input("Pilih menu : ")
        print('-'*44)
        if pilihan == "1" :
            tambah_barang()
        elif pilihan == "2" :
            hapus_barang()
        elif pilihan == "3" :
            edit_barang()
        elif pilihan == "4" :
            daftar_barang()
        elif pilihan == "5" :
            nama_barang()
        elif pilihan == "6" :
            cek_indeks()
            
            A = False
            exit = input('Enter untuk keluar : ')
            if exit == ' ':
                break
        else :
            print(' TERIMA KASIH '.center(44,"+"))
            break
menu()