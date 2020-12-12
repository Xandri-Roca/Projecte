# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:15:07 2020

@author: bxz19
"""
import time
import requests # Maybe upgrade to only use urllib and not requests
import os
from bs4 import BeautifulSoup
import io

from selenium import webdriver

import graphic_menu



class WebScraper():
    
    def __init__(self):
        self.finnish = False
        
    
    def scraper(self, web_url, method, menu, sod):
        
        # We relocate in the folder of this file
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        
        # We clean up the url to make it fit our required format
        web_url = self.url_cleanup(web_url)
        
        # We request the server to send us the html, and then we start the parsing.
        if(sod == 's'):
           html = self.get_static_html(web_url)
            
        if(sod == 'd'):
            html = self.get_dynamic_html(web_url)
            
        
        # A new directory where all the content will be stored is created with the name of the website.
        self.directory_creator(web_url)
        
        
        if method == 1:
            
            if menu == 't':            
                print("\n\nDownloading pictures from " + web_url)
            self.image_scraper(html)
            if menu == 't':
                print("Successful Scraping!")
                
            if menu == 'a':
                text = "Successful Scraping!"
                frame = graphic_menu.OtherFrame(text)
            
        if method == 2 or method == 3:
            if menu == 't' and method == 2:
                print("\n\nSaving all the text from " + web_url + " in a .txt file.")
            if menu == 't' and method == 3:
                print("\n\nSaving the html from " + web_url + " in a .txt file.")
                
            self.text_scraper(html, web_url, method, menu)
            
            if menu == 't':
                print("Successful Scraping!")
            if menu == 'a':
                text = "Successful Scraping!"
                frame = graphic_menu.OtherFrame(text)
                
        if method == 4:
            if menu == 't':            
                print("\n\nDownloading pictures from " + web_url)
            self.image_scraper(html)
            if menu == 't':
                print("\n\nSaving all the text from " + web_url + " in a .txt file.")
            self.text_scraper(html, web_url, 2, menu)
            if menu == 't':
                print("\n\nSaving the html from " + web_url + " in a .txt file.")
            self.text_scraper(html, web_url, 3, menu)
            if menu == 't':
                print("Successful Scraping!")
            if menu == 'a':
                text = "Successful Scraping!"
                frame = graphic_menu.OtherFrame(text)
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

    
    def text_scraper(self, html, url, method, menu):
        
        # We eliminate all not html content
        for script in html(['script', 'style']):
            script.extract()
        
        text = html.get_text()

        if method == 3:
            with io.open('html.txt', 'w', encoding = 'utf-8') as f:
                f.write(str(html))
        
        else:
            
            if menu == 't':
                print("If you want the raw text, select 1. If you want layout text without blank lines, select 2.")
                raw = int(input())
            
            if menu == 'a':
                raw = 2
                
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
            
    def get_static_html(self, url):
        request = requests.get(url)
        return BeautifulSoup(request.text, 'html.parser')
    
    
    def get_dynamic_html(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        
        html = driver.page_source
        
        driver.close()
        return BeautifulSoup(html, 'html.parser')
            

#scraper = WebScraper()
#scraper.terminal_menu()