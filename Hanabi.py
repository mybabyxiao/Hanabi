import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import cv2
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



def adb_screenshot(device, output_path: str = "./temp/screenshot/screenshot.png"):
    """
    截取当前设备屏幕截图并保存到本地。
    :param device: 连接的 ADB 设备实例。
    :param output_path: 截图保存路径。
    """
    try:
        # 截图命令
        remote_path = "/sdcard/screenshot.png"
        device.shell(f"screencap -p {remote_path}")

        # 拉取截图到本地
        with open(output_path, "wb") as f:
            for data in device.pull(remote_path):
                f.write(data)
        print(f"截图成功，保存到本地：{output_path}")

        # 删除设备中的临时截图
        device.shell(f"rm {remote_path}")
    except Exception as e:
        print(f"截图失败：{e}")


class StartGame():
    pass


class Tabbar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0, y=0)

        self.tab1 = tk.Button(self, width=50)
        self.tab1["text"] = "任务"
        self.tab1["command"] = None
        self.tab1.grid(row=0, column=0)
        self.tab2 = tk.Button(self, width=50)
        self.tab2["text"] = "设置"
        self.tab2["command"] = None
        self.tab2.grid(row=0, column=1)


class BackgroundOutput(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=3)


class Settings(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=2)


class StartButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=2, column=1)
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
        self.grid(row=1, column=1)

        # 按钮定义
        self.Frame_StartGame = tk.Frame(self, bg='white')
        self.Check_StartGame = tk.IntVar()
        self.Check_StartGame_button = tk.Checkbutton(self.Frame_StartGame, text="启动游戏", variable=self.Check_StartGame, onvalue=1, offvalue=0,
                                                     height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.StartGame_Setting_button = tk.Button(
            self.Frame_StartGame, text="设置", command=None)
        self.Frame_MissionCenter = tk.Frame(self, bg='white')
        self.Check_MissionCenter = tk.IntVar()
        self.Check_MissionCenter_button = tk.Checkbutton(self.Frame_MissionCenter, text="任务集会所", variable=self.Check_MissionCenter, onvalue=1, offvalue=0,
                                                         height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.MissionCenter_Setting_button = tk.Button(
            self.Frame_MissionCenter, text="设置", command=None)
        self.Frame_Raid = tk.Frame(self, bg='white')
        self.Check_Raid = tk.IntVar()
        self.Check_Raid_button = tk.Checkbutton(self.Frame_Raid, text="小队突袭", variable=self.Check_Raid, onvalue=1, offvalue=0,
                                                height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.Raid_Setting_button = tk.Button(
            self.Frame_Raid, text="设置", command=None)
        self.Frame_PointsRace = tk.Frame(self, bg='white')
        self.Check_PointsRace = tk.IntVar()
        self.Check_PointsRace_button = tk.Checkbutton(self.Frame_PointsRace, text="积分赛", variable=self.Check_PointsRace, onvalue=1, offvalue=0,
                                                      height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.PointsRace_Setting_button = tk.Button(
            self.Frame_PointsRace, text="设置", command=None)
        self.Frame_SurvivalChallenges = tk.Frame(self, bg='white')
        self.Check_SurvivalChallenges = tk.IntVar()
        self.Check_SurvivalChallenges_button = tk.Checkbutton(self.Frame_SurvivalChallenges, text="生存挑战", variable=self.Check_SurvivalChallenges, onvalue=1, offvalue=0,
                                                              height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.SurvivalChallenges_Setting_button = tk.Button(
            self.Frame_SurvivalChallenges, text="设置", command=None)
        self.Frame_OrganizePrayers = tk.Frame(self, bg='white')
        self.Check_OrganizePrayers = tk.IntVar()
        self.Check_OrganizePrayers_button = tk.Checkbutton(self.Frame_OrganizePrayers, text="组织祈福", variable=self.Check_OrganizePrayers, onvalue=1, offvalue=0,
                                                           height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.OrganizePrayers_Setting_button = tk.Button(
            self.Frame_OrganizePrayers, text="设置", command=None)
        self.Frame_FunShop = tk.Frame(self, bg='white')
        self.Check_FunShop = tk.IntVar()
        self.Check_FunShop_button = tk.Checkbutton(self.Frame_FunShop, text="玩法商店", variable=self.Check_FunShop, onvalue=1, offvalue=0,
                                                   height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.FunShop_Setting_button = tk.Button(
            self.Frame_FunShop, text="设置", command=None)
        self.Frame_EmailReceive = tk.Frame(self, bg='white')
        self.Check_EmailReceive = tk.IntVar()
        self.Check_EmailReceive_button = tk.Checkbutton(self.Frame_EmailReceive, text="邮件领取", variable=self.Check_EmailReceive, onvalue=1, offvalue=0,
                                                        height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.EmailReceive_Setting_button = tk.Button(
            self.Frame_EmailReceive, text="设置", command=None)
        self.Frame_Fortune = tk.Frame(self, bg='white')
        self.Check_Fortune = tk.IntVar()
        self.Check_Fortune_button = tk.Checkbutton(self.Frame_Fortune, text="金币祈福", variable=self.Check_Fortune, onvalue=1, offvalue=0,
                                                   height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.Fortune_Setting_button = tk.Button(
            self.Frame_Fortune, text="设置", command=None)
        self.Frame_Instance = tk.Frame(self, bg='white')
        self.Check_Instance = tk.IntVar()
        self.Check_Instance_button = tk.Checkbutton(self.Frame_Instance, text="副本", variable=self.Check_Instance, onvalue=1, offvalue=0,
                                                    height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.Instance_Setting_button = tk.Button(
            self.Frame_Instance, text="设置", command=None)
        self.Frame_Share = tk.Frame(self, bg='white')
        self.Check_Share = tk.IntVar()
        self.Check_Share_button = tk.Checkbutton(self.Frame_Share, text="每日分享", variable=self.Check_Share, onvalue=1, offvalue=0,
                                                 height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.Share_Setting_button = tk.Button(
            self.Frame_Share, text="设置", command=None)
        self.Frame_FengRaoZhiJian = tk.Frame(self, bg='white')
        self.Check_FengRaoZhiJian = tk.IntVar()
        self.Check_FengRaoZhiJian_button = tk.Checkbutton(self.Frame_FengRaoZhiJian, text="丰饶之间", variable=self.Check_FengRaoZhiJian, onvalue=1, offvalue=0,
                                                          height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.FengRaoZhiJian_Setting_button = tk.Button(
            self.Frame_FengRaoZhiJian, text="设置", command=None)
        self.Frame_AutoFight = tk.Frame(self, bg='white')
        self.Check_AutoFight = tk.IntVar()
        self.Check_AutoFight_button = tk.Checkbutton(self.Frame_AutoFight, text="自动战斗", variable=self.Check_AutoFight, onvalue=1, offvalue=0,
                                                     height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.AutoFight_Setting_button = tk.Button(
            self.Frame_AutoFight, text="设置", command=None)
        self.Frame_MissionRecieve = tk.Frame(self, bg='white')
        self.Check_MissionRecieve = tk.IntVar()
        self.Check_MissionRecieve_button = tk.Checkbutton(self.Frame_MissionRecieve, text="奖励领取", variable=self.Check_MissionRecieve, onvalue=1, offvalue=0,
                                                          height=1, width=15, bg='#FFFFFF', bd=0, activebackground='#F3F3F3')
        self.MissionRecieve_Setting_button = tk.Button(
            self.Frame_MissionRecieve, text="设置", command=None)

        # 按钮布局
        self.Frame_StartGame.pack(fill="x")
        self.Check_StartGame_button.pack(side="left", fill='x')
        self.StartGame_Setting_button.pack(side="right")
        self.Frame_MissionCenter.pack(fill="x")
        self.Check_MissionCenter_button.pack(side="left", fill='x')
        self.MissionCenter_Setting_button.pack(side="right")
        self.Frame_Raid.pack(fill="x")
        self.Check_Raid_button.pack(side="left", fill='x')
        self.Raid_Setting_button.pack(side="right")
        self.Frame_PointsRace.pack(fill="x")
        self.Check_PointsRace_button.pack(side="left", fill='x')
        self.PointsRace_Setting_button.pack(side="right")
        self.Frame_SurvivalChallenges.pack(fill="x")
        self.Check_SurvivalChallenges_button.pack(side="left", fill='x')
        self.SurvivalChallenges_Setting_button.pack(side="right")
        self.Frame_OrganizePrayers.pack(fill="x")
        self.Check_OrganizePrayers_button.pack(side="left", fill='x')
        self.OrganizePrayers_Setting_button.pack(side="right")
        self.Frame_FunShop.pack(fill="x")
        self.Check_FunShop_button.pack(side="left", fill='x')
        self.FunShop_Setting_button.pack(side="right")
        self.Frame_EmailReceive.pack(fill="x")
        self.Check_EmailReceive_button.pack(side="left", fill='x')
        self.EmailReceive_Setting_button.pack(side="right")
        self.Frame_Fortune.pack(fill="x")
        self.Check_Fortune_button.pack(side="left", fill='x')
        self.Fortune_Setting_button.pack(side="right")
        self.Frame_Instance.pack(fill="x")
        self.Check_Instance_button.pack(side="left", fill='x')
        self.Instance_Setting_button.pack(side="right")
        self.Frame_Share.pack(fill="x")
        self.Check_Share_button.pack(side="left", fill='x')
        self.Share_Setting_button.pack(side="right")
        self.Frame_FengRaoZhiJian.pack(fill="x")
        self.Check_FengRaoZhiJian_button.pack(side="left", fill='x')
        self.FengRaoZhiJian_Setting_button.pack(side="right")
        self.Frame_AutoFight.pack(fill="x")
        self.Check_AutoFight_button.pack(side="left", fill='x')
        self.AutoFight_Setting_button.pack(side="right")
        self.Frame_MissionRecieve.pack(fill="x")
        self.Check_MissionRecieve_button.pack(side="left", fill='x')
        self.MissionRecieve_Setting_button.pack(side="right")


class Mission(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=1)


class Content(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master

        self.place(x=5, y=0)


Hanabi = tk.Tk()
Hanabi.geometry('770x600')
content = Content(master=Hanabi)
mission = Mission(master=content)
missionlist = MissionList(master=mission)
startbutton = StartButton(master=mission)
settings = Settings(master=content)
background = BackgroundOutput(master=content)
taskbar = Tabbar(master=Hanabi)
Hanabi.title('Hanabi')
content.mainloop()