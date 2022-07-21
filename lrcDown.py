# -*- coding:utf-8 -*-
import wx.adv
import wx
import tkinter as tk
import os
from tkinter import filedialog
import MusicTool_code
name = []
def lrc():
    class Frame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, title='下载', size=(754, 489),name='frame',style=541072448)
            icon = wx.Icon(r'.\data\musictool_icon.png')
            self.SetIcon(icon)
            self.selectAnddownload = wx.Panel(self)
            self.Centre()
            self.xzxz = wx.CheckListBox(self.selectAnddownload,size=(270, 303),pos=(50, 29),name='listBox',choices=name,style=1073741824)
            self.an2 = wx.Button(self.selectAnddownload,size=(100, 50),pos=(60, 351),label='全选',name='button')
            self.an2.Bind(wx.EVT_BUTTON,self.an2_anbdj)
            self.an3 = wx.Button(self.selectAnddownload,size=(100, 50),pos=(203, 353),label='全不选',name='button')
            self.an3.Bind(wx.EVT_BUTTON,self.an3_anbdj)
            self.bq1 = wx.StaticText(self.selectAnddownload,size=(303, 164),pos=(376, 70),label=f'从您选择的文件夹中共找到了共计：{len(name)}首歌曲\n\n请选择自己想补全的歌曲~\n\n点击下方按钮开始补全',name='staticText',style=2321)
            self.ydan1 = wx.adv.CommandLinkButton(self.selectAnddownload,size=(158, 62),pos=(575, 384),name='button',mainLabel='开始下载',note='点击即可下载')
            self.ydan1.Bind(wx.EVT_BUTTON,self.ydan1_anbdj)

        def an2_anbdj(self, event):

            self.xzxz.SetChecked(range(0, self.xzxz.GetCount()))


        def an3_anbdj(self, event):

            self.xzxz.SetChecked([])



        def ydan1_anbdj(self,event):


            if len(self.xzxz.GetCheckedItems()) == 0:
                wx.MessageBox(f'请至少选择一首歌进行下载', 'Warn')
            else:
                wx.MessageBox(f'已经开始下载进程\n共计将要下载{len(self.xzxz.GetCheckedItems())}首歌的歌词', 'Tip')
                t = ''
                for i in name:
                    try:
                        songid = MusicTool_code.nameToOneid(i)
                        MusicTool_code.lyricDownload(i,songid)
                    except:
                        t += i + '的歌词下载失败'

                if t == '':
                    wx.MessageBox('下载完成', 'Info')
                    self.Destroy()
                else:
                    wx.MessageBox(t, 'Warn')
                    self.Destroy()



    class myApp(wx.App):
        def  OnInit(self):
            self.frame = Frame()
            self.frame.Show(True)
            return True


    app = myApp()
    app.MainLoop()
root = tk.Tk()
root.withdraw()

f_path = filedialog.askdirectory()
Allsongs = os.listdir(f_path)
for i in Allsongs:
    if i[-4:] == '.mp3':
        name.append(i[:-4])

    else:
        pass
lrc()