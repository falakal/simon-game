#start of test
import unittest
import my_project
class test_graph1fucntions(unittest.TestCase):

    def test_graph1_reg(self):
        self.assertEqual(my_project.Register.graph1("test"), "test")
        self.assertEqual(my_project.Register.graph1("!!"), "!!")

    def test_graph1_reg2(self):
        self.assertEqual(my_project.Register.graph1("111"), "111")

    def test_graph1_prob(self):
        self.assertEqual(my_project.Register.graph2("me"), "me")

    def test_graph1_prob2(self):
       self.assertEqual(my_project.Register.graph2("user1"), "user1")
       self.assertEqual(my_project.Register.graph2("1"), "1")

    def test_graph1_admin(self):
       self.assertEqual(my_project.Register.graph2("els"), "els")
       self.assertEqual(my_project.Register.graph2("2"), "2")

#find data register log
class testentryregister(unittest.TestCase):

    def test_finduser(self):
        self.assertEqual(my_project.Register.find_used("falak"),"falak")
        self.assertEqual(my_project.Register.find_used("hseen"), "hseen")

    def test_finduser2(self):
        self.assertEqual(my_project.Register.find_used("no"), "no")

    def test_register_username(self):
        self.assertEqual("hseen","hseen")
        self.assertEqual("falak","falak")

        self.user = {
            'hseen': 'hseen',
            'falak': 'falak',
            'same': 'same'

        }


    def test_age(self):
        self.assertEqual("20", "20")
        self.age = {
            '12': '13',
        }

    def test_age2(self):
        self.assertEqual("20", "20")
        self.assertEqual("21", "21")
        self.age = {
            '18': '18',
            '20':'20',
            '14':'14'

        }

if __name__ == '__main__':
    unittest.main()