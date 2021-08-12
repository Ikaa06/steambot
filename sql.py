import sqlite3

conn = sqlite3.connect("db.sqlite3")  # или :memory: чтобы сохранить в RAM
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def toFixed(num, digits=0):
    if type(num) == float:
        return f'{num:.{digits}f}'
    else:
        indx = num.index('.') + digits

        return num[:indx + 1]


def save_user(account, t, f, img, data):
    add_user = 'INSERT INTO Tovar_market(name,kolfek,kol,paymin,payself,pay_max,pamax,pasred,Steam_price,zatype,account) VALUES (?,?,?,?,?,?,?,?,?,?,?)'

    max_ranok, min_pay, average_price, Steam_price = data

    if t == 'Активный':
        t = '0'
    elif t == 'Неактивный':
        t = '1'

    f = toFixed(f, 2)
    max_ranok = toFixed(max_ranok, 2)
    min_pay = toFixed(min_pay, 2)
    average_price = toFixed(average_price, 2)
    Steam_price = toFixed(Steam_price, 2)
    data_person = (img, '0.01', '20', f, f, max_ranok, min_pay, average_price, Steam_price, t, account)
    cursor.execute(add_user, data_person)
    conn.commit()


# cursor.close()
def proverka_tovarov(img, account):
    # print("start")
    # cursor = conn.cursor()
    set = 'SELECT * FROM Tovar_market WHERE name="{}" and account="{}"'.format(img, account)
    cursor.execute(set)
    nit = cursor.fetchall()
    print(nit, 'Получить')
    if nit:
        # cursor.close()
        return nit[0]
    else:
        # cursor.close()
        return False


def proverka_time():
    set = 'SELECT * FROM Vremy_market'
    cursor.execute(set)
    nit = cursor.fetchall()[0]
    return nit['time']


def sferka(account, img, t):
    if t == 'Активный':
        set = 'SELECT id,zatype,account FROM Tovar_market WHERE name="{}"'.format(img)
        cursor.execute(set)
        nit = cursor.fetchall()
        if nit:
            for i in nit:
                if i['account'] != account:
                    if i['zatype'] == '1':
                        set = 'UPDATE Tovar_market SET zatype="0" WHERE name="{}" and account="{}"'.format(img, account)
                        cursor.execute(set)
                        conn.commit()
                    else:
                        set = 'UPDATE Tovar_market SET zatype="1" WHERE name="{}" and account="{}"'.format(img, account)
                        cursor.execute(set)
                        conn.commit()


def updata(account, img, t, data, f):
    if t == 'Активный':
        t = '0'
    elif t == 'Неактивный':
        t = '1'
    max_ranok, min_pay, average_price, Steam_price = data
    f = toFixed(f, 2)
    max_ranok = toFixed(max_ranok, 2)
    min_pay = toFixed(min_pay, 2)
    average_price = toFixed(average_price, 2)
    Steam_price = toFixed(Steam_price, 2)
    set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="{}" WHERE name="{}" and account="{}"'.format(
        f, max_ranok, min_pay, average_price, Steam_price, t, img, account)
    cursor.execute(set)
    conn.commit()


def start_work(img, account):
    # cursor = conn.cursor()
    set = 'SELECT * FROM Tovar_market WHERE name="{}" and account="{}" and zatype="0" '.format(img, account)
    cursor.execute(set)
    nit = cursor.fetchall()
    if nit:
        # cursor.close()
        return nit[0]
    else:
        # cursor.close()
        return False


def update_tovar(img, account, max_ranok_2, int_f):
    int_f = toFixed(int_f, 2)
    max_ranok_2 = toFixed(max_ranok_2, 2)
    set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}" WHERE name="{}" and account="{}" '.format(int_f,
                                                                                                       max_ranok_2, img,
                                                                                                       account)
    cursor.execute(set)
    conn.commit()


# print(proverka_time())
# te = proverka('img','account')
# print(te)
# 			if zatype == '1' and accoun == account:
# 				if t == '1':
# 					set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="{}" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 					cursor.execute(set)
# 					conn.commit()

# 				elif t == '0':
# 					set = 'SELECT id FROM Tovar_market WHERE name="{}" and zatype="0" '.format(img)
# 					cursor.execute(set)
# 					nit_2 = cursor.fetchall()
# 					if len(nit_2) == 2:
# 						set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="1" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 						cursor.execute(set)
# 						conn.commit()
# 					elif nit_2[0].get('id') == id_nit:
# 						set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="0" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 						cursor.execute(set)
# 						conn.commit()
# 					else:
# 						set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="1" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 						cursor.execute(set)
# 						conn.commit()
# 			elif zatype == '0' and accoun == account:

# if zatype == '1' and accoun == account:
# 			set = 'SELECT id FROM Tovar_market WHERE name="{}" and zaty="0" '.format(img)
# 			cursor.execute(set)
# 			nit_2 = cursor.fetchall()
# 			if nit_2:

# 				set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="{}",zaty="1" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 				cursor.execute(set)
# 				conn.commit()
# 			else:
# 				set = 'UPDATE Tovar_market SET payself="{}",pay_max="{}",pamax="{}",pasred="{}",Steam_price="{}",zatype="{}",zaty="0" WHERE id="{}"'.format(f,max_ranok,min_pay,average_price,Steam_priceid,t_nit)
# 				cursor.execute(set)
# conn.commit()
# удаление уже не рабочих товаров
def delet_tovar(tovar_name, account):
    set = 'SELECT name,id FROM Tovar_market WHERE account="{}"'.format(account)
    cursor.execute(set)
    nit = cursor.fetchall()
    if nit:
        for img in tovar_name:
            for i in nit:
                if i['name'] == img:
                    flag = True
                    break
                else:
                    flag = False
            if flag:
                continue
            else:
                set = 'DELETE FROM Tovar_market WHERE account="{}" and name ="{}"'.format(account, img)
                cursor.execute(set)
