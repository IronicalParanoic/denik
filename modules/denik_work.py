import pprint as p
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
			if all([kniha[key] == hledany_dict[key] for key in hledany_dict.keys()]):
				return (kniha)
		raise ValueError(zapis_neni_str)
	else:
		raise ArgError

def vymaz_zapis(denik, autor_titul_str):
	kniha = najdi_zapis(denik, autor_titul_str)
	denik.remove(kniha)

def krasny_print(denik):
	if type(denik) == list:
		for kniha in denik:
			p.pprint(kniha, sort_dicts=False)
			print('\n')
	else:
		p.pprint(denik, sort_dicts=False)