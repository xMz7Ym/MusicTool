# -*- coding:utf-8 -*-
import wx.adv
import wx
import MusicTool_code
id = []
song_list = []
def idMaker():
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='', size=(651, 391),name='frame',style=541072960)
            self.qdck = wx.Panel(self)
            self.Centre()
            self.bq1 = wx.StaticText(self.qdck,size=(507, 75),pos=(80, 7),label='请在下方输入您想要下载个歌曲的名称\\id\\网址\n如果想多输如下载可以回车换行继续输如下一首的名称\\id\\网址\n可以支持三种格式混合下载 但是每一行必须是名称\\id\\网址',name='staticText',style=2321)
            self.bjk2 = wx.TextCtrl(self.qdck,size=(367, 166),pos=(140, 90),value='',name='text',style=1073741856)
            self.an1 = wx.Button(self.qdck,size=(196, 48),pos=(230, 263),label='输入完成',name='button')
            self.an1.Bind(wx.EVT_BUTTON,self.an1_anbdj)
            self.cjljk1 = wx.adv.HyperlinkCtrl(self.qdck,size=(60, 22),pos=(563, 331),name='hyperlink',label='网易云官网',url='https://music.163.com/',style=1)


        def an1_anbdj(self,event):

            text = str(self.bjk2.GetValue())
            t = ''
            for i in text:
                if i != '\n':
                    t += i
                else:
                    song_list.append(t)
                    t = ''
            song_list.append(t)
            sl = [i for i in song_list if i != '']
            t = ''
            for i in sl:
                try:
                    id.append(int(i))
                except:
                    try:
                        id.append(MusicTool_code.songURL(i))
                    except:
                        try:
                            id.append(MusicTool_code.nameToOneid(i))

                        except:
                            t+= i+'解析错误'

            if t != '':
                wx.MessageBox(t, 'Warn')
            else:
                self.Destroy()
                pass
    class myApp(wx.App):
        def  OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True


    app = myApp()
    app.MainLoop()


def selectAndDown():
    # -*- coding:utf-8 -*-
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='下载', size=(754, 489), name='frame', style=541072448)
            icon = wx.Icon(r'.\data\musictool_icon.png')
            self.SetIcon(icon)
            self.selectAnddownload = wx.Panel(self)
            self.Centre()
            self.xzxz = wx.CheckListBox(self.selectAnddownload, size=(270, 303), pos=(50, 29), name='listBox',
                                        choices=nameN, style=1073741824)
            self.an2 = wx.Button(self.selectAnddownload, size=(100, 50), pos=(60, 351), label='全选', name='button')
            self.an2.Bind(wx.EVT_BUTTON, self.an2_anbdj)
            self.an3 = wx.Button(self.selectAnddownload, size=(100, 50), pos=(203, 353), label='全不选', name='button')
            self.an3.Bind(wx.EVT_BUTTON, self.an3_anbdj)
            self.bq1 = wx.StaticText(self.selectAnddownload, size=(303, 164), pos=(376, 71),
                                     label=f'从您输入的歌曲中共找到了共计：{len(nameN)}首歌曲\n\n请在左侧复选框中将您想要的歌曲选取\n\n然后再点击开始下载\n\n如果歌曲不对的话请检查是否歌曲名是否正确\n\n或者选择输入歌曲ID进行下载\n',
                                     name='staticText', style=2321)
            self.dxk1 = wx.CheckBox(self.selectAnddownload, size=(80, 24), pos=(439, 300), name='check', label='歌曲下载',
                                    style=16384)
            self.dxk1.SetValue(True)
            self.dxk2 = wx.CheckBox(self.selectAnddownload, size=(80, 24), pos=(570, 300), name='check', label='歌词下载',
                                    style=16384)
            self.dxk2.SetValue(True)
            self.ydan1 = wx.adv.CommandLinkButton(self.selectAnddownload, size=(158, 62), pos=(575, 384), name='button',
                                                  mainLabel='开始下载', note='点击即可下载')
            self.ydan1.Bind(wx.EVT_BUTTON, self.ydan1_anbdj)

        def an2_anbdj(self, event):

            self.xzxz.SetChecked(range(0, self.xzxz.GetCount()))

        def an3_anbdj(self, event):

            self.xzxz.SetChecked([])


        def ydan1_anbdj(self, event):

            warn_Tip = ''
            song_id = self.xzxz.GetCheckedItems()
            if len(song_id) == 0:
                wx.MessageBox(f'请至少选择一首歌进行下载', 'Warn')
            else:
                wx.MessageBox(f'已经开始下载进程\n共计将要下载{len(song_id)}首歌', 'Tip')
                for i in song_id:
                    try:
                        MusicTool_code.musicDownload(nameN[i], id[i], self.dxk1.GetValue())
                        try:
                            MusicTool_code.lyricDownload(nameN[i], id[i], self.dxk2.GetValue())
                        except:
                            wx.MessageBox(f'{nameN[i]}的歌词下载错误，请稍候再试', 'Warn')
                            warn_Tip += f'{nameN[i]}的歌词下载错误\n'
                    except:
                        wx.MessageBox(f'{nameN[i]}的歌曲下载错误，请稍候再试', 'Warn')
                        warn_Tip += f'{nameN[i]}的歌曲下载错误\n'
                else:
                    wx.MessageBox(f'下载完成\n{warn_Tip}', 'Tip')
                    self.Destroy()


    class myApp(wx.App):
        def OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True


    app = myApp()
    app.MainLoop()
idMaker()
nameN = []
for i in id:
    nameN.append(MusicTool_code.idToname(i))

selectAndDown()