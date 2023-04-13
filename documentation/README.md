# Introduction
The proj folder contains the selenium test cases as well as API tests for Trello board
API tests are in cards.feature
Selenium UI tests are in automation.feature
All necessary packages mentioned in requirements.txt are installed in venv folder.
Allure files are present in allure-2.21.0 needed for reporting
# Documentation folder contains 
Excel sheet with UI and API testcases and test plan
Readme.md
# How to to run
go to proj directory
behave -f allure_behave.formatter:AllureFormatter -o reports . 
.\allure-2.21.0\bin\allure serve reports
# Reports
Once allure serve command is ran, a web page will open with the results shown.
# Docker file
Running the Dockerfile will generate an image on which all the API tests can be run.
At the moment the UI tests are supported with Dockerfile.