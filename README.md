# Scooter Rental Website Automated Testing

This project is dedicated to automated testing of a scooter rental website using Python, Pytest, and Allure.

## Prerequisites

Before running the tests, make sure you have the following prerequisites installed on your system:

- Python 3.x
- pytest
- allure-pytest

You can install the required packages using pip:

```bash
pip install pytest allure-pytest
Running the Tests
To execute the tests, run the following command from the project's root directory:

bash
Copy code
pytest -v --alluredir=./allure-results
This command will run the tests and store the test results in the ./allure-results directory.

Viewing Test Reports
After running the tests, you can generate and view an Allure test report. Use the following command to generate the report:

bash
Copy code
allure serve ./allure-results
This command will start a local web server, and you can access the report in your web browser.

Test Descriptions
TestDropdown
This test checks the text of dropdown elements on the main page of the scooter rental website.

TestScooterOrder
This test verifies the process of ordering a scooter on the website. It includes filling out the order form and verifying the success message.

TestClickScooterLogo
This test ensures that clicking the scooter logo on the order page takes the user back to the home page of the website.

TestClickYandexLogo
This test confirms that clicking the Yandex logo on the order page opens the Yandex Zen page in a new tab.

