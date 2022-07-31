from time import sleep
import selenium
from selenium import webdriver as wb
webD = wb.Chrome()
webD.get("https://www.pinterest.com/Kuricho/womens-t-shirts/")

img_links = []
print("Please scroll down as far as possible for 20 seconds")
for k in range(5):
    for j in range(5):
        webD.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

    productInfoList = webD.find_elements_by_class_name("Hb7")

    print ("*******\n", len(productInfoList))
    i = 1
    for el in productInfoList:
        pp2 = el.find_element_by_xpath('//*[@id="boardfeed:72902156407083261"]/div/div[1]/div[3]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img')
        img_links.append(pp2.get_attribute("src"))
        print(i)
        i += 1

import pandas as pd
df_pinterest_women = pd.DataFrame(columns=["img_links"])
df_pinterest_women["img_links"] = img_links
df_pinterest_women

df_pinterest_women.to_csv("df_pinterest_women.csv")