import requests
import json

api_key = "e4864d5a858f9fbe24d7a316"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ") # USD
alinan_doviz = input("Alınan döviz türü: ") # TRY
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? : "))

sonuc = requests.get(api_url + bozulan_doviz)
#print(sonuc) # Respone[200] sonucu geliyor bunu json modülü ile okunabilir hale getirmem gerekir

#print(sonuc.text)

sonuc_json = json.loads(sonuc.text)

print(sonuc_json["conversion_rates"][alinan_doviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))

print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))