from modules import *

def second_page(denik):
	if denik == None:
		denik = []

	while (True):
		print(denik)
		print("\nPro doplnění deníku napište [ doplň ]. \nPřejete si najít zápis, napište [ najdi ( autor, titul )] (bez závorek). \nPřejete-li si záznam smazat, napište [ vymaž ( autor, titul )]. Pro vymazání všech záznamů, napište pouze [ vymaž ]. \nPro uložení deníku a návrat do hlavního menu zmáčkněte [ x ]\n")
		vyber = input()
		if vyber == 'doplň':
			doplnit_denik(denik)
			print('\nDoplněno.')
		elif vyber.startswith('najdi'):
			autor_titul = vyber.split(" ", 1)[1]
			print(najdi_zapis(denik, autor_titul))
		elif vyber.startswith('vymaž'):
			if vyber == 'vymaž':
				denik.clear()
				print('\nZáznamy vymazány.')
			else:	
				autor_titul = vyber.split(' ', 1)[1]
				vymaz_zapis(denik, autor_titul)
				print('\nZápis vymazán.')
		elif vyber == 'x':
			return(denik)
			
		#else:
		#	error
	
#second_page('test')