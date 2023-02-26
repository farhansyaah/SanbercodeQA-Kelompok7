import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class EmployeeList(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
  def test_a_employee_search(self):
    driver = self.browser
    driver.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)
    #open menu PIM
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
    time.sleep(5)
    #search by employee name
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Orange')
    time.sleep(.5)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(2)
    
    res = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text
    self.assertIn('Orange',res)
    
      
  def tearDown(self):
    self.browser.close()



if __name__ == "__main__":
  unittest.main()