isim1 = input("İsminiz: ")
isim2 = input("Sevgilinizin ismi: ")
# len fonksiyonu ile isimlerin uzunluklarını alıyoruz
ask = len(isim1) + len(isim2)
if len(isim1) >= len(isim2):
    ask -= 5
else:
    ask += 3
    ask *= 52
    ask = ask / (100 + len(isim2))
if ask>10:
    ask = 10
else:
    # round fonksiyonu ile sonucumuzu yuvarlıyoruz
    ask = round(ask)
print(isim1, "ve ",isim2," Aşk Puanınız 💕 --> ",ask)