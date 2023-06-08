from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def book(sport, day, time, phoneNumber, email, name):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000')
    try:
        elements = browser.find_elements(By.CLASS_NAME, "content")
        for element in elements:
            if element.get_attribute("innerHTML") == sport:
                element.click()
    except:
        #people in group
        numPeople = browser.find_element(By.ID, "reservationCount")
        numPeople.clear()
        numPeople.send_keys("2")
        submit = browser.find_element(By.ID, "submit-btn")
        submit.click()
        #time select
        elements = browser.find_elements(By.CLASS_NAME, "header-text")
        for element in elements:
            text = element.get_attribute("innerHTML")
            if day in text:
                element.click()
                elements = browser.find_elements(By.CLASS_NAME, "available-time")
                for element in elements:
                    text = element.get_attribute("innerHTML")
                    if time in text:
                        parent = element.find_element(By.XPATH, "./..")
                        parent.click()
                        #final page
                        phonenumber = browser.find_element(By.NAME, "PhoneNumber")
                        phonenumber.send_keys(phoneNumber)
                        email = browser.find_element(By.NAME, "Email")
                        email.send_keys(email)
                        name = browser.find_element(By.NAME, "field3196")
                        name.send_keys(name)
                        submit = browser.find_element(By.ID, "submit-btn")
                        submit.click()
                        #real final page
                        submit = browser.find_element(By.ID, "submit-btn")
                        submit.click()
f = open("info.txt", "r")
lines = f.readlines()
bookings = int(len(lines)/3)
for i in range (0,bookings):
    print(i)
    book("Badminton", "Thursday", "11:30", lines[3*i], lines[3*i + 1], lines[3*i + 2])