def res_to_admin(self):
    self.res_to_admin_bg = ImageTk.PhotoImage(file="img3.jpg")
    res_to_admin_bg = Label(self.root, image=self.res_to_admin_bg).place(x=0, y=0, relwidth=1, relheight=1)
    frame_admin_1 = Frame(self.root, bg="#2E2E2E")
    frame_admin_1.place(x=200, y=100, width=550, height=312)
    btn_f_score_adm_t_menu = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                    fg="peachpuff", width=12, cursor="hand2", command=self.admin).place(x=30, y=50)
    title_admin = Label(frame_admin_1, text="Show Report on a specific user", font=("times new roman", 20, "bold"),
                        bg="#2E2E2E",
                        fg="#FF3030").place(x=20, y=30)
    username_results = Label(frame_admin_1, text="Enter User Name:", font=("times new roman", 20, "bold"), bg="#2E2E2E",
                             fg="#CD5555").place(x=20, y=70)
    self.user_results = Entry(frame_admin_1, font=("times new roman", 15), bg="lightgray")
    self.user_results.place(x=20, y=130, width=200)
    btn_res = Button(frame_admin_1, text="Search", font=("times new roman", 20, "bold"), bg="#CD5555", fg="#2E2E2E",
                     width=10,
                     cursor="hand2", command=self.report).place(x=20, y=180)


def user_type(self, user):
    wb11 = openpyxl.load_workbook('good.xlsx')
    ws11 = wb11['Sheet1']
    flag = 0
    for j in range(1, 1048576):
        if (ws11.cell(row=j, column=1).value == user):
            flag = 1
            self.user_row = j
            break
    if (flag == 0):  # the user not founded
        empty = 'empty'
        return empty
    if (flag == 1):
        self.age_to_admin = ws11.cell(row=self.user_row, column=2).value  # the age for admin
        wb11_engo = openpyxl.load_workbook('rating.xlsx')  # enjoy for admin
        ws11_engo = wb11_engo['Sheet1']
        if (ws11_engo.cell(row=self.user_row, column=2).value is None):
            self.enjoy = 'empty1'  # enjoy for admin
        else:
            self.enjoy = ws11_engo.cell(row=self.user_row, column=2).value  # enjoy for admin
        return ws11.cell(row=self.user_row, column=3).value  # return for admin the user type


def report(self):
    self.type_scores = self.user_type(self.user_results.get())  # turn the function on and send the user as a parameter
    if (self.type_scores == 'empty'):
        messagebox.showerror("Error", "You Entered an incorrect UserName ", parent=self.root)
        self.user_results.delete(0, END)
    # print(self.type_scores)
    elif (self.type_scores == 'Regular user'):
        self.find_out = ""
        self.find_avg = 0
        # dd
        self.bg_scores_admin = ImageTk.PhotoImage(file="img3.jpg")
        bg_scores_admin = Label(self.root, image=self.bg_scores_admin).place(x=0, y=0, relwidth=1, relheight=1)
        btn_f_score_adm_t_menu = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                        fg="peachpuff", width=7, cursor="hand2", command=self.res_to_admin).place(x=30,
                                                                                                                  y=50)
        frame_score_1 = Frame(self.root, bg="#CDC0B0")
        frame_score_1.place(x=130, y=35, width=1100, height=600)
        title_score_1 = Label(frame_score_1, text="Last Ten Score for the user",
                              font=("times new roman", 15, "bold"), bg="#CDC0B0",
                              fg="#8B8378").place(x=800, y=20)
        title_score_2 = Label(frame_score_1, text=self.user_results.get(),
                              font=("times new roman", 15, "bold"),
                              bg="#CDC0B0",
                              fg="#8B8378").place(x=800, y=60)
        title_score_3 = Label(frame_score_1, text="USER REPORT",
                              font=("times new roman", 35, "bold"),
                              bg="#CDC0B0",
                              fg="#8B2323").place(x=30, y=20)
        username_report1 = Label(frame_score_1, text="USER Name: ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=100)
        username_report2 = Label(frame_score_1, text=self.user_results.get(),
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#8B5F65").place(x=30, y=140)
        userage_report1 = Label(frame_score_1, text="Age: ",
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#3B3B3B").place(x=30, y=180)
        userage_report2 = Label(frame_score_1, text=self.age_to_admin,
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#8B5F65").place(x=30, y=220)
        usertype_report1 = Label(frame_score_1, text="User Type: ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=260)
        usertype_report2 = Label(frame_score_1, text="Regular user",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#8B5F65").place(x=30, y=300)
        enjoying_report1 = Label(frame_score_1, text="Is the user enjoying the game? ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=340)
        if (self.enjoy == 'empty1'):
            enjoying_report2 = Label(frame_score_1, text="The user didn't rate the game",
                                     font=("times new roman", 20, "bold"),
                                     bg="#CDC0B0",
                                     fg="#8B5F65").place(x=30, y=380)
        else:
            enjoying_report2 = Label(frame_score_1, text=self.enjoy,
                                     font=("times new roman", 20, "bold"),
                                     bg="#CDC0B0",
                                     fg="#8B5F65").place(x=30, y=380)
        averege_report2 = Label(frame_score_1, text="The average of the user at the game:",
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#3B3B3B").place(x=30, y=420)
        wb_reg_adm = openpyxl.load_workbook('user1.xlsx')
        ws_reg_adm = wb_reg_adm['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=1):
            if (ws_reg_adm.cell(row=1, column=i).value == self.user_results.get()):
                self.userPlacec = i
                break
        if (ws_reg_adm.cell(row=2, column=self.userPlacec).value is None):
            no_scores = Label(frame_score_1, text="There is no previous results",
                              font=("times new roman", 15, "bold"),
                              bg="#CDC0B0", fg="#458B74").place(x=800, y=120)
            self.find_out = "non"
        else:
            global num1_admin
            num1_admin = 0
            num1_admin = 120
            for h in range(1, 11):
                num1_admin = num1_admin + 30
                num_scores = Label(frame_score_1, text=h,
                                   font=("times new roman", 15, "bold"),
                                   bg="#CDC0B0", fg="#8B8378").place(x=800, y=num1_admin)
                num_scores_2 = Label(frame_score_1, text="-",
                                     font=("times new roman", 15, "bold"),
                                     bg="#CDC0B0", fg="#8B8378").place(x=825, y=num1_admin)
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        count1_reg = 0
        helpvair = 120
        self.l = np.array([])  # $$%^#$^%^&*&  #to get a graph
        for k, _ in enumerate(iter(bool, True), start=2):
            if (ws_reg_adm.cell(row=k, column=self.userPlacec).value is None):
                for ro in range(k - 1, 1, -1):
                    if count1_reg == 10:
                        break
                    else:
                        count1_reg = count1_reg + 1
                        helpvair = helpvair + 30
                        scores_to_screen = Label(frame_score_1,
                                                 text=ws_reg_adm.cell(row=ro, column=self.userPlacec).value,
                                                 font=("times new roman", 15, "bold"),
                                                 bg="#CDC0B0", fg="#8B5F65").place(x=845, y=helpvair)

                        b = np.append(self.l, [ws_reg_adm.cell(row=ro, column=self.userPlacec).value])

                    self.l = b
                wb_reg_adm.save('user1.xlsx')
                break
        wb_reg_adm.close()
        if (ws_reg_adm.cell(row=2, column=i).value is not None):
            self.long = len(self.l)
            btn_for_graph = Button(frame_score_1, text="Graph for the scores",
                                   font=("times new roman", 14, "bold"),
                                   bg="#8B5F65",
                                   fg="#D3D3D3", width=20, cursor="hand2", command=self.graph).place(x=420, y=500)
        self.type_user_1 = 'Regular user'
        self.AGE = self.age_to_admin
        btn_for_pdf = Button(frame_score_1, text="Generate Report",
                             font=("times new roman", 14, "bold"),
                             bg="#8B5F65",
                             fg="#D3D3D3", width=17, cursor="hand2", command=self.Generate_report).place(x=220,
                                                                                                         y=500)

        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # add a chart
        '''game_number =np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        fig, ax = plt.subplots()
        ax.plot(game_number, self.l, label="scores")
        ax.legend()
        plt.show()'''

        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # calcuate averege for the user
        wb_reg_adm1 = openpyxl.load_workbook('user1.xlsx')
        ws_reg_adm1 = wb_reg_adm1['Sheet1']
        sum = 0
        countofdata = 0
        for a, _ in enumerate(iter(bool, True), start=2):
            if (ws_reg_adm.cell(row=a, column=self.userPlacec).value is not None):
                countofdata = countofdata + 1
                sum = sum + ws_reg_adm.cell(row=a, column=self.userPlacec).value
            if (ws_reg_adm.cell(row=a, column=self.userPlacec).value is None):
                break
        if (countofdata == 0):
            averege_report1 = Label(frame_score_1, text="the user didn't play yet, there is no average",
                                    font=("times new roman", 20, "bold"),
                                    bg="#CDC0B0",
                                    fg="#8B5F65").place(x=30, y=460)
        elif (countofdata != 0):
            avg = sum / countofdata
            averege_report1 = Label(frame_score_1, text=avg,
                                    font=("times new roman", 20, "bold"),
                                    bg="#CDC0B0",
                                    fg="#8B5F65").place(x=30, y=460)
            self.find_avg = avg
        wb_reg_adm1.save('user1.xlsx')
        wb_reg_adm1.close()








    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    elif (self.type_scores == "User with vision problem"):
        self.find_out = ""
        self.find_avg = 0
        self.bg_scores_admin = ImageTk.PhotoImage(
            file="img3.jpg")
        bg_scores_admin = Label(self.root, image=self.bg_scores_admin).place(x=0, y=0, relwidth=1, relheight=1)
        btn_f_score_adm_t_menu = Button(self.root, text="Back", font=("times new roman", 15, "bold"),
                                        bg="indianred",
                                        fg="peachpuff", width=7, cursor="hand2", command=self.res_to_admin).place(
            x=30, y=50)
        frame_score_1 = Frame(self.root, bg="#CDC0B0")
        frame_score_1.place(x=130, y=35, width=1100, height=600)
        title_score_1 = Label(frame_score_1, text="Last Ten Score for the user",
                              font=("times new roman", 15, "bold"), bg="#CDC0B0",
                              fg="#8B8378").place(x=800, y=20)
        title_score_2 = Label(frame_score_1, text=self.user_results.get(),
                              font=("times new roman", 15, "bold"),
                              bg="#CDC0B0",
                              fg="#8B8378").place(x=800, y=60)
        title_score_3 = Label(frame_score_1, text="USER REPORT",
                              font=("times new roman", 35, "bold"),
                              bg="#CDC0B0",
                              fg="#8B2323").place(x=30, y=20)
        username_report1 = Label(frame_score_1, text="USER Name: ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=100)
        username_report2 = Label(frame_score_1, text=self.user_results.get(),
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#8B5F65").place(x=30, y=140)
        userage_report1 = Label(frame_score_1, text="Age: ",
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#3B3B3B").place(x=30, y=180)
        userage_report2 = Label(frame_score_1, text=self.age_to_admin,
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#8B5F65").place(x=30, y=220)
        usertype_report1 = Label(frame_score_1, text="User Type: ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=260)
        usertype_report2 = Label(frame_score_1, text="User with vision problem",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#8B5F65").place(x=30, y=300)
        enjoying_report1 = Label(frame_score_1, text="Is the user enjoying the game? ",
                                 font=("times new roman", 20, "bold"),
                                 bg="#CDC0B0",
                                 fg="#3B3B3B").place(x=30, y=340)
        if (self.enjoy == 'empty1'):
            enjoying_report2 = Label(frame_score_1, text="The user didn't rate the game",
                                     font=("times new roman", 20, "bold"),
                                     bg="#CDC0B0",
                                     fg="#8B5F65").place(x=30, y=380)
        else:
            enjoying_report2 = Label(frame_score_1, text=self.enjoy,
                                     font=("times new roman", 20, "bold"),
                                     bg="#CDC0B0",
                                     fg="#8B5F65").place(x=30, y=380)
        averege_report2 = Label(frame_score_1, text="The averge of the user at the game:",
                                font=("times new roman", 20, "bold"),
                                bg="#CDC0B0",
                                fg="#3B3B3B").place(x=30, y=420)
        wb_reg_adm = openpyxl.load_workbook('user2.xlsx')
        ws_reg_adm = wb_reg_adm['Sheet1']
        for i, _ in enumerate(iter(bool, True), start=1):
            if (ws_reg_adm.cell(row=1, column=i).value == self.user_results.get()):
                self.userPlacec = i
                break
        if (ws_reg_adm.cell(row=2, column=i).value is None):
            no_scores = Label(frame_score_1, text="There is no previous results",
                              font=("times new roman", 15, "bold"),
                              bg="#CDC0B0", fg="#458B74").place(x=800, y=120)
            self.find_out = "non"
        else:
            global num2_admin
            num2_admin = 0
            num2_admin = 120
            for h in range(1, 11):
                num2_admin = num2_admin + 30
                num_scores = Label(frame_score_1, text=h,
                                   font=("times new roman", 15, "bold"),
                                   bg="#CDC0B0", fg="#8B8378").place(x=800, y=num2_admin)
                num_scores_2 = Label(frame_score_1, text="-",
                                     font=("times new roman", 15, "bold"),
                                     bg="#CDC0B0", fg="#8B8378").place(x=825, y=num2_admin)
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        count1_reg = 0
        helpvair = 120
        self.l = np.array([])  # $$%^#$^%^&*&
        for k, _ in enumerate(iter(bool, True), start=2):
            if (ws_reg_adm.cell(row=k, column=self.userPlacec).value is None):
                for ro in range(k - 1, 1, -1):
                    if count1_reg == 10:
                        break
                    else:
                        count1_reg = count1_reg + 1
                        # print(sheet1_score.cell(row=ro, column=self.userPlace).value)
                        helpvair = helpvair + 30
                        scores_to_screen = Label(frame_score_1,
                                                 text=ws_reg_adm.cell(row=ro, column=self.userPlacec).value,
                                                 font=("times new roman", 15, "bold"), bg="#CDC0B0",
                                                 fg="#8B5F65").place(x=845, y=helpvair)
                        c = np.append(self.l, [ws_reg_adm.cell(row=ro, column=self.userPlacec).value])
                    self.l = c
                wb_reg_adm.save('user2.xlsx')
                break
        wb_reg_adm.close()
        if (ws_reg_adm.cell(row=2, column=i).value is not None):
            self.long = len(self.l)
            btn_for_graph = Button(frame_score_1, text="Graph for the scores",
                                   font=("times new roman", 14, "bold"),
                                   bg="#8B5F65",
                                   fg="#D3D3D3", width=20, cursor="hand2", command=self.graph).place(x=420, y=500)
        self.type_user_1 = "User with vision problem"
        self.AGE = self.age_to_admin
        btn_for_pdf = Button(frame_score_1, text="Generate Report",
                             font=("times new roman", 14, "bold"),
                             bg="#8B5F65",
                             fg="#D3D3D3", width=17, cursor="hand2", command=self.Generate_report).place(x=220, y=500)

        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # add a chart
        '''game_number = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        fig, ax = plt.subplots()
        ax.plot(game_number, self.l, label="scores")
        ax.legend()
        plt.show()'''

        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # &*^%^&*&^%%$$##$*&(*^%$$#
        # calcuate averege for the user
        wb_reg_adm1 = openpyxl.load_workbook('user2.xlsx')
        ws_reg_adm1 = wb_reg_adm1['Sheet1']
        sum = 0
        countofdata = 0
        for a, _ in enumerate(iter(bool, True), start=2):
            if (ws_reg_adm.cell(row=a, column=self.userPlacec).value is not None):
                countofdata = countofdata + 1
                sum = sum + ws_reg_adm.cell(row=a, column=self.userPlacec).value
            if (ws_reg_adm.cell(row=a, column=self.userPlacec).value is None):
                break
        if (countofdata == 0):
            averege_report1 = Label(frame_score_1, text="the user didn't play yet, there is no average",
                                    font=("times new roman", 20, "bold"),
                                    bg="#CDC0B0",
                                    fg="#8B5F65").place(x=30, y=460)
        elif (countofdata != 0):
            avg = sum / countofdata
            averege_report1 = Label(frame_score_1, text=avg,
                                    font=("times new roman", 20, "bold"),
                                    bg="#CDC0B0",
                                    fg="#8B5F65").place(x=30, y=460)
            self.find_avg = avg
        wb_reg_adm1.save('user2.xlsx')
        wb_reg_adm1.close()