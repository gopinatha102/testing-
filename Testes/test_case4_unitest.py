import unittest


def setUpModule():
    print("Starting The Module ")


def tearDownModule():
    print("Ending The Module ")


class Apptesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("*"*33)
        print("*", " Welcome for Testing ", "*")
        print("*" * 33)


    @classmethod
    def tearDown(cls):
        print("-" * 34)
        print("|","Testing Completed Successfully", "|")
        print("-" * 34)

    @classmethod
    def setUpClass(cls):
        print("|"*30)
        print("Open Application")
        print("|" * 30)

    @classmethod
    def tearDownClass(cls):
        print("|" * 30)
        print("Close Application")
        print("|" * 30)


    def testcase_search(self):
        print("The Text Searching")

    def test_case_login(self):
        print("The page is login")

    def test_case_logout(self):
        print("The page is logout ")

if __name__ == "__main()__":
    unittest.main()
