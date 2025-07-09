# admin_id = [{'username' : 'admin1', 'password' : '1234'}, {'username' : 'admin2', 'password' : '1234'}]


# while True:
#     username_admin = input('Masukkan username: ')
#     password_admin = input('Masukkan password: ')


#     for i in admin_id:
#         if username_admin == i['username'] and password_admin == i['password']:
#             print(f'Selamat datang {username_admin}')
#             break
            
#     else:
#         print('Username atau Password anda salah!')
#         continue
#     break

data_member = [ 
    {'id_member': 1, 'nama_depan': 'uriel', 'nama_belakang': 'siboro', 'umur': 26, 'sisa_membership_bulan': 12, 'sisa_sesi_pt': 0},
    {'id_member': 2, 'nama_depan': 'hugo', 'nama_belakang': 'pratama', 'umur': 26, 'sisa_membership_bulan': 8, 'sisa_sesi_pt': 0},
    {'id_member': 3, 'nama_depan': 'kevin', 'nama_belakang': 'putra', 'umur': 26, 'sisa_membership_bulan': 6, 'sisa_sesi_pt': 0}
]


def hapus():
    while True:
        input_id = int(input('masukkan id yang ingin di delete: '))
        for member in data_member:
            if member['id_member'] == input_id:
                konfirmasi = input(f"Yakin hapus {member['nama_depan']} {member['nama_belakang']}? (Y/N): ").lower()
                if konfirmasi == 'y':
                    data_member.remove(member)
                    for i in data_member:
                        print(f'{i['id_member'],i['nama_depan'], i['nama_belakang'], i['umur'], i['sisa_membership_bulan'], i['sisa_sesi_pt'] }')
                    return
                else:
                    print('Penghapusan dibatalkan.')
                    break 
        else: 
            print('ID tidak ditemukan. Silakan coba lagi.')
            continue

hapus()
