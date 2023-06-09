from selenium import webdriver
from csv import writer
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\webdivers\chromedriver.exe")

driver.get('https://www.trendyol.com/sr/?mid=147182&sst=SCORE&wc=1181&os=1&pi=2')

with open('trendyol.csv', 'w', encoding='utf-8') as trendyol_csv:
    csv_writer = writer(trendyol_csv)
    csv_writer.writerow(['name','ratingcount', 'price', 'kupon'])

    
    hats = driver.find_elements(By.CLASS_NAME, 'product-down')
    for hat in hats:
            name = hat.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
            ratingcount = hat.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
            price = hat.find_element(By.CLASS_NAME, 'ratingCount').text
            kupon = hat.find_element(By.CLASS_NAME, 'prc-box-dscntd').text

            csv_writer.writerow([name, ratingcount, price, kupon])

driver.quit()


    