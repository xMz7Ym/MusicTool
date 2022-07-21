# -*- coding:utf-8 -*-
import wx.adv
import wx
import MusicTool_code

L = []
def playlistDownload():
    class downloadURL(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='歌曲下载', size=(502, 230), name='SingeDown', style=541072896)
            icon = wx.Icon(r'.\data\musictool_icon.png')
            self.SetIcon(icon)
            self.qdck = wx.Panel(self)
            self.Centre()
            self.bq2 = wx.StaticText(self.qdck, size=(312, 40), pos=(93, 29),
                                     label='请在下方输入您想要下载歌单的网址或者是歌单ID~~~\n按下Enter（回车）键即可开始下载', name='staticText',
                                     style=2321)
            self.cjljk1 = wx.adv.HyperlinkCtrl(self.qdck, size=(60, 22), pos=(415, 161), name='hyperlink',
                                               label='网易云官网', url='https://music.163.com/', style=1)
            self.bjk2 = wx.TextCtrl(self.qdck, size=(364, 22), pos=(77, 72), value='', name='text', style=4096)
            self.an2 = wx.Button(self.qdck, size=(80, 32), pos=(211, 134), label='确认输入', name='button')
            self.an2.Bind(wx.EVT_BUTTON, self.an2_anbdj)

        def an2_anbdj(self, event):
            try:
                a = int(self.bjk2.GetValue())
                L.append(a)
                self.Destroy()
            except:
                try:
                    L.append(MusicTool_code.playlistURL(self.bjk2.GetValue()))
                    self.Destroy()

                except:
                    wx.MessageBox('请输入正确的网址或者歌单id','Warn')







    class URL(wx.App):
        def OnInit(self):
            self.frame = downloadURL()
            self.frame.Show(True)
            return True

    app = URL()
    app.MainLoop()


def selectAndDownload():
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='下载', size=(754, 489),name='frame',style=541072448)
            icon = wx.Icon(r'.\data\musictool_icon.png')
            self.SetIcon(icon)
            self.selectAnddownload = wx.Panel(self)
            self.Centre()
            self.xzxz = wx.CheckListBox(self.selectAnddownload,size=(270, 303),pos=(50, 30),name='listBox',choices=name,style=1073741824)
            self.an2 = wx.Button(self.selectAnddownload,size=(100, 50),pos=(60, 351),label='全选',name='button')
            self.an2.Bind(wx.EVT_BUTTON,self.an2_anbdj)
            self.an3 = wx.Button(self.selectAnddownload,size=(100, 50),pos=(203, 353),label='全不选',name='button')
            self.an3.Bind(wx.EVT_BUTTON,self.an3_anbdj)
            self.bq1 = wx.StaticText(self.selectAnddownload,size=(303, 164),pos=(376, 72),label=f'从该歌单中共找到：{len(name)}首歌曲\n\n请在左侧复选框中选择您要下载的歌曲(纯音乐无歌词)\n\n因为网易云Web端限制，只能显示并下载前10首\n\n如果有想下载的歌比较多的情况\n\n建议使用 歌曲下载 模式 或者多开歌单多次下载',name='staticText',style=2321)
            self.dxk1 = wx.CheckBox(self.selectAnddownload,size=(80, 24),pos=(439, 300),name='check',label='歌曲下载',style=16384)
            self.dxk1.SetValue(True)
            self.dxk2 = wx.CheckBox(self.selectAnddownload,size=(80, 24),pos=(570, 300),name='check',label='歌词下载',style=16384)
            self.dxk2.SetValue(True)
            self.ydan1 = wx.adv.CommandLinkButton(self.selectAnddownload,size=(158, 62),pos=(575, 384),name='button',mainLabel='开始下载',note='点击即可下载')
            self.ydan1.Bind(wx.EVT_BUTTON,self.ydan1_anbdj)
            self.xzxz.SetChecked(range(0, self.xzxz.GetCount()))


        def an2_anbdj(self,event):

            self.xzxz.SetChecked(range(0,self.xzxz.GetCount()))


        def an3_anbdj(self,event):

            self.xzxz.SetChecked([])



        def ydan1_anbdj(self,event):

            song_id = self.xzxz.GetCheckedItems()

            warn_Tip = ''
            if len(song_id) == 0:
                wx.MessageBox(f'请至少选择一首歌进行下载', 'Warn')
            else:
                wx.MessageBox(f'已经开始下载进程\n共计将要下载{len(song_id)}首歌', 'Tip')
                for i in song_id:
                    try:
                        MusicTool_code.musicDownload(name[i],id[i],self.dxk1.GetValue())
                        try:
                            MusicTool_code.lyricDownload(name[i], id[i], self.dxk2.GetValue())
                        except:
                            wx.MessageBox(f'{name[i]}的歌词下载错误，请稍候再试', 'Warn')
                            warn_Tip += f'{name[i]}的歌词下载错误\n'
                    except:
                        wx.MessageBox(f'{name[i]}的歌曲下载错误，请稍候再试', 'Warn')
                        warn_Tip += f'{name[i]}的歌曲下载错误\n'
                else:
                    wx.MessageBox(f'下载完成\n{warn_Tip}', 'Tip')
                    self.Destroy()

    class myApp(wx.App):
        def  OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True
    app = myApp()
    app.MainLoop()


playlistDownload()
id,name = MusicTool_code.palylistInfo(L[0])
selectAndDownload()