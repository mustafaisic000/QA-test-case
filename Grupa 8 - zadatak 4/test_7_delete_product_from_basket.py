import time #implicitni wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_product_to_the_basket(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()
 
    search_field_tuple = (By.ID, "search")
    search_field = wait.until(EC.element_to_be_clickable(search_field_tuple))
    search_field.click()
    search_field.clear()
    search_field.send_keys("kolica")
    search_button = driver.find_element(By.CLASS_NAME, "ec-search")
    search_button.click()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()
    
    product_item=driver.find_element(By.XPATH,"//h3[contains(text(), 'KOLICA CLASSIC SET ZOOMIX KNORR BABY')]")
    product_item.click()

    dodaj_u_korpu_button=driver.find_element(By.ID,"unos")
    dodaj_u_korpu_button.click()

    brisi_iz_korpe_tuple = (By.CLASS_NAME, "delete")
    brisi_iz_korpe=wait.until(EC.element_to_be_clickable(brisi_iz_korpe_tuple))
    brisi_iz_korpe.click()
    text_in_basket_touple = (By.CLASS_NAME, "lead-title.text-center.cart-empty")
    text_in_basket_element = wait.until(EC.visibility_of_element_located(text_in_basket_touple))
    basket_text = text_in_basket_element.text
    expected_text = "Vaša korpa je trenutno prazna"
    assert basket_text == expected_text
                                        

  