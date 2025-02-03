from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep  # for waiting
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def accept_cookies(the_driver):
    try:
        accept_cookies = the_driver.find_element(By.XPATH, "//button[text()='Accept']")
        accept_cookies.click()
    except:
        pass

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

actions = ActionChains(driver)
driver.implicitly_wait(6)

driver.get("https://www.imdb.com/")

sleep(2)

accept_cookies(driver) 

sleep(4)

driver.find_element(By.ID, 'suggestion-search-button').click()
sleep(2)

movies_tv = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="advanced-search-chip-tt"]')
movies_tv.click()
sleep(2)

wait = WebDriverWait(driver, 10)  # 10 saniyeye kadar bekle


try:
    # "Movie" butonu zaten görünüyorsa doğrudan tıkla
    movie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="test-chip-id-movie"]')))
    print("Movie butonu zaten açık, doğrudan tıklanıyor.")
    movie_button.click()
except:
    # Eğer "Movie" butonu görünmüyorsa, önce "Title type" butonuna tıkla
    print("Movie butonu açık değil, 'Title type' butonuna tıklanıyor.")
    title_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Title type"]')))
    title_type.click()
    sleep(2)

    # "Movie" butonu tekrar beklenip tıklanmalı
    movie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="test-chip-id-movie"]')))
    movie_button.click()

sleep(2)

try:
    # "Action" butonunu bekle
    action = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]')))
    print("Action butonu tıklanabilir durumda, tıklanıyor.")
    
    # JavaScript ile tıklama
    driver.execute_script("arguments[0].click();", action)
    
except Exception as e:
    print(f"Hata oluştu: {e}")
    print("Action butonu açık değil, önce Genre butonuna tıklanacak.")

    # "Genre" butonuna tıkla
    genre = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Genre"]')))
    genre.click()
    sleep(2)  # Menü açılması için bekle

    # "Action" butonunu JavaScript ile tıklama
    action = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]')))
    driver.execute_script("arguments[0].click();", action)

sleep(1)

try:
    # "Awards & recognition" butonunu bekle ve tıkla
    awards_recog = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Awards & recognition"]')))
    print("Awards & recognition butonu tıklanabilir, tıklanıyor.")
    awards_recog.click()

    # "Oscar Nominated" butonunu bekle ve tıkla
    oscar_nominated = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="test-chip-id-oscar-nominated"]')))
    print("Oscar Nominated butonu tıklanabilir, tıklanıyor.")
    oscar_nominated.click()

except Exception as e:
    print(f"Hata oluştu: {e}")
    print("Awards & recognition veya Oscar Nominated butonları açık değil, önce gerekli öğelere tıklanacak.")

    # Eğer butonlar görünmüyorsa, önce "Awards & recognition" butonuna tıkla
    awards_recog = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Awards & recognition"]')))
    awards_recog.click()
    sleep(2)  # Menü açılması için bekle

    # Ardından "Oscar Nominated" butonunu tıkla
    oscar_nominated = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="test-chip-id-oscar-nominated"]')))
    driver.execute_script("arguments[0].click();", oscar_nominated)


# WebDriverWait ile tıklanabilir olana kadar bekle
see_results = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="adv-search-get-results"]')))
print("See Results butonu görünür, fareyi hareket ettirip tıklanıyor.")

# Scroll yaparak öğeyi görünür kıl
driver.execute_script("arguments[0].scrollIntoView(true);", see_results)

# ActionChain ile öğeye hareket et ve tıkla
actions.move_to_element(see_results).perform()

# Bekleme sonrası tıklama
see_results.click()


input("Press Enter to continue...")