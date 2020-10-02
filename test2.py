import wx
from pubsub import pub


class mainFrame(wx.Frame):
    def __init__(self):
        # in Python 3, super() is enough, no need for the parameters inside, i.e. super(mainFrame, self) -> super()
        super(mainFrame, self).__init__(None, wx.ID_ANY, 'Mail App', size=(400, 500),
                                        style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        self.CreateStatusBar()
        self.SetStatusText('TestApp')
        self.GetStatusBar().SetBackgroundColour(None)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.set_screen(Panel_1)

    def set_screen(self, panel):
        self.sizer.Clear(False)
        self.DestroyChildren()

        self.now_panel = panel(self)
        self.sizer.Add(self.now_panel, 1, wx.EXPAND)
        self.sizer.Layout()


class Panel_1(wx.Panel):
    def __init__(self, parent):
        # super(Panel_1, self) -> super()
        super(Panel_1, self).__init__(parent, wx.ID_ANY)
        self.parent = parent
        pub.subscribe(self.myListener, "panelListener")

        btn = wx.Button(self, label="Input email addresses")
        btn.Bind(wx.EVT_BUTTON, self.onOpenFrame)

        # title
        title_text = wx.StaticText(self, wx.ID_ANY, 'TITLE', style=wx.TE_CENTER)
        font_title = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_title)
        title_text.SetToolTip('Hello')

        # message
        msg = wx.StaticText(self, wx.ID_ANY, 'MESSAGE', style=wx.TE_CENTER)
        msg.SetForegroundColour('#808080')

        # daily button
        daily_button = wx.Button(self, wx.ID_ANY, 'DAILY')

        # week button
        week_button = wx.Button(self, wx.ID_ANY, 'WEEKLY')
        # week_button.Bind(wx.EVT_BUTTON, self.click_week_button)

        # month button
        month_button = wx.Button(self, wx.ID_ANY, 'MONTHLY')

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(wx.Size(0, 10))
        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 10))
        layout.Add(msg, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 30))
        layout.Add(daily_button, flag=wx.ALIGN_CENTER)
        layout.Add(week_button, flag=wx.ALIGN_CENTER)
        layout.Add(month_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    # def click_week_button(self, event):
    #     self.parent.set_screen(Panel_2)

    def myListener(self, msg1, msg2, msg3):
        print("TO: " + msg1 + " CC: " + msg2 + " BCC: " + msg3)

        answer = wx.StaticText(self, wx.ID_ANY, "\r\r\r" + "TO: " + msg1 + "\r" + "CC: " + msg2 + "\r" + "BCC: " + msg3)

    def onOpenFrame(self, event):
        frame = OtherFrame()
        frame.Show()


class OtherFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Email Addresses", size=(250, 200))
        panel = wx.Panel(self)

        # textbox
        to_label = wx.StaticText(self, wx.ID_ANY, 'TO: ')
        self.to_text = wx.TextCtrl(self, -1, size=(200, -1))

        cc_label = wx.StaticText(self, wx.ID_ANY, 'CC: ')
        self.cc_text = wx.TextCtrl(self, -1, size=(200, -1))

        bcc_label = wx.StaticText(self, wx.ID_ANY, 'BCC: ')
        self.bcc_text = wx.TextCtrl(self, -1, size=(200, -1))

        doneBtn = wx.Button(self, wx.ID_ANY, 'done')
        doneBtn.Bind(wx.EVT_BUTTON, self.onSendAndClose)

        layout = wx.BoxSizer(wx.VERTICAL)

        layout.Add(to_label, flag=wx.ALIGN_CENTER)
        layout.Add(self.to_text, flag=wx.ALIGN_CENTER)
        layout.Add(cc_label, flag=wx.ALIGN_CENTER)
        layout.Add(self.cc_text, flag=wx.ALIGN_CENTER)
        layout.Add(bcc_label, flag=wx.ALIGN_CENTER)
        layout.Add(self.bcc_text, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 20))
        layout.Add(doneBtn, flag=wx.ALIGN_RIGHT)

        self.SetSizer(layout)

    def onSendAndClose(self, event):
        to_text = self.to_text.GetValue()

        cc_text = self.cc_text.GetValue()

        bcc_text = self.bcc_text.GetValue()

        pub.sendMessage("panelListener", msg1=to_text, msg2=cc_text, msg3=bcc_text)

        self.Close()


class Panel_2(wx.Panel):
    def __init__(self, parent):
        super(Panel_2, self).__init__(parent, wx.ID_ANY)
        self.parent = parent

        # title
        title_text = wx.StaticText(self, wx.ID_ANY, 'TITLE', style=wx.TE_CENTER)
        font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_Title)

        # message
        msg = wx.StaticText(self, wx.ID_ANY, 'MESSAGE', style=wx.TE_CENTER)
        msg.SetForegroundColour('#808080')

        # textbox
        to_label = wx.StaticText(self, wx.ID_ANY, 'To: ')
        # to_textbox = wx.TextCtrl(self, wx.ID_ANY)
        self.to_text = wx.TextCtrl(self, value="")

        cc_label = wx.StaticText(self, wx.ID_ANY, 'Cc: ')
        # cc_textbox = wx.TextCtrl(self, wx.ID_ANY)
        self.cc_text = wx.TextCtrl(self, value="")

        bcc_label = wx.StaticText(self, wx.ID_ANY, 'Bcc: ')
        # bcc_textbox = wx.TextCtrl(self, wx.ID_ANY)
        self.bcc_text = wx.TextCtrl(self, value="")

        # back button
        back_button = wx.Button(self, wx.ID_ANY, '<<')
        back_button.Bind(wx.EVT_BUTTON, self.click_back_button)

        # next button
        next_button = wx.Button(self, wx.ID_ANY, '>>')
        next_button.Bind(wx.EVT_BUTTON, self.click_next_button)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(wx.Size(0, 10))
        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 10))
        layout.Add(msg, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 10))
        layout.Add(to_label, flag=wx.ALIGN_CENTER)
        # layout.Add(to_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(self.to_text, flag=wx.ALIGN_CENTER)
        layout.Add(cc_label, flag=wx.ALIGN_CENTER)
        # layout.Add(cc_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(self.cc_text, flag=wx.ALIGN_CENTER)
        layout.Add(bcc_label, flag=wx.ALIGN_CENTER)
        # layout.Add(bcc_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(self.bcc_text, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 30))
        layout.Add(back_button, flag=wx.ALIGN_CENTER)
        layout.Add(next_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    def click_back_button(self, event):
        self.parent.set_screen(Panel_1)

    def click_next_button(self, event):
        self.parent.set_screen(Panel_3)


class Panel_3(wx.Panel):
    def __init__(self, parent):
        super(Panel_3, self).__init__(parent, wx.ID_ANY)
        self.parent = parent

        # title
        # title_text = wx.StaticText(self, wx.ID_ANY, 'TITLE', style=wx.TE_CENTER)
        # font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        # title_text.SetFont(font_Title)

        # message
        # msg = wx.StaticText(self, wx.ID_ANY, 'MESSAGE', style=wx.TE_CENTER)
        # msg.SetForegroundColour('#808080')

        # address
        # address_to =

        # back button
        # back_button = wx.Button(self, wx.ID_ANY, '<<')
        # back_button.Bind(wx.EVT_BUTTON, self.click_back_button)

        # # next button
        # next_button = wx.Button(self, wx.ID_ANY, 'fox')
        # next_button.Bind(wx.EVT_BUTTON, self.click_next_button)

        # layout = wx.BoxSizer(wx.VERTICAL)
        # layout.Add(title_text, flag=wx.ALIGN_CENTER)
        # layout.Add(msg, flag=wx.ALIGN_CENTER)
        # layout.Add(back_button, flag=wx.ALIGN_CENTER)
        # layout.Add(next_button, flag=wx.ALIGN_CENTER)

        # self.SetSizer(layout)

    # def click_back_button(self, event):
    # self.parent.set_screen(Panel_2)


if __name__ == '__main__':
    application = wx.App()
    frame = mainFrame()
    frame.Show()
    application.MainLoop()