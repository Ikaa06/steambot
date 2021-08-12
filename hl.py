while True:
    k = 0
    while True:

        try:
            posts = driver.find_elements_by_xpath(
                '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[2]/user-side/div/user-inventory/assets-card-scroll/div/div/asset-card')
            break
        except:
            if k == 0:
                driver.refresh()
                time.sleep(30)
                k += 1

            else:
                time.sleep(5)

    print(len(posts))
    alt_spisok = []
    for i in posts:
        # имя товара
        img = i.find_element_by_class_name('c-asset__img').get_attribute('alt')
        alt_spisok.append(img)
    for img in alt_spisok:
        # запрос к api
        url = f'https://api.dmarket.com/exchange/v1/target/advice-price/a8db?title={img}'
        while True:
            try:
                data_op = requests.get(url)
            except:
                time.sleep(60)
            if data_op.status_code == 200:
                break
        # даные о товаре на рынке
        data_op = data_op.json()
        data = op_tovar(data_op)

        poisk = './/asset-card//img[@alt="{}"]/ancestor::asset-card'.format(img)

        try:
            post = driver.find_element_by_xpath(poisk)
        except:
            try:
                time.sleep(2)
                driver.refresh()
                time.sleep(30)
                post = driver.find_element_by_xpath(poisk)
            except:
                driver.refresh()
                time.sleep(30)
                continue

        # статус товара
        try:
            t = post.find_element_by_class_name('c-asset__status').text
        except:
            time.sleep(2)
            driver.refresh()
            time.sleep(30)
            try:
                post = driver.find_element_by_xpath(poisk)
                t = post.find_element_by_class_name('c-asset__status').text
            except:
                driver.refresh()
                time.sleep(30)
                continue
        # цена товара
        try:
            f = post.find_element_by_class_name('c-asset__priceNumber').text
        except:
            time.sleep(5)
            try:

                f = post.find_element_by_class_name('c-asset__priceNumber').text
            except:
                try:
                    post = driver.find_element_by_xpath(poisk)
                    f = post.find_element_by_class_name('c-asset__priceNumber').text
                    driver.refresh()
                    time.sleep(30)
                except:
                    driver.refresh()
                    time.sleep(30)
                    continue
        test = proverka_tovarov(img, account)
        # Условие проверки при значании False
        if not test:
            # сохранение товара
            save_user(account, t, f, img, data)
        else:
            # обновление данных о товаре
            updata(account, img, t, data, f)
        # проверка на одинаковый товар
        sferka(account, img, t)
        test = proverka_tovarov(img, account)
        if test['zatype'] == '0':
            max_ranok = data[0]
            kolfek = float(test['kolfek'])
            kol = float(test['kol'])
            payself = float(test['payself'])
            f = float(f)
            paymin = float(test['paymin'])
            max_ranok = float(max_ranok)
            if f == max_ranok:
                # Вход в товар
                try:
                    btn = post.find_element_by_class_name('c-asset__action').click()
                    time.sleep(10)
                except:

                    driver.refresh()
                    time.sleep(30)
                    try:
                        post = driver.find_element_by_xpath(poisk)
                        btn = post.find_element_by_class_name('c-asset__action').click()
                    except:
                        driver.refresh()
                        time.sleep(20)
                        continue

                # вход и обновление товар до одного долора
                input_btn(driver, poisk)
                # update_tovar(img,account,max_ranok_2,int_f)
                time.sleep(10)
                try:
                    post = driver.find_element_by_xpath(poisk)
                except:
                    time.sleep(2)
                    driver.refresh()
                    time.sleep(20)
                    try:
                        post = driver.find_element_by_xpath(poisk)
                    except:
                        driver.refresh()
                        time.sleep(20)
                        continue
                while True:
                    data_op = requests.get(url)
                    if data_op.status_code == 200:
                        break
                # даные о товаре на рынке
                data_op = data_op.json()
                max_ranok_2 = op_tovar(data_op)
                max_ranok_2 = max_ranok_2[0]
                if f > max_ranok_2:
                    if max_ranok_2 < paymin and max_ranok_2 < kol:
                        # Вход в товар

                        try:
                            btn = post.find_element_by_class_name('c-asset__action').click()
                            time.sleep(10)
                        except:

                            driver.refresh()
                            time.sleep(50)
                            try:
                                post = driver.find_element_by_xpath(poisk)
                                btn = post.find_element_by_class_name('c-asset__action').click()
                            except:
                                driver.refresh()
                                time.sleep(20)
                                continue

                        time.sleep(10)
                        input_btn(driver, poisk, paymin)
                        update_tovar(img, account, max_ranok_2, f)
                        time.sleep(10)

                    elif max_ranok_2 >= paymin and max_ranok_2 < kol:
                        # while True:
                        # 	data_op = requests.get(url)
                        # 	if data_op.status_code == 200:
                        # 		break
                        # даные о товаре на рынке
                        # data_op = data_op.json()
                        # max_ranok_2 = op_tovar(data_op)
                        # max_ranok_2 = max_ranok_2[0]
                        # print('max_ranok_2 >= paymin and max_ranok_2 < kol')
                        # print('Цена рынка',max_ranok_2)
                        int_f = max_ranok_2 + kolfek
                        int_f = round(int_f, 2)

                        # Вход в товар
                        try:
                            btn = post.find_element_by_class_name('c-asset__action').click()
                            time.sleep(10)
                        except:

                            driver.refresh()
                            time.sleep(50)
                            try:
                                post = driver.find_element_by_xpath(poisk)
                                btn = post.find_element_by_class_name('c-asset__action').click()
                            except:
                                driver.refresh()
                                time.sleep(20)
                                continue

                        time.sleep(10)
                        input_btn(driver, poisk, int_f)
                        update_tovar(img, account, max_ranok_2, int_f)
                        time.sleep(10)
                    else:
                        # Вход в товар
                        try:
                            btn = post.find_element_by_class_name('c-asset__action').click()
                            time.sleep(10)
                        except:

                            driver.refresh()
                            time.sleep(50)
                            try:
                                post = driver.find_element_by_xpath(poisk)
                                btn = post.find_element_by_class_name('c-asset__action').click()
                            except:
                                driver.refresh()
                                time.sleep(20)
                                continue

                        time.sleep(10)
                        input_btn(driver, poisk, paymin)
                        update_tovar(img, account, max_ranok_2, paymin)
                        time.sleep(10)
                elif f <= max_ranok_2 and max_ranok_2 < kol:

                    # while True:
                    # 	data_op = requests.get(url)
                    # 	if data_op.status_code == 200:
                    # 		break
                    # даные о товаре на рынке
                    # data_op = data_op.json()
                    # max_ranok_2 = op_tovar(data_op)
                    # max_ranok_2 = max_ranok_2[0]
                    # print('Цена нашей ставки',f)
                    # print('Цена рынка',max_ranok_2)
                    int_f = max_ranok_2 + kolfek
                    int_f = round(int_f, 2)

                    # Вход в товар
                    try:
                        btn = post.find_element_by_class_name('c-asset__action').click()
                        time.sleep(10)
                    except:

                        driver.refresh()
                        time.sleep(50)
                        try:
                            post = driver.find_element_by_xpath(poisk)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                        except:
                            driver.refresh()
                            time.sleep(20)
                            continue

                    time.sleep(10)
                    input_btn(driver, poisk, int_f)
                    update_tovar(img, account, max_ranok_2, int_f)
                    time.sleep(10)

                else:
                    # Вход в товар
                    try:
                        btn = post.find_element_by_class_name('c-asset__action').click()
                        time.sleep(10)
                    except:

                        driver.refresh()
                        time.sleep(50)
                        try:
                            post = driver.find_element_by_xpath(poisk)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                        except:
                            driver.refresh()
                            time.sleep(20)
                            continue

                    time.sleep(8)
                    input_btn(driver, poisk, paymin)
                    update_tovar(img, account, max_ranok_2, paymin)
                    time.sleep(8)
            elif f <= max_ranok:
                # while True:
                # 	data_op = requests.get(url)
                # 	if data_op.status_code == 200:
                # 		break
                # # даные о товаре на рынке
                # data_op = data_op.json()
                # max_ranok = op_tovar(data_op)
                # max_ranok = max_ranok[0]
                if max_ranok < kol:
                    int_f = max_ranok + kolfek
                    int_f = round(int_f, 2)
                    # Вход в товар
                    try:
                        btn = post.find_element_by_class_name('c-asset__action').click()
                        time.sleep(8)
                    except:

                        driver.refresh()
                        time.sleep(50)
                        try:
                            post = driver.find_element_by_xpath(poisk)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                        except:
                            driver.refresh()
                            time.sleep(20)
                            continue

                    time.sleep(10)
                    input_btn(driver, poisk, int_f)
                    update_tovar(img, account, max_ranok, int_f)

                elif max_ranok > kol:
                    # Вход в товар
                    try:
                        btn = post.find_element_by_class_name('c-asset__action').click()
                        time.sleep(8)
                    except:

                        driver.refresh()
                        time.sleep(50)
                        try:
                            post = driver.find_element_by_xpath(poisk)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                        except:
                            driver.refresh()
                            time.sleep(20)
                            continue

                    time.sleep(8)
                    input_btn(driver, poisk, paymin)
                    update_tovar(img, account, max_ranok, paymin)


            else:
                # btn = post.find_element_by_class_name('c-asset__action').click()
                # time.sleep(10)
                # input_btn(driver,paymin)
                # update_tovar(img,account,max_ranok,paymin)
                # time.sleep(10)
                continue

        else:
            continue
    print('Удаление')
    driver.refresh()
    time.sleep(40)
    posts = driver.find_elements_by_xpath(
        '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[2]/user-side/div/user-inventory/assets-card-scroll/div/div/asset-card')
    print(len(posts))
    tovar_name = []
    for i in posts:
        # имя товара
        img = i.find_element_by_class_name('c-asset__img').get_attribute('alt')
        tovar_name.append(img)
    delet_tovar(tovar_name, account)
    print('Конец цикла')
    tin = int(proverka_time()) * 60
    time.sleep(tin)
    driver.refresh()
    time.sleep(40)