def top_three_reg(self):
    self.bg_top_five_reg_admin = ImageTk.PhotoImage(file="img3.jpg")
    bg_top_five_reg_admin = Label(self.root, image=self.bg_top_five_reg_admin).place(x=0, y=0, relwidth=1, relheight=1)
    btn_f_top_five_adm_reg_ = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                     fg="peachpuff", width=7, cursor="hand2", command=self.admin).place(x=30,
                                                                                                        y=50)
    frame_top_reg = Frame(self.root, bg="#CDC0B0")
    frame_top_reg.place(x=300, y=35, width=700, height=500)
    title_top_five_1 = Label(frame_top_reg, text="Top 3 players of Regular user type: ",
                             font=("times new roman", 25, "bold"), bg="#CDC0B0",
                             fg="#8B0000").place(x=40, y=20)
    # finding the top 5
    wb_avg_top_adm1 = openpyxl.load_workbook('user1.xlsx')
    ws_avg_top_adm1 = wb_avg_top_adm1['Sheet1']

    sum = 0
    countofdata = 0
    avg_max1 = 0
    avg_max2 = 0
    avg_max3 = 0
    name1 = 'There is no one in this rank yet'
    name2 = 'There is no one in this rank yet'
    name3 = 'There is no one in this rank yet'
    flag = 0
    for c, _ in enumerate(iter(bool, True), start=2):
        sum = 0
        countofdata = 0
        if (ws_avg_top_adm1.cell(row=1, column=c).value is not None):  # user 1 go throw all the names
            for d, _ in enumerate(iter(bool, True), start=2):
                if (ws_avg_top_adm1.cell(row=d, column=c).value is not None):  # count avg for the user
                    countofdata = countofdata + 1
                    sum = sum + ws_avg_top_adm1.cell(row=d, column=c).value
                if (ws_avg_top_adm1.cell(row=d, column=c).value is None):
                    break
            if (countofdata != 0 and flag == 0):  # need to save names also
                flag = 1
                avg = sum / countofdata
                avg_max1 = avg
                name1 = ws_avg_top_adm1.cell(row=1, column=c).value
                continue
            if (countofdata != 0 and flag == 1):
                avg = sum / countofdata
                if (avg >= avg_max1):
                    avg_max3 = avg_max2
                    name3 = name2
                    avg_max2 = avg_max1
                    name2 = name1
                    avg_max1 = avg
                    name1 = ws_avg_top_adm1.cell(row=1, column=c).value
                if (avg < avg_max1 and avg >= avg_max2):
                    avg_max3 = avg_max2
                    name3 = name2
                    avg_max2 = avg
                    name2 = ws_avg_top_adm1.cell(row=1, column=c).value
                if (avg < avg_max2 and avg >= avg_max3):
                    avg_max3 = avg
                    name3 = ws_avg_top_adm1.cell(row=1, column=c).value
        if (ws_avg_top_adm1.cell(row=1, column=c).value is None):
            break
    '''print(avg_max3)
    print(name3)
    print(avg_max2)
    print(name2)
    print(avg_max1)
    print(name1)'''
    wb_avg_top_adm1.save('user1.xlsx')
    wb_avg_top_adm1.close()
    num1 = 80

    for h in range(1, 4):
        num1 = num1 + 50
        num_scores = Label(frame_top_reg, text=h,
                           font=("times new roman", 20, "bold"),
                           bg="#CDC0B0", fg="#8B0000").place(x=30, y=num1)
        num_scores_2 = Label(frame_top_reg, text="-",
                             font=("times new roman", 20, "bold"),
                             bg="#CDC0B0", fg="#8B0000").place(x=60, y=num1)
    name1_in_top = Label(frame_top_reg, text=name1,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=130)
    name2_in_top = Label(frame_top_reg, text=name2,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=180)
    name3_in_top = Label(frame_top_reg, text=name3,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=230)
    if (name1 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_reg, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=130)
    if (name2 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_reg, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=180)
    if (name3 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_reg, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=230)
    if (name1 != 'There is no one in this rank yet'):
        avg1_in_top = Label(frame_top_reg, text=avg_max1,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=130)
    if (name2 != 'There is no one in this rank yet'):
        avg2_in_top = Label(frame_top_reg, text=avg_max2,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=180)
    if (name3 != 'There is no one in this rank yet'):
        avg3_in_top = Label(frame_top_reg, text=avg_max3,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=230)


def top_three_prob(self):
    self.bg_top_five_prob_admin = ImageTk.PhotoImage(file="img3.jpg")
    bg_top_five_prob_admin = Label(self.root, image=self.bg_top_five_prob_admin).place(x=0, y=0, relwidth=1,
                                                                                       relheight=1)
    btn_f_top_five_adm_reg_ = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                     fg="peachpuff", width=7, cursor="hand2", command=self.admin).place(x=30, y=50)
    frame_top_prob = Frame(self.root, bg="#CDC0B0")
    frame_top_prob.place(x=300, y=35, width=700, height=500)
    title_top_five_1 = Label(frame_top_prob, text="Top 3 players of 'User with vision problem' user type",
                             font=("times new roman", 20, "bold"), bg="#CDC0B0", fg="#8B0000").place(x=40, y=20)

    sum = 0
    countofdata = 0
    avg_max1 = 0
    avg_max2 = 0
    avg_max3 = 0
    name1 = 'There is no one in this rank yet'
    name2 = 'There is no one in this rank yet'
    name3 = 'There is no one in this rank yet'
    flag = 0
    wb_avg_top_adm2 = openpyxl.load_workbook('user2.xlsx')
    ws_avg_top_adm2 = wb_avg_top_adm2['Sheet1']
    for c, _ in enumerate(iter(bool, True), start=2):
        sum = 0
        countofdata = 0
        if (ws_avg_top_adm2.cell(row=1, column=c).value is not None):  # user 1 go throw all the names
            for d, _ in enumerate(iter(bool, True), start=2):
                if (ws_avg_top_adm2.cell(row=d, column=c).value is not None):  # count avg for the user
                    countofdata = countofdata + 1
                    sum = sum + ws_avg_top_adm2.cell(row=d, column=c).value
                if (ws_avg_top_adm2.cell(row=d, column=c).value is None):
                    break
            if (countofdata != 0 and flag == 0):  # need to save names also
                flag = 1
                avg = sum / countofdata
                avg_max1 = avg
                name1 = ws_avg_top_adm2.cell(row=1, column=c).value
                continue
            if (countofdata != 0 and flag == 1):
                avg = sum / countofdata
                if (avg >= avg_max1):
                    avg_max3 = avg_max2
                    name3 = name2
                    avg_max2 = avg_max1
                    name2 = name1
                    avg_max1 = avg
                    name1 = ws_avg_top_adm2.cell(row=1, column=c).value
                if (avg < avg_max1 and avg >= avg_max2):
                    avg_max3 = avg_max2
                    name3 = name2
                    avg_max2 = avg
                    name2 = ws_avg_top_adm2.cell(row=1, column=c).value
                if (avg < avg_max2 and avg >= avg_max3):
                    avg_max3 = avg
                    name3 = ws_avg_top_adm2.cell(row=1, column=c).value
        if (ws_avg_top_adm2.cell(row=1, column=c).value is None):
            break
    wb_avg_top_adm2.save('user2.xlsx')
    wb_avg_top_adm2.close()
    '''print(avg_max3)
    print(name3)
    print(avg_max2)
    print(name2)
    print(avg_max1)
    print(name1)'''
    num1 = 80

    for h in range(1, 4):
        num1 = num1 + 50
        num_scores = Label(frame_top_prob, text=h,
                           font=("times new roman", 20, "bold"),
                           bg="#CDC0B0", fg="#8B0000").place(x=30, y=num1)
        num_scores_2 = Label(frame_top_prob, text="-",
                             font=("times new roman", 20, "bold"),
                             bg="#CDC0B0", fg="#8B0000").place(x=60, y=num1)
    name1_in_top = Label(frame_top_prob, text=name1,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=130)
    name2_in_top = Label(frame_top_prob, text=name2,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=180)
    name3_in_top = Label(frame_top_prob, text=name3,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=230)
    if (name1 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_prob, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=130)
    if (name2 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_prob, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=180)
    if (name3 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top_prob, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=230)
    if (name1 != 'There is no one in this rank yet'):
        avg1_in_top = Label(frame_top_prob, text=avg_max1,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=130)
    if (name2 != 'There is no one in this rank yet'):
        avg2_in_top = Label(frame_top_prob, text=avg_max2,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=180)
    if (name3 != 'There is no one in this rank yet'):
        avg3_in_top = Label(frame_top_prob, text=avg_max3,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=230)


def graph(self):
    # add a chart
    game_number = np.arange(1, self.long + 1)
    fig, ax = plt.subplots()
    ax.plot(game_number, self.l, label="score at the game")
    ax.legend()
    plt.ylabel('scores')
    plt.xlabel('game number')
    plt.suptitle('User progression in the last 10 games')
    plt.show()