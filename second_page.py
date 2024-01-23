from modules.text_work import *
from modules.denik_work import *

def second_page(denik):

	if denik == 0:
		denik = []

	while (True):
		try:
			print(rozdeleni)
			if denik == []:
				print(zadne_zapisy_str)
			else:
				krasny_print(denik)

			print(menu2_str)
			vyber = input()
			if vyber == 'doplnit':
				novy_zapis = doplnit_denik()
				denik.append(novy_zapis)
				print(doplneno_str)
				input(enter)
			elif vyber == 'najdi':
				najdeny_zapis = najdi_zapis(denik)
				krasny_print(najdeny_zapis)
				input(enter)
			elif vyber == 'vymazat':
				vyber2 = input()
				if vyber2 == 'zápis':
					denik.clear()
					print(komplet_vymaz_str)
					input(enter)
				elif vyber2 == 'deník':	
					vymaz_zapis(denik)
					print(zapis_vymaz_str)
					input(enter)
				else:
					print(vyber_err_str)
			elif vyber == 'upravit':
				uprav_zapis(denik)
				
			elif vyber == 'x' or 'X':
				return (denik)
			else:
				print(vyber_err_str)

		except KeyError as keyerr:
			print(keyerr)
			input(enter)
		except ValueError as valerr:
			print(valerr)
			input(enter)
	
#second_page('test')