# Imports
from bs4 import BeautifulSoup
import requests as req

# User Inputs
with open("logo.txt", "r") as f:
    print('\n\n\n')
    print(f'\033[95m {f.read()}\n\n\n')

url = input("\033[92m [+] Enter The Target URL: ")

def main():
    print(f'Trying To Connect {url}...')
    res = None
    try:
        res = req.get(url)
    except:
        
        print(f'\033[91m >...< Crap! Unable to connect to {url}')
        exit()

    print(f'Yosha! Got Into {url}')
    text_content = res.text
    soup = BeautifulSoup(text_content, 'html.parser')
    a_tags = soup.find_all('a')
    for a in a_tags:
        href = a['href']
        print(f'\033[94m [-] {a.get_text()}\t {href if "https://" in href else "https://facebook.com"+href}')

if __name__ == "__main__":
    main()
