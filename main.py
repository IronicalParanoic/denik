from modules import *
from second_page import second_page

print("##### Vítejte ve své Čtenářské knihovně! #####")

while(True):
	files = seznam_deniku()
	if len(files) != 0:
		print("\nVaše deníky: " + str(files))
	else:
		print("Zatím nemáte žádné deníky.")
	print("\nPro vytvoření nového deníku napište [ vytvoř ]. \nPro výběr deníku napište [ otevři (název deníku) ] bez závorek. \nPro zrušení deníku napiš [ zruš (název deníku) ]. \nPro ukončení programu zmáčněte [ x ]. \n")

	vyber = input()
	if vyber == 'vytvoř':
		vytvorit_novy_denik(input('Zadejte název nového deníku: '))
		print('Deník vytvořen.')
	elif vyber.startswith('zruš'):
		nazev_deniku = vyber.split(' ', 1)[1]
		vymaz_denik(nazev_deniku)
		print('Deník zrušen.')
	elif vyber.startswith('otevři'):
		nazev_deniku = vyber.split(' ', 1)[1]
		print("\nOtevírám deník...")
		otevreny_denik = second_page(nacist_denik(nazev_deniku))
		ulozit_denik(nazev_deniku, otevreny_denik)
	elif vyber == 'x':
		print('### Na shledanou! ###')
		break

	#else:
    #	error