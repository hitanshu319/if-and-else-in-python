import time
import webbrowser
from googlesearch import search
web=input("eneter to search")
url=[]
for i in search(web,stop=3):
    print(i)
    webbrowser.open_new_tab(i)	
    time.sleep(1)
    url.append(i)

print(url)
