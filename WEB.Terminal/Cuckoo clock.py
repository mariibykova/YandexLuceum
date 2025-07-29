import schedule
import time
from datetime import datetime

def print_ku():
    now = datetime.now()
    hour = now.hour % 12 
    if hour == 0:
        hour = 12  
    ku_string = "Ку " * hour
    print(ku_string.strip())


schedule.every().hour.at(":00").do(print_ku)

while True:
    schedule.run_pending()
    time.sleep(1)