from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_wishlist(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()
 
    categories_tuple = (By.XPATH, "//a[text()='Kategorije']")
    categories_field = wait.until(EC.element_to_be_clickable(categories_tuple))
    categories_field.click()
    
    category_field = driver.find_element(By.XPATH, "//a[text()=' Igračke ']")
    category_field.click()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()

    product_tuple = (By.XPATH, "//ul[@id='listList']/li[1]/div[@class='media']/div[@class='media-left']/a")
    product_field = wait.until(EC.element_to_be_clickable(product_tuple))
    product_field.click()

    add_product_tuple = (By.XPATH, "//div[@class='summary entry-summary']/div[@class='action-buttons']/a[@class='add_to_wishlist']")
    add_product_field = wait.until(EC.element_to_be_clickable(add_product_tuple))
    add_product_field.click()

    swal_tuple = (By.CLASS_NAME, 'swal2-container')
    wait.until(EC.visibility_of_element_located(swal_tuple))
    wait.until(EC.invisibility_of_element_located(swal_tuple))

    search_button_tuple = driver.find_element(By.CLASS_NAME, "ec-favorites")
    search_button = wait.until(EC.element_to_be_clickable(search_button_tuple))
    search_button.click()

    wishlist_product_element_touple=(By.XPATH, "//tbody[@class='wishlist_body']/tr/td[@class='product-name']/a")
    wishlist_product_text_element=wait.until(EC.element_to_be_clickable(wishlist_product_element_touple))
    wishlist_product_rezultat = wishlist_product_text_element.text

    assert wishlist_product_rezultat == 'DRUŠTVENA IGRA MEMORING'

    
