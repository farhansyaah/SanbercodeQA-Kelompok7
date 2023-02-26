import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddJobTitleInvalid(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_add_job_title_invalid_data(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_Job").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_viewJobTitleList").click()
        time.sleep(1)
        driver.find_element(By.ID, "Add-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "jobTitle_jobTitle").send_keys("Software Engineering")
        time.sleep(1)
        driver.find_element(By.ID, "jobTitle_jobDescription").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "jobTitle_jobSpec").send_keys(".png")
        time.sleep(1)
        driver.find_element(By.ID, "jobTitle_note").send_keys("not note")
        time.sleep(1)
        driver.find_element(By.ID, "Save-button").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.XPATH,"").text
        self.assertEqual('SAVE', response_data)
    
def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()