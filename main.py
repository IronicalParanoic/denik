from modules import *
from second_page import second_page

print("##### Vítejte ve své Čtenářské knihovně! #####")

while(True):
	files = seznam_deniku()
	if len(files) != 0:
		print("\nVaše deníky: " + str(files))
	else:
		print("\nZatím nemáte žádné deníky.")
	print("\nPro vytvoření nového deníku napište [ vytvoř ]. \nPro výběr deníku napište [ otevři (název deníku) ] bez závorek. \nPro zrušení deníku napiš [ zruš (název deníku) ]. \nPro ukončení programu zmáčněte [ x ]. \n")

	vyber = input()
	if vyber == 'vytv':
		vytvorit_novy_denik(input('Zadejte název nového deníku: '))
		print('\nDeník vytvořen.')
	elif vyber.startswith('zr'):
		nazev_deniku = vyber.split(' ', 1)[1]
		vymaz_denik(nazev_deniku)
		print('\nDeník zrušen.')
	elif vyber.startswith('otev'):
		nazev_deniku = vyber.split(' ', 1)[1]
		print("\nOtevírám deník...")
		otevreny_denik = nacist_denik(nazev_deniku)
		ulozit_denik(nazev_deniku, second_page(otevreny_denik))
	elif vyber == 'x':
		print('### Na shledanou! ###')
		break

	#else:
    #	error