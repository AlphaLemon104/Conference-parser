import sys
import re
from urllib.request import urlopen

url = sys.argv[1]
page = urlopen(url)
html = page.read().decode("utf-8")

title_pattern = "<title>.*?conference.*?<\/title>"
date_pattern = "((0[1-9]|[12][0-9]|3[01]) - )?(0[1-9]|[12][0-9]|3[01]) (Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?) ([1-9][0-9]{3})"
price_pattern = "([0-9]+ (USD|EUR(O?S?))|\$[0-9]+|[0-9]+ €)"


title_results = re.search(title_pattern, html, re.IGNORECASE)
if (title_results): 
    title = title_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags

    date_results = re.search(date_pattern,html, re.IGNORECASE)
    price_results = re.search(price_pattern,html,re.IGNORECASE)
        
    print("Title: " + title)
    if(date_results):
        date = date_results.group()
        print("Date: " + date)
    else:
        print("No date available")

    if(price_results):
        price = price_results.group()
        print("Price: " + price)
    else:
        print("No price available")
    
else:
    print("This website is not about a conference")

