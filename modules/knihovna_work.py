import pathlib as path
import json
from .text_work import *

#Modul pro práci se soubory

#Práce s directories
def denik_path(filename = ""): #bez argumentu funkce vrací path do složky deniku
	denik_dir = path.Path.cwd() / 'deniky'
	if filename != "":
		denik_dir = denik_dir / f"{filename}.json"
	return (denik_dir)

def seznam_deniku():
	files = []
	for file in denik_path().iterdir():
		if file.suffix == '.json':
			files.append(file.stem)
	return (files)

def vytvorit_novy_denik(name):
	if denik_path(name).exists():
		raise NameError(exists_err_str)
	else:
		with open(denik_path(name), 'w') as f:
			f.close()

def vymaz_denik(name):
	if denik_path(name).is_file():
		denik_path(name).unlink()
	else:
		raise NameError(nonexist_file_err_str)

#Otevírání a zabírání souboru
def nacist_denik(name):
	if denik_path(name).is_file():
		with open(denik_path(name), 'r') as f:
			contents = f.read()
			if len(contents) != 0:
				denik = json.loads(contents)
				return (denik)
			else:
				return (0)
	else:
		raise NameError(nonexist_file_err_str)
    
def ulozit_denik(name, zapis):
	with open(denik_path(name), 'w') as f:
		f.write(json.dumps(zapis))
	return (None)
