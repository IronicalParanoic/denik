from modules import *
from second_page import second_page

print("##### Vítejte ve své Čtenářské knihovně! #####")

files = seznam_deniku()
if len(files) != 0:
	print("Vaše deníky: " + str(files))
else:
	print("Zatím nemáte žádné deníky.")
print("Pro vytvoření nového deníku napište [ vytvoř ]. \nPro výběr deníku napište [ otevři (název deníku) ] bez závorek.")

vyber = input()
if vyber == 'vytvoř':
	vytvorit_novy_denik(input('Zadejte název nového deníku: '))
elif vyber.startswith('otevři'):
	nazev_deniku = vyber.split(' ', 1)[1]
	print("\nOtevírám deník...")
	otevreny_denik = nacist_denik(nazev_deniku)
	second_page(otevreny_denik)

#else:
    #error