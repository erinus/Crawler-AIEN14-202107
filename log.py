import colorama
import datetime

def log(text):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text = '\n                      '.join(text.split('\n'))
    print(f'{colorama.Fore.LIGHTBLUE_EX}[{now}]{colorama.Style.RESET_ALL} {text}')

def info(text):
    log(f'{colorama.Fore.WHITE}{text}{colorama.Style.RESET_ALL}')

def debug(text):
    log(f'{colorama.Fore.GREY}{text}{colorama.Style.RESET_ALL}')

def trace(text):
    log(f'{colorama.Fore.BLUE}{text}{colorama.Style.RESET_ALL}')

def error(text):
    log(f'{colorama.Fore.LIGHTRED_EX}{text}{colorama.Style.RESET_ALL}')

def warning(text):
    log(f'{colorama.Fore.YELLOW}{text}{colorama.Style.RESET_ALL}')

def success(text):
    log(f'{colorama.Fore.GREEN}{text}{colorama.Style.RESET_ALL}')