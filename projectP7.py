def Generate_report(self):
    messagebox.showinfo("The report has been generated",
                        "You can found the report of the user in the Folder were the program exist, at the name 'UserReport'",
                        parent=self.root)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'BU', 16)
    pdf.cell(40, 10, 'Generate report for the user', ln=True)

    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(240, 128, 128)
    pdf.cell(20, 10, 'User name:', ln=True)
    pdf.set_text_color(16, 78, 139)
    pdf.cell(20, 10, self.user_results.get(), ln=True)

    # %$^^&*(**&&^^%$%#$
    # find user age
    wb112 = openpyxl.load_workbook('good.xlsx')
    ws112 = wb112['Sheet1']
    for j in range(1, 1048576):
        if (ws112.cell(row=j, column=1).value == self.user_results.get()):
            self.user_row1 = j
            break
    self.age_to_admin1 = ws112.cell(row=self.user_row1, column=2).value
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(240, 128, 128)
    pdf.cell(20, 10, 'User Age:', ln=True)
    pdf.set_text_color(16, 78, 139)
    converted_age = f'{self.age_to_admin1}'
    pdf.cell(20, 10, converted_age, ln=True)

    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(240, 128, 128)
    pdf.cell(20, 10, 'User Type:', ln=True)
    pdf.set_text_color(16, 78, 139)
    pdf.cell(20, 10, self.type_user_1, ln=True)

    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(240, 128, 128)
    pdf.cell(20, 10, 'Is the user enjoying the game?', ln=True)
    pdf.set_text_color(16, 78, 139)
    if (self.enjoy == 'empty1'):
        pdf.cell(20, 10, "The user didn't rate the game", ln=True)
    else:
        pdf.cell(20, 10, self.enjoy, ln=True)

    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(240, 128, 128)
    pdf.cell(20, 10, 'The average of the user at the game:', ln=True)
    pdf.set_text_color(16, 78, 139)
    if (self.find_out == "non"):
        pdf.cell(20, 10, "the user didn't play yet, there is no average", ln=True)
    else:
        converted_avg = f'{self.find_avg}'
        pdf.cell(20, 10, converted_avg, ln=True)
    pdf.output('UserReport.pdf', 'F')