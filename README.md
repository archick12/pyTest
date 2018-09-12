# PyTestAndRequests

# To run tests
* clone the project 
```git clone```
* open the project in PyCharm
* put your jira credentials in "credentials.py"
* click on green triangle near test that you want to run

# BUILD STATUS ON CI - [![CircleCI](https://circleci.com/gh/archick12/PyTestAndRequests.svg?style=svg)](https://circleci.com/gh/archick12/PyTestAndRequests)

# To get Allure report
* install allure command line ```brew install allure```. More details at - https://docs.qameta.io/allure/#_installing_a_commandline
* run tests , for example ```python3.6 -m pytest --alluredir allure_result_folder```
* ```allure serve allure_result_folder/```. More details at - https://pypi.org/project/allure-pytest/