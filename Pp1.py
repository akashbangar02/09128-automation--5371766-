from selenium import webdriver
from selenium.webdriver.common.by import By



def expected():
    driver = webdriver.Chrome("C:\\Users\\DELL\\Downloads\\chromedriver.exe")

    driver.get('http://amazon.com')

    driver.find_element(By.CLASS_NAME, "twotabsearchtextbox").send_keys("dell").click()

    expected = "displaying at least 10 search results"


def actual():


    actual ="displaying at least 10 search results"


assert actual() == expected()