import tkinter as tk
import tkinter.ttk as ttk
import glob
import g
import pygame.mixer as pgm
from time import sleep
import gc

class Play:
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
        
        
    

    def get_entry_text(self):
        self.bgm.stop()
        self.se.play(0)
        sleep(1)
        
        ql = self.ql_m.curselection()
        with open(f'quizedata/{self.ql_m.get(ql)}.txt', 'r', encoding='utf-8') as f:
            qandf = f.readlines()
        
        self.rootP.destroy()
        self.bgm2.play(-1)
        
        self.quize = [qandf[i * 2] for i in range(5)]
        self.fact = [qandf[i * 2 + 1] for i in range(5)]
        
        g.val4 = 0
        
        
        self.game(self.quize,self.fact)

    def game(self,quize,fact):#pray2 この中で5回
            #kはiみたいな 
            g.val3=16
            
            
            rootPP=tk.Tk()
            rootPP.geometry("1000x750+200+100")
            rootPP.configure(bg="black")
            rootPP.grid_columnconfigure(1, weight=1)
            rootPP.grid_columnconfigure(2, weight=1)
            rootPP.grid_columnconfigure(3, weight=1)
            q_l=tk.Label(rootPP,text=quize[g.val4],font=("HGP創英角ポップ体","40","bold"),wraplength=1000,width=1000,fg='white',bg='black',height=2,pady=30)
            q_l.grid(row=0,column=0,columnspan=5)
            def co():#g.val3
                
                if g.val3>0:
                    g.val3=g.val3-1
                    time.config(text=g.val3)
                    g.val2=rootPP.after(1000,lambda:co())
                
                elif g.val3==0:
                    button.invoke()
                
                if g.val3==14:
                    button['state']='normal'
                
            def anser(quize,fact):
                rootPP.after_cancel(g.val2)
                button['state']='disabled'
                self.se.play(0)
                
                a.set(yorn.get())
                if int(a.get())==0:
                    ai='はい\n'
                elif int(a.get())==1:
                    ai='いいえ\n'
                    
                
                
                def ne(TEXT,c):
                    time.config(text=TEXT)
                    if g.val4<4:
                        no.config(image=n)
                        yes.config(image=y)
                        g.val3=16
                        g.val4=g.val4+1
                                                
                        
                        
                        if c==0:
                            def setime():
                                q_l.config(text=quize[g.val4])

                                self.se2.play(0)
                                time.config(text='スライムがあらわれたのじゃ！')
                            rootPP.after(1000,lambda:setime())
                            rootPP.after(1200,lambda:s.config(image=s1))
                            rootPP.after(1400,lambda:s.config(image=s0))
                            rootPP.after(1600,lambda:s.config(image=s1))
                            rootPP.after(1800,lambda:s.config(image=s0))
                            rootPP.after(2000,lambda:s.config(image=s1))
                            rootPP.after(2000,lambda: co())
                        else:
                            q_l.config(text=quize[g.val4])
                            rootPP.after(1000,lambda: co())
                    else:
                        rootPP.destroy()
                if ai==fact[g.val4]:
                    
                    self.se1_.play(0)
                    time.config(text='せいかいなのじゃ！')
                    g.val1=g.val1+1
                    #1000-1500やられ
                    rootPP.after(1000,lambda:s.config(image=s2))
                    rootPP.after(1100,lambda:s.config(image=s1))
                    rootPP.after(1200,lambda:s.config(image=s2))
                    rootPP.after(1300,lambda:s.config(image=s1))
                    rootPP.after(1400,lambda:s.config(image=s2))
                    rootPP.after(1500,lambda:s.config(image=s0))
                    TEXT='スライムをたおしたのじゃ！！'
                    rootPP.after(2000,lambda:ne(TEXT,0))
                else:
                    
                    self.se2_.play(0)
                    time.config(text='ありゃ、ちがうようじゃ')
                    TEXT='スライムがまだいるのじゃ'
                    rootPP.after(2000,lambda:ne(TEXT,1))
            #def anser(f,id_,quize(sorezoreno))
                #ボタン無効化
                #正誤判定　kekka resalut
                #g.val3=resalt  (yn_lのてｘｔ
                #3sec g.val3=15
                
                #ボタン有効か
            def see(nam):
                self.se.play(0)
                if nam==0:
                    yes.config(image=y2)
                    no.config(image=n)
                elif nam==1:
                    no.config(image=n2)
                    yes.config(image=y)
            #suraimusuraimu
            s0=tk.PhotoImage(file='s_0.png',master=rootPP)#なし
            s0=s0.subsample(3)
            s1=tk.PhotoImage(file='s_1.png',master=rootPP)#通常
            s1=s1.subsample(3)
            s2=tk.PhotoImage(file='s_2.png',master=rootPP)#赤
            s2=s2.subsample(3)
            
            ###
            
            time = tk.Label(rootPP,text='スライムがあらわれたのじゃ！',font=("HGP創英角ポップ体","50","bold"),fg='red',bg='black')
            time.grid(row=1, column=0,columnspan=5)
            
            s=tk.Label(rootPP,image=s0,relief='solid')
            s.grid(row=2,column=2)
            
            
            y=tk.PhotoImage(file='mark_yes_no_hai.png',master=rootPP)
            y=y.subsample(4)
            n=tk.PhotoImage(file='mark_yes_no_iie.png',master=rootPP)
            n=n.subsample(4)
            y2=tk.PhotoImage(file='mark_yes_no_hai2.png',master=rootPP)
            y2=y2.subsample(4)
            n2=tk.PhotoImage(file='mark_yes_no_iie2.png',master=rootPP)
            n2=n2.subsample(4)
            
            a=tk.IntVar()
            yorn=tk.IntVar()
            yes=tk.Radiobutton(rootPP,value=0,variable=yorn,image=y,indicatoron="False",command=lambda:see(0))
            yes.grid(row=3,column=1)
            
            no=tk.Radiobutton(rootPP,value=1,variable=yorn,image=n,indicatoron="False",command=lambda:see(1))
            no.grid(row=3,column=3)
            button=tk.Button(rootPP,text='けってい！！',font=("HGP創英角ポップ体","25","bold"),fg='red',relief="solid", command=lambda: anser(quize,fact))
            button['state']='disabled'
            button.grid(row=4, column=1,columnspan=3)
            
            rootPP.after(200,lambda:s.config(image=s1))
            rootPP.after(400,lambda:s.config(image=s0))
            rootPP.after(600,lambda:s.config(image=s1))
            rootPP.after(800,lambda:s.config(image=s0))
            rootPP.after(1000,lambda:s.config(image=s1))
            rootPP.after(1000,lambda:co())
            rootPP.mainloop()
            ###