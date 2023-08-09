                                Automation Challenge for Stori Position

DESCRIPTION

This is an automation project with the goal of accomplishing the requirements stated in the pdf file with name:
'Tech_Challenge_-_QA_Engineer_'
The repository is structured following the Page Object model. The 'driver.py' file contains a fixture which is called
before any test. It is the file which calls the driver and select the browser in which the tests will be done.

Pytest-BDD
The first test is done in pytest-bdd as an example of how to implement Behave Driven Development technique in an
Automation test. You can see it in the folder 'features'. It will be automatically executed along with the main test.

test_stori_card.py
This file will execute all the tests which correspond to the requirements.

REQUIREMENTS

Please, make sure to install all the dependencies in the 'requirements.txt' file before execution.
Locate yourself in the directory of the project. Make sure you are using your virtual environment and execute the
following command:
        -----------------------------------------------------------------------------------------------------
        -----                            pip install -r requirements.txt                                -----
        -----------------------------------------------------------------------------------------------------

EXECUTION

Use the following command to run the test in chrome browser and generate a html report:

        ------------------------------------------------------------------------------------------------------
        -----          pytest --browser chrome --html=Reports/report.html --self-contained-html          -----
        ------------------------------------------------------------------------------------------------------

Use the following command to generate a xml report:

        ------------------------------------------------------------------------------------------------------
        -----          pytest --browser chrome --junit-xml=Reports/report.xml                            -----
        ------------------------------------------------------------------------------------------------------

Note that you can replace chrome with firefox or edge. Each command will execute the tests in a different browser.

A report will be automatically generated, thanks to pytest-html, in the folder 'Reports' with the name report.html
You can access it opening it through a web browser.


Thanks for your time and consideration!
Ernesto Sennhauser
linkedIn: https://www.linkedin.com/in/ersennhauser/
github: https://github.com/esennhauser

