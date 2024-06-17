import datetime

class Transaction:
    codeList = {"11":"Deposit", "12":"Interest", "13":"Rebate", "14":"Cashback", "21": "Withdraw", "22":"Withholding Tax", "23":"Admin Fee"}
    codeSign = {"11":1, "12":1, "13":1, "14":1, "21":-1, "22":-1, "23":-1}
    
    #pastikan code ada dalam codeList
    def __init__(self, txid, cabang, code, amount):
        self.date = datetime.date.today()
        self.txid = txid
        self.cabang = cabang
        self.code = code
        self.amount = amount*self.codeSign[code]
        self.timestamp = datetime.datetime.now()
        
    def show(self):
        print("Date:", self.date)
        print("Code:", self.code)
        print("Amount:", f'{self.amount:,}')
        print("Timestamp:", self.timestamp)
        
    def print(self):
        print(self.date, self.code.rjust(4), f'{self.amount:,}'.rjust(15), str(self.txid).ljust(15), self.timestamp)
              
class ArrayTransaction:
    def __init__(self):
        self.array=[]
        self.count=0
        
    def newTransaction(self, cabang, code, amount):
        self.count+=1
        transaction=Transaction(self.count, cabang, code, amount)
        self.array.append(transaction)
        return transaction
            
    def list(self):
        lastPosition=0
        print("\n\n>>DAFTAR TRANSAKSI\n")
        print("-"*(70+4))
        print("Tanggal".ljust(10),"Code","Amount".rjust(15),"TXID".ljust(15),"Timestamp".ljust(20))
        print("-"*(70+4))
        while lastPosition<self.count:
            transaction=self.array[lastPosition]
            transaction.print()
            lastPosition+=1            