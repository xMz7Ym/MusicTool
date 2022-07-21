# -*- coding:utf-8 -*-
import requests
import wx
import wx.adv
import os
list1 = []
def warn():
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='MuiscTool', size=(594, 153),name='frame',style=541072960)

            self.qdck = wx.Panel(self)
            self.Centre()
            self.bq1 = wx.StaticText(self.qdck,size=(578, 37),pos=(-3, 16),label='本软件仅供学习交流，如作他用所承受的法律责任一概与作者无关,下载者务必24小时内删除本软件',name='staticText',style=2321)
            self.agree = wx.Button(self.qdck,size=(80, 32),pos=(327, 60),label='同意观点',name='agree')
            self.agree.Bind(wx.EVT_BUTTON,self.agree_anbdj)
            self.quit = wx.Button(self.qdck,size=(80, 32),pos=(137, 60),label='退出程序',name='quit')
            self.quit.Bind(wx.EVT_BUTTON,self.quit_anbdj)

        def agree_anbdj(self,event):
            list1.append(1)
            self.Destroy()




        def quit_anbdj(self,event):
            self.Destroy()



    class myApp(wx.App):
        def  OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True


    app = myApp()
    app.MainLoop()
    del app




# -*- coding:utf-8 -*-


def body():
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='MuiscTool', size=(844, 578), name='frame', style=541072384)
            icon = wx.Icon(r'.\data\musictool_icon.png')
            self.SetIcon(icon)
            self.qdck = wx.Panel(self)
            self.Centre()
            self.bq1 = wx.StaticText(self.qdck, size=(328, 24), pos=(-23, 520), label='作者：不会GUI的xMz7Ym，不会Java的Chank',
                                     name='staticText', style=2309)
            self.cjljk1 = wx.adv.HyperlinkCtrl(self.qdck, size=(75, 22), pos=(753, 520), name='hyperlink',
                                               label='GitHub地址', url='https://github.com/xmz7ym', style=1)
            self.ydan1 = wx.adv.CommandLinkButton(self.qdck, size=(200, 57), pos=(550, 79), name='button',
                                                  mainLabel='下载歌单', note='根据歌单下载歌曲')
            self.ydan1.Bind(wx.EVT_BUTTON, self.ydan1_anbdj)
            self.ydan2 = wx.adv.CommandLinkButton(self.qdck, size=(200, 69), pos=(550, 162), name='button',
                                                  mainLabel='下载歌曲', note='根据歌曲名或歌曲id下载歌曲')
            self.ydan2.Bind(wx.EVT_BUTTON, self.ydan2_anbdj)
            self.ydan3 = wx.adv.CommandLinkButton(self.qdck, size=(200, 87), pos=(550, 260), name='button',
                                                  mainLabel='歌词下载', note='根据用户文件夹内的歌曲补全对应的歌词（可以在MP3等设备上看到歌词）')
            self.ydan3.Bind(wx.EVT_BUTTON, self.ydan3_anbdj)
            self.ydan4 = wx.adv.CommandLinkButton(self.qdck, size=(200, 95), pos=(550, 380), name='button',
                                                  mainLabel='ncm转码', note='将网易云加密音频文件转码成mp3文件')
            self.ydan4.Bind(wx.EVT_BUTTON, self.ydan4_anbdj)
            self.bq5 = wx.StaticText(self.qdck, size=(376, 74), pos=(33, 400),
                                     label='温馨提示：本工具永久免费\n如若从任何渠道付费获得，请立即给其差评。\n因为本产品用Python写编的，可能会出现缺库的情况\n如果出现闪退请使用win10及以上的操作系统来执行本程序\n',
                                     name='staticText', style=2321)
            tpk2_p = wx.Image(r'.\data\musictool_ui.png').ConvertToBitmap()
            self.tpk2 = wx.StaticBitmap(self.qdck, bitmap=tpk2_p, size=(298, 259), pos=(75, 64), name='staticBitmap',
                                        style=0)

        def ydan1_anbdj(self, event):

            self.Destroy()
            import playlistDownload
            body()


        def ydan2_anbdj(self, event):

            self.Destroy()
            import songsDownload
            body()


        def ydan3_anbdj(self, event):
            self.Destroy()
            import lrcDown

            body()

        def ydan4_anbdj(self, event):

            wx.MessageBox(f'暂未开发，加入q群576329671一键催更~~~', 'Tip')

    class myApp(wx.App):
        def OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True


    app = myApp()
    app.MainLoop()
    del app
def icon():
    dir_name = 'data'  # 设置文件夹的名字
    if not os.path.exists(dir_name):  # os模块判断并创建
        os.mkdir(dir_name)
        source = requests.get(url="http://43.138.199.122:8081/images/musictool_ui.png").content
        with open(r'.\data\musictool_ui.png', 'wb') as f:
            f.write(source)
        source = requests.get(url="http://43.138.199.122:8081/images/page.png").content
        with open(r'.\data\musictool_icon.png', 'wb') as f:
            f.write(source)


warn()

icon()
if list1 != []:

    body()
else:
    pass
