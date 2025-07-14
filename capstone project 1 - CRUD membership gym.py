# Daftar akun admin beserta passwordnya
admin_id = [{'username' : 'admin1', 'password' : '1234'}, {'username' : 'admin2', 'password' : '1234'}]

# Data member FitClub, masing-masing berisi ID unik, nama, umur, membership, dan sesi PT
data_member = [ 
    {'id_member': 1, 'nama_depan': 'uriel', 'nama_belakang': 'siboro', 'umur': 26, 'sisa_membership_bulan': 12, 'sisa_sesi_pt': 0},
    {'id_member': 2, 'nama_depan': 'hugo', 'nama_belakang': 'pratama', 'umur': 26, 'sisa_membership_bulan': 8, 'sisa_sesi_pt': 0},
    {'id_member': 3, 'nama_depan': 'kevin', 'nama_belakang': 'putra', 'umur': 26, 'sisa_membership_bulan': 6, 'sisa_sesi_pt': 0}
]

# Paket membership yang tersedia
informasi_paket = [
    {'Nama Paket': 'pro', 'Harga Membership': 1_000_000, 'jumlah_bulan_membership': 12},
    {'Nama Paket': 'atlit', 'Harga Membership': 600_000, 'jumlah_bulan_membership': 6},
    {'Nama Paket': 'pemula', 'Harga Membership': 400_000, 'jumlah_bulan_membership': 3}
]

# Paket Personal Trainer yang tersedia
informasi_paket_pt = [
    {'Nama Paket': 'binaragawan', 'Harga pt': 1_000_000, 'jumlah_sesi_pt': 12},
    {'Nama Paket': 'olahragawan', 'Harga pt': 600_000, 'jumlah_sesi_pt': 6},
    {'Nama Paket': 'pemula', 'Harga pt': 400_000, 'jumlah_sesi_pt': 3}
]

# Fungsi login untuk admin, maksimal 3 percobaan
def admin_login():
    while True:
        input_konfirmasi = input('Apakah anda yakin login menggunakan credential admin? (y atau n): ').lower().strip()
        if input_konfirmasi == 'n':
            return
        elif input_konfirmasi == 'y':
            for attempt in range(3):
                print('\n=== Selamat Datang Admin FitClub ===\n')
                username_admin = input('Masukkan username anda: ')
                password_admin = input('Masukkan password anda: ')

                # Cek username dan password sesuai admin_id
                for admin in admin_id:
                    if username_admin == admin['username'] and password_admin == admin['password']:
                        print(f'\nLogin berhasil! Selamat datang {username_admin}!\n')
                        return admin
                else:
                    print('\nUsername atau Password salah!\n')
                    while True:
                        input_utama = input('Kembali ke menu utama? (Y atau N): ').lower().strip()
                        if input_utama == 'y':
                            return main_menu()
                        elif input_utama == 'n':
                            break
                        else:
                            print('input harus y atau n!')
                            continue
            else:
                print('Anda gagal login 3 kali, silahkan tunggu 5 menit sebelum login!')
                return
        else:
            print('input harus y atau n!')
            continue


# Menu khusus admin: lihat member, hapus, tambah, logout
def menu_admin(admin):
    while True:
        print('\n=== Menu Admin ===')
        print('1. Lihat Informasi Member')
        print('2. Hapus Member')
        print('3. Tambah Member')
        print('4. Menu Utama')
        input_menu = input('Masukkan pilihan (1-4): ')
        if input_menu == '1':
            tunjukkan_member()
        elif input_menu == '2':
            delete_member()
        elif input_menu == '3':
            tambah_member()
        elif input_menu == '4':
            return 
        else:
            print('Pilihan tidak valid.')


# Fungsi login untuk member: validasi nama_depan dan id_member
def member_login():
    while True:
        input_konfirmasi = input('Apakah anda yakin login menggunakan credential member? (y atau n): ').lower().strip()
        if input_konfirmasi == 'n':
            return
        elif input_konfirmasi == 'y':            
            for attempt in range(3):
                print('\n=== Selamat Datang Member FitClub! ===\n')
                while True:
                    try:
                        id_member_input = int(input('Masukkan ID member anda: '))
                        break
                    except ValueError:
                        print('ID harus berupa angka!')

                nama_depan_input = input('Masukkan nama depan anda: ').lower().strip()

                # Cari member yang cocok
                for member in data_member:
                    if member['id_member'] == id_member_input and member['nama_depan'] == nama_depan_input:
                        return member
                else:
                    print('ID atau nama depan salah!\n')
                    while True:
                        input_utama = input('Kembali ke menu utama? (Y atau N): ').lower().strip()
                        if input_utama == 'y':
                            return main_menu() 
                        elif input_utama == 'n':
                            break
                        else:
                            print('Input harus y atau n!')
                            continue

            else:
                print('Gagal login 3 kali, silakan tunggu 5 menit.')
                return
        else:
            print('Input harus y atau n!')
            continue

# Menu member: perpanjang membership, perpanjang PT, cek sisa, logout
def menu_member(member):
    while True:
        print('\n=== Menu Member ===')
        print('1. Perpanjang Membership')
        print('2. Perpanjang Sesi Personal Trainer')
        print('3. Cek Sisa Membership dan Sesi PT')
        print('4. Menu Utama')
        input_menu = input('Masukkan pilihan (1-4): ')
        if input_menu == '1':
            payment_member(member)
        elif input_menu == '2':
            payment_member_pt(member)
        elif input_menu == '3':
            print(f"\nMembership tersisa: {member['sisa_membership_bulan']} bulan")
            print(f"Sesi PT tersisa: {member['sisa_sesi_pt']} sesi")
        elif input_menu == '4':
            return
        else:   
            print('Pilihan tidak valid.')

# Menu untuk non-member: cek harga membership, daftar, atau kembali ke main menu
def non_member_menu():
    while True:
        print('\n=== Menu Non-Member ===')
        print('1. Cek Harga Membership')
        print('2. Daftar Membership')
        print('3. Menu Utama')
        pilihan = input('Masukkan pilihan (1-3): ')
        if pilihan == '1':
            tunjukkan_harga_membership()
        elif pilihan == '2':
            daftar_member_baru()
        elif pilihan == '3':
            return 

# Fungsi menambah member (khusus admin)
def tambah_member():
    input_id = input_id_unik()
    nama_depan = input('Masukkan nama depan: ').lower().strip()
    nama_belakang = input('Masukkan nama belakang: ').lower().strip()
    while True:
        try:
            umur = int(input('Masukkan umur: '))
            if umur < 12:
                print('Umur harus minimal 12 tahun!')
                continue
            break
        except ValueError:
            print('Umur harus berupa angka!')
    while True:
        try:
            bulan = int(input('Masukkan bulan membership: '))
            break
        except ValueError:
            print('Input harus angka!')

    while True:
        try:
            sesi = int(input('Masukkan jumlah sesi PT: '))
            break
        except ValueError:
            print('Input harus angka!')
    # Tambahkan ke data_member
    data_member.append({
        'id_member': input_id,
        'nama_depan': nama_depan,
        'nama_belakang': nama_belakang,
        'umur': umur,
        'sisa_membership_bulan': bulan,
        'sisa_sesi_pt': sesi
    })
    print('Member baru berhasil ditambahkan!')

# Fungsi hapus member
def delete_member():
    while True:
        tunjukkan_member()
        try:
            input_id = int(input('Masukkan ID member yang ingin dihapus: '))
        except ValueError:
            print('ID harus angka!')
            continue 

        # Cari member sesuai ID
        for member in data_member:
            if member['id_member'] == input_id:
                konfirmasi = input(f"Yakin hapus {member['nama_depan']} {member['nama_belakang']}? (Y/N): ").lower().strip()
                if konfirmasi == 'y':
                    data_member.remove(member)
                    print('Member dihapus.')
                else:
                    print('Penghapusan dibatalkan.')
                return  
        print('ID tidak ditemukan. Silakan coba lagi.')

# Menampilkan daftar member
def tunjukkan_member():
    print('\n=== Daftar Member FitClub ===')
    for m in data_member:
        print(f"ID: {m['id_member']} | Nama: {m['nama_depan']} {m['nama_belakang']} | Umur: {m['umur']} | Membership: {m['sisa_membership_bulan']} bulan | Sesi PT: {m['sisa_sesi_pt']}")

# Menampilkan harga membership
def tunjukkan_harga_membership():
    print('\n=== Harga Membership ===')
    for p in informasi_paket:
        print(f"Paket {p['Nama Paket']}: {p['jumlah_bulan_membership']} bulan, Rp {p['Harga Membership']}")

# Menampilkan harga Personal Trainer
def tunjukkan_harga_pt():
    print('\n=== Harga Personal Trainer ===')
    for pt in informasi_paket_pt:
        print(f"Paket {pt['Nama Paket']}: {pt['jumlah_sesi_pt']} sesi, Rp {pt['Harga pt']}")

# Fungsi untuk proses pembayaran
def proses_pembayaran(harga):
    print(f"Total harus dibayar: Rp {harga}")
    while True:
        try:
            bayar = int(input('Masukkan jumlah uang anda: Rp '))
            kurang = harga - bayar
            if bayar < harga:
                print(f'Uang kurang Rp {kurang}')
                # ulangi input
                continue
            kembalian = bayar - harga
            if kembalian > 0:
                print(f"\nTransaksi berhasil. Kembalian: Rp {kembalian}")
            else:
                print("\nPembayaran pas.")
            return 'berhasil'
        except ValueError:
            print('Input harus angka.')

def daftar_member_baru():
    tunjukkan_harga_membership()
    while True:
        nama_paket = input('Pilih nama paket: ').lower().strip()
        for paket in informasi_paket:
            if nama_paket == paket['Nama Paket']:
                harga = paket['Harga Membership']
                bulan = paket['jumlah_bulan_membership']
                konfirmasi_input = input(f'Apakah anda yakin memilih paket {nama_paket}? (y atau n): ').lower().strip()
                if konfirmasi_input == 'n':
                    return
                if proses_pembayaran(harga) == 'berhasil':
                    input_id = input_id_unik()
                    nama_depan = input('Masukkan nama depan anda: ').lower().strip()
                    nama_belakang = input('Masukkan nama belakang anda: ').lower().strip()
                    while True:
                        try:
                            umur = int(input('Masukkan umur anda: '))
                            if umur < 12:
                                print('Umur harus minimal 12 tahun!')
                                continue
                            break
                        except ValueError:
                            print('Umur harus berupa angka!')
                    # Tambahkan ke data_member
                    data_member.append({
                        'id_member': input_id,
                        'nama_depan': nama_depan,
                        'nama_belakang': nama_belakang,
                        'umur': umur,
                        'sisa_membership_bulan': bulan,
                        'sisa_sesi_pt': 0
                    })
                    print('Pendaftaran berhasil!')
                    tunjukkan_member()
                    return
                else:
                    print('Pembayaran gagal.')
                    continue
        else:
            print('Nama paket tidak ditemukan.')

# Perpanjang membership (untuk member)
def payment_member(member):
    tunjukkan_harga_membership()
    while True:
        nama_paket = input('Pilih paket: ').lower().strip()
        for paket in informasi_paket:
            if nama_paket == paket['Nama Paket']:
                bulan = paket['jumlah_bulan_membership']
                harga = paket['Harga Membership']
                konfirmasi_input = input(f'Apakah anda yakin memilih paket {nama_paket}? (y atau n): ').lower().strip()
                if konfirmasi_input == 'n':
                    return

                if proses_pembayaran(harga) == 'berhasil':
                    member['sisa_membership_bulan'] += bulan
                    print(f"\nMembership anda diperpanjang menjadi {member['sisa_membership_bulan']} bulan")
                    return 
                else:
                    continue
        print('Nama paket tidak ditemukan.')
            
            
# Perpanjang sesi PT (untuk member)
def payment_member_pt(member):
    tunjukkan_harga_pt()
    while True:
        nama_paket = input('Pilih paket PT: ').lower().strip()
        for paket_pt in informasi_paket_pt:
            if nama_paket == paket_pt['Nama Paket']:
                bulan = paket_pt['jumlah_sesi_pt']
                harga = paket_pt['Harga pt']
                konfirmasi_input = input(f'Apakah anda yakin memilih paket {nama_paket}? (y atau n): ').lower().strip()
                if konfirmasi_input == 'n':
                    return
                if proses_pembayaran(harga) == 'berhasil':
                    member['sisa_sesi_pt'] += bulan
                    print(f'\nSesi PT anda diperpanjang menjadi {member['sisa_sesi_pt']} sesi')
                    return
                else:
                    continue
        print('Nama paket tidak ditemukan.')

# Validasi input ID baru (pastikan unik)
def input_id_unik():
    while True:
        try:
            input_id = int(input('Masukkan ID member baru: '))
        except ValueError:
            print('ID harus berupa angka!')
            continue

        if any(m['id_member'] == input_id for m in data_member):
            print(f'ID {input_id} sudah digunakan!')
            print('ID yang sudah terpakai:')
            for m in data_member:
                print(f"{m['id_member']}")
            continue  
        else:
            return input_id

# Menu utama program       
def main_menu():
    while True:
        print('\n=== Selamat Datang di FitClub ===')
        print('1. Admin')
        print('2. Member')
        print('3. Non-Member')
        print('4. Exit Program')
        pilihan = input('Pilih (1-4): ')
        if pilihan == '1':
            admin = admin_login()
            if admin:
                menu_admin(admin)
        elif pilihan == '2':
            member = member_login()
            if member:
                menu_member(member)
        elif pilihan == '3':
            non_member_menu()
        elif pilihan == '4':
            print('Terima kasih! Program selesai.')
            return
        else:
            print('Pilihan tidak valid.')

main_menu()
