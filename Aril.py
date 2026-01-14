
import time
import sys
lirik = [ 
"Dimana, akan ku cari", 
"Aku menangis seorang diri", 
"Hatiku slalu ingin bertemu", 
"Untukmu aku bernyayi", 




]
delay = 0.5, 0.3, 0.4, 0.3, 0.1, 0.3
def nyanyikan_kata(kata):
    print(kata, end=' ', flush=True)
    time.sleep(0.1)  

    waktu_mulai = time.time()
    kata_kata = split()
       
    for kata in kata_kata:
         if time.time() - waktu_mulai:
           break
    nyanyikan_kata(kata)
    sisa_waktu =  - (time.time() - waktu_mulai)
    if sisa_waktu > 0:
        time.sleep(sisa_waktu)
    print()
 