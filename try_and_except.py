angka = input('Type a Number, Please: ')
try:
    nilai = int(angka)
except:
    nilai = -1
if nilai > 0:
    print('Thank You')
else:
    print('Not a Number!, Try again!')