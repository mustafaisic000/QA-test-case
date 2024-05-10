from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_correct_login(driver):
    wait=WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    login_link=driver.find_element(By.LINK_TEXT, "Prijava")
    login_link.click()

    username_field_tuple=(By.ID,"Email")
    username_field=wait.until(EC.element_to_be_clickable(username_field_tuple))
    username_field.click()
    username_field.clear()
    username_field.send_keys("testFm13@outlook.com")
    
    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()
    

    lozinka_field=driver.find_element(By.ID,"Lozinka")
    lozinka_field.click()
    lozinka_field.clear()
    lozinka_field.send_keys("testiranjestranice13")
     
    loginButton=driver.find_element(By.XPATH, "//input[@value='Login' and @class='woocommerce-Button button']")
    loginButton.click()
    
    dobrodosli_text_element_touple=(By.XPATH, "//li[contains(text(),'Dobro došli')]/a/b")
    dobrodosli_text_element=wait.until(EC.visibility_of_element_located(dobrodosli_text_element_touple))
    dobrodosli_text = dobrodosli_text_element.text

    assert dobrodosli_text=="testiranje"

    
 