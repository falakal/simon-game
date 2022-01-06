def menu(self):
    # &&&&&&&&&&&&&&&&&&&&&&&
    # @@@@@@@@@@@@@@@@@@@@@@@
    global watch
    global count
    global tmp
    global gameover
    global timer_count
    global score
    global tmp_stt
    global stt
    score = 0
    timer_count = 0
    watch = True
    gameover = False
    tmp_stt = []
    stt = []
    tmp = len(stt)
    # $$$$$$$$$$$$$$$$$$$$$$$
    # @@@@@@@@@@@@@@@@@@@@@@@
    # back ground for the main menu
    if (self.change == 0):
        self.bg3 = ImageTk.PhotoImage(file="black.jpg")
        bg3 = Label(self.root, image=self.bg3).place(x=0, y=0, relwidth=1, relheight=1)
    else:
        self.bgchange = ImageTk.PhotoImage(file="img3.jpg")
        bgchange = Label(self.root, image=self.bgchange).place(x=0, y=0, relwidth=1, relheight=1)
    # simon photo in the menu
    self.simon_icon = ImageTk.PhotoImage(file="sss.jpg")
    simon_icon = Label(self.root, image=self.simon_icon, bg="gray").place(x=500, y=20, width=172, height=112)
    # buttons at the main menu
    # add the change off photo
    btn_back_ground = Button(self.root, text="change background", font=("times new roman", 15, "bold"), bg="rosybrown",
                             fg="darkred", width=15, cursor="hand2", command=self.background).place(x=50, y=33)
    btn1_menu = Button(self.root, text="New game", font=("times new roman", 15, "bold"), bg="limegreen", fg="black",
                       width=15, cursor="hand2", command=self.first).place(x=500, y=200)
    btn2_menu = Button(self.root, text="scores", font=("times new roman", 15, "bold"), bg="firebrick", fg="black", bd=0,
                       width=15, cursor="hand2", command=self.score_page).place(x=500, y=250)
    btn3_menu = Button(self.root, text="Rate Us ", font=("times new roman", 15, "bold"), bg="yellow", fg="black",
                       width=15, cursor="hand2", command=self.rate_us).place(x=500, y=300)
    btn4_menu = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="dodgerblue", fg="black",
                       width=15, cursor="hand2", command=self.exit).place(x=500, y=350)
    btn5_menu_inst = Button(self.root, text="Instructions", font=("times new roman", 15, "bold"), bg="rosybrown",
                            fg="darkred",
                            width=13, cursor="hand2", command=self.instructions).place(x=1000, y=33)


def background(self):
    if (self.change == 0):
        self.change = 1
    else:
        self.change = 0
    self.menu()


def exit(self):
    self.login()


def rate_us(self):
    self.bg_rate = ImageTk.PhotoImage(file="img3.jpg")
    bg_rate = Label(self.root, image=self.bg_rate).place(x=0, y=0, relwidth=1, relheight=1)
    frame_rate = Frame(self.root, bg="white")
    frame_rate.place(x=200, y=100, width=500, height=412)
    title = Label(frame_rate, text="RATE US", font=("times new roman", 20, "bold"), bg="white",
                  fg="red").place(x=50, y=30)
    title = Label(frame_rate, text="Enjoying The Game?", font=("times new roman", 20, "bold"), bg="white",
                  fg="pink").place(x=50, y=90)
    self.d = IntVar()

    Radiobutton(frame_rate, text="YES", variable=self.d, value=1, font=("times new roman", 15),
                bg="white").place(x=50, y=130)
    Radiobutton(frame_rate, text="NO", variable=self.d, value=2, font=("times new roman", 15),
                bg="white").place(x=50, y=170)
    btn_rate = Button(frame_rate, text="Submit", font=("times new roman", 15, "bold"), bg="pink", fg="red", width=15,
                      cursor="hand2", command=self.datarate).place(x=50, y=240)
    btn_rate_back = Button(frame_rate, text="Menu", font=("times new roman", 15, "bold"), bg="lightblue", fg="white",
                           width=10,
                           cursor="hand2", command=self.menu).place(x=50, y=340)


def datarate(self):
    wb_rate = openpyxl.load_workbook('rating.xlsx')
    ws_rate = wb_rate['Sheet1']
    if (self.d.get() != 1 and self.d.get() != 2):
        messagebox.showerror("ERROR", "All Fields Are Required", parent=self.root)
    else:
        for i, _ in enumerate(iter(bool, True), start=2):
            if (ws_rate.cell(row=i, column=1).value == self.The_User):
                self.therow = i  # the row of the user
                break
        # for some reason previous data is been deleted from the excel file after doing this
        if (self.d.get() == 1):
            ws_rate.cell(row=self.therow, column=2).value = 'YES'
            wb_rate.save('rating.xlsx')
        if (self.d.get() == 2):
            ws_rate.cell(row=self.therow, column=2).value = 'NO'
            wb_rate.save('rating.xlsx')
        messagebox.showinfo("Thank you", "We appreciate your participation in rating the game", parent=self.root)
    wb_rate.save('rating.xlsx')
    wb_rate.close()


if gameover == False:

    def ChangeColor(self, i=1):
        global stt
        global watch
        global count
        global timer_count
        count = len(stt)
        '''find out the user type'''
        wb = openpyxl.load_workbook('good.xlsx')
        ws = wb['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=2):
            if (ws.cell(row=i, column=1).value == self.The_User):
                self.therow = i
                break
        # if it is user 2 then add a button for improving
        if (ws.cell(row=self.therow, column=3).value == "User with vision problem"):  # user2
            for i in stt:
                time.sleep(0.2)

                if i == 1:
                    self.root.after((timer_count + 300), lambda: self.Green.config(bg='#7FFF00'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m15.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Green.config(bg='#458B00'))

                elif i == 2:
                    self.root.after((timer_count + 300), lambda: self.Red.config(bg='#FF0000'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m25.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Red.config(bg='#8B1A1A'))


                elif i == 3:
                    self.root.after((timer_count + 300), lambda: self.Yellow.config(bg='#FFFF00'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m35.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Yellow.config(bg='#8B8B00'))
                elif i == 4:
                    self.root.after((timer_count + 300), lambda: self.Blue.config(bg='#00F5FF'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m45.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Blue.config(bg='#36648B'))

                timer_count += 220
        else:
            for i in stt:
                time.sleep(0.2)

                if i == 1:
                    self.root.after((timer_count + 300), lambda: self.Green.config(bg='green'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m15.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))
                    self.root.after((timer_count + 500), lambda: self.Green.config(bg='#003300'))


                elif i == 2:
                    self.root.after((timer_count + 300), lambda: self.Red.config(bg='red'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m25.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Red.config(bg='#550000'))

                elif i == 3:
                    self.root.after((timer_count + 300), lambda: self.Yellow.config(bg='yellow'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m35.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Yellow.config(bg='#555500'))

                elif i == 4:
                    self.root.after((timer_count + 300), lambda: self.Blue.config(bg='blue'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.load('m45.wav'))
                    self.root.after((timer_count + 500), lambda: pygame.mixer.music.play(loops=0))

                    self.root.after((timer_count + 500), lambda: self.Blue.config(bg='#000055'))

                timer_count += 220


    def press(self, num=1):
        global watch
        global gameover
        global count
        global score
        if count > 0 and watch == False:
            if watch == False:
                if num == 1:
                    tmp_stt.append(1)
                    self.check(count, (len(tmp_stt) - 1), num)
                    count -= 1
                    pygame.mixer.music.load('m15.wav')
                    pygame.mixer.music.play(loops=0)

                elif num == 2:
                    tmp_stt.append(2)
                    self.check(count, (len(tmp_stt) - 1), num)
                    count -= 1
                    pygame.mixer.music.load('m25.wav')
                    pygame.mixer.music.play(loops=0)

                elif num == 3:
                    tmp_stt.append(3)
                    self.check(count, (len(tmp_stt) - 1), num)
                    count -= 1
                    pygame.mixer.music.load('m35.wav')
                    pygame.mixer.music.play(loops=0)

                elif num == 4:
                    tmp_stt.append(4)
                    self.check(count, (len(tmp_stt) - 1), num)
                    count -= 1
                    pygame.mixer.music.load('m45.wav')
                    pygame.mixer.music.play(loops=0)

        if count <= 0 and gameover == False:
            score += 1
            self.l0.config(text=score)
            watch = True
            tmp_stt.clear()
            self.start(watch, gameover)


    def check(self, count=100, x=0, num=1):
        global stt
        global gameover
        if stt[x] != num:
            gameover = True
            self.l1.configure(text="GAMEOVER")
            self.TheScore = score
            self.data_score()
            self.root.after(1000, self.game_is_over)

            # self.game_is_over()


def first(self):
    self.bg_game = ImageTk.PhotoImage(file="img3.jpg")
    bg_game = Label(self.root, image=self.bg_game).place(x=0, y=0, relwidth=1, relheight=1)
    #####*******************
    #####*******************
    #####*******************
    '''find out the user type'''
    wb = openpyxl.load_workbook('good.xlsx')
    ws = wb['Sheet1']
    for i, _ in enumerate(iter(bool, True), start=2):
        if (ws.cell(row=i, column=1).value == self.The_User):
            self.therow = i
            break
    # if it is user 2 then add a button for improving
    if (ws.cell(row=self.therow, column=3).value == "User with vision problem"):  # user2
        '''btn_fo_see_problem = Button(self.root, text="...ADD...", font=("times new roman", 15, "bold"), bg="pink",
                               fg="red", width=10,cursor="hand2").place(x=100, y=110)'''
        frame_over = Frame(self.root, bg="black")
        frame_over.place(x=250, y=35, width=750, height=600)
        self.l0 = Label(frame_over, text="0", font=("Courier", 45), bg="black", fg="#836FFF")
        self.l0.grid(padx=55, pady=2, row=0, columnspan=2)
        self.l1 = Label(frame_over, text="WATCH first, PLAY after", font=("Courier", 35), bg="black", fg="#836FFF")
        self.l1.grid(padx=55, pady=2, row=1, columnspan=2)
        self.Green = Button(frame_over, text="", font=1, bg="#458B00", activebackground='#7FFF00', width=34, height=10,
                            command=lambda: self.press(1))
        self.Green.grid(row=2, column=0)
        self.Red = Button(frame_over, text="", font=1, bg="#8B1A1A", activebackground='#FF0000', width=34, height=10,
                          command=lambda: self.press(2))
        self.Red.grid(row=2, column=1)
        self.Yellow = Button(frame_over, text="", font=1, bg="#8B8B00", activebackground='#FFFF00', width=34,
                             height=10,
                             command=lambda: self.press(3))
        self.Yellow.grid(row=3, column=0)
        self.Blue = Button(frame_over, text="", font=1, bg="#36648B", activebackground='#00F5FF', width=34, height=10,
                           command=lambda: self.press(4))
        self.Blue.grid(row=3, column=1)
        btn_f_game_t_menu = Button(self.root, text="Menu", font=("times new roman", 15, "bold"), bg="indianred",
                                   fg="peachpuff", width=12, cursor="hand2", command=self.menu).place(x=30, y=50)

    #####*******************
    #####*******************
    #####*******************
    else:
        frame_over = Frame(self.root, bg="black")
        frame_over.place(x=380, y=55, width=350, height=450)
        self.l0 = Label(frame_over, text="0", font=("Courier", 25), bg="black", fg="#FFB5C5")

        self.l0.grid(padx=55, pady=2, row=0, columnspan=2)
        self.l1 = Label(frame_over, text="WATCH first, PLAY after", bg="black", fg="#FFB5C5")

        self.l1.grid(padx=55, pady=2, row=1, columnspan=2)
        self.Green = Button(frame_over, text="", font=1, bg="#003300", activebackground='green', width=15, height=7,
                            command=lambda: self.press(1))
        self.Green.grid(row=2, column=0)
        self.Red = Button(frame_over, text="", font=1, bg="#550000", activebackground='red', width=15, height=7,
                          command=lambda: self.press(2))
        self.Red.grid(row=2, column=1)
        self.Yellow = Button(frame_over, text="", font=1, bg="#555500", activebackground='yellow', width=15,
                             height=7,
                             command=lambda: self.press(3))
        self.Yellow.grid(row=3, column=0)
        self.Blue = Button(frame_over, text="", font=1, bg="#000055", activebackground='blue', width=15, height=7,
                           command=lambda: self.press(4))
        self.Blue.grid(row=3, column=1)
        global watch
        global gameover
        btn_f_game_t_menu = Button(self.root, text="Menu", font=("times new roman", 15, "bold"), bg="indianred",
                                   fg="peachpuff", width=12, cursor="hand2", command=self.menu).place(x=30, y=50)

    if watch == True and gameover == False:
        tmp = random.randint(1, 4)
        stt.append(tmp)
        # print("stt=", stt)
        self.root.after(1000, self.ChangeColor)
        watch = False


def start(self, a=True, b=False):
    global watch
    global stt
    if a == True and b == False:
        tmp = random.randint(1, 4)
        stt.append(tmp)
        # print("stt=", stt)
        self.ChangeColor()
        watch = False


def game_is_over(self):
    global watch
    global count
    global tmp
    global gameover
    global timer_count
    global score
    global tmp_stt
    global stt
    score = 0
    timer_count = 0
    watch = True
    gameover = False
    tmp_stt = []
    stt = []
    tmp = len(stt)
    self.bg_game_over = ImageTk.PhotoImage(file="img3.jpg")
    bg_game_over = Label(self.root, image=self.bg_game_over).place(x=0, y=0, relwidth=1, relheight=1)
    frame_over = Frame(self.root, bg="black")
    frame_over.place(x=280, y=105, width=300, height=312)
    title_over = Label(frame_over, text="GAME OVER", font=("times new roman", 25, "bold"), bg="black",
                       fg="red").place(x=50, y=30)
    score_over1 = Label(frame_over, text="your score is  ", font=("times new roman", 20, "bold"), bg="black",
                        fg="white").place(x=50, y=70)
    score_over2 = Label(frame_over, text=self.TheScore, font=("times new roman", 20, "bold"),
                        bg="black",
                        fg="white").place(x=220, y=70)
    btn_over_back = Button(frame_over, text="Play again", font=("times new roman", 15, "bold"), bg="pink", fg="red",
                           width=10,
                           cursor="hand2", command=self.first).place(x=50, y=110)
    btn_over_menu = Button(frame_over, text="Menu", font=("times new roman", 15, "bold"), bg="lightblue", fg="red",
                           width=10,
                           cursor="hand2", command=self.menu).place(x=50, y=160)
    btn_over_exit = Button(frame_over, text="Exit", font=("times new roman", 15, "bold"), bg="pink", fg="red",
                           width=10,
                           cursor="hand2", command=self.login).place(x=50, y=210)