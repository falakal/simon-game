def averege_of_all(self):
    self.bg_avg_admin = ImageTk.PhotoImage(file="img3.jpg")
    bg_avg_admin = Label(self.root, image=self.bg_avg_admin).place(x=0, y=0, relwidth=1, relheight=1)
    btn_f_avg_adm_t_menu = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                  fg="peachpuff", width=7, cursor="hand2", command=self.admin).place(x=30,
                                                                                                     y=50)
    frame_avg = Frame(self.root, bg="#CDC0B0")
    frame_avg.place(x=300, y=35, width=700, height=500)
    title_avg_1 = Label(frame_avg, text=" Show average of users of the same type",
                        font=("times new roman", 25, "bold"), bg="#CDC0B0",
                        fg="#8B0000").place(x=40, y=20)
    title_avg_2 = Label(frame_avg, text="Average users of type 'Regular user' : ",
                        font=("times new roman", 15, "bold"), bg="#CDC0B0",
                        fg="#8B3A3A").place(x=40, y=120)
    title_avg_3 = Label(frame_avg, text="Average users of type 'User with vision problem' :",
                        font=("times new roman", 15, "bold"), bg="#CDC0B0",
                        fg="#8B3A3A").place(x=40, y=190)
    # avg for type 1 "regular user"
    wb_avg_reg_adm1 = openpyxl.load_workbook('user1.xlsx')
    ws_reg_adm1 = wb_avg_reg_adm1['Sheet1']
    # @@@@@@@@@
    sum = 0
    sum_for_all = 0
    countofdata = 0
    count_of_all = 0
    for a, _ in enumerate(iter(bool, True), start=2):
        sum = 0
        countofdata = 0
        if (ws_reg_adm1.cell(row=1, column=a).value is not None):
            count_of_all = count_of_all + 1
            for b, _ in enumerate(iter(bool, True), start=2):
                if (ws_reg_adm1.cell(row=b, column=a).value is not None):
                    countofdata = countofdata + 1
                    sum = sum + ws_reg_adm1.cell(row=b, column=a).value
                if (ws_reg_adm1.cell(row=b, column=a).value is None):
                    if (countofdata == 0):
                        count_of_all = count_of_all - 1
                        break
                    avg = sum / countofdata
                    sum_for_all = sum_for_all + avg
                    break
        if (ws_reg_adm1.cell(row=1, column=a).value is None):
            break
    avg_all = sum_for_all / count_of_all
    title_avg_2_reg = Label(frame_avg, text=avg_all,
                            font=("times new roman", 15, "bold"), bg="#CDC0B0",
                            fg="#8B0000").place(x=390, y=120)
    # print(avg_all)
    wb_avg_reg_adm1.save('user1.xlsx')
    wb_avg_reg_adm1.close()

    # avg for type 2 "user with vision problem"
    wb_avg_prop_adm1 = openpyxl.load_workbook('user2.xlsx')
    ws_avg_prop_adm1 = wb_avg_prop_adm1['Sheet1']
    # @@@@@@@@@
    sum = 0
    sum_for_all = 0
    countofdata = 0
    count_of_all = 0
    for c, _ in enumerate(iter(bool, True), start=2):
        sum = 0
        countofdata = 0
        if (ws_avg_prop_adm1.cell(row=1, column=c).value is not None):
            count_of_all = count_of_all + 1
            for d, _ in enumerate(iter(bool, True), start=2):
                if (ws_avg_prop_adm1.cell(row=d, column=c).value is not None):
                    countofdata = countofdata + 1
                    sum = sum + ws_avg_prop_adm1.cell(row=d, column=c).value
                if (ws_avg_prop_adm1.cell(row=d, column=c).value is None):
                    if (countofdata == 0):
                        count_of_all = count_of_all - 1
                        break
                    avg = sum / countofdata
                    sum_for_all = sum_for_all + avg
                    break
        if (ws_avg_prop_adm1.cell(row=1, column=c).value is None):
            break
    avg_all_p = sum_for_all / count_of_all
    title_avg_2_prob = Label(frame_avg, text=avg_all_p,
                             font=("times new roman", 15, "bold"), bg="#CDC0B0",
                             fg="#8B0000").place(x=490, y=190)
    # print(avg_all_p)
    wb_avg_prop_adm1.save('user2.xlsx')
    wb_avg_prop_adm1.close()


def top_three(self):
    self.bg_top_five_admin = ImageTk.PhotoImage(file="img3.jpg")
    bg_top_five_admin = Label(self.root, image=self.bg_top_five_admin).place(x=0, y=0, relwidth=1, relheight=1)
    btn_f_top_five_adm_t_ = Button(self.root, text="Back", font=("times new roman", 15, "bold"), bg="indianred",
                                   fg="peachpuff", width=7, cursor="hand2", command=self.admin).place(x=30,
                                                                                                      y=50)
    frame_top = Frame(self.root, bg="#CDC0B0")
    frame_top.place(x=300, y=35, width=700, height=500)
    title_top_five_1 = Label(frame_top, text="Top 3 players of all types: ",
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
        num_scores = Label(frame_top, text=h,
                           font=("times new roman", 20, "bold"),
                           bg="#CDC0B0", fg="#8B0000").place(x=30, y=num1)
        num_scores_2 = Label(frame_top, text="-",
                             font=("times new roman", 20, "bold"),
                             bg="#CDC0B0", fg="#8B0000").place(x=60, y=num1)
    name1_in_top = Label(frame_top, text=name1,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=130)
    name2_in_top = Label(frame_top, text=name2,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=180)
    name3_in_top = Label(frame_top, text=name3,
                         font=("times new roman", 20, "bold"),
                         bg="#CDC0B0", fg="#8B0000").place(x=90, y=230)
    if (name1 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=130)
    if (name2 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=180)
    if (name3 != 'There is no one in this rank yet'):
        so_in_top = Label(frame_top, text="- with average :",
                          font=("times new roman", 15, "bold"),
                          bg="#CDC0B0", fg="#8B0000").place(x=180, y=230)
    if (name1 != 'There is no one in this rank yet'):
        avg1_in_top = Label(frame_top, text=avg_max1,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=130)
    if (name2 != 'There is no one in this rank yet'):
        avg2_in_top = Label(frame_top, text=avg_max2,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=180)
    if (name3 != 'There is no one in this rank yet'):
        avg3_in_top = Label(frame_top, text=avg_max3,
                            font=("times new roman", 20, "bold"),
                            bg="#CDC0B0", fg="#8B0000").place(x=350, y=230)

