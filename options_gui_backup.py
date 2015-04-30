import wx


class ExamplePanel(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Hi !! You have to find a set of english words embedded in n by n matrix of characters.", pos=(20, 30), size=(375,300), style=wx.TE_MULTILINE | wx.TE_READONLY )
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        #self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # A button
        self.button =wx.Button(self, label="Start", pos=(150, 300))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        # the edit control - one line version.
        #self.lblname = wx.StaticText(self, label="Your name :", pos=(20,60))
        #self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150, 60), size=(140,-1))
        #self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        #self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)
        # the combobox Control
        self.sampleList = ['Animals', 'FootBall Stars', 'Movie Names']
        self.lblhear = wx.StaticText(self, label="Choose the Topic", pos=(20, 90))
        self.edithear = wx.ComboBox(self, pos=(20, 120), size=(150, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)# in pos(column,row)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        #self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # Checkbox
        #self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?", pos=(20,180))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)
        # Radio Boxes
        radioList = ['Easy', 'Medium', 'Hard']
        rb = wx.RadioBox(self, label="Difficulty Level", pos=(20, 180), choices=radioList,  majorDimension=3,
                          style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event):
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        self.level=event.GetInt()
    def EvtComboBox(self, event):
        self.dictionary=event.GetString()        
        #self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        game_settings(self.dictionary,self.level)
        #self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    #def EvtText(self, event):
    #    self.logger.AppendText('EvtText: %s\n' % event.GetString())
    #def EvtChar(self, event):
    #   self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
    #  event.Skip()
    #def EvtCheckBox(self, event):
    #    self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())

class myFrame(wx.Frame):

    def __init__(self, parent,window_name): 
        wx.Frame.__init__(self, parent, title=window_name)
        self.mypanel=ExamplePanel(self)

app = wx.App(False)
frame = myFrame(None,"Word Search Puzzle")
#panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()