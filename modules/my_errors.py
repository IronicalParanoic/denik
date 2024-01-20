#Všechno spojené s chybami a error-handlingem.

#chyby
class VyberError(Exception):
	"Neplatný příkaz, příkaz není v seznamu možností."
	pass
class ArgError(Exception):
	"\033[31mNeplatný počet argumentů. Zkontrolujte středníky.\033[0m\n"
	pass

#kontrola
def kontrola_argumentu(seznam_z_term, pocet_arg):
	if len(seznam_z_term) != pocet_arg:
		return (False)
	return (True)