import modules

print("##### Vítejte ve své Čtenářské knihovně! #####")

files = modules.seznam_deniku()
if len(files) != 0:
    print("Vaše deníky: " + str(files))
else:
    print("Zatím nemáte žádné deníky.")
print("Pro vytvoření nového deníku napište [ vytvoř ]. Pro výběr deníku napište [ otevři ].")

vyber = input()
if vyber == 'vytvoř':
    modules.vytvorit_novy_denik(input('Zadejte název nového deníku: '))
if vyber == 'otevři':
    denik = modules.otevrit_denik(input("Jaký deník chcete otevřít? "))
    print(type(modules.nacist_denik(denik)))
#else:
    #error