# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def get_xerve_product_details(user_search_term):
#     """
#     Fetches product information from Xerve based on the user's search term.

#     Args:
#         user_search_term (str): Search term input by the user.

#     Returns:
#         list: A list of dictionaries. Each dictionary contains details of a product such as name, image URL, and prices from various sellers.
#     """
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Runs Chrome in headless mode

#     service = Service(ChromeDriverManager().install())  # Manages ChromeDriver installation/update
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         url = f"https://www.xerve.in/prices?q={user_search_term}"
#         driver.get(url)

#         products = driver.find_elements(By.CSS_SELECTOR, "._tile_container")
        
#         product_list = []  # This will store the product details as a list of dictionaries
#         for product in products:
#             # Extracting product details
#             product_name = product.find_element(By.CSS_SELECTOR, "h3.I-name__heading").text
#             product_image = product.find_element(By.CSS_SELECTOR, "div.St-Img-M > img").get_attribute("src")
            
#             # Extracting price information for each seller
#             price_details = []
#             price_containers = product.find_elements(By.CSS_SELECTOR, "span.I-name__range.col_3.compcontainer")
#             for container in price_containers:
#                 seller_logo = container.find_element(By.CSS_SELECTOR, "span.__sellerlogo > img").get_attribute("data-src")
#                 price_text = container.find_element(By.TAG_NAME, "h4").text
#                 try:
#                     discount_text = container.find_element(By.CLASS_NAME, "_extradiscount").text
#                 except:
#                     discount_text = None  # No discount found
                
#                 price_details.append({
#                     "seller_logo": seller_logo,
#                     "price": price_text,
#                     "discount": discount_text,
#                 })

#             # Appending product details to the product_list
#             product_list.append({
#                 "name": product_name,
#                 "image": product_image,
#                 "prices": price_details,
#             })

#         return product_list
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     user_search_term = input("Enter your search term for Xerve: ")
#     product_details = get_xerve_product_details(user_search_term)
#     print("Extracted product details from Xerve:")
#     for product in product_details:
#         print(product)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_xerve_product_details(user_search_term):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = f"https://www.xerve.in/prices?q={user_search_term}"
        driver.get(url)

        last_count = 0
        stable_checks = 0
        while stable_checks < 3:
            current_count = len(driver.find_elements(By.XPATH, "//img[contains(@src, 'seller_logos') and not(contains(@src, 'rsz_blank_grey.jpg'))]"))
            if current_count == last_count:
                stable_checks += 1
            else:
                stable_checks = 0
                last_count = current_count
            time.sleep(2)

        products = driver.find_elements(By.CSS_SELECTOR, "._tile_container")
        product_list = []

        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, "h3.I-name__heading").text
            product_image = product.find_element(By.CSS_SELECTOR, "div.St-Img-M > img").get_attribute("src")
            price_details = []

            price_containers = product.find_elements(By.CSS_SELECTOR, "span.I-name__range.col_3.compcontainer")
            for container in price_containers:
                seller_logo = container.find_element(By.CSS_SELECTOR, "span.__sellerlogo > img").get_attribute("data-src")
                
                # Extracting price by searching within the span containing the price and discount
                price_element = container.find_element(By.CSS_SELECTOR, "span._split-comp > h4")
                price_text = price_element.text
                
                # Extracting discount using the 'xr_off' class for the discount percentage
                discount_elements = container.find_elements(By.CLASS_NAME, "xr_off")
                discount_text = discount_elements[0].text if discount_elements else None

                price_details.append({
                    "seller_logo": seller_logo,
                    "price": price_text,
                    "discount": discount_text,
                })

            product_list.append({
                "name": product_name,
                "image": product_image,
                "prices": price_details,
            })

        return product_list
    finally:
        driver.quit()

if __name__ == "__main__":
    user_search_term = input("Enter your search term for comparison: ")
    product_details = get_xerve_product_details(user_search_term)
    print("Extracted product details from Xerve:")
    for product in product_details:
        print(product)