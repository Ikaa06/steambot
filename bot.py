import logging
import pickle
from sys import argv

import requests
from selenium import webdriver

from fanks import *
from sql import save_user, proverka_tovarov, sferka, updata, proverka_time, update_tovar, delet_tovar

driver = webdriver.Firefox('D://botPaySteem/botPaySteem/steambot0.2')

# вход в на сайт
driver.get('https://dmarket.com/ru/ingame-items/item-list/csgo-skins')
# авторизация на сайте
account, passwort = argv[1:]
print('Войдите в аккаунт в ручную ', account, passwort)
try:
    cookies = pickle.load(open(f"cokiss/{account}.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
except Exception as e:
    print('Войтите в аккаунт в ручную ', account, '\n', passwort)
    input('АВТ')
    pickle.dump(driver.get_cookies(), open(f"cokiss/{account}.pkl", "wb"))

input('Для начало работ нажмите enter')
login_btn = driver.find_element_by_xpath(
    '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[1]/div['
    '1]/user-inventory-tabs/div/div[3]').click()
# ожидание
time.sleep(10)
print('Сохранение товара')
# создание списка товаров

while True:
    k = 0
    while True:
        try:
            posts = driver.find_elements_by_xpath(
                '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div['
                '2]/user-side/div/user-inventory/assets-card-scroll/div/div/asset-card')
            break
        except Exception as e:
            logging.info(e)
            if k == 0:
                driver.refresh()
                time.sleep(30)
                k += 1

            else:
                time.sleep(5)

    print(len(posts))
    alt_spisok = []
    # Работа робота
    for i in posts:  # сборка имен товаров
        # имя товара
        img = i.find_element_by_class_name('c-asset__img').get_attribute('alt')
        alt_spisok.append(img)
    for img in alt_spisok:
        # запрос к api
        url = f'https://api.dmarket.com/exchange/v1/target/advice-price/a8db?title={img}'
        # первый бесконечный цикл получение данных от сервера
        while True:
            try:
                data_op = requests.get(url)
            except Exception as e:
                logging.info(e)
                print('получение данных от сервера')
                time.sleep(60)
                continue
            if data_op.status_code == 200:
                break
        # данные о товаре на рынке
        data_op = data_op.json()
        data = op_tovar(data_op)

        poisk = './/asset-card//img[@alt="{}"]/ancestor::asset-card'.format(img)

        try:
            post = driver.find_element_by_xpath(poisk)
        except Exception as e:
            logging.error(e)
            try:
                time.sleep(2)
                driver.refresh()
                time.sleep(20)
                driver.switch_to.window('main')
                post = driver.find_element_by_xpath(poisk)
            except Exception as e:
                logging.error(e)
                driver.refresh()
                time.sleep(20)
                continue

        # статус товара

        try:
            x_y = post.location_once_scrolled_into_view
            t = post.find_element_by_class_name('c-asset__status').text
        except Exception as e:
            logging.error(f'{e} 1')
            try:
                post = driver.find_element_by_xpath(poisk)
                x_y = post.location_once_scrolled_into_view
                time.sleep(2)
                data_post_tavar = post.text
                data_post_tavar = data_post_tavar.split('\n')
                t = data_post_tavar[-1]
            except Exception as e:
                logging.error(f'{e} 2')
                continue
        # цена товара
        if not t:
            x_y = post.location_once_scrolled_into_view
            time.sleep(5)
            data_post_tavar = post.text
            data_post_tavar = data_post_tavar.split('\n')
            t = data_post_tavar[-1]
            if not t:
                continue

        print('Статус товара', t)
        try:
            x_y = post.location_once_scrolled_into_view
            f = post.find_element_by_class_name('c-asset__priceNumber').text.replace('$', '')
        except Exception as e:
            logging.error(e)
            try:
                post = driver.find_element_by_xpath(poisk)
                x_y = post.location_once_scrolled_into_view
                data_post_tavar = post.text
                data_post_tavar = data_post_tavar.split('\n')
                f = data_post_tavar[0].replace('$', '')
            except Exception as e:
                print(e, 'price')
                continue
        print('Цена товара', f)
        if not f:
            x_y = post.location_once_scrolled_into_view
            time.sleep(5)
            data_post_tavar = post.text
            data_post_tavar = data_post_tavar.split('\n')
            f = data_post_tavar[0].replace('$', '')
            if not f:
                continue
        test = proverka_tovarov(img, account)
        # Условие проверки при значение False
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
            payself = float(test['payself'].replace('$', ''))
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
                # данные о товаре на рынке
                data_op = data_op.json()
                max_ranok_2 = op_tovar(data_op)
                max_ranok_2 = max_ranok_2[0]
                if f > max_ranok_2:
                    if max_ranok_2 < paymin and max_ranok_2 < kol:
                        # Вход в товар

                        try:
                            x_y = post.location_once_scrolled_into_view
                            time.sleep(2)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                            time.sleep(10)
                        except:

                            driver.refresh()
                            time.sleep(50)
                            try:
                                post = driver.find_element_by_xpath(poisk)
                                x_y = post.location_once_scrolled_into_view
                                time.sleep(2)
                                btn = post.find_element_by_class_name('c-asset__action').click()
                            except:
                                driver.refresh()
                                time.sleep(20)
                                continue

                        time.sleep(10)
                        input_btn(driver, poisk, paymin)
                        update_tovar(img, account, max_ranok_2, f)
                        time.sleep(10)

                    elif paymin <= max_ranok_2 < kol:
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
                                x_y = post.location_once_scrolled_into_view
                                time.sleep(2)
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
                                x_y = post.location_once_scrolled_into_view
                                time.sleep(2)
                                btn = post.find_element_by_class_name('c-asset__action').click()
                            except:
                                driver.refresh()
                                time.sleep(20)
                                continue

                        time.sleep(10)
                        input_btn(driver, poisk, paymin)
                        update_tovar(img, account, max_ranok_2, paymin)
                        time.sleep(10)
                elif f <= max_ranok_2 < kol:
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
                            x_y = post.location_once_scrolled_into_view
                            time.sleep(2)
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
                            x_y = post.location_once_scrolled_into_view
                            time.sleep(2)
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
                            x_y = post.location_once_scrolled_into_view
                            time.sleep(2)
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
                            x_y = post.location_once_scrolled_into_view
                            time.sleep(2)
                            btn = post.find_element_by_class_name('c-asset__action').click()
                        except:
                            driver.refresh()
                            time.sleep(20)
                            continue

                    time.sleep(8)
                    input_btn(driver, poisk, paymin)
                    update_tovar(img, account, max_ranok, paymin)


            else:
                continue

        else:
            continue
    # Конец работ
    print('Удаление')
    driver.refresh()
    time.sleep(40)
    posts = driver.find_elements_by_xpath(
        '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div['
        '2]/user-side/div/user-inventory/assets-card-scroll/div/div/asset-card')
    print(len(posts))
    tovar_name = []
    for i in posts:
        # имя товара
        img = i.find_element_by_class_name('c-asset__img').get_attribute('alt')
        tovar_name.append(img)
    delet_tovar(tovar_name, account)
    pickle.dump(driver.get_cookies(), open(f"cokiss/{account}.pkl", "wb"))
    print('Конец цикла')
    tin = int(proverka_time()) * 60
    time.sleep(tin)
    driver.refresh()
    time.sleep(40)
