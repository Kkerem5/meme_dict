import time

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEES": "onaylamamak"
            }
while True:
    word = input("Kelime anlamına bakmak için 'k', kelime eklemek için 'ke', çıkmak için 'çık' yazın")
    time.sleep(1)
    if word == 'k':
            while True:
                kelime = input("Anlamadığınız bir kelime yazın, çıkmak için 'çık' yazın (hepsini büyük harflerle yazın!): ")
                if kelime in meme_dict.keys():
                    time.sleep(1)
                    print(kelime, 'kelimesinin anlamı:',meme_dict[kelime])
                elif kelime == 'çık':
                    break
                else:
                    time.sleep(1)
                    print('Kelime bulunamadı')
    if word == 'ke':
        while True:
            eklenicek_kelime = input("Eklemek istediğiniz kelimeyi büyük harflerle girin, çıkmak için 'çık' yazın")
            if eklenicek_kelime == 'çık':
                break
            else:
                
                anlami = input('Kelimenizin anlamı nedir?')
                time.sleep(1)
                meme_dict[eklenicek_kelime] = anlami
                print('kelimeniz eklenmiştir')
