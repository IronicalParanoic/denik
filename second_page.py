from modules import *

def second_page(denik):

	if denik == 0:
		denik = []

	while (True):
		print(rozdeleni)
		if denik == []:
			print(zadne_zapisy_str)
		else:
			print(*denik, sep = ', ')
		print(menu2_str)
		vyber = input()
		if vyber == 'doplnit':
			doplnit_denik(denik)
			print(doplneno_str)
		elif vyber.startswith('najdi'):
			autor_titul = vyber.split(" ", 1)[1]
			print(najdi_zapis(denik, autor_titul))
		elif vyber.startswith('vymazat'):
			if vyber == 'vymazat':
				denik.clear()
				print(komplet_vymaz_str)
			else:	
				autor_titul = vyber.split(' ', 1)[1]
				vymaz_zapis(denik, autor_titul)
				print(zapis_vymaz_str)
		elif vyber == 'x' or 'X':
			return (denik)
			
		#else:
		#	error
	
#second_page('test')