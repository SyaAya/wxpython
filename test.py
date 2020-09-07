import wx
class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()

        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit')
        exitItem.SetBitmap(wx.Bitmap('C:\\Users\\cxie\\PycharmProjects\\wxpython\\quit.png'))
        fileButton.Append(exitItem)

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

        yesNoBox = wx.GenericMessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color Question',
                                             ['Green', 'Red', 'Blue', 'Yellow'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))

        aweText = wx.StaticText(panel, -1, "Awesome Text", (3, 3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3, 30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')

        self.SetTitle('Welcome ' + userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()


# family_name = input('Enter your family name: ')
# last_name = input('Enter your last name: ')
# department_name = input('Enter your department name: ')
# period_from = input('The week is from: ')
# period_to = input('to: ')
# period = (period_from + '-' + period_to)
# project_status = input('Enter your project status: ')
#
# print('【週報】' + family_name +'_週間作業実績報告(' + period + ')')
# print('関係各位\nお疲れ様です。\n' + family_name + last_name + '@' + department_name + 'です。\n')
# print('この一週間の作業をご報告いたします。\n報告期間：' + period)







#replace
#str(num)