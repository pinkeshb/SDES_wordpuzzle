# grid size is not intputted from user. but default of 8 is used
import wx
class ExamplePanel(wx.Panel):
    """This is the panel has Dictionary, Level, Grid size widgets"""
    def __init__(self, parent,app):
        wx.Panel.__init__(self, parent)
        self.level=0
        self.dictionary="Animals"# default values
        self.grid_size=12
        self.app=app
        
        self.quote = wx.StaticText(self, label="Hi !! You have to find a set of english words embedded in n by n matrix of characters.", pos=(20, 30), size=(375,300), style=wx.TE_MULTILINE | wx.TE_READONLY )
        # A button
        self.button =wx.Button(self, label="Start", pos=(150, 320))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        
        # the combobox Control
        self.sampleList = ['Animals', 'Car Brands']
        self.lblhear = wx.StaticText(self, label="Choose the Topic", pos=(20, 90))

        self.edithear = wx.ComboBox(self, pos=(20, 120), size=(150, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)# in pos(column,row)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        
        self.lblhear1 = wx.StaticText(self, label="Grid Size", pos=(20, 170))

        self.edithear1 = wx.ComboBox(self, pos=(20, 200), size=(150, -1), choices=['8 x 8', '12 x 12'], style=wx.CB_DROPDOWN)# in pos(column,row)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox1, self.edithear1)
        

        # Radio Boxes
        radioList = ['Easy', 'Medium', 'Hard']
        rb = wx.RadioBox(self, label="Difficulty Level", pos=(20, 250), choices=radioList,  majorDimension=3,
                          style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event):
        
        self.level=event.GetInt()
    def EvtComboBox(self, event):
        self.dictionary=event.GetString()        
        
    def EvtComboBox1(self, event):
        temp=event.GetString()
        if temp=="8 x 8":
            self.grid_size=8
        else:
            self.grid_size=12

    
    def OnClick(self,event):
        
        self.app.ExitMainLoop()
        #self.parent1.Close(True)
        
    
class myFrame(wx.Frame):

    def __init__(self, parent,window_name,app): 
        wx.Frame.__init__(self, parent, title=window_name)
        
        self.mypanel=ExamplePanel(self,app)
        
    def OnExit(self):# could not rectify clsing the frame problem
        self.Close(True)


if __name__=='__main__':
    app = wx.App(False)
    frame = myFrame(None,"Word Search Puzzle",app)
    #panel = ExamplePanel(frame)
    frame.Show()
    app.MainLoop()
    #frame.Close()
    print frame.mypanel.level, frame.mypanel.dictionary, frame.mypanel.grid_size
    

def start_setup():
    app = wx.App(False)
    frame = myFrame(None,"Word Search Puzzle",app)
    frame.Show()
    app.MainLoop()
    #frame.Close()
    return frame.mypanel.level, frame.mypanel.dictionary, frame.mypanel.grid_size
    
