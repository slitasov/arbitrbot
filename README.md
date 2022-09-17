# arbitrbot
### На первом курсе ФЭНа НИУ ВШЭ во время прохождения курса 'Финансовые рынки' нам рассказали о торговой стратегии парного арбитража. Кратко говоря, парный арбитраж заключается в следующем: на рынке есть два и более актива, ценовые движения которых по тем или иным причинам (одна отрасль, один эмитент, и др) обладает высокой корреляцией). Это приводит к образованию среднего устойчивого спреда (разницы между ценой актива А и актива Б). Таким образом, если цена актива А резко улетает вверх, а цена актива Б все еще остается на том же уровне, можно с высокой степенью достоверности предположить, что цена актива Б вскоре тоже начнет расти, чтобы текущий спред между этими активами вернулся к среднему значению. Тогда (подробнее в файле 'Алгоритм.md'), можно открывать сделки таким образом, чтобы нам было абсолютно не важно, растут активы или падают в цене. Единственное, что нас будет интересовать - спред между ними. Чтобы проверить эту теорию, я решил написать алгоритм, который будет автоматически совершать сделки по этой стратегии