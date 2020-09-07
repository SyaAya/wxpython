import wx

def click_button_1(event):
    frame.SetStatusText('Click! button_1')

def click_button_2(event):
    frame.SetStatusText('Click! button_2')

def click_button(event):
    if event.GetId() == 3333:
        frame.SetStatusText('Click! button_3')
    elif event.GetId() == 4444:
        frame.SetStatusText('Click! button_4')

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('#AFAFAF')
label = wx.StaticText(panel, -1, '作成したいレポートを選択してください。', pos=(10, 10))

button_1 = wx.Button(panel, wx.ID_ANY, 'ボタン１')
button_2 = wx.Button(panel, wx.ID_ANY, 'ボタン２')
button_3 = wx.Button(panel, 3333, 'ボタン３')
button_4 = wx.Button(panel, 4444, 'ボタン４')

button_1.Bind(wx.EVT_BUTTON, click_button_1)
button_2.Bind(wx.EVT_BUTTON, click_button_2)
frame.Bind(wx.EVT_BUTTON, click_button, button_3)
frame.Bind(wx.EVT_BUTTON, click_button, button_4)

layout = wx.GridSizer(rows=2, cols=2, gap=(0, 0))
layout.Add(button_1, 0, wx.GROW)
layout.Add(button_2, 0, wx.GROW)
layout.Add(button_3, 0, wx.GROW)
layout.Add(button_4, 0, wx.GROW)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()