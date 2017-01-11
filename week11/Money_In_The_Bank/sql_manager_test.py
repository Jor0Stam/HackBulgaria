import sys
import unittest
import os
import sql_manager


sys.path.append("..")


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', '123123')

        sql_manager.cursor.execute('''SELECT Count(*)
                                      FROM clients
                                      WHERE username = (?)
                                      AND password = (?)''', ('Dinko',
                                                              '123123'))
        self.assertFalse(sql_manager.cursor.fetchone())
        sql_manager.register('Dinko', 'A#$123123')

        sql_manager.cursor.execute('''SELECT Count(*)
                                      FROM clients
                                      WHERE username = (?)
                                      AND password = (?)''', ('Dinko',
                                                              'A#$123123'))
        self.assertTrue(sql_manager.cursor.fetchone())

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_sql_injections(self):
        self.assertFalse(sql_manager.login('OR 1 = 1', ''))


if __name__ == '__main__':
    unittest.main()
