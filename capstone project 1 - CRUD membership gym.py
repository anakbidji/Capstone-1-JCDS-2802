admin_id = {'admin1': '1234', 'admin2': '4321'}

def admin_login():
    for attempt in range(3):
        print('\n=== Selamat Datang Admin FitClub ===\n')
        username = input('Masukkan username anda: ')
        password = input('Masukkan password anda: ')

       
        if username in admin_id and password == admin_id[username]:
            print(f'\nLogin berhasil! Selamat datang {username}\n!')
            return username
        else:
            print('\nUsername atau Password yang anda masukkan salah!\n')
            input_utama = input('Apakah anda ingin kembali ke menu utama? (Y atau N): ').lower()
            if input_utama == 'y':
                return main_menu()
            else:
                continue
            
    else:
        print('Anda gagal login 3 kali, silahkan tunggu 5 menit sebelum login!')
    

def menu_admin(admin):
        if admin:
            while True:
                print('\n=== Daftar Menu ===')
                print('1. Lihat Informasi Member')
                print('2. Hapus Member')
                print('3. Tambah Member')
                print('4. Logout')
                input_menu_admin = input('Masukkan pilihan menu (1-4): ')
                if input_menu_admin == '1':
                    tunjukkan_member()
                
                elif input_menu_admin == '2':
                    delete_member()

                elif input_menu_admin == '3':
                    tambah_member()
                    
                elif input_menu_admin == '4':
                    print('Logout berhasil. Sampai jumpa!')
                    return main_menu()



def member_login():
    for attemp in range(3):
        print('\n=== Selamat Datang Member FitClub! ===\n')
        while True:
            try:
                id_member_input = int(input('Masukkan id member anda: '))
                break
            except ValueError:
                print('id member harus berupa angka!')

        nama_member_input = input('Masukkan nama anda: ').lower()

      
        for member in data_member:
            if nama_member_input == member['nama_member'] and id_member_input == member['id_member']:
                return member
                          
        else:
            print('\nid atau nama yang anda masukkan salah!\n')
            inpututama = input('Apakah anda ingin kembali ke menu utama? (Y atau N): ').lower
            if inpututama == 'y':
                return main_menu()
            else:
                continue
    else:
        print('\nAnda gagal login 3 kali. Silahkan tunggu 5 menit sebelum login!\n')

def menu_member(member):
    if member: 
        while True:
            print('\n=== Daftar Menu ===')
            print('1. Perpanjang Membership')
            print('2. Perpanjang Sesi Personal Trainer')
            print('3. Cek Sisa Membership dan Sisa Sesi Personal Trainer')
            print('4. Logout')
            input_menu_member = input('Masukkan pilihan menu (1-4): ').strip()
            print('\n')

            if input_menu_member == '1':
                payment_member(member)

            elif input_menu_member == '2':
                payment_member_pt(member)

            elif input_menu_member == '3':
                print(f'Membership anda tersisa: {member['sisa_membership_bulan']} bulan')
                print(f'Sesi Personal Trainer anda tersisa sebanyak: {member['sisa_sesi_pt']}')
            
            elif input_menu_member == '4':
                print('Logout berhasil. Sampai jumpa!')
                return main_menu()
            else:
                print('Pilihan tidak valid.')
    else:
        print('Login gagal. Program dihentikan.')


def non_member_menu():
    while True:
        print('\n=== Daftar Menu ===')
        print('1. Cek Harga Membership')
        print('2. Daftar Membership')
        print('3. Menu Utama')
        input_non_member = input('Masukkan pilihan menu (1-3): ')
        if input_non_member == '1':
            tunjukkan_harga_membership()
        if input_non_member == '2':
            tunjukkan_harga_membership()
            nama_paket = input('Pilih nama paket yang diinginkan: ').lower()
            for payment in informasi_paket:
                if nama_paket == payment['Nama Paket'].lower():
                    harga = payment['Harga Membership']
                    bulan = payment['jumlah_bulan_membership']
                    hasil = proses_pembayaran(harga)
                    if hasil == 'berhasil':
                        nama_member_baru = input('Masukkan nama anda: ')

                        while True:
                            try:
                                input_id = int(input('Masukkan ID anda: '))
                            except ValueError:
                                print('ID harus berupa angka!')
                                continue
                            id_sudah_dipakai = any(member['id_member'] == input_id for member in data_member)
                            if id_sudah_dipakai:
                                print(f'ID {input_id} sudah digunakan!')
                                print('ID yang sudah terpakai:')
                                for i in data_member:
                                    print(f'-{i['id_member']}')
                                continue
                            else:
                                break

                        while True:
                            try:
                                umur_member_baru = int(input('Masukkan umur anda: '))
                                break
                            except ValueError:
                                print('Umur harus berupa angka!')
                            continue

                        data_member_baru = {'id_member': input_id, 
                                            'nama_member': nama_member_baru, 
                                            'umur': umur_member_baru, 
                                            'sisa_membership_bulan': bulan, 
                                            'sisa_sesi_pt': 0}
                        
                        data_member.append(data_member_baru)
                        tunjukkan_member()
            else:
                print('Nama paket tidak ditemukan! Pilih nama paket yang tersedia!')
                continue


        if input_non_member == '3':
            return main_menu()
                    






data_member = [ 
    {'id_member': 1,
     'nama_member': 'uriel',
     'umur': 26,
     'sisa_membership_bulan': 12,
     'sisa_sesi_pt': 0},
     
    {'id_member': 2,
     'nama_member': 'hugo',
     'umur': 26,
     'sisa_membership_bulan': 8,
     'sisa_sesi_pt': 0},

    {'id_member': 3,
     'nama_member': 'kevin',
     'umur': 26,
     'sisa_membership_bulan': 6,
     'sisa_sesi_pt': 0}
]

        
informasi_paket = [
    {'Nama Paket': 'pro',
        'Harga Membership': 1_000_000,
     'jumlah_bulan_membership': 12 },
     {'Nama Paket': 'atlit',
         'Harga Membership': 600_000,
     'jumlah_bulan_membership': 6 },
     {'Nama Paket': 'pemula',
         'Harga Membership': 400_000,
     'jumlah_bulan_membership': 3 }
]

informasi_paket_pt = [
    {'Nama Paket': 'binaragawan',
     'Harga pt': 1_000_000,
     'jumlah_sesi_pt': 12 },
     {'Nama Paket': 'olahragawan',
         'Harga pt': 600_000,
     'jumlah_sesi_pt': 6 },
     {'Nama Paket': 'pemula',
         'Harga pt': 400_000,
     'jumlah_sesi_pt': 3 }
]

def delete_member():
    print("\n=== Daftar Member Saat Ini ===")
    for i in data_member:
        print(f"ID Member: {i['id_member']} | Nama: {i['nama_member']} | Umur: {i['umur']} | "
              f"Membership: {i['sisa_membership_bulan']} bulan | Sesi PT: {i['sisa_sesi_pt']}")

    try:
        input_delete = int(input('\nMasukkan ID Member yang ingin dihapus: '))
    except ValueError:
        print("Input harus berupa angka!")
        return

    # Cek apakah ID member ditemukan
    for i, member in enumerate(data_member):
        if member['id_member'] == input_delete:
            konfirmasi = input(f"Yakin ingin menghapus member '{member['nama_member']}'? (Y atau N): ").lower()
            if konfirmasi == 'y':
                del data_member[i]
                print("Member berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            return  # sangat penting! keluar setelah hapus

    print("ID Member tidak ditemukan.")

def tambah_member():
    while True:
        try:
            input_id = int(input('Masukkan ID member baru: '))
        except ValueError:
            print('ID harus berupa angka!')
            continue

        id_sudah_dipakai = any(member['id_member'] == input_id for member in data_member)
        if id_sudah_dipakai:
            print(f"ID {input_id} sudah digunakan!")
            print("ID yang sudah terpakai:")
            for i in data_member:
                print(f"- {i['id_member']}")
            continue  # kembali minta input ID baru
        else:
            break  # keluar dari loop jika ID valid

    
    nama_baru = input('Masukkan nama member baru: ')
    while True:
        try:
            umur_baru = int(input('Masukkan umur member baru: '))
            break
        except ValueError:
            print('umur harus berupa angka!')
            continue
    while True:
        try:
            membership_bulan_baru = int(input('Masukkan jumlah bulan membership: '))
            break
        except ValueError:
            print('umur harus berupa angka!')
            continue
    while True:
        try:
            sesi_pt_baru = int(input('Masukkan jumlah sesi PT baru: '))
            break
        except ValueError:
            print('umur harus berupa angka!')
            continue
    
    data_member_baru = {'id_member': input_id,
     'nama_member': nama_baru,
     'umur': umur_baru,
     'sisa_membership_bulan': membership_bulan_baru,
     'sisa_sesi_pt': sesi_pt_baru}
    
    konfirmasi = input('Apakah kamu yakin mau memasukkan data member tersebut?(Y atau N): ').lower()
    if konfirmasi == 'y':
        data_member.append(data_member_baru)
    else:
        return menu_admin()



def tunjukkan_harga_membership():
    for paket in informasi_paket: #Loop untuk menunjukan informasi paket membership
        print(f'Paket {paket['Nama Paket']} menawarkan langganan {paket['jumlah_bulan_membership']} bulan, seharga Rp {paket['Harga Membership']}\n')

def tunjukkan_harga_pt():
    for pt in informasi_paket_pt: #Loop untuk menunjukan informasi paket membership
        print(f'Paket {pt['Nama Paket']} menawarkan sesi sebanyak {pt['jumlah_sesi_pt']} sesi, seharga Rp {pt['Harga pt']}\n')

def tunjukkan_member():
    print('=== Daftar Member FitClub ===')
    for i in data_member:
        print(f'ID Member: {i['id_member']} | Nama: {i['nama_member']} | Umur Member: {i['umur']} | Jumlah Bulan Membership: {i['sisa_membership_bulan']} | Jumlah Sesi PT: {i['sisa_sesi_pt']}')

def proses_pembayaran(harga):
    print(f"\nTotal yang harus dibayar: Rp {harga}")
    try:
        jumlah_uang = int(input("Masukkan jumlah uang Anda: Rp "))
        if jumlah_uang < harga:
            kurang = harga - jumlah_uang
            print(f"Uang anda kurang sebesar Rp {kurang}. Transaksi dibatalkan.")
            return 'gagal'
        else:
            kembalian = jumlah_uang - harga
            if kembalian > 0:
                print(f"Pembayaran berhasil. Kembalian anda: Rp {kembalian}")
            else:
                print("Pembayaran pas. Terima kasih.")
            return 'berhasil'
    except ValueError:
        print("Input harus berupa angka. Transaksi dibatalkan.")
        return 'gagal'

def payment_member(member):
    tunjukkan_harga_membership()
    for attempt in range(100):
        nama_paket = input('Masukkan nama paket yang diinginkan: ').lower()

        for payment in informasi_paket:
            if nama_paket == payment['Nama Paket'].lower():
                harga = payment['Harga Membership']
                hasil = proses_pembayaran(harga)

                if hasil == 'berhasil':
                    bulan = payment['jumlah_bulan_membership']
                    member['sisa_membership_bulan'] += bulan
                    print(f"\nTransaksi berhasil. Membership anda sekarang: {member['sisa_membership_bulan']} bulan")
                else:
                    print("Transaksi gagal. Silakan coba lagi.")
                return menu_member(member)

        print("Nama paket tidak ditemukan. Silakan coba lagi.\n")
    

def payment_member_pt(member):
    tunjukkan_harga_pt()
    for attempt in range(100):
        nama_paket_pt = input('Masukkan nama paket Personal Trainer yang diinginkan: ').lower()

        for payment_pt in informasi_paket_pt:
            if nama_paket_pt == payment_pt['Nama Paket'].lower():
                harga = payment_pt['Harga pt']
                hasil = proses_pembayaran(harga)

                if hasil == 'berhasil':
                    sesi = payment_pt['jumlah_sesi_pt']
                    member['sisa_sesi_pt'] += sesi
                    print(f"\nTransaksi berhasil. Sisa sesi Personal Trainer anda: {member['sisa_sesi_pt']} sesi")
                else:
                    print("Transaksi gagal. Silakan coba lagi.")
                return menu_member(member)

        print("Nama paket tidak ditemukan. Silakan coba lagi.\n")



def main_menu():
    print('\n=== Selamat Datang Di FitClub! ===\n')
    print('1. Admin')
    print('2. Member')
    print('3. Non-Member')
    input_main_menu = input('Pilih login sesuai credential anda: ')
    while True:
        if input_main_menu == '1':
            admin = admin_login()
            if admin:
                menu_admin(admin)
            else:
                break
        
        if input_main_menu == '2':
            member = member_login()
            if member:
                menu_member(member)
            else:
                break

        if input_main_menu == '3':
            non_member_menu()

            

main_menu()
