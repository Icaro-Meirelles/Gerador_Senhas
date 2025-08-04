
import pyfiglet




def ascii_art(): # FUnção para gerar a ASCII Art
    banner = "GEN/SENHAS"
    banner_ascii_art = pyfiglet.figlet_format(banner, font='small')
    print(banner_ascii_art)