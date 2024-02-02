import requests, string
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin

class gen_wordlist:
    def __init__(self, url, outfile, verbose) -> None:
        self.counter=0
        self.words_used=[]
        self.url = url
        self.links =[]
        self.outfile = open(outfile, "w")
        self.verbose=verbose
        self.write_wordlist()

    def get_text_links(self):
        response = requests.get(self.url)
        parser = BeautifulSoup(response.content, 'html.parser')
        text = [p.get_text() for p in parser.find_all('p')]
        links = [urljoin(self.url, link.get('href')) for link in parser.find_all('a', href=True)]
        self.links.append(links[0])
        return text
    
    def count_freq(self, text):
        words = ' '.join(text).split()
        word_freq = Counter(words)
        sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
        return sorted_freq
    
    def write_wordlist(self):
        words=self.count_freq(self.get_text_links())
        for word in words:
            cleaned=self.clean(word)
            if len(cleaned) > 6 and cleaned not in self.words_used:
                if self.verbose=='0':
                    print("[+] Adding word: "+cleaned)
                self.outfile.write(cleaned+"\n")
                self.words_used.append(cleaned)
        self.next_link()
    
    def clean(self, word:str):
        cleaner = str.maketrans("","",string.punctuation+"’")
        return word.translate(cleaner).lower()
    
    def next_link(self):
        self.counter+=1
        if self.counter < 3 and self.links!=[]:
            self.url = self.links[0]
            self.links.pop(0)
            self.write_wordlist()

if __name__ == '__main__':
    generator=gen_wordlist('http://example.com', "example_wordlist.txt")