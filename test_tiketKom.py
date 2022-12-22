from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

driver = webdriver.Edge()

def test_login():
    driver.get("https://www.tiket.com")
    driver.maximize_window()
    assert "tiket.com - Satu Aplikasi untuk Kebutuhan Liburanmu" in driver.title
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "Masuk").click()
    driver.find_element(By.ID, value="nomor-ponsel-atau-email").send_keys("arisadeline72@gmail.com")
    driver.find_element(By.XPATH, value="//button[@class='KV-nSG_button KV-nSG_full_width KV-nSG_horizontal_padding KV-nSG_variant_primary']").click()
    driver.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Traine123")
    driver.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
    time.sleep(5)
    try:
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#modal-root > div"))
        )
        time.sleep(60)
    finally:
        assert "tiket.com - Satu Aplikasi untuk Kebutuhan Liburanmu" in driver.title
        time.sleep(10)
        driver.quit()