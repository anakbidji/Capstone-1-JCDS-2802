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



def admin_login():
    """ Fungsi admin_login digunakan untuk proses login sebagai admin FitClub. 
    Fungsi ini memulai dengan menanyakan konfirmasi apakah pengguna benar-benar ingin login sebagai admin. 
    Apabila setuju, pengguna diberikan maksimal 3 percobaan untuk memasukkan username dan password yang dicocokkan dengan data yang tersimpan di list admin_id.
    Jika berhasil login, fungsi akan mengembalikan data admin yang sesuai. 
    Jika gagal, pengguna diberikan pilihan untuk kembali ke menu utama atau mencoba lagi. 
    Apabila gagal login sebanyak 3 kali, sistem akan memberitahukan kegagalan dan mengembalikan pengguna ke menu utama."""
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




def menu_admin(admin):
    """ Fungsi menu_admin menyediakan menu khusus untuk admin setelah berhasil login. 
    Di menu ini, admin dapat melihat daftar member yang terdaftar, menghapus member, menambah member baru, atau kembali ke menu utama. 
    Fungsi ini berulang terus hingga admin memilih untuk keluar ke menu utama."""
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



def member_login():
    """ Fungsi member_login digunakan agar member FitClub dapat login ke sistem. 
    Member perlu mengonfirmasi ingin login sebagai member, lalu diberi hingga 3 kesempatan untuk memasukkan ID member (yang harus berupa angka) dan nama depan (dalam huruf kecil).
    Data tersebut divalidasi terhadap data_member yang sudah tersimpan. 
    Jika sesuai, fungsi mengembalikan data member. 
    Jika gagal login, member dapat memilih kembali ke menu utama atau mencoba lagi. 
    Setelah 3 kali gagal login, member diminta menunggu sebelum mencoba kembali. """
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



def menu_member(member):
    """ Fungsi menu_member menyediakan pilihan menu untuk member FitClub yang sudah login. 
    Di sini, member dapat memperpanjang masa aktif membership, menambah jumlah sesi personal trainer, mengecek sisa membership dan sesi PT, atau kembali ke menu utama. 
    Menu ini akan terus tampil hingga member memilih keluar. """
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



def non_member_menu():
    """ Fungsi non_member_menu adalah menu khusus bagi calon member yang belum terdaftar. 
    Calon member dapat mengecek daftar harga membership, melakukan pendaftaran membership baru, atau kembali ke menu utama. 
    Menu ini memberikan kemudahan bagi pengguna baru untuk mengenal layanan FitClub."""
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



def tambah_member():
    """Fungsi tambah_member hanya dapat diakses oleh admin. 
    Admin dapat menambahkan member baru dengan memasukkan ID yang unik, nama depan dan belakang, umur, jumlah bulan membership, serta jumlah sesi PT. 
    Fungsi ini memastikan bahwa ID member yang baru tidak boleh sama dengan ID yang sudah ada."""
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



def delete_member():
    """Fungsi delete_member hanya dapat digunakan oleh admin untuk menghapus member dari data_member. 
    Fungsi ini meminta admin untuk memasukkan ID member yang ingin dihapus. 
    Setelah ditemukan, sistem akan meminta konfirmasi sebelum benar-benar menghapus data member tersebut."""
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



def tunjukkan_member():
    """Fungsi tunjukkan_member menampilkan seluruh daftar member FitClub lengkap dengan ID, nama, umur, sisa membership, dan jumlah sesi PT. 
    Fungsi ini berguna agar admin maupun member dapat melihat informasi terkini mengenai member yang terdaftar."""
    print('\n=== Daftar Member FitClub ===')
    for m in data_member:
        print(f"ID: {m['id_member']} | Nama: {m['nama_depan']} {m['nama_belakang']} | Umur: {m['umur']} | Membership: {m['sisa_membership_bulan']} bulan | Sesi PT: {m['sisa_sesi_pt']}")



def tunjukkan_harga_membership():
    """Fungsi tunjukkan_harga_membership digunakan untuk menampilkan informasi semua paket membership yang tersedia di FitClub. 
    Setiap paket ditampilkan dengan nama, jumlah bulan membership, dan harga. 
    fungsi ini membantu calon member atau member untuk memilih paket yang sesuai."""
    print('\n=== Harga Membership ===')
    for p in informasi_paket:
        print(f"Paket {p['Nama Paket']}: {p['jumlah_bulan_membership']} bulan, Rp {p['Harga Membership']}")



def tunjukkan_harga_pt():
    """Fungsi tunjukkan_harga_pt digunakan untuk menampilkan semua paket Personal Trainer (PT) yang tersedia. 
    Sama seperti membership, setiap paket PT ditampilkan dengan nama, jumlah sesi, dan harga. 
    Fungsi ini membantu member untuk memutuskan paket PT yang sesuai dengan kebutuhan mereka."""
    print('\n=== Harga Personal Trainer ===')
    for pt in informasi_paket_pt:
        print(f"Paket {pt['Nama Paket']}: {pt['jumlah_sesi_pt']} sesi, Rp {pt['Harga pt']}")



def proses_pembayaran(harga):
    """Fungsi proses_pembayaran bertugas untuk menangani simulasi proses pembayaran. 
    Pengguna diminta memasukkan jumlah uang yang dibayarkan, lalu dihitung apakah jumlah tersebut mencukupi atau tidak.
    Jika uang pas atau lebih, transaksi dianggap berhasil dan kembalian ditampilkan jika ada. 
    Fungsi ini memastikan pembayaran berhasil sebelum melanjutkan proses selanjutnya."""
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
    """Fungsi daftar_member_baru digunakan bagi calon member (non-member) yang ingin mendaftar membership FitClub. 
    Calon member memilih paket membership, melakukan konfirmasi, dan membayar sesuai harga paket. 
    Jika pembayaran berhasil, data member baru akan ditambahkan ke data_member."""  
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



def payment_member(member):
    """Fungsi payment_member digunakan untuk memperpanjang membership member yang sudah terdaftar. 
    Member dapat memilih paket membership, lalu melakukan konfirmasi dan pembayaran. 
    Jika pembayaran berhasil, jumlah bulan membership member akan ditambahkan sesuai paket yang dipilih."""
    tunjukkan_harga_membership()
    while True:
        nama_paket = input('Pilih paket: ').lower().strip()
        for paket in informasi_paket:
            if nama_paket == paket['Nama Paket']:
                bulan = paket['jumlah_bulan_membership']
                harga = paket['Harga Membership']
                konfirmasi_input = input(f'Apakah anda yakin memilih paket {nama_paket}? (y atau n): ').lower()
                if konfirmasi_input == 'n':
                    return

                if proses_pembayaran(harga) == 'berhasil':
                    member['sisa_membership_bulan'] += bulan
                    print(f"\nMembership anda diperpanjang menjadi {member['sisa_membership_bulan']} bulan")
                    return 
                else:
                    continue
        print('Nama paket tidak ditemukan.')
            
            


def payment_member_pt(member):
    """Fungsi payment_member_pt digunakan untuk menambah jumlah sesi personal trainer (PT) bagi member. 
    Member dapat memilih paket PT yang tersedia, lalu melakukan pembayaran. 
    Setelah berhasil, jumlah sesi PT member akan ditambah sesuai paket yang dipilih."""
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



def input_id_unik():
    """Fungsi input_id_unik memastikan bahwa saat menambah member baru (baik oleh admin atau saat pendaftaran), ID member yang dimasukkan harus unik dan belum digunakan. 
    Fungsi ini akan meminta input ulang jika ID sudah dipakai oleh member lain."""
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

     
def main_menu():
    """Fungsi main_menu adalah pusat navigasi utama program FitClub. 
    Pengguna dapat memilih login sebagai admin, login sebagai member, mengakses menu non-member, atau keluar dari program.
    Fungsi ini selalu kembali menampilkan pilihan menu setelah selesai menjalankan fungsi lain, kecuali jika pengguna memilih keluar."""  
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
