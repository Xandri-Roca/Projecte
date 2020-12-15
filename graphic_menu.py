import wx
import scraping_motor



class HelloFrame(wx.Frame):
   
    def __init__(self, title, sod):
        super().__init__(None, title= title, size=(350, 500))
       
        
        self.sod = sod
        
        vertical_box_sizer = wx.BoxSizer(wx.VERTICAL) #Creem la finestra
        self.SetSizer(vertical_box_sizer)
        
        panel = wx.Panel(self) #Crear el panel (top en la jerarquía) on afegirem els widgets.
        
        vertical_box_sizer.Add(panel,
                               wx.ID_ANY,
                               wx.EXPAND | wx.ALL,
                               10) # Afegim el panell al frame creat (10 es la separació)
       
        grid = wx.GridSizer(6, 1, 0, 0) # Creem la matriu on afegirem els widgets
        
        self.text = wx.TextCtrl(panel, size=(150, -1)) # Creem els
     
        # Now configure the enter button
        enter_button = wx.Button(panel, label='Scrap', style=wx.ALIGN_LEFT)
        enter_button.Bind(wx.EVT_BUTTON, self.set_name)
        # Next set up the text label
        self.label = wx.StaticText(panel,
                                   label='Welcome',
                                   style=wx.ALIGN_LEFT)
        font_label = wx.Font(20, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        self.label.SetFont(font_label)
        
        self.label1 = wx.StaticText(panel,
                                   label='Insert URL:',
                                   style=wx.ALIGN_LEFT)
        
        self.label2 = wx.StaticText(panel,
                                   label='Chose Option:',
                                   style=wx.ALIGN_LEFT)
        
        
        
        self.option = wx.ListBox(panel)
        self.option.InsertItems(['1- Only images','2- All the text','3- Whole html file','4- All elements'],0)
        
        
        
        
       
        # Add the widgets to the grid sizer to handle layout
        grid.AddMany([self.label, self.label1 ,self.text, self.label2, self.option, enter_button])
        # Set the sizer on the panel
        panel.SetSizer(grid)
        # Centre the Frame on the Computer Screen
        self.Centre()
       
        
       
    def show_message(self, event):
        
        dialog = wx.MessageDialog(None,
                                      message="Files storedd at" + ' ' +self.directory.GetLineText(0),
                                      caption="Hello",
                                      style=wx.OK)
        dialog.ShowModal()
       
    def set_name(self, event):
        
        
        if  self.text.IsModified() and (self.option.IsSelected(0) or self.option.IsSelected(1) or self.option.IsSelected(2) or self.option.IsSelected(3)):
            self.name = self.text.GetLineText(0)
            self.optionChosed = self.option.GetSelection()
            self.label.SetLabelText('Scrapping ' + self.name +' with option ' + str(self.optionChosed + 1))
            
            scraping_motor.WebScraper().scraper(self.name, self.optionChosed + 1, 'a', self.sod)
            
        else:
            
            self.label.SetLabelText('Fullfill all the options..')


class OtherFrame(wx.Frame):
    
    #Class used for creating frames other than the main one
    

    def __init__(self, text, title='Message', parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        panel = wx.Panel(self)
        istr = wx.StaticText(panel, label=text)
        font_istr = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        istr.SetFont(font_istr)
        self.Show()



# Run the GUI application
#app = wx.App()
#frame = HelloFrame('WebScraper')
#frame.Show()
#app.MainLoop()
  
