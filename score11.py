def data_score(self):
    '''find out the user type'''
    wb = openpyxl.load_workbook('good.xlsx')
    ws = wb['Sheet1']
    for i, _ in enumerate(iter(bool, True), start=2):
        if (ws.cell(row=i, column=1).value == self.The_User):
            self.therow = i
            break
    # need to check the type of the user in good file and then put the data at the right file
    if (ws.cell(row=self.therow, column=3).value == "Regular user"):  # user1
        wb_reg = openpyxl.load_workbook('user1.xlsx')
        sheet1 = wb_reg['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=1):
            if (sheet1.cell(row=1, column=i).value == self.The_User):
                for j, _ in enumerate(iter(bool, True), start=1):
                    if (sheet1.cell(row=j, column=i).value is None):
                        sheet1.cell(row=j, column=i).value = self.TheScore
                        wb_reg.save('user1.xlsx')
                        break
                break
        wb_reg.close()

    if (ws.cell(row=self.therow, column=3).value == "User with vision problem"):  # user2
        wb_prob = openpyxl.load_workbook('user2.xlsx')
        sheet2 = wb_prob['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=1):
            if (sheet2.cell(row=1, column=i).value == self.The_User):
                for j, _ in enumerate(iter(bool, True), start=1):
                    if (sheet2.cell(row=j, column=i).value is None):
                        sheet2.cell(row=j, column=i).value = self.TheScore
                        wb_prob.save('user2.xlsx')
                        break
                break
        wb_prob.close()


def score_page(self):
    self.bg_scores = ImageTk.PhotoImage(file="img3.jpg")
    bg_scores = Label(self.root, image=self.bg_scores).place(x=0, y=0, relwidth=1, relheight=1)
    btn_f_score_t_menu = Button(self.root, text="Menu", font=("times new roman", 15, "bold"), bg="indianred",
                                fg="peachpuff", width=12, cursor="hand2", command=self.menu).place(x=30, y=50)
    frame_score = Frame(self.root, bg="#8B8386")
    frame_score.place(x=380, y=35, width=550, height=600)
    title_score = Label(frame_score, text="Last Ten Score", font=("times new roman", 30, "bold"), bg="#8B8386",
                        fg="#EEE0E5").place(x=10, y=20)
    # ************************
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@
    '''find out the user type'''
    wb = openpyxl.load_workbook('good.xlsx')
    ws = wb['Sheet1']
    for i, _in in enumerate(iter(bool, True), start=1):
        if (ws.cell(row=i, column=1).value == self.The_User):
            self.therow = i
            break
    # need to check the type of the user in good file and then put the data at the right file
    if (ws.cell(row=self.therow, column=3).value == "Regular user"):  # user1
        global count1_reg
        count1_reg = 0
        global helpvair
        helpvair = 0
        helpvair = 80
        wb_reg_score = openpyxl.load_workbook('user1.xlsx')
        sheet1_score = wb_reg_score['Sheet1']
        for j, _ in enumerate(iter(bool, True), start=1):  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            if (sheet1_score.cell(row=1, column=j).value == self.The_User):
                self.userPlace = j
                break
        if (sheet1_score.cell(row=2, column=self.userPlace).value is None):  # there is no scores
            no_scores = Label(frame_score, text="There is no previous results", font=("times new roman", 20, "bold"),
                              bg="#8B8386", fg="#EEE0E5").place(x=10, y=80)

        else:
            global num1
            num1 = 0
            num1 = 80

            for h in range(1, 11):
                num1 = num1 + 30
                num_scores = Label(frame_score, text=h,
                                   font=("times new roman", 20, "bold"),
                                   bg="#8B8386", fg="#EEE0E5").place(x=30, y=num1)
                num_scores_2 = Label(frame_score, text="-",
                                     font=("times new roman", 20, "bold"),
                                     bg="#8B8386", fg="#EEE0E5").place(x=60, y=num1)

        for k, _ in enumerate(iter(bool, True), start=2):
            if (sheet1_score.cell(row=k, column=self.userPlace).value is None):
                for ro in range(k - 1, 1, -1):
                    if count1_reg == 10:
                        break
                    else:
                        count1_reg = count1_reg + 1
                        # print(sheet1_score.cell(row=ro, column=self.userPlace).value)
                        helpvair = helpvair + 30
                        scores_to_screen = Label(frame_score,
                                                 text=sheet1_score.cell(row=ro, column=self.userPlace).value,
                                                 font=("times new roman", 15, "bold"),
                                                 bg="#FFF8DC", fg="#DC143C").place(x=90, y=helpvair)
                wb_reg_score.save('user1.xlsx')
                break
        wb_reg_score.close()
    if (ws.cell(row=self.therow, column=3).value == "User with vision problem"):  # user2
        global count2_prob
        count2_prob = 0
        global helpvairp
        helpvairp = 0
        helpvairp = 80
        wb_prob_score = openpyxl.load_workbook('user2.xlsx')
        sheet1_score_prob = wb_prob_score['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=1):
            if (sheet1_score_prob.cell(row=1, column=i).value == self.The_User):
                self.userPlacep = i
                break
        if (sheet1_score_prob.cell(row=2, column=self.userPlacep).value is None):  # there is no scores
            no_scores = Label(frame_score, text="There is no previous results", font=("times new roman", 20, "bold"),
                              bg="#8B8386", fg="#EEE0E5").place(x=10, y=80)
        else:
            global num2
            num2 = 0
            num2 = 80
            for f in range(1, 11):
                num2 = num2 + 30
                num_scores = Label(frame_score, text=f,
                                   font=("times new roman", 20, "bold"),
                                   bg="#8B8386", fg="#EEE0E5").place(x=30, y=num2)
                num_scores_2 = Label(frame_score, text="-",
                                     font=("times new roman", 20, "bold"),
                                     bg="#8B8386", fg="#EEE0E5").place(x=60, y=num2)
        for t, _ in enumerate(iter(bool, True), start=2):
            if (sheet1_score_prob.cell(row=t, column=self.userPlacep).value is None):
                for prob in range(t - 1, 1, -1):
                    if count2_prob == 10:
                        break
                    else:
                        count2_prob = count2_prob + 1
                        # print(sheet1_score_prob.cell(row=prob, column=self.userPlacep).value)
                        helpvairp = helpvairp + 30
                        scores_to_screen = Label(frame_score,
                                                 text=sheet1_score_prob.cell(row=prob, column=self.userPlacep).value,
                                                 font=("times new roman", 15, "bold"),
                                                 bg="#FFF8DC", fg="#DC143C").place(x=90, y=helpvairp)
                wb_prob_score.save('user2.xlsx')
                break
        wb_prob_score.close()
def instructions(self):
        self.bg_instructions = ImageTk.PhotoImage(file="img3.jpg")
        bg_instructions = Label(self.root, image=self.bg_instructions).place(x=0, y=0, relwidth=1, relheight=1)
        frame_instructions = Frame(self.root, bg="beige")
        frame_instructions.place(x=100, y=50, width=1100, height=390)
        title_instructions = Label(frame_instructions, text="Instructions for the game:", font=("times new roman", 20, "bold"), bg="beige",
                      fg="dimgray").place(x=50, y=20)
        instructions1= Label(frame_instructions, text="-1-Simon will give the first signal. Repeat the signal by pressing the same color lens.", font=("times new roman", 15, "bold"),
                      bg="beige",
                      fg="firebrick").place(x=50, y=80)
        instructions2 = Label(frame_instructions,
                              text="-2-Simon will duplicate the first signal and add one. Repeat these two signals by pressing the same color lenses, in order.",
                              font=("times new roman", 15, "bold"),
                              bg="beige",
                              fg="firebrick").place(x=50, y=110)
        instructions3 = Label(frame_instructions,
                              text="-3-Simon will duplicate these first two signals and add one.",
                              font=("times new roman", 15, "bold"),
                              bg="beige",
                              fg="firebrick").place(x=50, y=140)
        instructions4 = Label(frame_instructions,
                              text="-4-Continue playing as long as you can repeat each sequence of signals correctly.",
                              font=("times new roman", 15, "bold"),
                              bg="beige",
                              fg="firebrick").place(x=50, y=170)
        instructions5 = Label(frame_instructions,
                              text="-5-If you fail to repeat a sequence exactly,this means you've lost, and the sequence of signals ends.",
                              font=("times new roman", 15, "bold"),
                              bg="beige",
                              fg="firebrick").place(x=50, y=200)
        btn_instructions_back = Button(frame_instructions, text="Menu", font=("times new roman", 15, "bold"), bg="firebrick",
                               fg="beige",
                               width=10,
                               cursor="hand2", command=self.menu).place(x=800, y=270)
def admin(self):
        self.bg_admin = ImageTk.PhotoImage(file="img3.jpg")
        bg_admin = Label(self.root, image=self.bg_admin).place(x=0, y=0, relwidth=1, relheight=1)
        frame_admin = Frame(self.root, bg="#2E2E2E")
        frame_admin.place(x=200, y=100, width=650, height=512)
        title_admin = Label(frame_admin, text="Hello Admin", font=("times new roman", 25, "bold"), bg="#2E2E2E", fg="#FF3030").place(
            x=20, y=30)
        btn_f_adm_t_out = Button(self.root, text="Log out", font=("times new roman", 15, "bold"), bg="indianred",
                                        fg="peachpuff", width=12, cursor="hand2", command=self.login).place(x=30, y=50)
        btn2 = Button(frame_admin, text="- Show Report on a specific user", font=("times new roman", 14, "bold"), bg="#2E2E2E",
                      fg="#8B6914", bd=0, width=30, cursor="hand2",command=self.res_to_admin).place(x=20, y=90)
        btn3 = Button(frame_admin, text="- Show average of users of the same type", font=("times new roman", 14, "bold"),
                      bg="#2E2E2E",
                      fg="#8B6914", bd=0, width=35, cursor="hand2",command=self.averege_of_all).place(x=20, y=140)
        btn4 = Button(frame_admin, text="- Top 3 players of all types",
                      font=("times new roman", 14, "bold"),
                      bg="#2E2E2E",
                      fg="#8B6914", bd=0, width=23, cursor="hand2",command=self.top_three).place(x=20, y=190)
        btn5 = Button(frame_admin, text="- Top 3 players of Regular user type",
                      font=("times new roman", 14, "bold"),
                      bg="#2E2E2E",
                      fg="#8B6914", bd=0, width=30, cursor="hand2",command=self.top_three_reg).place(x=20, y=240)
        btn6 = Button(frame_admin, text="- Top 3 players of 'User with vision problem' user type",
                      font=("times new roman", 14, "bold"),
                      bg="#2E2E2E",
                      fg="#8B6914", bd=0, width=40, cursor="hand2",command=self.top_three_prob).place(x=20, y=290)
