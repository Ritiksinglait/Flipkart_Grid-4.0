import selenium
from selenium import webdriver as wb
import pandas as pd

def get_flipkart():
	webD = wb.Chrome("D:/User Files/Programming/Flipkart GRID/chromedriver.exe")
	cat = [
		"Men's Topwear", "Men's Bottomwear", "Men's Footwear", "Men's Sportswear",
		"Women's Topwear", "Women's Bottomwear", "Women's Partywear", "Women's Sportswear",
		"Kid's Topwear", "Kid's Bottomwear", "Kid's Footwear", "Kid's Partywear"
	]
	urls = [
		"https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=nmenu_sub_Men_0_Top%20wear",

		"https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo%2Cvua&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=nmenu_sub_Men_0_Bottom%20wear",

		"https://www.flipkart.com/mens-footwear/pr?sid=osp,cil&otracker=nmenu_sub_Men_0_Footwear",

		"https://www.flipkart.com/clothing-and-accessories/tracksuits/pr?sid=clo,nyk&otracker=categorytree",

		"https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DWomen&p[]=facets.ideal_for%255B%255D%3Dwomen&otracker=categorytree&otracker=nmenu_sub_Women_0_Topwear",

		"https://www.flipkart.com/clothing-and-accessories/bottomwear/~cs-g50m8job1g/pr?sid=clo%2Cvua&collection-tab-name=Trousers%20and%20Capris&otracker=nmenu_sub_Women_0_Trousers%20%26%20Capris",

		"https://www.flipkart.com/clothing-and-accessories/dresses-and-gown/dress/women-dress/pr?sid=clo%2Codx%2Cmaj%2Cjhy&otracker=categorytree&p%5B%5D=facets.occasion%255B%255D%3DParty&otracker=nmenu_sub_Women_0_Party%20Dresses",

		"https://www.flipkart.com/clothing-and-accessories/~cs-xy1011hvj1/pr?sid=clo&collection-tab-name=Sports%20and%20Gym%20Wear&otracker=nmenu_sub_Women_0_Sports%20Wear",

		"https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/pr?sid=clo%2Cash%2Cank&p%5B%5D=facets.ideal_for%255B%255D%3DBoys&otracker=categorytree&otracker=nmenu_sub_Baby+%26+Kids_0_T-Shirts&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBaby%2BBoys%2B%2526%2BBaby%2BGirls",

		"https://www.flipkart.com/clothing-and-accessories/bottomwear/shorts/pr?sid=clo%2Cvua%2Ce8g&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&otracker=categorytree&otracker=nmenu_sub_Baby+%26+Kids_0_Shorts&p%5B%5D=facets.ideal_for%255B%255D%3DBaby%2BBoys%2B%2526%2BBaby%2BGirls",

		"https://flipkart.com/footwear/kids-infant-footwear/boys-footwear/sandals/pr?sid=osp,mba,o3t,wqv&otracker=categorytree&otracker=nmenu_sub_Baby%20%26%20Kids_0_Sandals",

		"https://www.flipkart.com/clothing-and-accessories/kurtas-ethnic-sets-and-bottoms/pr?sid=clo%2Ccfv&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DBoys&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBaby%2BBoys%2B%2526%2BBaby%2BGirls&otracker=nmenu_sub_Baby%20%26%20Kids_0_Ethnic%20Wear"


	]


	names = []
	ratings = []
	no_revs_list = []
	img_links = []
	categories = []

	for u in range(12):
		webD.get(urls[u])
		links = []

		count = 1
		while(count < 2):
			productInfoList = webD.find_elements_by_class_name('_2UzuFa')
			for el in productInfoList:
				link = el.get_attribute("href")
				links.append(link)
				
			next_page = webD.find_elements_by_class_name("ge-49M")[count]
			webD.get(next_page.get_attribute("href"))
			count += 1

		print(len(links))
		i = 1
		for link in links:
			try:
				webD.get(link[:100])
				name = webD.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]').text
				rating = webD.find_elements_by_class_name('_3LWZlK')[0].text
				no_revs = webD.find_elements_by_class_name('_2_R_DZ')[0].text
				no_revs = no_revs.split()[0]
				img_link = webD.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/img').get_attribute("src")
				names.append(name)
				categories.append(cat[u])
				ratings.append(rating)
				no_revs_list.append(no_revs)
				img_links.append(img_link)
				print ("*")
			except:
				pass
			# 	try:
			# 	    name = webD.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]').text
			# 		rating = webD.find_elements_by_class_name('_3LWZlK')[0].text
			# 		no_revs = webD.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div/span[2]/span').text
			# 		no_revs = no_revs.split()[0]
			# 		img_link = webD.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/img').get_attribute("src")
			# 	    names.append(name)
			# 	    ratings.append(rating)
			# 	    no_revs_list.append(no_revs)
			# 	    img_links.append(img_link)
			# 	except:
			# 	    pass
			print(i)
			i += 1

	df_flipkart = pd.DataFrame(columns=["name", "category", "rating", "no_of_reviews", "img_links"])
	df_flipkart["name"] = names
	df_flipkart["category"] = categories
	df_flipkart["rating"] = ratings
	df_flipkart["no_of_reviews"] = no_revs_list
	df_flipkart["img_links"] = img_links

	df_flipkart.to_csv("df_flipkart.csv")

	webD.quit()
	

def get_vogue():
	webD = wb.Chrome()
	webD.get("https://www.vogue.in/vogue-closet/?closet=vogue_closet&filter_type=product_collection&order_by=recent&q=t+shirt&celebrity=&occasion=&price=&product-type=clothing")

	img_links = []
	i = 0
	while(i < 75):
		try:
		    productInfoList = webD.find_elements_by_class_name("product-wrapper")
		    for el in productInfoList:
		        pp1 = el.find_element_by_tag_name("a")
		        pp2 = pp1.find_element_by_tag_name("img")
		        img_links.append(pp2.get_property("src"))
		    page_nav = webD.find_element_by_class_name("pagination")
		    butts = page_nav.find_elements_by_tag_name("a")[-1]
		    butts.click()
		except:
		    pass
		i += 1


	df_vogue = pd.DataFrame(columns=["img_links"])
	df_vogue["img_links"] = img_links

	df_vogue.to_csv("df_vogue.csv")


	

def get_myntra():
	webD = wb.Chrome()
	webD.get("https://www.myntra.com/tshirts")

	links = []
	i = 0
	while(i < 40):
		try:
		    productInfoList = webD.find_elements_by_class_name("product-base")
		    for el in productInfoList:
		        pp1 = el.find_element_by_tag_name("a")
		        links.append(pp1.get_attribute("href"))
		    nav = webD.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul")
		    butt = nav.find_elements_by_tag_name("li")[-1]
		    butt_anc = butt.find_element_by_tag_name("a")
		    butt_anc.click()
		except:
		    pass
		i += 1

	img_links = []
	for link in links:
		webD.get(link)
		try:
		    img_l = webD.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[1]/div[1]/div/div[1]").get_attribute("style")[23:-3]
		    img_links.append(img_l)
		except:
		    pass

	df_myntra = pd.DataFrame(columns=["img_links"])
	df_myntra["img_links"] = img_links

	df_myntra.to_csv("df_myntra.csv")


get_flipkart()
#get_myntra()
# get_vogue()
