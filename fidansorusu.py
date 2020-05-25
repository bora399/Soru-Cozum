dikdortgen_uzun = int(input("Dikdörtgenin Uzun Kenarını Giriniz : "))
dikdortgen_kisa = int(input("Dikdörtgenin Kısa Kenarını Giriniz : "))
aralik = int(input("Kaç Metre Aralıkla Fidan Dikildiğini Giriniz : "))
fidan = (dikdortgen_uzun*2 + dikdortgen_kisa*2) / aralik
koseler_varmi = input("Köşelere gelecek mi : ")
kosesiz_fidan = ((dikdortgen_uzun*2 + dikdortgen_kisa*2)/aralik)

if koseler_varmi == "Evet" or koseler_varmi =="evet":
	print("Şu kadar fidan dikilecektir : {}".format(kosesiz_fidan))
else:
	print("Şu kadar fidan dikilecektir : {}".format(fidan-4))	

	
