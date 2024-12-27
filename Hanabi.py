import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import random
import time
import os
import sys
import copy
import json
from tkinter import ttk
import numpy as np
from collections import defaultdict
from itertools import permutations
from itertools import combinations

class Menubar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='top',fill='x')

class Background(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')

class Settings(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        

class StartButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=2,column=1)
        self.Start = tk.Button(self)
        self.Start["text"] = "开始任务"
        self.Start["command"] = self.say_hi
        self.Start.pack()
        

        
    def say_hi(self):
        print(self.Check_Start)
        print(type(self.Check_Start))

class MissionList(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1,column=1)
        self.Frame_StartGame = tk.Frame(self, bg='white')
        self.Check_StartGame = tk.IntVar()
        self.Check_StartGame_button = tk.Checkbutton(self.Frame_StartGame, text = "启动游戏", variable = self.Check_StartGame, onvalue = 1, offvalue = 0, 
                                                 height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.StartGame_Setting_button = tk.Button(self.Frame_StartGame, text = "设置", command = None)
        self.Frame_MissionCenter = tk.Frame(self, bg='white')
        self.Check_MissionCenter = tk.IntVar()
        self.Check_MissionCenter_button = tk.Checkbutton(self.Frame_MissionCenter, text = "任务集会所", variable = self.Check_MissionCenter, onvalue = 1, offvalue = 0,
                                                         height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.MissionCenter_Setting_button = tk.Button(self.Frame_MissionCenter, text = "设置", command = None)
        self.Frame_Raid = tk.Frame(self, bg='white')
        self.Check_Raid = tk.IntVar()
        self.Check_Raid_button = tk.Checkbutton(self.Frame_Raid, text = "团队战役", variable = self.Check_Raid, onvalue = 1, offvalue = 0,
                                                height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.Raid_Setting_button = tk.Button(self.Frame_Raid, text = "设置", command = None)
        self.Frame_PointsRace = tk.Frame(self, bg='white')
        self.Check_PointsRace = tk.IntVar()
        self.Check_PointsRace_button = tk.Checkbutton(self.Frame_PointsRace, text = "积分赛", variable = self.Check_PointsRace, onvalue = 1, offvalue = 0,
                                                      height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.PointsRace_Setting_button = tk.Button(self.Frame_PointsRace, text = "设置", command = None)
        self.Frame_SurvivalChallenges = tk.Frame(self, bg='white')
        self.Check_SurvivalChallenges = tk.IntVar()
        self.Check_SurvivalChallenges_button = tk.Checkbutton(self.Frame_SurvivalChallenges, text = "生存挑战", variable = self.Check_SurvivalChallenges, onvalue = 1, offvalue = 0,
                                                              height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.SurvivalChallenges_Setting_button = tk.Button(self.Frame_SurvivalChallenges, text = "设置", command = None)
        self.Frame_OrganizePrayers = tk.Frame(self, bg='white')
        self.Check_OrganizePrayers = tk.IntVar()
        self.Check_OrganizePrayers_button = tk.Checkbutton(self.Frame_OrganizePrayers, text = "组织祈祷", variable = self.Check_OrganizePrayers, onvalue = 1, offvalue = 0,
                                                           height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.OrganizePrayers_Setting_button = tk.Button(self.Frame_OrganizePrayers, text = "设置", command = None)
        self.Frame_FunShop = tk.Frame(self, bg='white')
        self.Check_FunShop = tk.IntVar()
        self.Check_FunShop_button = tk.Checkbutton(self.Frame_FunShop, text = "乐园商店", variable = self.Check_FunShop, onvalue = 1, offvalue = 0,
                                                   height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.FunShop_Setting_button = tk.Button(self.Frame_FunShop, text = "设置", command = None)
        self.Frame_EmailReceive = tk.Frame(self, bg='white')
        self.Check_EmailReceive = tk.IntVar()
        self.Check_EmailReceive_button = tk.Checkbutton(self.Frame_EmailReceive, text = "邮件领取", variable = self.Check_EmailReceive, onvalue = 1, offvalue = 0,
                                                        height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.EmailReceive_Setting_button = tk.Button(self.Frame_EmailReceive, text = "设置", command = None)
        self.Frame_Fortune = tk.Frame(self, bg='white')
        self.Check_Fortune = tk.IntVar()
        self.Check_Fortune_button = tk.Checkbutton(self.Frame_Fortune, text = "金币祈福", variable = self.Check_Fortune, onvalue = 1, offvalue = 0,
                                                   height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.Fortune_Setting_button = tk.Button(self.Frame_Fortune, text = "设置", command = None)
        self.Frame_Instance = tk.Frame(self, bg='white')
        self.Check_Instance = tk.IntVar()
        self.Check_Instance_button = tk.Checkbutton(self.Frame_Instance, text = "副本", variable = self.Check_Instance, onvalue = 1, offvalue = 0,
                                                    height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.Instance_Setting_button = tk.Button(self.Frame_Instance, text = "设置", command = None)
        self.Frame_Share = tk.Frame(self, bg='white')
        self.Check_Share = tk.IntVar()
        self.Check_Share_button = tk.Checkbutton(self.Frame_Share, text = "分享", variable = self.Check_Share, onvalue = 1, offvalue = 0,
                                                 height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.Share_Setting_button = tk.Button(self.Frame_Share, text = "设置", command = None)
        self.Frame_FengRaoZhiJian = tk.Frame(self, bg='white')
        self.Check_FengRaoZhiJian = tk.IntVar()
        self.Check_FengRaoZhiJian_button = tk.Checkbutton(self.Frame_FengRaoZhiJian, text = "风绕之间", variable = self.Check_FengRaoZhiJian, onvalue = 1, offvalue = 0,
                                                         height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.FengRaoZhiJian_Setting_button = tk.Button(self.Frame_FengRaoZhiJian, text = "设置", command = None)
        self.Frame_MissionRecieve = tk.Frame(self, bg='white')
        self.Check_MissionRecieve = tk.IntVar()
        self.Check_MissionRecieve_button = tk.Checkbutton(self.Frame_MissionRecieve, text = "任务接收", variable = self.Check_MissionRecieve, onvalue = 1, offvalue = 0,
                                                         height = 1, width = 15 ,bg='#FFFFFF',bd = 0,activebackground='#F3F3F3')
        self.MissionRecieve_Setting_button = tk.Button(self.Frame_MissionRecieve, text = "设置", command = None)
        
        
        
        
        

        

        self.Frame_StartGame.grid(row=1,column=1)
        self.Check_StartGame_button.grid(row=1,column=1)
        self.StartGame_Setting_button.grid(row=1,column=2)
        self.Frame_MissionCenter.grid(row=2,column=1)
        self.Check_MissionCenter_button.grid(row=1,column=1)
        self.MissionCenter_Setting_button.grid(row=1,column=2)
        self.Frame_Raid.grid(row=3,column=1)
        self.Check_Raid_button.grid(row=1,column=1)
        self.Raid_Setting_button.grid(row=1,column=2)
        self.Frame_PointsRace.grid(row=4,column=1)
        self.Check_PointsRace_button.grid(row=1,column=1)
        self.PointsRace_Setting_button.grid(row=1,column=2)
        self.Frame_SurvivalChallenges.grid(row=5,column=1)
        self.Check_SurvivalChallenges_button.grid(row=1,column=1)
        self.SurvivalChallenges_Setting_button.grid(row=1,column=2)
        self.Frame_OrganizePrayers.grid(row=6,column=1)
        self.Check_OrganizePrayers_button.grid(row=1,column=1)
        self.OrganizePrayers_Setting_button.grid(row=1,column=2)
        self.Frame_FunShop.grid(row=7,column=1)
        self.Check_FunShop_button.grid(row=1,column=1)
        self.FunShop_Setting_button.grid(row=1,column=2)
        self.Frame_EmailReceive.grid(row=8,column=1)
        self.Check_EmailReceive_button.grid(row=1,column=1)
        self.EmailReceive_Setting_button.grid(row=1,column=2)
        self.Frame_Fortune.grid(row=9,column=1)
        self.Check_Fortune_button.grid(row=1,column=1)
        self.Fortune_Setting_button.grid(row=1,column=2)
        self.Frame_Instance.grid(row=10,column=1)
        self.Check_Instance_button.grid(row=1,column=1)
        self.Instance_Setting_button.grid(row=1,column=2)
        self.Frame_Share.grid(row=11,column=1)
        self.Check_Share_button.grid(row=1,column=1)
        self.Share_Setting_button.grid(row=1,column=2)
        self.Frame_FengRaoZhiJian.grid(row=12,column=1)
        self.Check_FengRaoZhiJian_button.grid(row=1,column=1)
        self.FengRaoZhiJian_Setting_button.grid(row=1,column=2)
        self.Frame_MissionRecieve.grid(row=13,column=1)
        self.Check_MissionRecieve_button.grid(row=1,column=1)
        self.MissionRecieve_Setting_button.grid(row=1,column=2)
        
        
        

class Mission(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='top')

class Content(tk.Frame):
    
    
    def __init__(self, master=None):
        
        super().__init__(master)
        self.master = master
        
        self.pack(side='left',fill='both')
        
        


        
        
        



Hanabi = tk.Tk()
Hanabi.geometry('800x600+200+100')
content = Content(master=Hanabi)
mission = Mission(master=content)
missionlist = MissionList(master=mission)
startbutton = StartButton(master=mission)
settings = Settings(master=content)
background = Background(master=content)
taskbar = Menubar(master=Hanabi)
Hanabi.title('Hanabi')
content.mainloop()