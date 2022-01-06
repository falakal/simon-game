#start of test
import unittest
import my_project

#test for the simon game project
class test_fileopen(unittest.TestCase):

    def test_files_xlsx_all(self):
        self.assertEqual(my_project.Register.fileopen("good.xlsx"), True)
    def test_files_xlsx_reg(self):
        self.assertEqual(my_project.Register.fileopen("user1.xlsx"), True)
    def test_files_xlsx_pro(self):
        self.assertEqual(my_project.Register.fileopen("user2.xlsx"), True)
    def test_files_xlsxrat(self):
        self.assertEqual(my_project.Register.fileopen("rating.xlsx"), True)
    def test_fileopen_image(self):
        self.assertEqual(my_project.Register.fileopen_image("as.png"), True)
        self.assertEqual(my_project.Register.fileopen_image("black.png"), True)
        self.assertEqual(my_project.Register.fileopen_image("img3.png"), True)
    def test_fileopen_sound(self):
        self.assertEqual(my_project.Register.fileopen_sound("m15.wav"), True)
    def test_fileopen_sound2(self):
        self.assertEqual(my_project.Register.fileopen_sound("m25.wav"), True)
    def test_fileopen_sound2(self):
        self.assertEqual(my_project.Register.fileopen_sound("m35.wav"), True)
    def test_fileopen_sound2(self):
        self.assertEqual(my_project.Register.fileopen_sound("m45.wav"), True)


class scoretestfuctions(unittest.TestCase):
    def test_getscorefunction(self):
        self.assertEqual(33,my_project.Register.score_get(33))

    def test_getscorefunction2(self):
            self.assertEqual(4, my_project.Register.score_get(4))

    def test_topthreescoreget(self):
        self.assertEqual(True,my_project.Register.topthreescoreget("yes"))
        self.assertEqual(False, my_project.Register.topthreescoreget("NO"))
    def test_topthreescoreget_reg(self):
        self.assertEqual(True,my_project.Register.topthreescoreget("yes"))
        self.assertEqual(False, my_project.Register.topthreescoreget("NO"))

    def test_topthreescoreget_pro(self):
        self.assertEqual(True,my_project.Register.topthreescoreget("yes"))
        self.assertEqual(False, my_project.Register.topthreescoreget("NO"))

#login info
class login_functions(unittest.TestCase):

    def test_finduser(self):
        self.assertEqual(my_project.Register.loginfind_name2("falak"),"falak")
        self.assertEqual(my_project.Register.loginfind_name2("hseen"), "hseen")
        self.assertEqual(my_project.Register.loginfind_name2("yos"), "yos")

    def test_finduser2(self):
        self.assertEqual(my_project.Register.loginfind_name2("aa"),"aa")

#instructions details
class instructions1test(unittest.TestCase):

    def test_instructions1(self):
        self.assertEqual(True, my_project.Register.instructions1("yes"))
        self.assertEqual(False, my_project.Register.instructions1("NO"))

    def test_instructions2(self):
        self.assertEqual(True, my_project.Register.instructions1("yes"))
        self.assertEqual(False, my_project.Register.instructions1("aa"))
if __name__ == '__main__':
    unittest.main()
