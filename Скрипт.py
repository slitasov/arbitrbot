
import time

depo = 0
quantity_SBER = 1
quantity_SBERP = 13

def spread(activ1, activ2):
    """Считаем средний спред"""
    sum_spread = 0
    for i in range(len(activ1)):
        sum_spread += abs(activ1[i] - activ2[i]) #накапливаем сумму спредов
    mean_spread = sum_spread/len(activ1) #делим на кол - во цен в массивчике
    return mean_spread

def prices_sber():
    Prices_sber = []
    f = open('PRICESSBER.txt', 'r')
    sber_info = f.readlines()
    f.close()
    c = 36001
    for info in sber_info:
        info = info.split(';')
        pok = int(info[3][:2])*3600 + int(info[3][2:4])*60 + int(info[3][4:])
        if c > 82799:
            break
        if c > 67259 and c < 68699:
            c = 68700
        if pok > c:
            while pok > c:
               Prices_sber.append(Prices_sber[-1])
               c += 0.5
        if pok == c:
            Prices_sber.append(float(info[4]))
            c += 0.5
    return Prices_sber

def prices_sberp():
    Prices_sberp = []
    f = open('PRICESSBERP.txt', 'r')
    sberp_info = f.readlines()
    f.close()
    c = 36001
    for info in sberp_info:
        info = info.split(';')
        pok = int(info[3][:2])*3600 + int(info[3][2:4])*60 + int(info[3][4:])
        if c > 82799:
            break
        if c > 67259 and c < 68699:
            c = 68700
        if pok > c:
            while pok > c:
                Prices_sberp.append(Prices_sberp[-1])
                c += 0.5
        if pok == c:
            Prices_sberp.append(float(info[4]))
            c += 0.5
    return Prices_sberp

if __name__ == '__main__':
    
    tickers = ['SBER', 'SBERP'] 

    pricesSBER = [] #очередь цен для сбера обычного, здесь хранится 120 последних цен, они попадают сюда каждые 2 секунды
    pricesSBERP = [] #очередь цен для сбера охуенного, здесь хранится 120 последних цен, они попадают сюда каждые 2 секунды

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    kom = 0.04*10
    k = 200
    r = 0
    time_ed = 0.5
    param_time = 2000 # /2секунд
    

    pricesSBER = prices_sber()
    pricesSBERP = prices_sberp()

    pricesSBER_svalka = pricesSBER[:k]
    pricesSBERP_svalka = pricesSBERP[:k]
    pricesSBER = pricesSBER[k:]
    pricesSBERP = pricesSBERP[k:]

    #spread_list = [] #это чисто по приколу, чтобы записывать данные о спреде в эксель
    #spread_dict = {} #и это

    gg = min(len(pricesSBER), len(pricesSBERP))

    i = 0
    while i < gg:
        pricesSBER_svalka = pricesSBER_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
        pricesSBER_svalka.append(pricesSBER[i])
        pricesSBERP_svalka = pricesSBERP_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
        pricesSBERP_svalka.append(pricesSBERP[i])
        print('Последняя цена на сбер: ', pricesSBER_svalka[-1], ' ', 'Последняя цена на сберп: ', pricesSBERP_svalka[-1])
        mean_spread = spread(pricesSBER_svalka, pricesSBERP_svalka)#пересчитываем средний спред, так как у нас обновились очереди
        print('Средний спред на данный момент: ', mean_spread)
        moment_spread = pricesSBER_svalka[-1] - pricesSBERP_svalka[-1]
        print('Моментальный спред на данный момент: ', moment_spread)
        #spread_dict = {'Моментальный спред': moment_spread, 'Средний спред': mean_spread}#создаем словарик
        #spread_list.append(spread_dict)#суем словарик в листик
        print('Криетрий сценария 1: ', abs(moment_spread) - mean_spread - 4*kom - m1)
        print('Критерий сценария 2: ', abs(moment_spread) - mean_spread + 4*kom + m2)
        print()
        if abs(moment_spread) - mean_spread - 4*kom/10 - m1 > 0:
            if moment_spread < 0:
                depo = depo - 10*pricesSBER_svalka[-1] - kom
                print('Купили SBER по ', pricesSBER_svalka[-1])
                open_SBER = 10*pricesSBER_svalka[-1]
                depo = depo + 10*pricesSBERP_svalka[-1] - kom
                print('Продали SBERP по ', pricesSBERP_svalka[-1])
                open_SBERP = 10*pricesSBERP_svalka[-1]
                flag = True
            else:
                depo = depo - 10*pricesSBERP_svalka[-1] - kom
                print('Купили SBERP по ', pricesSBERP_svalka[-1])
                open_SBERP = 10*pricesSBERP_svalka[-1]
                depo = depo + 10*pricesSBER_svalka[-1] - kom
                print('Продали SBER по ', pricesSBER_svalka[-1])
                open_SBER = 10*pricesSBER_svalka[-1]
                flag = False
            i += 1
            stop_time = 0
            while int(stop_time) < param_time and  i < gg and abs(moment_spread) - mean_spread +2*kom/10 + m3>0:
                pricesSBER_svalka = pricesSBER_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
                pricesSBER_svalka.append(pricesSBER[i])
                pricesSBERP_svalka = pricesSBERP_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
                pricesSBERP_svalka.append(pricesSBERP[i])
                print('Последняя цена на сбер: ', pricesSBER_svalka[-1], ' ', 'Последняя цена на сберп: ', pricesSBERP_svalka[-1])
                mean_spread = spread(pricesSBER_svalka, pricesSBERP_svalka)#пересчитываем средний спред, так как у нас обновились очереди
                print('Средний спред на данный момент: ', mean_spread)
                moment_spread = pricesSBER_svalka[-1] - pricesSBERP_svalka[-1]
                print('Моментальный спред на данный момент: ', moment_spread)
                print('Критерий закрытия сделки на данный момент: ', abs(moment_spread) - mean_spread - 2*kom - m3)
                print()
                i += 1
                stop_time += time_ed
            if flag == False:
                depo = depo - 10*pricesSBER_svalka[-1] - kom
                print('Купили SBER по ', pricesSBER_svalka[-1])
                depo = depo + 10*pricesSBERP_svalka[-1] - kom
                print('Продали SBERP по ', pricesSBERP_svalka[-1])
                print('Заработано: ', (open_SBER - 10*pricesSBER_svalka[-1]-2*kom),' за куплю сбера', (10*pricesSBERP_svalka[-1] - open_SBERP-2*kom ), ' за продажу сберп', ' всего', (open_SBER - 10*pricesSBER_svalka[-1]) + (10*pricesSBERP_svalka[-1] - open_SBERP)-4*kom)
                time.sleep(r)
            else:
                depo = depo - 10*pricesSBERP_svalka[-1] - kom
                print('Купили SBERP по ', pricesSBERP_svalka[-1])
                depo = depo + 10*pricesSBER_svalka[-1] - kom
                print('Продали SBER по ', pricesSBER_svalka[-1])
                print('Заработано: ', (open_SBERP - 10*pricesSBERP_svalka[-1]-2*kom), ' за куплю сберп', (10*pricesSBER_svalka[-1] - open_SBER -2*kom ), ' за продажу сберп', ' всего', (open_SBERP - 10*pricesSBERP_svalka[-1]) + (10*pricesSBER_svalka[-1] - open_SBER)-4*kom)
                time.sleep(r)
            print()
        elif abs(moment_spread) - mean_spread + 4*kom/10 + m2 < 0:
            if moment_spread < 0:
                depo = depo - 10*pricesSBERP_svalka[-1] - kom
                print('Купили SBERP по ', pricesSBERP_svalka[-1])
                open_SBERP = 10*pricesSBERP_svalka[-1]
                depo = depo + 10*pricesSBER_svalka[-1] - kom
                print('Продали SBER по ', pricesSBER_svalka[-1])
                open_SBER = 10*pricesSBER_svalka[-1]
                flag = True
            else:
                depo = depo - 10*pricesSBER_svalka[-1] - kom
                print('Купили SBER по ', pricesSBER_svalka[-1])
                open_SBER = 10*pricesSBER_svalka[-1]
                depo = depo + 10*pricesSBERP_svalka[-1] - kom
                print('Продали SBERP по ', pricesSBERP_svalka[-1])
                open_SBERP = 10*pricesSBERP_svalka[-1]
                flag = False
            i += 1
            stop_time = 0
            while int(stop_time) < param_time and i < gg and abs(moment_spread) - mean_spread - 2*kom/10 - m4 < 0:
                pricesSBER_svalka = pricesSBER_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
                pricesSBER_svalka.append(pricesSBER[i])
                pricesSBERP_svalka = pricesSBERP_svalka[1:]#когда мы получаем новую цену, нужно выкинуть самую первую цену, а новую записать в самый конец
                pricesSBERP_svalka.append(pricesSBERP[i])
                print('Последняя цена на сбер: ', pricesSBER_svalka[-1], ' ', 'Последняя цена на сберп: ', pricesSBERP_svalka[-1])
                mean_spread = spread(pricesSBER_svalka, pricesSBERP_svalka)#пересчитываем средний спред, так как у нас обновились очереди
                print('Средний спред на данный момент: ', mean_spread)
                moment_spread = pricesSBER_svalka[-1] - pricesSBERP_svalka[-1]
                print('Моментальный спред на данный момент: ', moment_spread)
                print('Критерий закрытия сделки на данный момент: ', abs(moment_spread) - mean_spread + 4*kom + m4)
                i += 1
                stop_time += time_ed
                print()
            if flag == False:
                depo = depo - 10*pricesSBERP_svalka[-1] - kom
                print('Купили SBERP по ', pricesSBERP_svalka[-1])
                depo = depo + 10*pricesSBER_svalka[-1] - kom
                print('Продали SBER по ', pricesSBER_svalka[-1])
                print('Заработано: ', (open_SBERP - 10*pricesSBERP_svalka[-1]-2*kom), ' за куплю сберп', (10*pricesSBER_svalka[-1] - open_SBER -2*kom), ' за продажу сбер', ' всего', (open_SBERP - 10*pricesSBERP_svalka[-1]) + (10*pricesSBER_svalka[-1] - open_SBER )-4*kom)
                time.sleep(r)
            else:
                depo = depo - 10*pricesSBER_svalka[-1] - kom
                print('Купили SBER по ', pricesSBER_svalka[-1])
                depo = depo + 10*pricesSBERP_svalka[-1] - kom
                print('Продали SBERP по ', pricesSBERP_svalka[-1])
                print('Заработано: ', (open_SBER - 10*pricesSBER_svalka[-1]-2*kom), ' за куплю сбер', (10*pricesSBERP_svalka[-1] - open_SBERP -2*kom),  ' за продажу сберп', ' всего', (open_SBER - 10*pricesSBER_svalka[-1]) + (10*pricesSBERP_svalka[-1] - open_SBERP )-4*kom)
                time.sleep(r)
            print()
        print()
        i += 1
    print(depo)