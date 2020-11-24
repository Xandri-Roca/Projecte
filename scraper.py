# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:07:43 2020

@author: bxz19
"""
import requests # Maybe upgrade to only use urllib and not requests
import os
from bs4 import BeautifulSoup
import io
    
class WebScraper():
    
    def __init__(self):
        self.finnish = False


    def terminal_menu(self):
        #This menu is to use this software from the terminal itself.
        print("\n\nHi, welcome to this Web Scraper")
        print("Introduce the url of the web you would like to scrape:", end = '')
        url = input()
        while not self.finnish:
            try:
                os.chdir(os.path.dirname(os.path.realpath(__file__)))
                methods = [1, 2, 3, 4]
                print("""\n\nThere are different types of scraping available
                          1) Only images.
                          2) All the text.
                          3) The whole html file.
                          4) Graps everything and organises following tags.
                \nWhat scraping method do you want to use?""")
                method = int(input())
                
                if not method in methods:
                    print("""\n\n
##########################################################################
This is not an available option. Please select one of the offered options.
##########################################################################
\n\n""")
                    continue

                
                self.scraper(url, method)
                print('\n')
                print("\n\nDo you want to scrap anything else from this website? (y/n)", end = '')
                answer = str(input())
                
                if answer == 'n':
                    print("\nDo you want to scrap another web page? (y/n)", end = '')
                    answer = str(input())
                    if(answer == 'n'):
                        print("\nClosing Scraper.")
                        self.finnish = True
                    else:
                        print("Introduce the url of the web you would like to scrape:", end = '')
                        url = input()
                    
                
            except:
                print("""\n\n
####################
Somthing went wrong.
####################
\n\n""")
    
    
    
    def scraper(self, web_url, method):
        # We request the server to send us the html, and then we start the parsing
        web_url = self.url_cleanup(web_url)
        request = requests.get(web_url)
        html = BeautifulSoup(request.text, 'html.parser')
        self.directory_creator(web_url)
        if method == 1:
            print("\n\nDownloading pictures from " + web_url)
            self.image_scraper(html)
            print("Successful Scraping!")
            
        if method == 2 or method == 3:
            print("\n\nSaving all the text from " + web_url + " in a .txt file.")
            self.text_scraper(html, web_url, method)
            print("Successful Scraping!")
            
        
        
    def image_scraper(self, html):

        image_tags = html.findAll('img')

        succesful_downloads = 0
        num_elements = len(image_tags) + 1

        self.printProgressBar( 0, num_elements, prefix = 'Progress:', suffix = 'Downloaded', length = 50)
        for i, image in enumerate(image_tags):
            i += 1
            try:
                url = image['src']
                response = requests.get(url)
            except:
                try:
                    url = image['data-src']
                    response = requests.get(url)
                except:
                    self.printProgressBar(i + 1, num_elements, prefix = 'Progress:', suffix = 'Complete', length = 50)
                    continue
                
            
            if response.status_code == 200:
                with open('img-' + str(succesful_downloads) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    #print("Downloading picture number: " + str(succesful_downloads))
                    f.close()
                    succesful_downloads += 1
            self.printProgressBar(i + 1, num_elements, prefix = 'Progress:', suffix = 'Complete', length = 50)

    
    def text_scraper(self, html, url, method):
        
        # We eliminate all not html content
        for script in html(['script', 'style']):
            script.extract()
        
        text = html.get_text()

        if method == 3:
            with io.open('html.txt', 'w', encoding = 'utf-8') as f:
                f.write(str(html))
        
        else:
        
            print("If you want the raw text, select 1. If you want layout text without blank lines, select 2.")
            raw = int(input())
            if raw == 1:
                with io.open('raw_text.txt', 'w', encoding = 'utf-8') as f:
                    f.write(text) 
                    
            if raw == 2:
                splitted_text = text.splitlines()
                with io.open('cleaned_text.txt', 'w', encoding = 'utf-8')  as f:
                    for line in splitted_text:
                        if line !='' and line != '\t' and not str.isspace(line):
                            f.write(line + '\n')
    
    
    
    def url_cleanup(self, url):
    
        if url.startswith('http://') or url.startswith('https://'):
            url = url
        elif url.startswith('www.'):
            url = 'http://' + url
        else:
            url = 'http://www.' + url
    
        return url
    
    
    def directory_creator(self, url):
        
        dir_name = url.split('.')[1]
        # create directory for model images
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # move to new directory
        os.chdir(dir_name)

    
    def printProgressBar (self, iteration, total, prefix = '', suffix = '', length = 100, fill = '|'):
    
        percent = ("{:.1f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        
        #print( str(prefix) + ' |' + str(bar) + '| ' + str(percent) + '% ' + str(suffix) + '\r', end = '\r')
        
        # Since we are using Spyder to develop this code, we are forced to learn how to use fstrings, because it's the only way that the 
        # code interpreter respects the carriage return when printint through terminal 
        print(F'\r{prefix} |{bar}| {percent}% {suffix}', end = '\r')
        
        # Print New Line on Complete
        if iteration == total: 
            print()
            
            

#scraper = WebScraper()
#scraper.terminal_menu()