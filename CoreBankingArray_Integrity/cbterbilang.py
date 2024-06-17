# file terbilang.py
class Terbilang:
    def __init__(self) -> None:
        self.huruf = [
            '', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam',
            'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas'
        ]
    
    def pilih_huruf(self, num):
        if num < 12:
            temp = ' ' + self.huruf[num]
        elif num < 20:
            temp = str(self.pilih_huruf(num - 10)) + ' belas'
        elif num < 100:
            temp = str(self.pilih_huruf(num // 10)) + ' puluh' + str(self.pilih_huruf(num % 10))
        elif num < 200:
            temp = 'seratus' + str(self.pilih_huruf(num - 100))
        elif num < 1000:
            temp = str(self.pilih_huruf(num // 100)) + ' ratus' + str(self.pilih_huruf(num % 100))
        elif num < 2000:
            temp = 'seribu' + str(self.pilih_huruf(num - 1000))
        elif num < 1000000:
            temp = str(self.pilih_huruf(num // 1000)) + ' ribu' + str(self.pilih_huruf(num % 1000))
        elif num < 1000000000:
            temp = str(self.pilih_huruf(num // 1000000)) + ' juta' + str(self.pilih_huruf(num % 1000000))
        elif num < 1000000000000:
            temp = str(self.pilih_huruf(num // 1000000000)) + ' milyar' + str(self.pilih_huruf(num % 1000000000))
        elif num < 1000000000000000:
            temp = str(self.pilih_huruf(num // 1000000000000)) + ' trilyun' + str(self.pilih_huruf(num % 1000000000000))
        return temp
    
    def terbilang(self, num: int = None):
        if num == None:
            hasil = ''
        elif num < 0:
            hasil = 'minus ' + self.pilih_huruf(abs(num))
        elif num == 0:
            hasil = 'nol'
        else:
            hasil = self.pilih_huruf(num)
        return hasil.replace("  "," ")