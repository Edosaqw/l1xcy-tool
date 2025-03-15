import os
import time
import sys

# Colorama'yı yükleyip yüklemediğini kontrol et
try:
    from colorama import Fore, Style, init
except ImportError:
    print("Colorama kütüphanesi bulunamadı. Kuruluyor...\n")

    # Animasyonlu yükleme çubuğu
    animation = "|/-\\"
    for i in range(10):
        sys.stdout.write(f"\r{Fore.YELLOW}Yükleniyor... {animation[i % len(animation)]}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.3)

    os.system("pip install colorama")
    print(f"\n{Fore.GREEN}Kurulum tamamlandı!{Style.RESET_ALL}\n")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")  # Ekranı temizle

    from colorama import Fore, Style, init  # Yeniden import et

# Colorama başlat
init(autoreset=True)

# Dil seçimi
def select_language():
    os.system("cls" if os.name == "nt" else "clear")  # Terminali temizle
    ascii_art = f"""{Fore.CYAN}
 ___                                                                     
(   )                                                                    
 | |    .---.   ___ .-.     .--.    ___  ___    .---.    .--.     .--.   
 | |   / .-, \ (   )   \   /    \  (   )(   )  / .-, \  /    \   /    \  
 | |  (__) ; |  |  .-. .  ;  ,-. '  | |  | |  (__) ; | ;  ,-. ' |  .-. ; 
 | |    .'`  |  | |  | |  | |  | |  | |  | |    .'`  | | |  | | |  | | | 
 | |   / .'| |  | |  | |  | |  | |  | |  | |   / .'| | | |  | | |  |/  | 
 | |  | /  | |  | |  | |  | |  | |  | |  | |  | /  | | | |  | | |  ' _.' 
 | |  ; |  ; |  | |  | |  | '  | |  | |  ; '  ; |  ; | | '  | | |  .'.-. 
 | |  ' `-'  |  | |  | |  '  `-' |  ' `-'  /  ' `-'  | '  `-' | '  `-' / 
(___) `.__.'_. (___)(___)  `.__. |   '.__.'   `.__.'_.  `.__. |  `.__.'  
                           ( `-' ;                      ( `-' ;          
                            `.__.                        `.__.           
{Style.RESET_ALL}"""

    print(ascii_art)
    print(f"{Fore.GREEN}Dil Seçiniz / Select Language:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1️⃣ Türkçe{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2️⃣ English{Style.RESET_ALL}")

    lang_choice = input(f"{Fore.YELLOW}[?] Seçiminiz / Your Choice: {Style.RESET_ALL}").strip()

    if lang_choice == "1":
        return "TR"
    elif lang_choice == "2":
        return "EN"
    else:
        print(f"{Fore.RED}Geçersiz seçim! / Invalid selection!{Style.RESET_ALL}")
        time.sleep(1)
        return select_language()


# Kullanıcının dilini al
language = select_language()

def loading_animation():
    os.system("cls" if os.name == "nt" else "clear")  # Ekranı temizle
    loading_text = "YÜKLENİYOR..."
    print("\n")
    
    for char in loading_text:
        sys.stdout.write(Fore.YELLOW + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    
    time.sleep(1)

def exit_program():
    os.system("cls" if os.name == "nt" else "clear")  # Terminali temizle
    exit_art = f"""{Fore.RED}
 (            (                    
 )\        )  )\ ) (        (  (   
((_)(   ( /( (()/( )\  (    )\))(  
 _  )\  )(_)) ((_)|(_) )\ )((_))\  
| |((_)((_)_  _| | (_)_(_/( (()(_) 
| / _ \/ _ / _ | | | ' \)) _ |  
|_\___/\__,_\__,_| |_|_||_|\__, |  
                           |___/     
{Style.RESET_ALL}"""

    print(exit_art)
    print(f"\n{Fore.RED}Program kapatılıyor...{Style.RESET_ALL}")
    time.sleep(2)
    exit()

def main():
    os.system("cls" if os.name == "nt" else "clear")  # Terminali temizle

    # Menü tasarımı (TR/EN)
    if language == "TR":
        menu_text = f"""{Fore.MAGENTA}
╔═══════════════════════════════════╗
║        ⚡ HACK TOOL MENÜ ⚡       ║
╠═══════════════════════════════════╣
║  1️⃣ DDOS Saldırısı                ║
║  2️⃣ SqlMap                        ║
║  3️⃣ SMS Bomber                    ║
║  4️⃣ Gizli Numaradan Mesaj         ║
║  0️⃣ Çıkış                         ║
╚═══════════════════════════════════╝
{Style.RESET_ALL}"""
    else:
        menu_text = f"""{Fore.MAGENTA}
╔═══════════════════════════════════╗
║        ⚡ HACK TOOL MENU ⚡       ║
╠═══════════════════════════════════╣
║  1️⃣ DDOS attack                   ║
║  2️⃣ SqlMap                        ║
║  3️⃣ SMS Bomber                    ║
║  4️⃣ Anonymous Message             ║
║  0️⃣ Exit                          ║
╚═══════════════════════════════════╝
{Style.RESET_ALL}"""

    # ASCII sanatını göster
    ascii_art = f"""{Fore.CYAN}
╔════════════════════════════════════╗
║  _  __                             ║
║ | |/  |                            ║
║ | || |__  _____ _   _             ║
║ | | | |\ \/ / __| | | |            ║
║ | |_| |_>  < (__| |_| |            ║
║ |_|\___/_/\_\___|\__, |            ║
║                   __/ |            ║
║                  |___/             ║
╚════════════════════════════════════╝
{Style.RESET_ALL}"""

    print(ascii_art)
    print(menu_text)

    choice = input(f"{Fore.YELLOW}[?] Seçiminiz / Your Choice: {Style.RESET_ALL}").strip()

    # Yükleme animasyonu
    loading_animation()

    # Seçim yapıldığında ASCII sanatını göster
    selected_ascii = f"""{Fore.CYAN}
 __   ___  _ _  ___   ___ __  _ ___   __ __  ___  
 \ v' / || | |/ / | | __|  \| | \ v' //__\| _ \ 
  . .'| \/ |   <| |_| _|| | ' | |. .'| \/ | v / 
   !_!  \__/|_|\_\___|___|_|\__|_| !_!  \__/|_|_\   
{Style.RESET_ALL}"""

    print(selected_ascii)
    time.sleep(1)

    # Seçenekler
    if choice == '1':  # WebHack seçilirse
        print(f"\n{Fore.GREEN}Ddos açılıyor...{Style.RESET_ALL}")
        if os.name == 'nt':  # Windows
            os.system("start ddos.py")
        else:  # Linux/macOS
            os.system("python3 /home/kali/Desktop/l1xcy-tool/python/ddos.py")

    elif choice == '2':  # SQLMap seçilirse
        print(f"\n{Fore.GREEN}SQLMap açılıyor...{Style.RESET_ALL}")
        if os.name == 'nt':  # Windows
            os.system("start sqlmap.py")
        elif os.name == 'posix':  # Linux/macOS
            os.system("python3 /home/kali/Desktop/l1xcy-tool/python/sqlmap.py")

    elif choice == '3':  # SMS Bomber seçilirse
        print(f"\n{Fore.GREEN}SMS Bomber açılıyor...{Style.RESET_ALL}")
        if os.name == 'nt':  # Windows
            os.system("start smsbomber.py")
        elif os.name == 'posix':  # Linux/macOS
            os.system("python3 /home/kali/Desktop/l1xcy-tool/python/smsbomber.py")
        else:
            print(f"{Fore.RED}SMS Bomber sadece Linux tabanlı sistemlerde çalıştırılabilir!{Style.RESET_ALL}")

    elif choice == '4':  # Gizli Numaradan Mesaj seçilirse
        print(f"\n{Fore.GREEN}Gizli Numaradan Mesaj açılıyor...{Style.RESET_ALL}")
        os.system("start gizlinumaradanmesaj.py")
    
    elif choice == '0':  # Çıkış yapılırsa
        exit_program()

    else:
        print(f"\n{Fore.YELLOW}! Geçersiz seçim!{Style.RESET_ALL}")
        time.sleep(1)
        main()

# Programı çalıştır
main()
