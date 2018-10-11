import requests


class BaseAPITest:
    jiraUrl = 'http://jira.hillel.it:8080'
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def authenticate():
        if BaseAPITest.cookie == "":
            result = requests.get('http://jira.hillel.it:8080',
                                  auth=('webinar5', 'webinar5'))
            assert 200 == result.status_code
            BaseAPITest.cookie = {'JSESSIONID': result.cookies.get("JSESSIONID")}
