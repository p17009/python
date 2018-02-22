import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

tetragwno=[]

for i in range (0,10000):
    tetragwno.insert(i,random.choice(letters))

for j in range (0,10000):
    if j%100==0:
        print
    print (tetragwno[j])
     


leksi = input("dwse orizontia leksi:")
leksi = list(leksi)
length = len(leksi)
for j in range (0,10000,100):
    for i in range (j,j+99-length+2):
        if leksi[0:length]==tetragwno[i:i+length]:
            print (leksi)
leksi2 = input("dwse katheth leksi:")
leksi2 = list(leksi2)
length2 = len(leksi2)
for j in range (0,100):
    for i in range (j,10000,100):
        if leksi2[0:length2]==tetragwno[i:i+length2]:
            print (leksi2)






