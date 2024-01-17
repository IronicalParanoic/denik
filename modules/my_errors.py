#Všechno spojené s chybami a error-handlingem.
from .text_work import *

#chyby
class VyberError(Exception):
	"Neplatný příkaz, příkaz není v seznamu možností."
	pass

#kontrola
def kontrola_argumentu(seznam_z_term, pocet_arg):
	if len(seznam_z_term) != pocet_arg:
		assert ValueError(arg_err_str)
		return (False)
	return (True)