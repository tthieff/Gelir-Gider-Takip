gelir=int (input("Aylık Gelir Miktarınızı Giriniz:"))
gider=int (input("Aylık Gider Miktarınızı giriniz :"))
print("--------------------------------------------")
toplam =gelir-gider

print("Size kalan miktar şu kadardır",toplam)
if toplam<2000 :
    print(toplam,"İle çarşıda gezip birşeyler yiyebilirsiniz \n"
          "Sinemaya gidebilirsiniz\n")
    
elif toplam<=2000 & toplam<5000:
    print(toplam,"İle tur otobuslerine binip şehirleri gezebilirsin\n")

else:
    print(toplam,"İle tatile gidebilirsin \n"
          "Yurt dışına çıkabilirsin")
    
          


