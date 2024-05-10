from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_correct_search(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()
 
    search_field_tuple = (By.ID, "search")
    search_field = wait.until(EC.element_to_be_clickable(search_field_tuple))
    search_field.click()
    search_field.clear()
    search_field.send_keys("kolica")
    search_button = driver.find_element(By.CLASS_NAME, "ec-search")
    search_button.click()

    trazeni_rezultat_text_element_touple=(By.ID, "title")
    trazeni_rezultat_text_element=wait.until(EC.visibility_of_element_located(trazeni_rezultat_text_element_touple))
    trazeni_rezultat = trazeni_rezultat_text_element.text

    assert trazeni_rezultat == 'Traženi rezultati: kolica'


    
