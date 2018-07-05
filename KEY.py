#
# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
import time
import os
import string
import configparser
from ctypes import *
version = '1002_wyfx'
copyChannel=[
    '3102',
    '3103']
gateCount=1
cellCount=1

APP=[
    "DbCacheApp.exe",
    "MailApp.exe",
    #"LogDbApp.exe",
    "CellMgrApp.exe",
    "CellApp.exe",
    "InterApp.exe",
    "GateMgrApp.exe",
    "GateApp.exe",
    "CopyApp.exe",
    #"SnapshotApp.exe",
    "LoginApp.exe"
    ]
def _MyCallback( hwnd, extra ):  
  windows = extra  
  temp=[] 
  temp.append(win32gui.GetWindowText(hwnd))
  if win32gui.GetClassName(hwnd) == "ConsoleWindowClass":
      windows[hwnd] = temp

def normal_closs_app():
  windows = {}
  win32gui.EnumWindows(_MyCallback,windows)
  for item in windows :
      for app in APP:
          if windows[item][0].find(app) > 0 :
              win32gui.ShowWindow(item,1)
              win32gui.SetForegroundWindow (item)
              win32api.keybd_event(0x0D,0,0,0)
              win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
              time.sleep(1)

def start_one_app( path, appname,param):
    win32api.ShellExecute(0,        #父窗口
                          'open',   #操作类型，open，print
                          path + appname,#可执行文件
                          param,       #参数
                          path,     #执行路径
                          1)        #是否显示

def start_all_app( path ):
    for app in APP:
        if app.find('Copy') >= 0 :
            for channel in copyChannel:
                start_app( path, app,'--copy-channel='+channel)
        elif app.find('Cell') >= 0 :
            i=0
            while i<=cellCount:
                start_app( path, app,'')
                ++i
        elif app.find('Gate') >=0 :
            i=0
            while i<=gateCount:
                start_app( path, app,'')
                ++i
        else:
            start_app( path, app,'')

def getconfig():
  cf=configparser.ConfigParser()
  cf.read("config.ini")
  secs=cf.sections()
  print(secs)

  appsection=cf.options('app')
  apps=[]
  for a in appsection:
    apps.append(cf.get('app',a))
  print(apps)

  channels=cf.options('channel')
  items=[]
  for c in channels:
    items.append(cf.get('channel',c))
  print(items)
  
if __name__ == "__main__":
    path='D:\\'+version+'\\Src\\Public\\runnable\\runnableExe\\'
    #start_all_app( path )
    #normal_closs_app()
    getconfig()
