from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDeleteJobTitle(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_delete_job_title(self):
    # steps
        driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login as admin
        username = driver.find_element_by_id("txtUsername")
        username.send_keys("Admin")

        password = driver.find_element_by_id("txtPassword")
        password.send_keys("admin123")

        login_btn = driver.find_element_by_id("btnLogin")
        login_btn.click()

    # Access the Job menu and select Job Titles
        admin_menu = driver.find_element_by_id("menu_admin_viewAdminModule")
        admin_menu.click()

        job_menu = driver.find_element_by_id("menu_admin_Job")
        job_menu.click()

        job_title_menu = driver.find_element_by_id("menu_admin_viewJobTitleList")
        job_title_menu.click()

    # Delete the first job title
        checkbox = driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[1]/td[1]/input")
        checkbox.click()

        delete_btn = driver.find_element_by_id("btnDelete")
        delete_btn.click()

        alert = driver.switch_to.alert
        alert.accept()

    # validasi
        response_data = driver.find_element(By.XPATH,"").text
        self.assertEqual('SAVE', response_data)
    
def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()




