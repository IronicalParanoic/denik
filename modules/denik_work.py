import pprint as p
from .text_work import *

#Modul pro práci s dictionary

def doplnit_denik():
	autor = input("Jméno autora: ")
	titul = input("Titul: ")
	zanry = input("Žánry: ")
	rok = input("Rok vydání: ")
	strany = input("Počet stran: ")
	datum = input("Datum přečtení: ")
	kniha = {'autor':autor, 'titul':titul, 'zanry':zanry, 'rok':rok, 'strany':strany, 'datum':datum}
	return (kniha)

def najdi_zapis(denik):
	autor = input("Napište jméno autora: ")
	titul = input("Napište název titulu: ")
	hledany_dict = dict(zip(['autor', 'titul'], [autor, titul]))
	for kniha in denik:
		if all([kniha[key] == hledany_dict[key] for key in hledany_dict.keys()]):
			return (kniha)
	raise ValueError(zapis_neni_str)

def vymaz_zapis(denik):
	kniha = najdi_zapis(denik)
	denik.remove(kniha)

def uprav_zapis(denik):
	kniha = najdi_zapis(denik)
	novy_str = "Nový zápis: "
	while True:
		vyber = input(upravit_str)
		if vyber == 'autor':
			kniha['autor'] = input(novy_str)
		elif vyber == 'titul':
			kniha['titul'] = input(novy_str)
		elif vyber == 'žánry':
			kniha['zanry'] = input(novy_str)
		elif vyber == 'rok':
			kniha['rok'] = input(novy_str)
		elif vyber == 'strany':
			kniha['strany'] = input(novy_str)
		elif vyber == 'datum':
			kniha['datum'] = input(novy_str)
		elif vyber == '':
			break
		else:
			print(vyber_err_str)

def krasny_print(denik):
	if type(denik) == list:
		for kniha in denik:
			p.pprint(kniha, sort_dicts=False)
			print('\n')
	else:
		p.pprint(denik, sort_dicts=False)