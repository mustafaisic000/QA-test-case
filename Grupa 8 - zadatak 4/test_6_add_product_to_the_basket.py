import time #implicitni wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_the_basket(driver):
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
    product_in_basket_touple=(By.XPATH, "//tr[@class='cart_item']//td[@class='product-name']")
    product_in_basket_element=wait.until(EC.visibility_of_element_located(product_in_basket_touple))
    product_text = product_in_basket_element.text
    
    assert product_text=="KOLICA CLASSIC SET ZOOMIX KNORR BABY"
  