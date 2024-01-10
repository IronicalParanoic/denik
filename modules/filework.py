import os
import dictwork as dict

deniky_dir = os.getcwd() + '/deniky'

def seznam_deniku():
    files = []
    for file in os.listdir(deniky_dir):
        if file.endswith('.pkl'):
            files.append(file)
    return files

def vytvorit_novy_denik(name):
    with open(os.path.join(deniky_dir, f"{name}.pkl"), 'w') as f:
        f.close()

def otevrit_denik(name):
    with open(os.path.join(deniky_dir, name), 'r+') as f:
        denik = f.read()
        f.close()
    return denik

def nacist_denik(filename):
    curr_denik = dict.load(filename)
    print(curr_denik)