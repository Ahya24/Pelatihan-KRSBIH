nama_all = []

while True:
    print("="*20)
    print("1. Masukan Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = int(input("Masukan Pilihan Anda : "))
    
    if pilihan == 1:
        print("Masukan Nama")
        nama = str(input("Nama : "))
        nama_all.append(nama)
        
    elif pilihan == 2:
        print("Data Mahasiswa")
        for i, j in enumerate(nama_all):
            print(f"{i + 1}. {j}")
            
    elif pilihan == 3:
        print("Ubah Nomer Berapa")
        nomer = int(input("No : "))
        nama_new = str(input("Nama : "))
        nama_all[nomer - 1] = nama_new
        
    elif pilihan == 4:
         print("Hapus Nomer Berapa")
         nomer_hps = int(input("No : "))
         nama_all.pop(nomer_hps - 1)
         
    elif pilihan == 5:
        print("Terima Kasih")
        break
