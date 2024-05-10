from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remove_product_from_wishlist(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()

    categories_tuple = (By.XPATH, "//a[text()='Kategorije']")
    categories_field = wait.until(EC.element_to_be_clickable(categories_tuple))
    categories_field.click()
    
    category_field = driver.find_element(By.XPATH, "//a[text()=' Igračke ']")
    category_field.click()


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

    brisi_iz_liste_tuple = (By.CLASS_NAME, "deleteWL.delete.remove.remove_from_wishlist")
    brisi_iz_liste = wait.until(EC.element_to_be_clickable(brisi_iz_liste_tuple))
    brisi_iz_liste.click()

    text_in_list_touple = (By.CLASS_NAME, "lead-title.text-center.cart-empty")
    text_in_list_element = wait.until(EC.visibility_of_element_located(text_in_list_touple))
    list_text = text_in_list_element.text
    expected_text = "Vaša lista želja je trenutno prazna"
    assert list_text == expected_text


    
