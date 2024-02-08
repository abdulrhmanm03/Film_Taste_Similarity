from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def scrap(username, q):
    ratings_map = {
        '½': 1,
        '★': 2,
        '★½': 3,
        '★★': 4,
        '★★½': 5,
        '★★★': 6,
        '★★★½': 7,
        '★★★★': 8,
        '★★★★½': 9,
        '★★★★★': 10
    }
    user = {}

    url = f"https://letterboxd.com/{username}/films"
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(20)

    def main(url):
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        span_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.poster-container')))
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
        for span_element in span_elements:
            child = span_element.find_element(By.CSS_SELECTOR, 'p.poster-viewingdata')
            if child.text:
                def func():
                    try:
                        return span_element.find_element(By.CSS_SELECTOR, 'div.poster').get_attribute('data-film-id')
                    except StaleElementReferenceException:
                        WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.poster')))
                        func()
                name = func()
                rating = span_element.find_element(By.CSS_SELECTOR, 'span.rating').text
            
                user[name] = ratings_map[rating]
            
            
    try:
        print(username + ' start')
        main(url=url)

        n = int(driver.find_elements(By.CSS_SELECTOR, 'li.paginate-page')[-1].find_element(By.CSS_SELECTOR, 'a').text)
        for i in range(2, n+1):
            print(username, i)
            url = f"https://letterboxd.com/{username}/films/page/{i}"
            main(url=url)       

               
    finally:
        driver.quit()
        print(username + ' done')
        if not user:
            q.put({0:0})
        q.put(user)

   

