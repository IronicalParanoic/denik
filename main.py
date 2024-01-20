from modules.text_work import *
from modules.knihovna_work import *
from modules.my_errors import VyberError
from second_page import second_page

print(da_book)
print(vitejte_str)

while(True):
	try:
		print(rozdeleni)

		files = seznam_deniku()
		if len(files) != 0:
			print("\nVaše deníky: ")
			print(*files, sep = ', ')
		else:
			print(zadne_deniky_str)
		print(menu1_str)

		vyber = input()
		if vyber == 'vytvořit':
			vytvorit_novy_denik(input(novy_denik_str))
			print(denik_vytvoren_str)
			input(enter)
		elif vyber.startswith('zrušit'):
			nazev_deniku = vyber.split(' ', 1)[1]
			vymaz_denik(nazev_deniku)
			print(denik_zrusen_str)
			input(enter)
		elif vyber.startswith('otevři'):
			nazev_deniku = vyber.split(' ', 1)[1]
			otevreny_denik = nacist_denik(nazev_deniku)
			ulozit_denik(nazev_deniku, second_page(otevreny_denik))
		elif vyber in ['x', 'X']:
			print(exit_str)
			break
		else:
			raise VyberError

	except VyberError:
		print(vyber_err_str)
	except NameError as nameerr:
		print(nameerr)
		input(enter)
