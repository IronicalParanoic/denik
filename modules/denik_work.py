#Modul pro práci s dictionaries

def doplnit_denik(denik):
	print("\nZadejte ve stejném pořadí [ (autor); (titul); (žánry - oddělit čárkami); (rok vydání); (počet stran); (datum přečtení) ]. Pokud nějakou informaci neznáte, napište - . Oddělte čárkami. \n")
	zapis = input().split('; ')		
	info = ['autor', 'titul', 'zanry', 'rok', 'strany', 'datum']
	kniha = dict(zip(info, zapis))
	kniha['zanry'].split(', ') #žánry jsou teď v listu
	denik.append(kniha)

def najdi_zapis(denik, autor_titul_str):
	aut_tit_list = autor_titul_str.split(", ", 1)
	hledany_dict = dict(zip(['autor', 'titul'], aut_tit_list))
	for kniha in denik:
		for key in kniha.keys()[:2]:
			if kniha[key] == hledany_dict and kniha[key + 1] == hledany_dict[key + 1]:
				return (kniha)

def vymaz_zapis(denik, autor_titul_str):
	kniha = najdi_zapis(denik, autor_titul_str)
	denik.remove(kniha)
