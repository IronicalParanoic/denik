from modules.text_work import *
from modules.denik_work import *
from modules.my_errors import VyberError

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
			elif vyber.startswith('najdi'):
				autor_titul = vyber.split(" ", 1)[1]
				najdeny_zapis = najdi_zapis(denik, autor_titul)
				krasny_print(najdeny_zapis)
				input(enter)
			elif vyber.startswith('vymazat'):
				if vyber == 'vymazat':
					denik.clear()
					print(komplet_vymaz_str)
					input(enter)
				else:	
					autor_titul = vyber.split(' ', 1)[1]
					vymaz_zapis(denik, autor_titul)
					print(zapis_vymaz_str)
					input(enter)
			elif vyber == 'x' or 'X':
				return (denik)
			else:
				raise VyberError

		except VyberError:
			print(vyber_err_str)
		except KeyError as keyerr:
			print(keyerr)
			input(enter)
		except ArgError:
			print(arg_err_str)
			input(enter)
		except ValueError as valerr:
			print(valerr)
			input(enter)
	
#second_page('test')