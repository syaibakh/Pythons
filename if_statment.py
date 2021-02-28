nilai = int(input('Masukan Angka: '))

if 1 <= nilai < 9:
    print('Satuan')
elif 10 <= nilai < 99:
    print('Puluhan')
elif 100 <= nilai < 999:
    print('Ratusan')
elif 1000 <= nilai < 9999:
    print('Ribuan')
else:
    print('Banyakkk!')