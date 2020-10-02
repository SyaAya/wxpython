import wx
from pubsub import pub
class OtherFrame(wx.Frame):
    """"""
    def __init__(self):
        """Constructor"""
        super().__init__(None, title="Secondary Frame")
        panel = wx.Panel(self)
        msg = "Enter a Message to send to the main frame"
        instructions = wx.StaticText(panel, label=msg)
        self.msg_txt = wx.TextCtrl(panel, value="")
        close_btn = wx.Button(panel, label="Send and Close")
        close_btn.Bind(wx.EVT_BUTTON, self.on_send_and_slose)
        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL|wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msg_txt, 0, flags, 5)
        sizer.Add(close_btn, 0, flags, 5)
        panel.SetSizer(sizer)
    def on_send_and_slose(self, event):
        """
        Send a message and close frame
        """
        msg = self.msg_txt.GetValue()
        pub.sendMessage("panel_listener", message=msg)
        pub.sendMessage("panel_listener", message="test2",
                        arg2="2nd argument!")
        self.Close()
class MyPanel(wx.Panel):
    """"""
    def __init__(self, parent):
        """Constructor"""
        super().__init__(parent)
        pub.subscribe(self.my_listener, "panel_listener")
        btn = wx.Button(self, label="Open Frame")
        btn.Bind(wx.EVT_BUTTON, self.on_open_frame)
    def my_listener(self, message, arg2=None):
        """
        Listener function
        """
        print(f"Received the following message: {message}")
        if arg2:
            print(f"Received another arguments: {arg2}")
    def on_open_frame(self, event):
        """
        Opens secondary frame
        """
        frame = OtherFrame()
        frame.Show()
class MyFrame(wx.Frame):
    """"""
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None,
                          title="New PubSub API Tutorial")
        panel = MyPanel(self)
        self.Show()
if __name__ == "__main__":
    app = wx.App(False)








# import wx
# class windowClass(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(windowClass, self).__init__(*args, **kwargs)
#         self.basicGUI()
#
#     def basicGUI(self):
#         panel = wx.Panel(self)
#         menuBar = wx.MenuBar()
#         fileButton = wx.Menu()
#         editButton = wx.Menu()
#
#         exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit')
#         exitItem.SetBitmap(wx.Bitmap('C:\\Users\\cxie\\PycharmProjects\\wxpython\\quit.png'))
#         fileButton.Append(exitItem)
#
#         menuBar.Append(fileButton, 'File')
#         menuBar.Append(editButton, 'Edit')
#
#         self.SetMenuBar(menuBar)
#         self.Bind(wx.EVT_MENU, self.Quit, exitItem)
#
#         nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')
#
#         if nameBox.ShowModal()==wx.ID_OK:
#             userName = nameBox.GetValue()
#
#         yesNoBox = wx.GenericMessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
#         yesNoAnswer = yesNoBox.ShowModal()
#         yesNoBox.Destroy()
#
#         if yesNoAnswer == wx.ID_NO:
#             userName = 'Loser!'
#
#         chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
#                                              'Color Question',
#                                              ['Green', 'Red', 'Blue', 'Yellow'])
#         if chooseOneBox.ShowModal() == wx.ID_OK:
#             favColor = chooseOneBox.GetStringSelection()
#
#         wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))
#
#         aweText = wx.StaticText(panel, -1, "Awesome Text", (3, 3))
#         aweText.SetForegroundColour('#67cddc')
#         aweText.SetBackgroundColour('black')
#
#         rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3, 30))
#         rlyAweText.SetForegroundColour(favColor)
#         rlyAweText.SetBackgroundColour('black')
#
#         self.SetTitle('Welcome ' + userName)
#         self.Show(True)
#
#     def Quit(self, e):
#         self.Close()
#
# def main():
#     app = wx.App()
#     windowClass(None)
#     app.MainLoop()
#
# main()


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