#start of test
import unittest
import my_project

#chekcbuttons work
class buttontestcode(unittest.TestCase):

    def test_buttons_log(self):
        self.assertEqual(my_project.Register.buttons("login"),True)
        self.assertEqual(my_project.Register.buttons("login1"), False)

    def test_buttons_exit(self):
        self.assertEqual(my_project.Register.buttons("exit"),True)
        self.assertEqual(my_project.Register.buttons("exit1"), False)
    def test_buttons_rate(self):
        self.assertEqual(my_project.Register.buttons("Rate Us"),True)
        self.assertEqual(my_project.Register.buttons("Rate U"), False)
    def test_buttons_newgaem(self):
        self.assertEqual(my_project.Register.buttons("new game"), True)
        self.assertEqual(my_project.Register.buttons("els"), False)
    def test_count1(self):
        self.assertEqual(my_project.Register.count_bu(70),72)

    def test_count2(self):
        self.assertEqual(my_project.Register.count_bu(200+1), 203)
#admin
class buttontestadmin(unittest.TestCase):

    def test_buttons_logad(self):
        self.assertEqual(my_project.Register.buttons("login"),True)
        self.assertEqual(my_project.Register.buttons("logi"), False)

    def test_buttons_show(self):
        self.assertEqual(my_project.Register.admin_button("Show average of users of the same type"),True)
        self.assertEqual(my_project.Register.buttons("not here"), False)
    def test_buttons_show2(self):
        self.assertEqual(my_project.Register.admin_button("Average users of type 'Regular user"),True)
        self.assertEqual(my_project.Register.admin_button("aaaa"), False)
    def test_buttons_top1(self):
        self.assertEqual(my_project.Register.admin_button("Top 3 players of Regular user type:"), True)
        self.assertEqual(my_project.Register.admin_button("top3"), False)

    def test_buttons_top2(self):
        self.assertEqual(my_project.Register.admin_button("Top 3 players of 'User with vision problem' user type"), True)
        self.assertEqual(my_project.Register.admin_button("top3"), False)
    def test_buttons_top3(self):
        self.assertEqual(my_project.Register.admin_button("new game"), True)
    def test_count1(self):
        self.assertEqual(my_project.Register.count_bu(40),42)

    def test_count2(self):
        self.assertEqual(my_project.Register.count_bu(30+1), 33)
class Unit_Test_formtype(unittest.TestCase):
    '''Unit_Test_form'''
    def test_valid_Form(self):
        data={'login'}
        self.assertTrue(data,{'login'})

    def test_valid_Form(self):
        data={'message':'test'}
        self.assertTrue(data,{'message':'test'})

    def test_age_Form(self):
        age={"age"}
        self.assertTrue(age,{"age1"})

    def test_invalid1_Form(self):
        data={}
        self.assertFalse(data,{"aa"})

    def test_file_Form1(self):
        message={'message':'REGISTRATION FORM'}
        self.assertTrue(message,{'message':'REGISTRATION FORM'})
    def test_file_form2(self):
        file={'file_name':'user1','file':'xlsx'}
        len(file)
        self.assertTrue(file,{'file_name':'user1','file':'xlsx'})

    def test_name_form(self):
        a="aaaaaaaaaa"
        len(a)
        user={'name':'a','age':'20'}
        self.assertTrue(user,{'name':'a','age':'20'})

if __name__ == '__main__':
    unittest.main()