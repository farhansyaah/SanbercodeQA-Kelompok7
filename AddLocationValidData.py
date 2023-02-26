from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddLocationValid(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_add_location_valid_data(self):
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

    # Add a new location
        add_btn = driver.find_element_by_id("btnAdd")
        add_btn.click()

        name = driver.find_element_by_id("location_name")
        name.send_keys("Sumatera Selatan")

        city = driver.find_element_by_id("location_city")
        city.send_keys("Kota Palembang")

        postal_code = driver.find_element_by_id("location_zipCode")
        postal_code.send_keys("39114")

        phone = driver.find_element_by_id("location_phone")
        phone.send_keys("808")

        address = driver.find_element_by_id("location_address")
        address.send_keys("Jl Merdeka")

        province = driver.find_element_by_id("location_province")
        province.send_keys("Sumatera Selatan")

        country = Select(driver.find_element_by_id("location_country"))
        country.select_by_visible_text("Indonesia")

        fax = driver.find_element_by_id("location_fax")
        fax.send_keys("123456789")

        note = driver.find_element_by_id("location_notes")
        note.send_keys("not note")

        save_btn = driver.find_element_by_id("btnSave")
        save_btn.click()

    # validasi
        response_data = driver.find_element(By.XPATH,"").text
        self.assertEqual('SAVE', response_data)
    
def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
