#Modul pro texty a jejich úpravu.

#first page
vitejte_str = "\033[1m##### Vítejte ve své Čtenářské knihovně! #####\033[0m\n"
zadne_deniky_str = "Zatím nemáte žádné deníky.\n"
menu1_str = "\nPro vytvoření nového deníku napište \033[32m vytvořit \033[0m. \nPro výběr deníku napište \033[33m otevři (název deníku) \033[0m bez závorek. \nPro zrušení deníku napiš \033[31m zrušit (název deníku) \033[0m. \nPro ukončení programu napište \033[41m x \033[0m. \n"
novy_denik_str = "Zadejte název nového deníku: "
denik_vytvoren_str = "\n\033[3mDeník vytvořen.\n\033[0m"
denik_zrusen_str = "\033[3mDeník zrušen.\n\033[0m"
exit_str = "\033[1m### Na shledanou! ###\033[0m"

#second page
zadne_zapisy_str = "\nV deníku nemáte žádné zápisy.\n"
menu2_str = "\nPro doplnění deníku napište \033[32m doplnit \033[0m. \nPřejete si najít zápis, napište \033[36m najdi ( autor; titul ) \033[0m (bez závorek). \nPřejete-li si záznam smazat, napište \033[31m vymazat ( autor; titul ) \033[0m. Pro vymazání všech záznamů, napište pouze \033[31m vymazat \033[0m. \nPro uložení deníku a návrat do hlavního menu zadejte \033[41m x \033[0m. \n"
dopln_instrukce_str = "\nZadejte ve stejném pořadí \033[33m (autor); (titul); (žánry - oddělit čárkami); (rok vydání); (počet stran); (datum přečtení)\033[0m. Pokud nějakou informaci neznáte, napište ' - ' . Oddělte středníkem (' ; '). \n"
doplneno_str = "\033[3mDoplněno.\033[0m\n"
zapis_neni_str = "\033[3mZápis neexistuje.\033[0m\n"
komplet_vymaz_str = "\033[3mZáznamy vymazány.\033[0m\n"
zapis_vymaz_str = "\033[3mZápis vymazán.\033[0m\n"

#errors, style: "\033[31m \033[0m\n"
vyber_err_str = "\033[31mNeplatný příkaz, zkuste znovu.\033[0m\n"
exists_err_str = "\033[31mDeník s takovým názvem už existuje.\033[0m\n"
nonexist_file_err_str = "\033[31mDeník s takovým názvem neexistuje.\033[0m\n"
arg_err_str = "\033[31mNeplatný počet argumentů. Zkontrolujte středníky.\033[0m\n"


#some -;spice;-
da_book = """
    _______
   /      /,
  /      //
 /______//
(______(/
"""
rozdeleni = '\n~ 🕮  ~' #"=^..^= 9"
enter = "\n\033[4mPro návrat zpět stiskněte ENTER.\033[0m"
