import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_incorrect_login(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://onlineshop.ba/")
    driver.maximize_window()

    cookie_consent_button = driver.find_element(By.CLASS_NAME, 'pjAcceptCookieBarBtn')
    cookie_consent_button.click()

    login_link = driver.find_element(By.LINK_TEXT, "Prijava")
    login_link.click()

    username_field_tuple = (By.ID, "Email")
    username_field = wait.until(EC.element_to_be_clickable(username_field_tuple))
    username_field.click()
    username_field.clear()
    username_field.send_keys("neispravanemail@example.com")  # Unesite neispravne podatke za prijavu

    lozinka_field = driver.find_element(By.ID, "Lozinka")
    lozinka_field.click()
    lozinka_field.clear()
    lozinka_field.send_keys("neispravnaLozinka")

    loginButton = driver.find_element(By.XPATH, "//input[@value='Login' and @class='woocommerce-Button button']")
    loginButton.click()

    # Pričekajte da se prikaže poruka o neispravnim prijavnim podacima
    neispravna_prijava_text_element_touple = (By.XPATH, "//div[@class='text-danger']")
    neispravna_prijava_element = wait.until(EC.visibility_of_element_located(neispravna_prijava_text_element_touple))

    # Provjerite je li prikazani tekst točan
    neispravna_prijava_text = neispravna_prijava_element.text.strip()
    assert neispravna_prijava_text == "Login podaci netačni ili nepotpuni"
