'''
Indoprog Core Banking (Versi Linked List)
By: Hendra Soewarno (0119067305)

Jangan buang header ini untuk penghargaan kepada hak cipta

Adalah aplikasi pembelajaran Data Structure & Algorithm
yang mengimplementasikan setiap topik bahasan kedalam
aplikasi nyata sehari-hari untuk membantu pemahaman
dan ketertarikan mahasiswa akan bahasan teoritis,
serta merasakan manfaat didalam penerapan pada industri.

Aplikasi ini masih sederhana dengan struktur kendali
utama saja untuk memungkinkan aplikasi berjalan, sehingga
dibutuhkan pengembangan lanjutan.

Melalui contoh aplikasi ini diharapkan dapat memicu
kreatifitas mahasiswa didalam pengembangan aplikasi
kearah yang lebih advanced dan pengendalian yang lebih
baik melalui tantangan2 pada aplikasi.
'''

from cbaccounts import *
from cbterbilang import *

class CoreBankingUI:
    def __init__(self):
        self.cabang="1271110101"
        self.ArrAccount=ArrayAccount()   
    
    #belum ada login dan pengenalan cabang
    def CB_Menu(self):
        while True:
            print("\n\n>>INDOPROG CORE BANKING SYSTEM VER 1.0\n")
            print("1. New Account")
            print("2. Account List")
            print("3. Cash Deposit")
            print("4. Cash Withdraw")
            print("5. Account Information")
            print("X. Exit")
            choose=input("\n\nMasukan pilihan:")
            if choose=="1":
                self.CB_NewAccount()
            elif choose=="2":
                self.CB_AccountList()
            elif choose=="3":
                self.CB_Deposit()
            elif choose=="4":
                self.CB_Withdraw()
            elif choose=="5":
                self.CB_AccountInformation()
            elif choose.upper()=="X":
                break
               
    #belum ada validasi NIK dan Nama (masih boleh kosong)
    def CB_NewAccount(self):
        print("\n\nPembukaan Account Baru\n")        
        nik = input("NIK:");
        nama = input("Nama:");
        account=self.ArrAccount.newAccount(self.cabang, nik, nama)
        print("\n\nBerhasil Buka Account Baru\n")
        account.show()
        print("\n\nSegera lakukan deposit awal...\n")
        
    def CB_AccountList(self):
        self.ArrAccount.list()
    
    #belum ada validasi amount, dan masih dimungkinkan input dalam jumlah negatif
    def CB_Deposit(self):
        while True:
            noac=input("\n\nNo.AC:")
            if noac=="":
                break
            account=self.ArrAccount.find(noac)
            if not account:
                print("\n\nNo.AC tidak ditemukan atau salah\n")
                continue
            account.show()
            amount=int(input("Amount:"))
            print("\nTERBILANG: ", Terbilang().terbilang(amount).upper())
            yakin=input("\n\nYakin No.AC dan Amount telah benar[Y/T]?")
            if yakin.lower()!="y":
                continue
            account.deposit(self.cabang, amount)
            account.show()
    
    #belum ada validasi amount, dan masih dimungkinkan input dalam jumlah negatif
    def CB_Withdraw(self):
        while True:
            noac=input("\n\nNo.AC:")
            if noac=="":
                break
            account=self.ArrAccount.find(noac)
            if not account:
                print("\n\nNo.AC tidak ditemukan atau salah\n")
                continue
            account.show()
            amount=int(input("Amount:"))
            print("\nTerbilang:", Terbilang().terbilang(amount).upper())
            yakin=input("\n\nYakin No.AC dan Amount telah benar[Y/T]?")
            if yakin.lower()!="y":
                continue
            account.withdraw(self.cabang, amount)
            account.show()
    
    def CB_AccountInformation(self):
        while True:
            noac=input("\n\nNo.AC:")
            if noac=="":
                break            
            account=self.ArrAccount.find(noac)
            if not account:
                print("\n\nNo.AC tidak ditemukan atau salah\n")
                continue
            account.show()
            account.transaction.list()

#Entry Point                
coreBankingUI=CoreBankingUI()
coreBankingUI.CB_Menu()