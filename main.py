from modules import *
from second_page import second_page

print(da_book)
print(vitejte_str)

while(True):
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
	elif vyber.startswith('zrušit'):
		nazev_deniku = vyber.split(' ', 1)[1]
		vymaz_denik(nazev_deniku)
		print(denik_zrusen_str)
	elif vyber.startswith('otevři'):
		nazev_deniku = vyber.split(' ', 1)[1]
		print(otevreni_str)
		otevreny_denik = nacist_denik(nazev_deniku)
		ulozit_denik(nazev_deniku, second_page(otevreny_denik))
	elif vyber == 'x':
		print(exit_str)
		break

	#else:
    #	error