from datetime import datetime
import time

def horloge () :
    try:
        while True:
            current_time = datetime.now()
            print("Il est :", current_time.strftime("%H:%M:%S"))
            time.sleep(1) 
    except KeyboardInterrupt:
        #Permet de quitter la boucle
        print("\nHorloge arrêtée")

horloge()