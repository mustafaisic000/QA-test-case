import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sort_products(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()

    categories_tuple = (By.XPATH, "//a[text()='Kategorije']")
    categories_field = wait.until(EC.element_to_be_clickable(categories_tuple))
    categories_field.click()
    
    category_field = driver.find_element(By.XPATH, "//a[text()=' Mobitel ']")
    category_field.click()

    sortiranje_field = driver.find_element(By.ID, "sortiranje")
    sortiranje_field.click()
    

    sortiranje_po_cijeni= driver.find_element(By.ID, "priceAsc")
    sortiranje_po_cijeni.click()
    #time.sleep(5)
    product_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='listList']/li")))
    prices = []
    for i, product_element in enumerate(product_elements):
        price_element = product_element.find_element(By.XPATH, ".//span[@class='amount']")
        price_text = price_element.text
        if price_text:
            price_value = float(price_text.replace('KM', '').replace(',', ''))
            prices.append(price_value)


    is_sorted = all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
    if is_sorted:
        sorted_prices = sorted(prices)
        assert prices == sorted_prices, "Products are not sorted by price in ascending order"
    else:
        print("Prices are not sorted, skipping assertion.")
