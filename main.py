# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:51:24 2020

@author: bxz19
"""


import wx
import graphic_menu
import terminal_menu

  
   
if __name__ == "__main__":
    
    inp = str(input("Terminal[t] or Aplication[a]? "))
    sod = str(input("Do you want to use scraping on a static[s] or dynamic[d] website?"))

    
    while(True):        
        
        if inp == 'a':
            app = wx.App()
            frame = graphic_menu.HelloFrame('WebScraper', sod)
            frame.Show()
            app.MainLoop()
            
        elif inp == 't':
            terminal = terminal_menu.TerminalMenu()
            terminal.terminal_menu(inp, sod)
            
            close = str(input("Do you want to continue using the scraper? [y/n]"))
        
        if(close == 'n'):
            print("Closing scraper.")
            break
            
            
        
        if(close == 'y'):
            inp = str(input("Terminal[t] o Aplicació[a]? "))
    

