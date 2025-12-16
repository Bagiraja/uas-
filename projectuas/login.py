from pembeli import main as pembeli_main
from penjual import main as penjual_main
from menu import judul




datapenjual = {
    'user1':'pw1', 
    'user2':'pw2',

}

def optionslogin():
     while True:
          judul('SELAMAT DATANG DI HOTROD')
          print('1.Penjual')
          print('2.Pembeli')
          Pilih = input('pilih: ')

          if Pilih == "1":
            login()
          else:
            judul('SILAKAN MASUKAN NAMA ANDA')
            nama = input('Masukan Nama:')

            pembeli_main()


def login():
    judul('\t\t       LOGIN')
    username = input('Masukan Username:')
    password = input('Masukan Password:')

    if username in datapenjual and datapenjual[username] == password:
        print('login kehalaman penjual berhasil')
        penjual_main()

    else:
        print('password atau username salah')


         
       
       



if __name__ =='__main__':
        optionslogin()
