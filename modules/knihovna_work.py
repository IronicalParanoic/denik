import pathlib as path
import json

def denik_path(filename = ""): #bez argumentu funkce vraci path do slozky deniku
	denik_dir = path.Path.cwd() / 'deniky'
	if filename != "":
		denik_dir = denik_dir / f"{filename}.json"
	return denik_dir

def seznam_deniku():
	files = []
	for file in denik_path().iterdir():
		if file.suffix == '.json':
			files.append(file.stem)
	return files

def vytvorit_novy_denik(name):
	with open(denik_path(name), 'w') as f:
		f.close()

def vymaz_denik(name):
	if denik_path(name).exists():
		denik_path(name).unlink()

def nacist_denik(name):
	with open(denik_path(name), 'r') as f:
		contents = f.read()
		if len(contents) != 0:
			denik = json.loads(contents)
			return denik
		else:
			print("\nV deníku nemáte žádné zápisy.")
	return None
    
def ulozit_denik(name, zapis):
	with open(denik_path(name), 'w') as f:
		f.write(json.dumps(zapis))
