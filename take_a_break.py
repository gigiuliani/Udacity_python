from time import time, sleep
import time
from datetime import time as dt_time
import webbrowser

total_breaks=3
counter = 0
print ("This program started on "+ time.ctime())
while (counter < total_breaks):
    sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=rVeMiVU77wo")
    counter = counter +1
