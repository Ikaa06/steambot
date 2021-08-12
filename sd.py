posts = driver.find_elements_by_xpath('/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[2]/user-side/div/user-inventory/assets-card-scroll/div/div/asset-card')
print('Хохраниение товара')
# создание списка товаров
alt_spisok = []
for i in posts:
	img = i.find_element_by_class_name('c-asset__img').get_attribute('alt')
	alt_spisok.append(img)
# цикл по товару 
for i in alt_spisok:
	# определение повара
	poisk = './/asset-card//img[@alt="{}"]/ancestor::asset-card'.format(i)
	# print(poisk)
	post = driver.find_element_by_xpath(poisk)
	# имя товара
	img = i
	# статус товара
	t = post.find_element_by_class_name('c-asset__status').text
	# цена товара
	f = post.find_element_by_class_name('c-asset__priceNumber').text
	# подробная информация о товаре
	# time.sleep(4)
	btn = post.find_element_by_class_name('c-asset__action').click()
	# проверка товара на наличее в базе данных 
	time.sleep(5)
	# print(type(img),type(account))
	test = proverka_tovarov(img,account)
	# Условие проверки при значании False

	if not test:
		# получение списка пораметров товара
		time.sleep(5)
		text = driver.find_elements_by_class_name('c-dialogAsset__paramValue')
		data = []
		for tx in text:
			data.append(tx.text)
		print('not')
		data = data[2:-1]
		# сохранение товара
		save_user(account,t,f,img,data)
		# проверка на одинаковый товар 
		sferka(account,img,t)
		# возврат данных о товаре
		
	else:
		time.sleep(5)
		text = driver.find_elements_by_class_name('c-dialogAsset__paramValue')
		data = []
		for tx in text:
			data.append(tx.text)
		print('yes')
		data = data[2:-1]
		# обновление данных о товаре 
		updata(account,img,t,data,f)
		# проверка на одинаковый товар
		sferka(account,img,t)
	# выход
	btn = driver.find_element_by_class_name('c-dialog__button').click()
	time.sleep(5)
input('Нажмите интер')