from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDeleteLocation(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_delete_location(self):
    # steps
        driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login as admin
        username = driver.find_element_by_id("txtUsername")
        username.send_keys("Admin")

        password = driver.find_element_by_id("txtPassword")
        password.send_keys("admin123")

        login_btn = driver.find_element_by_id("btnLogin")
        login_btn.click()

    # Access the Organization menu and select Location
        admin_menu = driver.find_element_by_id("menu_admin_viewAdminModule")
        admin_menu.click()

        org_menu = driver.find_element_by_id("menu_admin_Organization")
        org_menu.click()

        location_menu = driver.find_element_by_id("menu_admin_viewLocations")
        location_menu.click()

    # Delete the first location
        checkbox = driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[1]/td[1]/input")
        checkbox.click()

        delete_btn = driver.find_element_by_id("btnDelete")
        delete_btn.click()

        alert = driver.switch_to.alert
        alert.accept()

    # Close the browser
        driver.quit()

# validasi
    response_data = driver.find_element(By.XPATH,"").text
    self.assertEqual('DELETE', response_data)
    
def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()




