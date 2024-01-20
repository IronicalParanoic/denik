from .text_work import *
from .my_errors import kontrola_argumentu, ArgError

#Modul pro práci s dictionary

def doplnit_denik():
	print(dopln_instrukce_str)
	zapis = input().split('; ')
	if kontrola_argumentu(zapis, 6):
		info = ['autor', 'titul', 'zanry', 'rok', 'strany', 'datum']
		kniha = dict(zip(info, zapis))
		kniha['zanry'].split(', ') #žánry jsou teď v listu
		return (kniha)
	else:
		raise ArgError

def najdi_zapis(denik, autor_titul_str):
	aut_tit_list = autor_titul_str.split("; ", 1)
	if kontrola_argumentu(aut_tit_list, 2):		
		hledany_dict = dict(zip(['autor', 'titul'], aut_tit_list))
		for kniha in denik:
			if kniha['autor'] == hledany_dict['autor'] and kniha['titul'] == hledany_dict['titul']:
				return (kniha)
			else:
				raise ValueError(zapis_neni_str)
	else:
		raise ArgError

def vymaz_zapis(denik, autor_titul_str):
	kniha = najdi_zapis(denik, autor_titul_str)
	denik.remove(kniha)