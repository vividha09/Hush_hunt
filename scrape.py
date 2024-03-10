from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_chrome():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"  # Adjust this path
    service = Service(executable_path=PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def find_product_asin(driver, product_name):
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)
    first_product_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")))
    product_url = first_product_link.get_attribute('href')
    driver.get(product_url)
    time.sleep(2)
    asin = driver.current_url.split('/dp/')[1].split('/')[0]
    return asin

def scrape_reviews(driver, asin):
    url = f'https://www.amazon.in/dp/product-reviews/{asin}?reviewerType=all_reviews'
    driver.get(url)
    time.sleep(2)
    reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')
    for review in reviews:
        reviewer_name = review.find_element(By.XPATH, './/span[contains(@class,"a-profile-name")]').text
        rating = review.find_element(By.XPATH, './/i[contains(@class, "review-rating")]/span').get_attribute('innerText').strip()
        title = review.find_element(By.XPATH, './/a[@data-hook="review-title"]/span').text
        review_date = review.find_element(By.XPATH, './/span[@data-hook="review-date"]').text
        review_text = review.find_element(By.XPATH, './/span[@data-hook="review-body"]/span').text
        print(f"Reviewer: {reviewer_name}")
        print(f"Rating: {rating}")
        print(f"Title: {title}")
        print(f"Date: {review_date}")
        print(f"Review: {review_text}\n")
        print("------------------------------------------------------------")

def main():
    product_name = input("Enter the product name you want to search on Amazon: ")
    driver = setup_chrome()
    try:
        asin = find_product_asin(driver, product_name)
        print(f"Found ASIN for '{product_name}': {asin}")
        scrape_reviews(driver, asin)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()