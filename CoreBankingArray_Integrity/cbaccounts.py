import hashlib
from cbtransaction import *

class Account:
    minDeposit=100000
    
    #default pin 123456
    def __init__(self, noac, nama, nik):
        self.__noac=noac
        self.nama=nama.upper()
        self.nik=nik
        self.__pin="123456"        
        self.__balance=0
        #untuk menjaga integritas dari record
        self.__integrity_hash= self.__generate_hash()
        
        #masing-masing Account punya tabel transaksi masing2
        self.transaction = ArrayTransaction()
        
    #membangkitkan integritas record
    def __generate_hash(self):
        data = f"{self.__noac}:{self.__balance}"
        return hashlib.sha256(data.encode()).hexdigest()

    #verifikasi integritas record
    def __verify_hash(self):
        expected_hash = self.__generate_hash()
        if expected_hash != self.__integrity_hash:
            raise ValueError("Data integrity check failed")      
        
    #periksa noac sesuai?
    def isNoAC(self, noac):
        return self.__noac==noac
        
    #ambil saldo
    def getBalance(self):
        self.__verify_hash();
        return self.__balance;

    #tambahkan pemeriksaan amount > 0
    def deposit(self, cabang, amount):
        #periksa integritas sebelum update balance
        self.__verify_hash()
        self.__balance+=amount
        #perbaharui record integrity
        self.__integrity_hash= self.__generate_hash()
        self.transaction.newTransaction(cabang, "12", amount)        
        
    #tambahkan pemeriksaan amount > 0
    #tambahkan pemeriksaan setelah penarikan tidak boleh < dari minDeposit
    def withdraw(self, cabang, amount):
        #periksa integritas sebelum update balance
        self.__verify_hash()
        self.__balance-=amount
        #perbaharui record integrity
        self.__integrity_hash= self.__generate_hash()        
        self.transaction.newTransaction(cabang, "21", amount)

    def show(self):
        print("\n\n>>RINCIAN ACCOUNT\n\n")
        print("No.AC:", self.__noac)
        print("Nama:", self.nama)
        print("NIK:", self.nik)
        print("Amount:", f'{self.getBalance():,}')

    def print(self):
        print(self.__noac.ljust(14), self.nama.ljust(50), self.nik.ljust(16))

class ArrayAccount:
    def __init__(self):
        self.array =[]
        self.count=0
        
    def newAccount(self,cabang, nik, nama):
        self.count+=1
        noac=cabang + str(self.count).rjust(4,"0")
        account=Account(noac, nama, nik)
        self.array.append(account)        
        return account
            
    #linear search
    def find(self, noac):
        lastPosition = 0
        while lastPosition < self.count:
            account=self.array[lastPosition]
            if account.isNoAC(noac):
                return account
            lastPosition+=1
        return None
        
    def list(self):
        lastPosition=0
        print("\n\n>>DAFTAR ACCOUNT\n\n")
        print("-"*(80+3))
        print("No.AC".ljust(14),"Nama".ljust(50),"NIK".ljust(16))
        print("-"*(80+3))
        while lastPosition < self.count:
            account=self.array[lastPosition]
            account.print()
            lastPosition+=1

#unit test
#12=Sumatera Utara, 71=Kota Medan, 11=Medan Johor, 01=Cabang 01, 01=Tabungan
#cabang="1271110101"
#savingAccount=LinkedListAccount()
#account1=savingAccount.newAccount(cabang, "1271181906730004", "Hendra Soewarno")
#assert account1.nik=="1271181906730004", "Error NIK 1271181906730004"
#account2=savingAccount.newAccount(cabang, "1271181906730005", "Susan")
#account3=savingAccount.newAccount(cabang, "1271181906730006", "Felicia Fortuna")
#account4=savingAccount.newAccount(cabang, "1271181906730007", "Viona Victoria")
#savingAccount.list()
#myAccount = savingAccount.find(account1.noac)
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.__balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.__balance==100000, "Error Deposit, new balance 200000 not match"
#myAccount.show()
#myAccount.withdraw(cabang, 100000)
#assert myAccount.__balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.transaction.list()