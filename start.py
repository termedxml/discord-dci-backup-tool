import os
import time
import colorama
from colorama import Fore
import pyfiglet
import random
import string
import threading
import webbrowser
import subprocess

# Initialisation de colorama pour la gestion des couleurs dans le terminal
colorama.init()

# Fonction pour générer un hash aléatoire
def generate_random_hash(length=8):
    characters = string.ascii_letters + string.digits  # Lettres et chiffres
    return ''.join(random.choice(characters) for _ in range(length))

# Fonction pour redimensionner la fenêtre du terminal
def resize_terminal(width, height):
    if os.name == 'nt':  # Si c'est Windows
        os.system(f'mode con: cols={width} lines={height}')
    else:  # Si c'est Linux/Mac
        os.system(f'printf "\\e[8;{height};{width}t"')

# Fonction pour changer le titre de la fenêtre du terminal
def change_terminal_title():
    while True:
        random_hash = generate_random_hash()  # Générer un hash aléatoire
        if os.name == 'nt':  # Si c'est Windows
            os.system(f'title {random_hash}')  # Changer le titre de la fenêtre sur Windows
        else:  # Si c'est Linux/Mac
            os.system(f'echo -e "\\033]0;{random_hash}\\007"')  # Changer le titre sur Linux/Mac
        time.sleep(0.1)  # Attendre 0.1 seconde avant de changer le titre

# Fonction pour effacer le terminal (fonction qui dépend du système d'exploitation)
def clear_screen():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Linux/Mac
        os.system('clear')

# Fonction pour afficher le texte ASCII en vert pomme
def print_ascii_text():
    ascii_text = pyfiglet.figlet_format("Termed.wblm backup tool")
    print(Fore.GREEN + ascii_text)

# Fonction pour afficher les messages
def print_messages():
    print(Fore.GREEN + "root$> Made with sum " + Fore.MAGENTA + "<3" + Fore.GREEN + " by termed.wblm Project" + Fore.RESET)
    print(Fore.GREEN + "root$> GitHub for open source code : " + Fore.GREEN + "https://github.com/termedxml")
    print(Fore.GREEN + "root$> Discord : " + Fore.BLUE + "https://discord.gg/2ekQJDm3kB")
    print("\n")

# Fonction pour lancer les fichiers Python
def run_python_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error while executing {script_name}: {e}" + Fore.RESET)

# Fonction pour rediriger vers un lien
def open_link(url):
    webbrowser.open(url)

# Fonction principale pour afficher les options et gérer l'entrée de l'utilisateur
def main():
    # Lancer le changement du titre dans un thread séparé
    threading.Thread(target=change_terminal_title, daemon=True).start()
    
    resize_terminal(100, 30)  # Définir la taille de la fenêtre (largeur: 100, hauteur: 30)
    
    while True:
        clear_screen()  # Efface l'écran à chaque boucle
        print_ascii_text()
        time.sleep(1)
        print_messages()
        
        print(Fore.YELLOW + "Main :")
        
        # Affichage des options avec des couleurs spécifiques
        print(Fore.WHITE + Fore.MAGENTA + "1: Backup" + Fore.RESET)
        print(Fore.WHITE + Fore.MAGENTA + "2: Restore" + Fore.RESET)
        print(Fore.WHITE + Fore.MAGENTA + "3: Add Discord Bot (not required)" + Fore.RESET)
        print(Fore.GREEN + "5: Exit" + Fore.RESET)

        choice = input(Fore.YELLOW + "root$> ")

        if choice == '1':
            print(Fore.MAGENTA + "Starting backup process..." + Fore.RESET)
            run_python_script('main.py')  # Lancer le fichier backup.py
        elif choice == '2':
            print(Fore.MAGENTA + "Starting restore process..." + Fore.RESET)
            run_python_script('main.py')
        elif choice == '3':
            print(Fore.MAGENTA + "Opening Discord bot link..." + Fore.RESET)
            open_link("https://discord.gg/2ekQJDm3kB")  # Rediriger vers le lien Discord
        elif choice == '4':
            print(Fore.MAGENTA + "Opening help..." + Fore.RESET)
            run_python_script('help.py')  # Lancer le fichier help.py
        elif choice == '5':
            print(Fore.GREEN + "Exiting the program... Goodbye!" + Fore.RESET)
            break
        else:
            print(Fore.RED + "Invalid choice, please try again." + Fore.RESET)
            time.sleep(1)  # Attente d'une seconde pour que l'utilisateur voie l'erreur

if __name__ == "__main__":
    main()
