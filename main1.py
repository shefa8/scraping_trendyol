from selenium import webdriver
from csv import writer
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\webdivers\chromedriver.exe")

driver.get('https://www.trendyol.com/sr/?mid=147182&sst=SCORE&wc=1181&os=1&pi=2')

items = []

last_height = driver.execute_script('return document.body.scrollHeight')

itemTargetCount = 100                                   
                                    
with open('trendyol.csv', 'w', encoding='utf-8') as trendyol_csv:
    csv_writer = writer(trendyol_csv)
    csv_writer.writerow(['name','ratingcount', 'price', 'kupon'])

    while itemTargetCount > len(items):
        driver.execute_script('window.scroll(0, document.body.scrollHeight);')

        time.sleep(1)

        new_height = driver.execute_script('returndocument.body.scrollHeight')

        if new_height == last_height:
            break

        last_height = new_height

        hats = driver.find_elements(By.CLASS_NAME, 'product-down')
        textHats = []
        for hat in hats:
            textHats.append(hat.text)

            name = hat.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
            ratingcount = hat.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
            price = hat.find_element(By.CLASS_NAME, 'ratingCount').text
            kupon = hat.find_element(By.CLASS_NAME, 'prc-box-dscntd').text

            csv_writer.writerow([name, ratingcount, price, kupon])

            textHats.append({
                name:name,
                ratingcount:ratingcount,
                price:price,
                kupon:kupon
            })

        items = textHats
print(items)



            

        

                
    

    
           
          
          
          

