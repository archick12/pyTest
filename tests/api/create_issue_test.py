import requests
from tests.api.utils.base_api_test import BaseAPITest
from tests.api.utils.json_fixture import JSONFixture


class TestLogin(BaseAPITest):

    def test_create_issue(self):
        result = requests.post(self.jiraUrl + "/rest/api/2/issue",
                               json=JSONFixture.for_create_issue(),
                               headers=self.headers,
                               cookies=BaseAPITest.cookie)
        assert 201 == result.status_code

    def test_create_issue2(self):
        result = requests.post(self.jiraUrl + "/rest/api/2/issue",
                               json=JSONFixture.for_create_issue(),
                               headers=self.headers,
                               cookies=BaseAPITest.cookie)
        assert 201 == result.status_code
