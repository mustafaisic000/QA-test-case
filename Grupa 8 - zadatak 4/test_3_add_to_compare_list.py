from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_compare_list(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()

    categories_tuple = (By.XPATH, "//a[text()='Kategorije']")
    categories_field = wait.until(EC.element_to_be_clickable(categories_tuple))
    categories_field.click()

    category_field = driver.find_element(By.XPATH, "//a[text()=' Laptop ']")
    category_field.click()

    product_tuple = (By.XPATH, "//ul[@id='listList']/li[1]/div[@class='media']/div[@class='media-left']/a")
    product_field = wait.until(EC.element_to_be_clickable(product_tuple))
    product_field.click()

    add_product_tuple = (By.XPATH, "//div[@class='summary entry-summary']/div[@class='action-buttons']/a[@class='add-to-compare-link']")
    add_product_field = wait.until(EC.element_to_be_clickable(add_product_tuple))
    add_product_field.click()

    swal_tuple = (By.CLASS_NAME, 'swal2-container')
    wait.until(EC.visibility_of_element_located(swal_tuple))
    wait.until(EC.invisibility_of_element_located(swal_tuple))

    categories_tuple = driver.find_element(By.XPATH, "//a[text()='Kategorije']")
    categories_field = wait.until(EC.element_to_be_clickable(categories_tuple))
    categories_field.click()

    category_field = driver.find_element(By.XPATH, "//a[text()=' Laptop ']")
    category_field.click()


    product_tuple = (By.XPATH, "//ul[@id='listList']/li[2]/div[@class='media']/div[@class='media-left']/a")
    product_field = wait.until(EC.element_to_be_clickable(product_tuple))
    product_field.click()


    add_product_tuple = (By.XPATH, "//div[@class='summary entry-summary']/div[@class='action-buttons']/a[@class='add-to-compare-link']")
    add_product_field = wait.until(EC.element_to_be_clickable(add_product_tuple))
    add_product_field.click()

    swal_tuple = (By.CLASS_NAME, 'swal2-container')
    wait.until(EC.visibility_of_element_located(swal_tuple))
    wait.until(EC.invisibility_of_element_located(swal_tuple))

    search_button_tuple = driver.find_element(By.CLASS_NAME, "ec-compare")
    search_button = wait.until(EC.element_to_be_clickable(search_button_tuple))
    search_button.click()

    compare_product_element_touple=(By.XPATH, "//table[@class='table table-compare compare-list']/tbody/tr[1]/td[2]/a[@class='product']/div[@class='product-info']/h3")
    compare_product_text_element=wait.until(EC.visibility_of_element_located(compare_product_element_touple))
    compare_product_rezultat = compare_product_text_element.text

    assert compare_product_rezultat ==  "LAPTOP 15,6\" ASUS E510MA-EJ951W 8GB/256GB SSD 49882"

    compare_second_product_element_touple=(By.XPATH, "//table[@class='table table-compare compare-list']/tbody/tr[1]/td[2]/a[@class='product']/div[@class='product-info']/h3")
    compare_second_product_text_element=wait.until(EC.visibility_of_element_located(compare_second_product_element_touple))
    compare_second_product_rezultat = compare_second_product_text_element.text

    assert compare_second_product_rezultat ==  "LAPTOP 15,6\" ASUS E510MA-EJ951W 8GB/256GB SSD 49882"

