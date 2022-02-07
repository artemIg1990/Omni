import unittest
import smoke_test_assist


class MyTestCase(unittest.TestCase):
    def test_order_no_pay(self):
        params = {"price": 0, "status": 0, "client_order": False}
        order = smoke_test_assist.create_order(params)
        assert order['code'] == 201



if __name__ == '__main__':
    unittest.main()
    MyTestCase.smoke_test()
