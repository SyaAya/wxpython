import wx

class mainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, 'レポート自動作成システム', size=(400, 500), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        self.CreateStatusBar()
        self.SetStatusText('TestApp')
        self.GetStatusBar().SetBackgroundColour(None)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.set_screen(Panel_1)


    def set_screen(self,panel):
        self.sizer.Clear(False)
        self.DestroyChildren()

        self.now_panel=panel(self)
        self.sizer.Add(self.now_panel, 1, wx.EXPAND)
        self.sizer.Layout()



class Panel_1(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.parent = parent

        # title
        title_text = wx.StaticText(self, wx.ID_ANY, 'レポート', style=wx.TE_CENTER)
        font_title = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_title)
        title_text.SetToolTip('Hello')

        # message
        msg = wx.StaticText(self, wx.ID_ANY, '作成したいレポートを選択してください', style=wx.TE_CENTER)
        msg.SetForegroundColour('#808080')

        # daily button
        daily_button = wx.Button(self, wx.ID_ANY, '日報')
        # daily_button.Bind(wx.EVT_BUTTON, self.click_daily_button)

        # week button
        week_button = wx.Button(self, wx.ID_ANY, '週報')
        week_button.Bind(wx.EVT_BUTTON, self.click_week_button)

        # month button
        month_button = wx.Button(self, wx.ID_ANY, '作業日報')
        # daily_button.Bind(wx.EVT_BUTTON, self.click_daily_button)

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

    def click_week_button(self, event):
        self.parent.set_screen(Panel_2)


class Panel_2(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.parent=parent

        # title
        title_text = wx.StaticText(self, wx.ID_ANY, '週報作成', style=wx.TE_CENTER)
        font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_Title)

        # message
        msg = wx.StaticText(self, wx.ID_ANY, '宛先を入力して下さい', style=wx.TE_CENTER)
        msg.SetForegroundColour('#808080')

        # textbox
        to_label = wx.StaticText(self, wx.ID_ANY, 'To: ')
        to_textbox = wx.TextCtrl(self, wx.ID_ANY)
        cc_label = wx.StaticText(self, wx.ID_ANY, 'Cc: ')
        cc_textbox = wx.TextCtrl(self, wx.ID_ANY)
        bcc_label = wx.StaticText(self, wx.ID_ANY, 'Bcc: ')
        bcc_textbox = wx.TextCtrl(self, wx.ID_ANY)

        self.to_txt = to_textbox

        # back button
        back_button = wx.Button(self, wx.ID_ANY, '戻る')
        back_button.Bind(wx.EVT_BUTTON, self.click_back_button)

        # next button
        next_button = wx.Button(self, wx.ID_ANY, '次へ')
        next_button.Bind(wx.EVT_BUTTON, self.click_next_button)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(wx.Size(0, 10))
        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 10))
        layout.Add(msg, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 10))
        layout.Add(to_label, flag=wx.ALIGN_CENTER)
        layout.Add(to_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(cc_label, flag=wx.ALIGN_CENTER)
        layout.Add(cc_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(bcc_label, flag=wx.ALIGN_CENTER)
        layout.Add(bcc_textbox, flag=wx.ALIGN_CENTER)
        layout.Add(wx.Size(0, 30))
        layout.Add(back_button, flag=wx.ALIGN_CENTER)
        layout.Add(next_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    def click_back_button(self, event):
        self.parent.set_screen(Panel_1)

    def click_next_button(self, event):
        self.parent.set_screen(Panel_3)
        print(self.to_txt)


class Panel_3(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.parent=parent

        # title
        title_text = wx.StaticText(self, wx.ID_ANY, '週報', style=wx.TE_CENTER)
        font_Title = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title_text.SetFont(font_Title)

        # message
        msg = wx.StaticText(self, wx.ID_ANY, '情報を埋めてください。', style=wx.TE_CENTER)
        msg.SetForegroundColour('#808080')

        # address
        #address_to =

        # back button
        back_button = wx.Button(self, wx.ID_ANY, '戻る')
        back_button.Bind(wx.EVT_BUTTON, self.click_back_button)

        # # next button
        # next_button = wx.Button(self, wx.ID_ANY, '次へ')
        # next_button.Bind(wx.EVT_BUTTON, self.click_next_button)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(title_text, flag=wx.ALIGN_CENTER)
        layout.Add(msg, flag=wx.ALIGN_CENTER)
        layout.Add(back_button, flag=wx.ALIGN_CENTER)
        # layout.Add(next_button, flag=wx.ALIGN_CENTER)

        self.SetSizer(layout)

    def click_back_button(self, event):
        self.parent.set_screen(Panel_2)

if __name__ == '__main__':

    application = wx.App()
    frame = mainFrame()
    frame.Show()
    application.MainLoop()