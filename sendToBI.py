# import requests
# import time
# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def setup_chrome():
#     chrome_options = Options()
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#     PATH = "C:\\Program Files (x86)\\chromedriver.exe"  # Adjust this path
#     service = Service(executable_path=PATH)
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     return driver

# def find_product_details(driver, product_name):
#     driver.get("https://www.amazon.in")
#     search_box = driver.find_element(By.ID, "twotabsearchtextbox")
#     search_box.send_keys(product_name)
#     search_box.send_keys(Keys.RETURN)
#     first_product_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")))
#     product_url = first_product_link.get_attribute('href')
#     driver.get(product_url)
#     time.sleep(5)
#     asin = driver.current_url.split('/dp/')[1].split('/')[0]

#     try:
#         global_ratings_element = driver.find_element(By.ID, "acrCustomerReviewText")
#         # Convert global ratings from string to a number
#         global_ratings = int(global_ratings_element.text.split(' ')[0].replace(',', ''))
#     except Exception as e:
#         print("Could not extract global ratings:", e)
#         global_ratings = None

#     return asin, global_ratings

# def scrape_reviews_and_send_to_powerbi(driver, asin, global_ratings):
#     url = f'https://www.amazon.in/dp/product-reviews/{asin}?reviewerType=all_reviews'
#     driver.get(url)
#     time.sleep(2)
#     reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')
#     review_data = []
#     for review in reviews:
#         reviewer_name = review.find_element(By.XPATH, './/span[contains(@class,"a-profile-name")]').text
#         rating_text = review.find_element(By.XPATH, './/i[contains(@class, "review-rating")]/span').get_attribute('innerText').strip()
#         # Extract numeric rating value
#         rating = float(rating_text.split(' out of')[0])
#         review_date_text = review.find_element(By.XPATH, './/span[@data-hook="review-date"]').text
#         # Convert review date to datetime object
#         review_date = datetime.strptime(review_date_text, 'Reviewed in India on %d %B %Y').strftime('%Y-%m-%d')
#         review_text = review.find_element(By.XPATH, './/span[@data-hook="review-body"]/span').text

#         review_data.append({
#             "Reviewer": reviewer_name,
#             "Rating": rating,
#             "Date": review_date,
#             "Review": review_text,
#             "Website": "Amazon",
#             "GlobalRatings": global_ratings
#         })

#     powerbi_url = "https://api.powerbi.com/beta/d1f14348-f1b5-4a09-ac99-7ebf213cbc81/datasets/e24712a9-9947-4d6c-ba8a-654fc82005f7/rows?experience=power-bi&key=s6Le1jmcE%2BFf1augaQrRKgtwjV8ElNT1VWV6PoN7ufZGcdRuHOYEz9n7QQbG5l6QylcpIBHiCddKtYF4JVFktA%3D%3D"
#     response = requests.post(powerbi_url, json=review_data)
#     if response.status_code in [200, 201]:
#         print("Data sent to Power BI successfully.")
#     else:
#         print(f"Failed to send data to Power BI. Status code: {response.status_code}, Response: {response.text}")

# def main():
#     product_name = input("Enter the product name you want to search on Amazon: ")
#     driver = setup_chrome()
#     try:
#         asin, global_ratings = find_product_details(driver, product_name)
#         print(f"Found ASIN for '{product_name}': {asin}, Global Ratings: {global_ratings}")
#         scrape_reviews_and_send_to_powerbi(driver, asin, global_ratings)
#     finally:
#         driver.quit()

# if _name_ == "_main_":
#     main()
import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_chrome():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    service = Service(executable_path=PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def find_product_details(driver, product_name):
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)
    first_product_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")))
    product_url = first_product_link.get_attribute('href')
    driver.get(product_url)
    time.sleep(5)
    asin = driver.current_url.split('/dp/')[1].split('/')[0]

    try:
        global_ratings_element = driver.find_element(By.ID, "acrCustomerReviewText")
        global_ratings = int(global_ratings_element.text.split(' ')[0].replace(',', ''))
    except Exception as e:
        print("Could not extract global ratings:", e)
        global_ratings = None

    return asin, global_ratings

def scrape_reviews_and_send_to_powerbi(driver, asin, global_ratings):
    url = f'https://www.amazon.in/dp/product-reviews/{asin}?reviewerType=all_reviews'
    driver.get(url)
    time.sleep(2)
    reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')
    review_data = []
    for review in reviews:
        reviewer_name = review.find_element(By.XPATH, './/span[contains(@class,"a-profile-name")]').text
        rating_text = review.find_element(By.XPATH, './/i[contains(@class, "review-rating")]/span').get_attribute('innerText').strip()
        rating = float(rating_text.split(' out of')[0])
        review_date_text = review.find_element(By.XPATH, './/span[@data-hook="review-date"]').text
        review_date = datetime.strptime(review_date_text, 'Reviewed in India on %d %B %Y').strftime('%Y-%m-%d')
        review_text = review.find_element(By.XPATH, './/span[@data-hook="review-body"]/span').text

        review_data.append({
            "Reviewer": reviewer_name,
            "Rating": rating,
            "Date": review_date,
            "Review": review_text,
            "Website": "Amazon",
            "GlobalRatings": global_ratings
        })

    powerbi_url = "https://api.powerbi.com/beta/d1f14348-f1b5-4a09-ac99-7ebf213cbc81/datasets/e24712a9-9947-4d6c-ba8a-654fc82005f7/rows?experience=power-bi&accessrequestuseroid=d2337c9e-ede6-4f98-8db6-f2e213340601&key=s6Le1jmcE%2BFf1augaQrRKgtwjV8ElNT1VWV6PoN7ufZGcdRuHOYEz9n7QQbG5l6QylcpIBHiCddKtYF4JVFktA%3D%3D"
    response = requests.post(powerbi_url, json=review_data)
    if response.status_code in [200, 201]:
        print("Data sent to Power BI successfully.")
    else:
        print(f"Failed to send data to Power BI. Status code: {response.status_code}, Response: {response.text}")

def scrape_and_send_to_powerbi(product_name):
    driver = setup_chrome()
    try:
        asin, global_ratings = find_product_details(driver, product_name)
        print(f"Found ASIN for '{product_name}': {asin}, Global Ratings: {global_ratings}")
        scrape_reviews_and_send_to_powerbi(driver, asin, global_ratings)
    finally:
        driver.quit()
