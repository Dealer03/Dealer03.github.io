from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import threading
import time
import datetime
import schedule

#This program is made to run in the backround and keep the app
#listening for a trigged event. 


def run_continuously(interval=1):

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

#this method keeps track of the time 
def background_job():

    #re-formats the time to be processed by the app
    current_date = datetime.datetime.now().strftime("%I,%M,%S")
    format_date = current_date.replace(",",":",2)
    time_entered = '10:30:00' 

    if format_date != time_entered: 
     print(format_date)
    else:

     if format_date == time_entered:
      return automation()

schedule.every().second.do(background_job)
    
     # Start the background thread
stop_run_continuously = run_continuously()

    

    #time.sleep(10)
    # Stop the background thread
    #stop_run_continuously.set()
       

def automation():
        
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    #open chrome browser and navigate to url
    driver = webdriver.Chrome(PATH)
    driver.get("https://hh-vr.seminolehardrock.com/ESS/login.aspx?")

    #record current date and formats to string
    current_date = datetime.datetime.now().strftime("%Y,%m,%d")

    format_date = current_date.replace(",","",2)


   # days = [0]
    user_input = "20230330"

    #login information    
    username_input = driver.find_element(By.ID,"txtUserName")
    password_input = driver.find_element(By.ID,"txtPassword")
                    
    username_input.send_keys("28")
    password_input.send_keys("123456")

    submit = driver.find_element(By.ID,"cmdLogin")
    submit.send_keys(Keys.ENTER)

    #variable already ran
    already_ran = True

    driver.implicitly_wait(10)

    #clicks the current day in the calender screen
    if format_date == user_input:
                calender = driver.find_element(By.ID,user_input)
                calender.click()
    elif format_date != user_input:
                driver.quit()

    if already_ran == True:

        #clicks the "add to EO List button - warning update: function ran again after 1st run"
        driver.implicitly_wait(3)
        eo_list = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/a[5]")
        eo_list.click()

        # clicks the submit button
        driver.implicitly_wait(3)
        eo_list_submit = driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div/div/div/div/div[3]/a[1]")
        eo_list_submit.click()

        #closes the "EO" modal window
        driver.implicitly_wait(2)
        eo_list_close = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div/div/div[3]/a")
        eo_list_close.click()

        time.sleep(10)
        driver.quit()  

    # Stop the background thread
#stop_run_continuously.set()

        

       

        
