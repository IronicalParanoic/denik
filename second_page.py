from modules import *

def second_page(denik):
	if denik == None:
		denik = []

	print("\nPro doplnění deníku napište [ doplň ]. \nPřejete si najít zápis, napište [ najdi ( autor, titul )] (bez závorek). \nPřejete-li si záznam smazat, napište [ vymaž ( autor, titul )]. Pro vymazání všech záznamů, napište pouze [ vymaž ]. \nPro návrat do hlavního menu, zmáčkněte [ x ].")
	vyber = input()
	if vyber == 'doplň':
		doplnit_denik(denik)
	elif vyber.startswith('najdi'):
		autor_titul = vyber.split(" ", 1)[1]
		print(najdi_zapis(denik, autor_titul))
	elif vyber.startswith('vymaž'):
		if vyber == 'vymaž':
			denik.clear()
		else:	
			autor_titul = vyber.split(' ', 1)[1]
			vymaz_zapis(denik, autor_titul)
	#else:
	#	error
	
#second_page('test')