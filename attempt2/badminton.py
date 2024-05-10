from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as timer
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000')
    
def book(sport, day, time, phoneNumber, emailAddress, bookingName):
    browser.get('https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000')
    try:
        elements = browser.find_elements(By.CLASS_NAME, "content")
        for element in elements:
            if element.get_attribute("innerHTML") == sport:
                element.click()
    except:
        #people in group
        try: 
            numPeople = browser.find_element(By.ID, "reservationCount")
            numPeople.clear()
            numPeople.send_keys("2")
            submit = browser.find_element(By.ID, "submit-btn")
            submit.click()
        except:
            print("booked 1")
        #time select
        elements = browser.find_elements(By.CLASS_NAME, "header-text")
        for element in elements:
            text = element.get_attribute("innerHTML")
            if day in text:
                element.click()
                elements = browser.find_elements(By.CLASS_NAME, "available-time")
                for element in elements:
                    text = element.get_attribute("innerHTML")
                    print(text)
                    if time in text:
                        parent = element.find_element(By.XPATH, "./..")
                        parent.click()
                        timer.sleep(1)
                        #info page
                        phonenumber = browser.find_element(By.NAME, "PhoneNumber")
                        phonenumber.send_keys(phoneNumber)
                        email = browser.find_element(By.NAME, "Email")
                        email.send_keys(emailAddress)
                        name = browser.find_element(By.NAME, "field2021")
                        name.send_keys(bookingName)
                        submit = browser.find_element(By.ID, "submit-btn")
                        submit.click()
                        timer.sleep(10000)
                        # try: 
                        #     
                        #     #real final page
                        #     submit = browser.find_element(By.ID, "submit-btn")
                        #     submit.click()
                        # except: 
def ping(sport, day):
    browser.get('https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000')
    try:
        elements = browser.find_elements(By.CLASS_NAME, "content")
        for element in elements:
            if element.get_attribute("innerHTML") == sport:
                element.click()
    except:
        #people in group
        try: 
            numPeople = browser.find_element(By.ID, "reservationCount")
            numPeople.clear()
            numPeople.send_keys("2")
            submit = browser.find_element(By.ID, "submit-btn")
            submit.click()
        except:
            print("booked 1")
        #time select
        elements = browser.find_elements(By.CLASS_NAME, "header-text")
        for element in elements:
            text = element.get_attribute("innerHTML")
            if day in text:
                return True
        return False
s = "Pickleball"
d = "Friday"
t = "11:30 AM"
p = "6138094885"
e = "timeluicifer@gmail.com"
n = "Mikael Booth"
result = ping(s, d)
while(not result):
    result = ping(s, d)
book(s, d, t, p, e, n)
# book("Badminton", "Sunday", "8:00", "6138094885", "timeluicifer@gmail.com", "Mikael Booth")