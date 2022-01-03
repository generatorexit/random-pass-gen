import random
from termcolor import colored

lower   = "qwertyuıopğü,işlkjhgfdsa<zxcvbnmöç"
upper   = "QWERTYUIOPĞÜ,İŞLKJHGFDSAZXCVBNMÖÇ"
numbers = "1234567890"
symbols = "!'^+%&/()=?~'||\}][{¾½½$#$£>é_,.:;<>"

while 1:
    try:
        total = lower+upper+numbers+symbols
        length = random.randint(16,40)
        password = "".join(random.sample(total,length))
        print(colored(f"\rCtrl+C to stop: {password}","red"),end="")
    except KeyboardInterrupt:
        print(colored(f"\nRecommended Password: {password}","green"))
        print(colored(f"Length: {len(password)}","green"))
        break