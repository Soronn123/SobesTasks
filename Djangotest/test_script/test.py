import unittest
import requests


class TestCase(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.defaultUrl = 'http://127.0.0.1:8000/'

    def testParamCorrectFirst(self):
        params = {
                "name": "Ronald Williams",
                "date": "2024-12-10",
                "phone": "81700351773",
                "email": "qbztH@gmail.com"
                }
        url = self.defaultUrl + 'get_form'

        response = requests.get(url, params=params)

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, 'people')

    def testParamCorrectSecond(self):
        params = {
            "name": "Rick Williams",
            "date": "2024-12-10",
            "phone": "88440631980",
            "email": "XrvTf@yandex.ru"
                }
        url = self.defaultUrl + 'get_form'

        response = requests.get(url, params=params)

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, 'avtors')

    def testParamCorrectSecond(self):
        params = {
            "name": "Rick Williams",
            "date": "2024-12-10",
            "phone": "88440631980",
            "email": "VJREd@gmail.com"
                }
        url = self.defaultUrl + 'get_form'

        response = requests.get(url, params=params)

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, 'Undefined')    

    def testPath(self):
        params = {
            "name": "Rick Williams",
            "date": "2024-12-10",
            "phone": "88440631980",
            "email": "XrvTf@yandex.ru"
                }
        url = self.defaultUrl
        response = requests.get(url, params=params)
        self.assertEqual(404, response.status_code)

        url = self.defaultUrl + 'admin'
        response = requests.get(url, params=params)
        self.assertEqual(404, response.status_code)

        url = self.defaultUrl + 'hachapyri'
        response = requests.get(url, params=params)
        self.assertEqual(404, response.status_code)

    def testValid(self):
        params = {
            "name": "Rick Williams",
            "date": "2024-12-10",
            "phone": "88440631980",
            "email": "XrvTf@yandex.ru" 
        }
        
        result = """
    name : text halo,
    date : date YYYY-MM-DD | DD.MM.YYYY 2024-10-12,
    phone : phone +79999999999,
    email : email example@yandex.ru
"""

        url = self.defaultUrl + 'get_form'
        
        params["date"] = "2024/12/10"
        response = requests.get(url, params=params)
        print(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, result)

        params["date"] = "2024/32/10"
        response = requests.get(url, params=params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, result)

        params["email"] = "dasjdasdyandex.ru"
        response = requests.get(url, params=params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, result)

        params["phone"] = "+754389403278686"
        response = requests.get(url, params=params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.text, result)


if __name__ == '__main__':
    unittest.main()