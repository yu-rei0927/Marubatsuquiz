import tkinter as tk
import g
import pygame.mixer as pgm
from time import sleep
import gc

class Game:
    def __init__(self, quize, fact):
        self.quize = quize
        self.fact = fact
        
        self.init_audio()
        self.start_game()

    def init_audio(self):
        gc.collect()
        pgm.init()
        self.se = pgm.Sound('maou_se_system49.wav')
        self.se.set_volume(0.3)
        
        self.se2 = pgm.Sound('maou_se_8bit15.wav')
        self.se2.set_volume(0.3)
        
        self.se1_ = pgm.Sound('クイズ正解1.wav')
        self.se2_ = pgm.Sound('クイズ不正解1.wav')

        self.bgm2=pgm.Sound('maou_bgm_8bit10.wav')
        self.bgm2.set_volume(0.2)
        self.bgm3=pgm.Sound('maou_game_jingle09.wav')
        self.bgm3.set_volume(0.2)

    def start_game(self):
        g.val3 = 16
        g.val4 = 0
        self.bgm2.play(-1)
        self.se2.play(0)
        self.rootPP = tk.Tk()
        self.rootPP.geometry("1000x750+200+100")
        self.rootPP.configure(bg="black")
        self.rootPP.grid_columnconfigure(1, weight=1)
        self.rootPP.grid_columnconfigure(2, weight=1)
        self.rootPP.grid_columnconfigure(3, weight=1)
        
        self.q_l = tk.Label(self.rootPP, text=self.quize[g.val4], font=("HGP創英角ポップ体", "40", "bold"), wraplength=1000, width=1000, fg='white', bg='black', height=2, pady=30)
        self.q_l.grid(row=0, column=0, columnspan=5)
        
        self.time = tk.Label(self.rootPP, text='スライムがあらわれたのじゃ！', font=("HGP創英角ポップ体", "50", "bold"), fg='red', bg='black')
        self.time.grid(row=1, column=0, columnspan=5)
        
        self.s0 = tk.PhotoImage(file='s_0.png', master=self.rootPP).subsample(3)
        self.s1 = tk.PhotoImage(file='s_1.png', master=self.rootPP).subsample(3)
        self.s2 = tk.PhotoImage(file='s_2.png', master=self.rootPP).subsample(3)
        
        self.s = tk.Label(self.rootPP, image=self.s0, relief='solid')
        self.s.grid(row=2, column=2)
        
        self.y = tk.PhotoImage(file='mark_yes_no_hai.png', master=self.rootPP).subsample(4)
        self.n = tk.PhotoImage(file='mark_yes_no_iie.png', master=self.rootPP).subsample(4)
        self.y2 = tk.PhotoImage(file='mark_yes_no_hai2.png', master=self.rootPP).subsample(4)
        self.n2 = tk.PhotoImage(file='mark_yes_no_iie2.png', master=self.rootPP).subsample(4)
        
        self.a = tk.IntVar()
        self.yorn = tk.IntVar()
        
        self.yes = tk.Radiobutton(self.rootPP, value=0, variable=self.yorn, image=self.y, indicatoron="False", command=lambda: self.see(0))
        self.yes.grid(row=3, column=1)
        
        self.no = tk.Radiobutton(self.rootPP, value=1, variable=self.yorn, image=self.n, indicatoron="False", command=lambda: self.see(1))
        self.no.grid(row=3, column=3)
        
        self.button = tk.Button(self.rootPP, text='けってい！！', font=("HGP創英角ポップ体", "25", "bold"), fg='red', relief="solid", command=self.answer)
        self.button['state'] = 'disabled'
        self.button.grid(row=4, column=1, columnspan=3)
        
        self.animate_slime()
        self.start_countdown()

        self.rootPP.mainloop()

    def animate_slime(self):
        self.rootPP.after(200, lambda: self.s.config(image=self.s1))
        self.rootPP.after(400, lambda: self.s.config(image=self.s0))
        self.rootPP.after(600, lambda: self.s.config(image=self.s1))
        self.rootPP.after(800, lambda: self.s.config(image=self.s0))
        self.rootPP.after(1000, lambda: self.s.config(image=self.s1))
    
    def start_countdown(self):
        def countdown():
            if g.val3 > 0:
                g.val3 -= 1
                self.time.config(text=g.val3)
                g.val2 = self.rootPP.after(1000, countdown)
            elif g.val3 == 0:
                self.button.invoke()
            if g.val3 == 14:
                self.button['state'] = 'normal'

        countdown()
    
    def answer(self):
        self.rootPP.after_cancel(g.val2)
        self.button['state'] = 'disabled'
        self.se.play(0)
        
        self.a.set(self.yorn.get())
        ai = 'はい\n' if int(self.a.get()) == 0 else 'いいえ\n'
        
        
        
        if ai == self.fact[g.val4]:
            self.se1_.play(0)
            self.time.config(text='せいかいなのじゃ！')
            g.val1 += 1
            self.rootPP.after(1000, lambda: self.s.config(image=self.s2))
            self.rootPP.after(1100, lambda: self.s.config(image=self.s1))
            self.rootPP.after(1200, lambda: self.s.config(image=self.s2))
            self.rootPP.after(1300, lambda: self.s.config(image=self.s1))
            self.rootPP.after(1400, lambda: self.s.config(image=self.s2))
            self.rootPP.after(1500, lambda: self.s.config(image=self.s0))
            TEXT = 'スライムをたおしたのじゃ！！'
            self.rootPP.after(2000, lambda: self.next_question(TEXT, 0))
        else:
            self.se2_.play(0)
            self.time.config(text='ありゃ、ちがうようじゃ')
            TEXT = 'スライムがまだいるのじゃ'
            self.rootPP.after(2000, lambda: self.next_question(TEXT, 1))

    def next_question(self,TEXT, c):
            self.time.config(text=TEXT)
            if g.val4 < 4:
                self.no.config(image=self.n)
                self.yes.config(image=self.y)
                g.val3 = 16
                g.val4 += 1
                
                if c == 0:
                    self.rootPP.after(1000, lambda: self.q_l.config(text=self.quize[g.val4]))
                    self.rootPP.after(1000, lambda: self.se2.play(0))
                    self.rootPP.after(1000, lambda: self.time.config(text='スライムがあらわれたのじゃ！'))
                    self.rootPP.after(1200, lambda: self.s.config(image=self.s1))
                    self.rootPP.after(1400, lambda: self.s.config(image=self.s0))
                    self.rootPP.after(1600, lambda: self.s.config(image=self.s1))
                    self.rootPP.after(1800, lambda: self.s.config(image=self.s0))
                    self.rootPP.after(2000, lambda: self.s.config(image=self.s1))
                    self.rootPP.after(2000, lambda: self.start_countdown())
                else:
                    self.q_l.config(text=self.quize[g.val4])
                    self.rootPP.after(1000, lambda: self.start_countdown())
            else:
                self.rootPP.destroy()
                self.end()

    def see(self, nam):
        self.se.play(0)
        if nam == 0:
            self.yes.config(image=self.y2)
            self.no.config(image=self.n)
        elif nam == 1:
            self.no.config(image=self.n2)
            self.yes.config(image=self.y)

    def end(self):
        pgm.stop()
        self.bgm3.play(0)
        rootE=tk.Tk()
        rootE.configure(bg="black")
        rootE.title('おしまい')
        
        if g.val1==5:
            
            labela=tk.Label(rootE,text='ぜんぶのスライムを\nたおしたのじゃ！',font=("HGP創英角ポップ体","50","bold"),bg='black',fg='white')
            g.val1=0
            I=tk.PhotoImage(file='perfect.png',master=rootE)
            labela.grid(row=0,column=0)
            ILUST=tk.Label(rootE,image=I,relief='solid')
            ILUST.grid(row=1,column=0)
        else:
            
            labela=tk.Label(rootE,text='{0}たいの　スライムを\nたおしたのじゃ'.format(g.val1),font=("HGP創英角ポップ体","50","bold"),bg='black',fg='white')
            labela.grid(row=0,column=0,columnspan=g.val1)
            #ばってん
            I=tk.PhotoImage(file='s_3.png',master=rootE)
            I=I.subsample(3)
            ILUST=[None]*g.val1
            for i in range(g.val1):
                ILUST[i]=tk.Label(rootE,image=I,relief='solid')
                ILUST[i].grid(row=1,column=i)
            
        g.val1=0
        
        
        
        rootE.after(5000,lambda: rootE.destroy())
        rootE.mainloop()
        

