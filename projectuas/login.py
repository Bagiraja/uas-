from pembeli import main as pembeli_main
from penjual import main as penjual_main
from menu import judul




datapenjual = {
    'user1':'pw1', 
    'user2':'pw2',

}

datapembeli = {
       'user3':'pw1',
       'user4':'pw2'
}

def login():
    judul('\t\t       LOGIN')
    username = input('Masukan Username:')
    password = input('Masukan Password:')

    if username in datapenjual and datapenjual[username] == password:
        print('login kehalaman penjual berhasil')
        penjual_main()
    elif username in datapembeli and datapembeli[username] == password:
        print('login kehalaman user berhasil')
        pembeli_main()
    else:
        print('password atau username salah')


         
       
       



if __name__ =='__main__':
        
        login()
