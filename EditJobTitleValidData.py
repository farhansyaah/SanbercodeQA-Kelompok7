import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestEditJobTitle(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_edit_job_title(self):
    # steps
        driver = self.browser
        driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login as Admin
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

    # Navigate to Job Titles page
        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        driver.find_element_by_id("menu_admin_Job").click()
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()

    # Edit Job Title
        job_title = "QA"
        edit_btn_xpath = "//a[text()='" + job_title + "']/../following-sibling::td[2]/a"
        driver.find_element_by_xpath(edit_btn_xpath).click()

        job_description = "Quality Assurance"
        job_description_field = driver.find_element_by_id("jobTitle_jobDescription")
        job_description_field.clear()
        job_description_field.send_keys(job_description)

        driver.find_element_by_id("btnSave").click()

    # Verify Job Title is updated
        updated_job_description = wait.until(EC.visibility_of_element_located((By.ID, "jobTitle_jobDescription"))).get_attribute("value")
        assert updated_job_description == job_description

def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
