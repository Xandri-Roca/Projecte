# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:03:50 2020

@author: bxz19
"""
import scraping_motor



class TerminalMenu():
    
    
    def __init__(self):
        self.finnish = False

        
    def terminal_menu(self, menu, sod):
            #This menu is to use this software from the terminal itself.
            print("\n\nHi, welcome to this Web Scraper")
            print("Introduce the url of the web you would like to scrape:", end = '')
            url = input()
            while not self.finnish:
                try:
                
                    methods = [1, 2, 3, 4]
                    print("""\n\nThere are different types of scraping available
                              1) Only images.
                              2) All the text.
                              3) The whole html file.
                              4) Save everything.
                    \nWhat scraping method do you want to use?""")
                    method = int(input())
                    
                    if not method in methods:
                        print("""\n\n
    ##########################################################################
    This is not an available option. Please select one of the offered options.
    ##########################################################################
    \n\n""")
                        continue
    
                    
                    scraping_motor.WebScraper().scraper(url, method, menu, sod)
    
                    
    
                    print('\n')
                    print("\n\nDo you want to scrap anything else from this website? (y/n)", end = '')
                    answer = str(input())
                    
                    if answer == 'n':
                        print("\nDo you want to scrap another web page? (y/n)", end = '')
                        answer = str(input())
                        if(answer == 'n'):
                            print("\nClosing Terminal Menu.")
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
    
    
        
        
        
