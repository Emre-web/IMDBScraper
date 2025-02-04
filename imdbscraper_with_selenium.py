from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep  # for waiting
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
import openpyxl
from selenium.common.exceptions import NoSuchElementException, TimeoutException

movie_dict = {
    'name': [],
    'year': [],
    'duration': [],
    'stars': [],
    'votes': [],
    'metascrore': [],
    'description': [],
}


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

    try:
        # Açılır menünün zaten açık olup olmadığını kontrol et
        menu_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "awards-section")]')  # Menü açık mı kontrol et

        if menu_elements:
            print("Menü zaten açık, tekrar tıklamaya gerek yok.")
        else:
            print("Menü kapalı, açıyorum...")
            awards_recog = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Awards & recognition"]')))

            # Menü butonu sayfanın dışında olabilir, önce sayfayı kaydır
            driver.execute_script("arguments[0].scrollIntoView(true);", awards_recog)
            sleep(1)  # Kaydırma sonrası bekleme

            awards_recog.click()
            sleep(2)  # Menü açılması için bekleme
            print("Awards & recognition butonu açıldı.")

        # Menü kapanmaması için ek önlem
        sleep(1)

        # Ardından "Oscar Nominated" butonunu tıkla
        oscar_nominated = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="test-chip-id-oscar-nominated"]')))

        # Eğer buton görünmüyorsa, sayfayı kaydır
        driver.execute_script("arguments[0].scrollIntoView(true);", oscar_nominated)
        sleep(1)  # Kaydırma sonrası bekleme

        # Buton tıklanamazsa JavaScript ile tıklama
        driver.execute_script("arguments[0].click();", oscar_nominated)
        print("Oscar Nominated butonuna tıklandı.")

    except NoSuchElementException:
        print("Öğe bulunamadı, sayfa yapısı değişmiş olabilir.")

    except TimeoutException:
        print("Öğe zamanında yüklenmedi veya buton tıklanabilir değil.")



# WebDriverWait ile tıklanabilir olana kadar bekle
see_results = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="adv-search-get-results"]')))
print("See Results butonu görünür, fareyi hareket ettirip tıklanıyor.")

# Scroll yaparak öğeyi görünür kıl
driver.execute_script("arguments[0].scrollIntoView(true);", see_results)

# ActionChain ile öğeye hareket et ve tıkla
actions.move_to_element(see_results).perform()

# Bekleme sonrası tıklama
see_results.click()


while True:
    sleep(2)
    more_buttons = driver.find_elements(By.CSS_SELECTOR, 'span.ipc-see-more__text')

    if not more_buttons:  # Eğer hiç buton yoksa çık
        break

    try:
        more_button = more_buttons[0]
        actions.move_to_element(more_button).perform()  # Scroll yaparak öğeyi görünür kıl
        more_button.click()
    except Exception as e:
        print(f"More butonu tıklanamadı: {e}")
        break  # Sonsuz döngüye girmemesi için çık

# Film listesi boşsa, verileri eklemeye çalışma
movies = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
if not movies:
    print("Film listesi boş, veri eklenmeyecek!")
    driver.quit()  # Tarayıcıyı kapat
    exit()

for movie in movies:
    try:
        raw_name = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
        name = ' '.join(raw_name.split(' ')[1:])
        print(name)
        movie_dict['name'].append(name)

        year = movie.find_elements(By.CSS_SELECTOR, 'span.dli-title-metadata-item')[0].text
        print(year)
        movie_dict['year'].append(year)

        duration = movie.find_elements(By.CSS_SELECTOR, 'span.dli-title-metadata-item')[1].text
        print(duration)
        movie_dict['duration'].append(duration)

        stars = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
        print(stars)
        movie_dict['stars'].append(stars)

        votes = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--voteCount').text.strip()[1:-1]
        print(votes)
        movie_dict['votes'].append(votes)

        try:
            metascore = movie.find_element(By.CSS_SELECTOR, 'span.metacritic-score-box').text
        except:
            metascore = 'Not found Metascore'
        
        print(metascore)
        movie_dict['metascrore'].append(metascore)

        description = movie.find_element(By.CSS_SELECTOR, 'div.ipc-html-content-inner-div').text
        print(description)
        movie_dict['description'].append(description)
        print('\n')

    except Exception as e:
        print(f"Hata oluştu: {e}")
        continue  # Hata oluşursa döngüyü atla

# Eksik verileri tamamlamak için boş değerler ekleme
max_length = max(map(len, movie_dict.values()))

for key in movie_dict:
    while len(movie_dict[key]) < max_length:
        movie_dict[key].append("N/A")

df = pd.DataFrame(movie_dict)
df.to_excel('movies.xlsx', index=False)  # Excel'e yazarken index olmadan kaydet

print("Veriler başarıyla kaydedildi.")

input("Press Enter to close the browser...")
driver.quit()  # Tarayıcıyı kapat
