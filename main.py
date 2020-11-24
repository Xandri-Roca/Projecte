# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:51:24 2020

@author: bxz19
"""
import wx
import first_Menu
import scraper

  
   
if __name__ == "__main__":
    
    while(True):
        inp = str(input("Terminal[t] o Aplicació[a]? "))
        if inp == 'a':
            app = wx.App()
            frame = first_Menu.HelloFrame('WebScraper')
            frame.Show()
            app.MainLoop()
        elif inp == 't':
            scraper.WebScraper().terminal_menu()
    
    