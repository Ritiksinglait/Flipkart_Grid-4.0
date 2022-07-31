import selenium
from selenium import webdriver as wb
webD = wb.Chrome("D:/User Files/Programming/Flipkart GRID/chromedriver.exe")
webD.get("https://www.amazon.in/s?k=t-shirts&i=apparel&bbn=1968123031&rh=n%3A1968120031%2Cn%3A1968123031%2Cp_72%3A1318479031&dc&qid=1596720041&rnid=1318475031&ref=sr_nr_p_72_4")

count = 1
links = []
import time
while(count < 2 and len(links) < 100):
    productInfoList = webD.find_elements_by_class_name("s-image-padding")
    for el in productInfoList:
        pp1 = el.find_element_by_tag_name("span")
        pp2 = pp1.find_element_by_tag_name("a")
        links.append(pp2.get_property("href"))
    try:
        temp = webD.find_element_by_class_name("a-pagination")
        butt = temp.find_elements_by_tag_name("li")[-1]
        butt.find_element_by_tag_name("a").click()
    except:
        pass
    time.sleep(2)
    count += 1

names = []
ratings = []
no_revs_list = []
img_links = []

print (len(links))
i = 1
for link in links[:100]:
    webD.get(link)
    time.sleep(3)
    try:
        name = webD.find_element_by_xpath("//*[@id='productTitle']").text
        rating = webD.find_element_by_xpath("//*[@id='acrPopover']/span[1]/a/i[1]/span").get_attribute("innerHTML")
        img_link = webD.find_element_by_xpath("//*[@id='landingImage']").get_attribute("src")
        no_revs = webD.find_element_by_xpath("//*[@id='acrCustomerReviewText']").text
        names.append(name)
        ratings.append(rating)
        no_revs_list.append(no_revs)
        img_links.append(img_link)
    except:
        try:
            name = webD.find_element_by_xpath("//*[@id='productTitle']").text
            rating = webD.find_element_by_xpath("//*[@id='acrPopover']/span[1]/a/i[1]/span").get_attribute("innerHTML")
            img_link = webD.find_element_by_xpath("//*[@id='landingImage']").get_attribute("src")
            no_revs = webD.find_element_by_xpath("//*[@id='acrCustomerReviewText']").text
            names.append(name)
            ratings.append(rating)
            no_revs_list.append(no_revs)
            img_links.append(img_link)
        except:
            pass
    print(i)
    i += 1
                     

import pandas as pd
df_amazon = pd.DataFrame(columns=["name", "rating", "no_of_reviews", "img_links"])
df_amazon["name"] = names
df_amazon["rating"] = ratings
df_amazon["no_of_reviews"] = no_revs_list
df_amazon["img_links"] = img_links

df_amazon.to_csv("./df_amazon.csv")       

webD.quit()