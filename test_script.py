from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# Scenario 1: User registration and login

# User registration with details such as username, mobile number, passsword and Email
def register(driver):

    # launch web page https://www.bookbazaar.com on chrome browser
    driver.maximize_window()
    driver.get("https://www.bookbazaar.com")

    # Click on the "Sign Up" link
    sign_up_link = driver.find_element(By.ID, "ctl00_loginname")
    sign_up_link.click()

    # Fill out the registration form
    username_input = driver.find_element(By.ID, "RegName")
    username_input.send_keys("testuser")

    mobile_input = driver.find_element(By.ID, "RegMobile")
    mobile_input.send_keys("1234567891")

    pass_input = driver.find_element(By.ID, "RegPass")
    pass_input.send_keys("1234567")

    pass_input1 = driver.find_element(By.ID, "RegPass1")
    pass_input1.send_keys("1234567")

    email_input = driver.find_element(By.ID, "RegEmail")
    email_input.send_keys("test@test.com")

    # Submit the registration form
    register_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_registerbtn")
    time.sleep(2)
    register_button.click()
    time.sleep(5)

    
    # registration_success_message = driver.find.element(By.id,"registration_success_message")

    # assert "Registration successful" in registration_success_message.text


# User login with registered credentials 
def login(driver):
    # Navigate to login page
    driver.get("https://www.bookbazaar.com")

    # Click on the "Sign in" link
    sign_up_link = driver.find_element(By.ID, "ctl00_signin")
    sign_up_link.click()

    # Log in with the registered credentials
    username_input = driver.find_element(By.ID, "LgnMobileOrEmail")
    username_input.send_keys("8310901162")

    password_input = driver.find_element(By.ID, "logintextpswd")
    password_input.send_keys("su@KM2496")

    # Submit the login form
    login_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnLogin")
    time.sleep(2)
    login_button.click()
    time.sleep(5)


    # login_success_message =driver.find.element(By.ID,"login_success_message")

    # assert "Login successful" in login_success_message.text

    
# Scenario 2: Product browsing and selection
    
def product_selection(driver):
    # Assuming user is already logged in
    driver.get("https://www.bookbazaar.com/stationery")

    # Browse products
    product_list = driver.find_element(By.ID, "listingofbook")
    product_list.click()
    time.sleep(2)

    # Log in with the registered credentials  confProductView
    selected_product = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_pro_bnow")
   
    # Click on each product to view details
    selected_product.click()
    time.sleep(5)


# Scenario 3: Adding products to the shopping cart
def product_checkout(driver):
    # Assuming user is already logged in and on products page
    driver.get("https://www.bookbazaar.com/checkout")
    time.sleep(5)

    # Submit the login form
    login_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnLogin")
    time.sleep(2)
    login_button.click()
    time.sleep(5)


# Test ui function to set chrome path and env path
def test_ui():
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the relative path to the Chromedriver executable
    chromedriver_path = os.path.join(current_directory, "..", "drivers", "chromedriver")

    # Add the directory to the PATH environment variable
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        register(driver)
        time.sleep(2)
        login(driver)
        time.sleep(2)
        product_selection(driver)
        time.sleep(5)
        product_checkout(driver)
        time.sleep(2)

    finally:
        # Close the browser window at the end
        driver.quit()


# main funtion to call test
if __name__ == "__main__":
    test_ui()
