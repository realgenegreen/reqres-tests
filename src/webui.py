import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as condition

class WEB:

    @staticmethod
    def clicks(driver, xpath, wait:int=False):

        driver.get('https://reqres.in/')
        element_1 = driver.find_element(By.XPATH, value=xpath)
        element_1.click()
        if wait:
            Wait(driver, wait).until(condition.invisibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/section[1]/div[2]/div[2]/div',)))
        element_2 = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/section[1]/div[2]/div[2]/p/strong/span')
        status_code = element_2.text
        element_3 = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/section[1]/div[2]/div[2]/pre').text
        if element_3 == '':
            body = dict([('status_code',status_code)])
            return body
        body = json.loads(element_3)
        body.update(dict([('status_code',status_code)]))
        
        return body



# ♥ for IBS with love ♥ #
