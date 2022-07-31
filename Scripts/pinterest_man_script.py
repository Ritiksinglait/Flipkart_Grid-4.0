from time import sleep
import selenium
from selenium import webdriver as wb
webD = wb.Chrome("./chromedriver.exe")
webD.get("https://www.pinterest.com/Marcellthekid/men-fashion-catalog/")

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
        pp2 = el.find_element_by_xpath('//*[@id="boardfeed:442408432084140808"]/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img')
        img_links.append(pp2.get_attribute("src"))
        print(i)
        i += 1

import pandas as pd
df_pintrest_men = pd.DataFrame(columns=["img_links"])
df_pintrest_men["img_links"] = img_links

df_pintrest_men.to_csv("./df_pintrest_men.csv")

webD.quit()
