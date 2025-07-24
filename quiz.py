import tkinter as tk
import tkinter.ttk as ttk
import glob
import g
import pygame.mixer as pgm
from time import sleep
import gc
from game import Game

class QuizApp:
    def __init__(self):
        gc.collect()
        pgm.init()
        
        self.bgm = pgm.Sound('maou_game_jingle05.wav')
        self.bgm.set_volume(0.2)
        self.bgm.play(-1)
        
        self.se = pgm.Sound('maou_se_system49.wav')
        self.se.set_volume(0.3)
        
        self.bgm2 = pgm.Sound('maou_bgm_8bit10.wav')
        self.bgm2.set_volume(0.2)
        
        self.se2 = pgm.Sound('maou_se_8bit15.wav')
        self.se2.set_volume(0.3)
        
        self.bgm3 = pgm.Sound('maou_game_jingle09.wav')
        self.bgm3.set_volume(0.2)
        
        self.se1_ = pgm.Sound('クイズ正解1.wav')
        self.se2_ = pgm.Sound('クイズ不正解1.wav')
        
        

        g.val1=0
        self.L=glob.glob(".\quizedata\*.txt")
        self.qlist=[None]
        for lists in self.L:
            lists=lists.removeprefix('.\\quizedata\\')
            lists=lists.removesuffix('.txt')
            self.qlist=self.qlist+[lists]

        del self.qlist[0]

        self.setup_ui()

    def setup_ui(self):
        self.rootP=tk.Tk()
        self.rootP.geometry("1180x750+100+50")
        self.rootP.configure(bg="black")
        self.rootP.title('あそぶ')
        self.setumei=tk.Label(self.rootP,text='スライムが　あらわれた！',font=("HGP創英角ポップ体","50","bold"),bg='black',fg='red')
        self.setumei2=tk.Label(self.rootP,text='クイズに　せいかいすると　スライムをたおせるのじゃ!',font=("HGP創英角ポップ体","30","bold"),bg='black',fg='white')
        self.setumei.grid(row=0,column=0,columnspan=2)
        self.setumei2.grid(row=1,column=0,columnspan=2)
        self.s=tk.PhotoImage(file='s_1.png',master=self.rootP)
        self.s=self.s.subsample(4)
        self.s_L=tk.Label(self.rootP,image=self.s,relief='solid')
        self.s_L.grid(row=0,column=2,rowspan=2)

        self.qlists=tk.StringVar(value=self.qlist)
        self.ql_m=tk.Listbox(self.rootP,font=("HGP創英角ポップ体","30","bold"),listvariable=self.qlists,height=7)
        self.ql_m.grid(row=2,column=1,pady=30,columnspan=2)
        self.scrollbar =ttk.Scrollbar(self.rootP,orient='vertical',command=self.ql_m.yview)
        self.ql_m['yscrollcommand']=self.scrollbar.set
        self.scrollbar.grid(row=2,column=3,sticky=('N','S'),pady=30)
        self.ql_l=tk.Label(self.rootP,text='みぎから\nあそびたいクイズを\nえらぶのじゃ',font=("HGP創英角ポップ体","50","bold"),relief="solid",fg='white',bg='black')
        self.ql_l.grid(row=2,column=0,pady=40)
	
	
        self.button = tk.Button(self.rootP, text="クイズをはじめる！",font=("HGP創英角ポップ体","50","bold"),fg='red',bg='white', command=self.get_entry_text)
        self.button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
	
	
	
        self.rootP.mainloop()

    def get_entry_text(self):
        self.bgm.stop()
        self.se.play(0)
        sleep(1)
        
        ql = self.ql_m.curselection()
        with open(f'quizedata/{self.ql_m.get(ql)}.txt', 'r', encoding='utf-8') as f:
            qandf = f.readlines()
        
        self.rootP.destroy()
        self.bgm2.play(-1)
        
        quize = [qandf[i * 2] for i in range(5)]
        fact = [qandf[i * 2 + 1] for i in range(5)]
        
        g.val4 = 0
        Game(quize, fact)

