import requests
from bs4 import BeautifulSoup
from collections import Counter

def run(url):
    wordlist = []
    code = requests.get(url).text
    soup = BeautifulSoup(code, 'html.parser')

    for each_text in soup.findAll('div', {'class' : 'entry-content'}):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\:;"<>?/., '
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word):
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    url = "https://www.geeksforgeeks.org/programming-language-choose/"
    run(url)     