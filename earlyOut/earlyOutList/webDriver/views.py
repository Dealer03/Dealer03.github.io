from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create your views here.


def update_webdriver(request):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    return render(request, 'webdriver.html')


def run_webdriver(request):
    # Set up ChromeDriver with the latest version
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    try:
        # Navigate to the website URL
        driver.get("https://hh-vr.seminolehardrock.com/ESS/login.aspx?")

        # Further actions using the web driver
        # login information
        username_input = driver.find_element(By.ID, "txtUserName")
        password_input = driver.find_element(By.ID, "txtPassword")

        username_input.send_keys("28")
        password_input.send_keys("123456")

        submit = driver.find_element(By.ID, "cmdLogin")
        submit.send_keys(Keys.ENTER)

        # placeholder for user inputs. this needs to be updated
        format_date = username_input
        user_input = username_input

        # clicks the current day in the calender screen
        if format_date == user_input:
            calender = driver.find_element(By.ID, user_input)
            calender.click()

            success_message = "Web Driver executed successfully!"
        return render(request, '/home.html', {'success_message': success_message})
    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        return render(request,  '/home.html', {'error_message': error_message})
    finally:
        # Quit the driver to release resources
        driver.quit()
