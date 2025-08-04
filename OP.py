
import string
import random




def gerador(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/"): # Parametros das Strings
    return ''.join(random.choice(chars) for _ in range(size)) # Utilizando Random para usar os parametros do chars e gerar as Strings
