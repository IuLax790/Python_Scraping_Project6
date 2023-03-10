from selenium import webdriver
from lxml import html
from time import sleep
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver")

for page_nb in range(0,21):
    driver.get('https://www.amazon.com/s?k=headphones&page={}'.format(page_nb))
    sleep(1)

    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('//div[contains(@data-cel-widget, "search_result_")]'):
        title = product_tree.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
        reviews = product_tree.xpath('.//span[@class="a-size-base s-underline-text"]/text()')
        price = product_tree.xpath('.//span[@class="a-offscreen"]/text()')
        print(title,reviews,price)
    print("\n\n\n\n\n\n")
driver.close()
