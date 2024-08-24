import random
import kelimeler

def oyun():
    harfler = []
    sayı = 0
    kelime = random.choice(kelimeler.havuz)
    while True:
        print("harf tahmin ediniz veya direk kelimeyi yazınız")
        sayı += 1
        if sayı <= 4:
            harf = input()
            harfler.append(harf)
            if len(list(harf)) == 1:
                for i in kelime:
                    if any(kelime in harfler for kelime in i):
                        print(f"{i} ",end="")
                    else:
                        print("- ",end="")

            else:
                if list(harf) == kelime:
                    print("başardın")
                    break
                else:
                    print("cevap doğru değil")

        else:
            print("haklarını doldurdun")
            for i in kelime:
                if any(kelime in harfler for kelime in i):
                    print(f"{i} ",end="")
                else:
                    print("- ",end="")
            print("kelimeyi tahmin et")
            tahmin = input("")
            if list(tahmin) == kelime:
                print("başardın")
                break
            else:
                print("başaramadın doğru cevap:")
                for i in kelime:
                    print(f"{i}",end="")
                print("\n")
                break


def menü():
    while True:
        print("Kelime Oynuna Hoşgeldin \n1-oyunu başlat\n2-oyunu kapat")
        işlem = input("")
        if işlem == "1":
            oyun()
        elif işlem == "2":
            break
menü()
