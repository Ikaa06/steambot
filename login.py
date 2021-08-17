import time


def log(driver, account, passwort):
    time.sleep(20)
    try:
        login = driver.find_element_by_id('onesignal-slidedown-cancel-button').click()
    except:
        pass
    time.sleep(4)
    try:
        login = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/mat-dialog-container/onboarding-dialog/div/button').click()
    except:
        pass
    try:
        coki = driver.find_element_by_xpath('//button[@class="c-cookieBanner__btn"]').click()
    except:
        pass
    login = driver.find_element_by_xpath(
        '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[1]/div[2]/header-navigation/navigation-controls/header-user-auth-btn/div/button[2]').click()
    time.sleep(5)
    login = driver.find_element_by_xpath(
        '//button[@class="c-authFooter__button o-dmButton o-dmButton--round o-dmButton--blue mat-ripple"]').click()
    time.sleep(5)
    login = driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(account)
    login = driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(passwort)
    login = driver.find_element_by_xpath(
        '//button[@class="c-authFooter__button c-authFooter__button--fluid o-dmButton o-dmButton--blue mat-ripple"]').click()
    time.sleep(10)
    try:
        # заказ
        proverka = driver.find_element_by_class_name('c-dialog__button').click()
        print(0)
    except:
        pass
    try:
        proverka = driver.find_element_by_xpath(
            '//*[@id="mat-dialog-1"]/auth-dialog/auth-flows/div/login-flow/div[2]/login-form/form/div[2]/button').click()
        print(1)
    except:
        pass
    try:
        proverka = driver.find_element_by_xpath(
            '//*[@id="mat-dialog-3"]/auth-dialog/auth-flows/div/steam-public-flow/div[1]/button').click()
        print(2)
    except:
        pass
    time.sleep(2)
    try:
        # кнопка стим
        login_btn = driver.find_element_by_xpath(
            '//*[@id="mat-dialog-2"]/auth-dialog/auth-flows/div/steam-public-flow/div[1]/button').click()
        print(3)
    except:
        pass
    time.sleep(5)
    try:

        # кнопка заказов
        login_btn = driver.find_element_by_xpath(
            '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/exchange/div/div[1]/div[1]/user-inventory-tabs/div/div[3]').click()
        print(4)
    except:
        pass
