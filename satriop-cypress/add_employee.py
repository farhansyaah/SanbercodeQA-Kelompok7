import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class EmployeeList(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
  def test_a_employee_add_data(self):
    fname = 'telo'
    lname = 'ungu'
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
    #click add data
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(2)
    #fill up fname
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys(fname)
    time.sleep(.5)
    #fill up lname
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(lname)
    time.sleep(.5)
    #submit
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
    time.sleep(10)
    
    res = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6').text
    self.assertIn(fname+" "+lname,res)
    
      
  def tearDown(self):
    self.browser.close()



if __name__ == "__main__":
  unittest.main()