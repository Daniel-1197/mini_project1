# GUVI Website Automation Using Python Selenium & PyTest Framework

This project automates the testing of the GUVI website "https://www.guvi.in" using Python Selenium PyTest Framework. The test cases contains all positive and negative scenarios.
The entire test suite is written using PyTest.
Browser management is handled using fixtures and implemented ChromeOptions() to run the driver in 'headless' mode in `conftest.py` file.

# Folder Structure in pycharm

mini_project_1/
  > conftest.py     # Browser setup
  > guvi_page.py    # Page Object Model for GUVI site
  > test_guvi.py    # Test cases using PyTest

# Test Cases

-  Guvi URL validation
-  Verification of website title
-  Check visibility & clickability of Login button
-  Check visibility & clickability of Sign-Up button
-  Check the existance of the webpage "https://www.guvi.in/sign-in/" using sign-ip button
-  Check valid login and logout
-  Handle invalid login and catch the error

# Technologies Used

- Python
- Selenium 
- PyTest
- Page Object Model (POM)

