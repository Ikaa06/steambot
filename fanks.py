import time


def input_btn(driver, poisk=None, f=1):
    try:
        btn_input = driver.find_element_by_xpath(
            '//*[@id="target-constructor-price"]/div/div[1]/mat-form-field/div/div[1]/div/input')
    except:
        time.sleep(5)
        btn_input = driver.find_element_by_xpath(
            '//*[@id="target-constructor-price"]/div/div[1]/mat-form-field/div/div[1]/div/input')
    btn_input.clear()

    btn_input.send_keys(str(f))
    time.sleep(5)
    # обновить и активировать

    try:
        btn = driver.find_element_by_xpath('//*[contains(text(), "Update и пополнить")]')
        btn = driver.find_element_by_class_name('c-dialog__button').click()
        time.sleep(2)
    except:
        try:
            # btn = driver.find_element_by_xpath('//*[contains(text(), "Update и активировать ")]').click()
            btn = driver.find_element_by_xpath('//*[contains(text(), "Обновить и активировать")]').click()
        except:
            try:
                time.sleep(5)
                btn = driver.find_element_by_xpath('//*[contains(text(), "Обновить и активировать")]').click()
            except:
                btn = driver.find_element_by_class_name('c-dialog__button').click()
                time.sleep(2)
                driver.refresh()
                time.sleep(60)
                return

        try:

            time.sleep(5)
            btn = driver.find_element_by_class_name('c-dialog__button').click()

        except:
            try:
                time.sleep(7)
                btn = driver.find_element_by_class_name('c-dialog__button').click()

            except:
                btn = driver.find_element_by_xpath('//button[@class="c-dialogHeader__close ng-star-inserted"]').click()
                time.sleep(10)
                try:
                    post = driver.find_element_by_xpath(poisk)
                except:
                    time.sleep(2)
                    driver.refresh()
                    time.sleep(20)
                    post = driver.find_element_by_xpath(poisk)
                time.sleep(10)
                btn = post.find_element_by_xpath('//*[@class="c-asset ng-star-inserted"]').click()
                time.sleep(5)
                btn = post.find_element_by_class_name('c-asset__action').click()
                time.sleep(10)
                input_btn(driver, poisk, f)

    time.sleep(5)


def op_tovar(data_op):
    data = []
    for key in data_op:

        if key == 'targets':
            break
        else:
            dp = data_op.get(key).get('amount')

            if '.' in dp:
                dp, _ = dp.split('.')
                dp = '0' + dp
                dp = float(dp)
                data.append(dp)
            elif len(dp) > 2:

                dp = data_op.get(key).get('amount')

                if dp[-2:] == '00':
                    dp = float(dp[:-2])
                else:
                    p = float('0.' + dp[-2:])
                    dp = float(dp[:-2]) + p
                    dp = float(dp)
                # print(dp)
                data.append(dp)
            else:
                dp = '0.' + dp
                dp = float(dp)
                data.append(dp)
    return data
