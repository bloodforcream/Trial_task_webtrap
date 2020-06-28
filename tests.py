import logging
import unittest
from unittest.mock import patch

import app
from test_logs_expected import logs_expected


class SetUpTests(unittest.TestCase):
    def setUp(self):
        self.messages_logged = []
        app.app.config['TESTING'] = True
        self.client = app.app.test_client()

    def log_info_mock(self, level, message, *args, **kwargs):
        level_txt = {
            logging.ERROR: "ERROR",
            logging.INFO: "INFO",
        }[level]

        self.messages_logged.append(f'{level_txt} - {message}')


class ApiTestCase(SetUpTests):
    def test_api_route(self):
        with patch('app.logger._log', self.log_info_mock):
            response = self.client.get('/api')
            self.assertEqual(response.status_code, 200)
            self.assertListEqual(self.messages_logged, logs_expected['test_api_route'])

    def test_api_route_post(self):
        with patch('app.logger._log', self.log_info_mock):
            response = self.client.post('/api')

            self.assertEqual(response.status_code, 200)
            self.assertListEqual(self.messages_logged, logs_expected['test_api_route_post'])

    def test_api_route_invalid_1_parameter(self):
        with patch('app.logger._log', self.log_info_mock):
            response = self.client.get('/api?invalid=1')

            self.assertEqual(response.status_code, 200)
            self.assertListEqual(self.messages_logged, logs_expected['test_api_route_invalid_1_parameter'])

    def test_api_route_invalid_path(self):
        with patch('app.logger._log', self.log_info_mock):
            response = self.client.get('/notapipath')

            self.assertEqual(response.status_code, 200)
            self.assertListEqual(self.messages_logged, logs_expected['test_api_route_invalid_path'])

    def test_api_route_notawaiting_1_parameter(self):
        with patch('app.logger._log', self.log_info_mock):
            response = self.client.get('/api?notawaiting=1')

            self.assertEqual(response.status_code, 200)
            self.assertListEqual(self.messages_logged, logs_expected['test_api_route_notawaiting_1_parameter'])


class ProcessesTestCase(SetUpTests):
    class RequestMock:
        def __init__(self, not_awaiting):
            self.args = {'notawaiting': not_awaiting}

    def test_process1(self):
        with patch('app.logger._log', self.log_info_mock):
            app.process1()

            self.assertListEqual(self.messages_logged, logs_expected['test_process1'])

    def test_process2(self):
        with patch('app.logger._log', self.log_info_mock):
            with patch('app.request', self.RequestMock('0')):
                app.process2()

                self.assertListEqual(self.messages_logged, logs_expected['test_process2'])

    def test_process2_not_awaiting_1(self):
        with patch('app.logger._log', self.log_info_mock):
            with patch('app.request', self.RequestMock('1')):
                app.process2()

                self.assertListEqual(self.messages_logged, logs_expected['test_process2_not_awaiting_1'])

    def test_process3(self):
        with patch('app.logger._log', self.log_info_mock):
            app.process3()

            self.assertListEqual(self.messages_logged, logs_expected['test_process3'])


if __name__ == '__main__':
    unittest.main()
