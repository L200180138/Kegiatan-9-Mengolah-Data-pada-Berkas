#!/usr/bin/python
# Kegiatan 1. Menulis berkas teks
kgtn = open ('L200180138', 'w')
kgtn.write ('L200180138\n')
kgtn.write ('17-12-1999\n')
kgtn.write ('Karina Muslimah\n')
kgtn.close ()

# Kegiatan 2. Membaca berkas teks
kgtn = open ('L200180138', 'r')
NIM = kgtn.readline()
Tanggal = kgtn.readline()
Nama = kgtn.readline()
Kota = 'Jakarta, '
Tanggal = '12-17-1999\n'
kgtn.close()

kgtn = open('L200180138', 'w')
kgtn.write (Nama)
kgtn.write (Kota)
kgtn.write (Tanggal)
kgtn.write (NIM)
kgtn.close ()

# Kegiatan 3. Membaca data dari berkas teks dan menyimpan ke shelve
import shelve
kgtn = open('L200180138', 'r')
Nama = kgtn.readline()
Tanggal = kgtn.readline()
NIM = kgtn.readline()
kgtn.close()

# Kegiatan 4. Membaca shelve
import shelve
kgt = shelve.open('karin')
kgt['k'] = [Nama, Tanggal, NIM]
print kgt['k'][0]
print kgt['k'][1]
print kgt['k'][2]
kgtn.close()
