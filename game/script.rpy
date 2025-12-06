define mc = Character("[player_name]", color="#ffffff")
define n = Character("Ник", color="#ffffff")
define p = Character("Парацетамол", color="#ffff9b")
define rtut = Character("Ртуть", color="#91cdff")
define ch = Character("Хлор", color="#ffbc49")
define golos = Character("Голос из комнаты", color="#42fffc")
define kasper = Character("Каспер", color="42fffc")
define kin = Character("Кин", color="#afff53")


label start:
    scene black_bg

    scene black
    with fade

    show text "{size=40}Что произошло?.. Кто я?.. Где я?.. Последнее, что я помню… яркий свет… разные голоса…" with dissolve
    pause 
    hide text with dissolve
 
    scene nik_room with fade
    n "Никель?.. Э-э… Я?..."

    scene black with fade
    show text "{size=40}Точно. Меня зовут Никель." with dissolve
    pause 
    hide text with dissolve

    scene location1_bg with fade

    n "Какое-то странное место… Металлические стены, пахнет химией?... И эти провода свисают с потолка..."
    n "Всё вокруг кажется таким холодным и... брошенным. Надо срочно выбираться отсюда."

    jump scene_1
    return


label scene_1:

    scene black with fade

    show text "{size=40}Никель осторожно движется по коридору. По стенам — большие аквариумы с причудливыми водорослями, которые подсвечиваются неестественным светом." with dissolve
    pause 
    hide text with dissolve

    scene corridor_aquariums with fade
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    n "Аквариумы? Растения? Интересно… для чего они тут?.."
    n "Странное чувство, словно за мной кто-то наблюдает..."

    scene black with fade
    show text "{size=40}Ник замирает, почувствовав движение в конце коридора." with dissolve
    pause
    show text"{size=40}Сначала он видит лишь две точки света — ярко-зеленые, фосфоресцирующие глаза, отражающие свет аквариумов.\nОни неподвижно смотрят на него из темноты.\nЗатем силуэт кота медленно отделяется от тени и бесшумно приближается." with dissolve
    pause 
    hide text with dissolve

    scene corridor_aquariums_paracetamol with fade
    pause 
    scene corridor_aquariums with fade
    show paracetamol neutral at Position(xalign=0.68, yalign=0.6)
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    p "Испугался? Не бойся, я друг! Я тебя не обижу. Ты видел их? Я их давно тут ищу."
    n "Кого?"
    p "Погоди, а ты вообще кто? Ты их не видел? А... А может, ты один из них? Я будто бы помню такого кота, похожего на тебя…"
    p "Мне тогда еще такую процедуру классную проводили… А, ладно… Слушай, да это точно ты! ты?"
    n "…"
    n "Я ищу выход. Ты знаешь, где он?"
    p "Знакомы? Я с незнакомцами не общаюсь. Я вот — кот Парацетамол, сын Цитрамона. Ты кем будешь?"
    n "Я Ник. Хочу найти выход. Ты помочь можешь?"
    p "О, ну другое дело, Ник! Только меня выход не интересует. Однако запомни одну вещь: бойся змей. А, блин, две вещи! И остерегайся числа {color=#F0E68C}{b}4{/b}."

    scene black with fade
    show system_notice at truecenter with dissolve
    pause 5
    hide system_notice with dissolve

    scene corridor_aquariums with fade
    show paracetamol neutral at Position(xalign=0.68, yalign=0.6)
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    n "…"
    n "Спасибо... Я, пожалуй, пойду тогда."
    p "Налево иди!"

    scene black with fade
    show text "{size=40}Какой странный кот… Надеюсь, мне еще повезет встретить \nздесь кого-нибудь адекватного… в своём уме." with dissolve
    pause 
    hide text with dissolve

    show text "{size=40}Что за звук? Вода?" with dissolve
    pause 
    hide text with dissolve

    jump scene_2
    return


label scene_2:

    scene pool_bg with fade
    show nickel neutral at Position(xalign=0.0, yalign=0.9) with dissolve

    n "Бассейн? Мяу… Я не люблю воду."
    n "Похоже, на той стороне есть дверь. Как же мне туда добраться?.."
    n "Мне показалось, или только что какая-то тень проплыла?.. Надо подойти поближе."

    scene black with fade
    show text "{size=40}Из воды выплывает выдра." at truecenter with dissolve
    pause 
    hide text with dissolve

    scene pool_bg with fade
    show rtut neutral at Position(xalign=0.27, yalign=0.96) with dissolve
    show nickel neutral at Position(xalign=-0.02, yalign=0.9) with dissolve

    rtut "Мяу!"
    n "Мяу?.. Извини?"
    rtut "Давно тебя не видела здесь! Ты вернулся? У меня появились новые ракушки!"
    n "Ага... Я не особо понимаю, о чём ты... Мне кажется, ты меня с кем-то путаешь. Но ты не подскажешь, где тут выход?"
    rtut "Выход? Откуда выход? Здесь и входа-то нет! Зато тут есть переправа! Вот с этим я могу помочь! Кстати, в бассейне ещё есть ракушки, и..."
    n "Подожди, но…"
    rtut "…И они все такие классные и блестящие! Мне особенно нравятся те жёлтые раковины — они так ярко переливаются!"
    rtut "... И ещё, а давай лучше покажу! И тут ещё у меня плоские, голубые и белые... Ой, извини, я заговорилась! Так о чём ты?"
    n "Ты что-то сказала про переправу…"
    rtut "О, да! Точно! Я помогаю всем друзьям! Услуга за услугу: друг помогает мне собрать ракушки, а я, в свою очередь, помогаю переплыть на другую сторону бассейна!"
    n "Я согласен."

    scene black with fade
    show text "{size=40}Ник решает помочь Ртути собрать ракушки..." at truecenter with dissolve
    pause 
    hide text with dissolve
    scene black with fade

    show rules_shells at truecenter with dissolve
    pause 
    hide rules_shells with dissolve

    call start_shells_game

    scene pool_bg with fade
    show rtut neutral at Position(xalign=0.27, yalign=0.96) with dissolve
    show nickel neutral at Position(xalign=-0.02, yalign=0.9) with dissolve
    rtut "Отличная командная работа! Теперь моя очередь!"

    scene black with fade
    show text "{size=40}Ртуть помогла Нику переплыть на другую сторону бассейна. Он отправляется дальше…" at truecenter with dissolve
    pause 
    hide text with dissolve

    jump scene_3
    return


label scene_3:

    scene corridor_green with fade
    show nickel neutral at Position(xalign=0.65, yalign=0.6) with dissolve:
            zoom 0.8

    n "(Не знаю, куда мне стоит пойти дальше…)"

    scene black with fade
    show text "{size=40}Ник идёт дальше.\n\nНеожиданно под лапами начинают попадаться сухие веточки и листья..." at truecenter with dissolve
    pause 
    hide text with dissolve

    show text "{size=40}Он видит приоткрытую дверь, из которой доносится запах свежей травы." at truecenter with dissolve
    pause 
    hide text with dissolve

    jump scene_4


label scene_4:

    scene bg_forest with fade
    show nickel neutral at Position(xalign=0.17, yalign=0.8)
    n "Лес? В лаборатории? Ох, я уже ничему не удивляюсь…"

    show chlor neutral at Position(xalign=0.7, yalign=0.6)
    ch "Один отдыхаешь?"

    n "Мряяяяяяяяяяяу!"

    ch "Да, друг мой, я помогу тебе. Хлор всем помогает, особенно друзьям. Тебе же нужна помощь приятеля Хлора, да?"

    n "(Этот, видимо, особенный случай…)"

    ch "Я как будто бы уже семь триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет… Поэтому сразу вижу, что ты какой-то печалик."

    n "Я ищу выход. Ты знаешь, где он?"

    ch "А я здесь ищу только одного — покоя, умиротворения и вот этой гармонии, от слияния с бесконечно вечн…"

    n "Хлор! Хлор ведь помогает друзьям? Мне нужна твоя помощь, чтобы выбраться отсюда!"

    ch "Где-то я был больше подобен растению… Где-то я больше был подобен птице. Там — червю… Где-то был просто сгусток камня… Это всё есть душа, понимаешь?"

    n "…"

    ch "Но тебе этого не понять… Поэтому ты… что ты?"

    n "Мне нужно найти выход, Хлор. Ты поможешь мне?"

    ch "Услышал тебя, друг мой… Есть у меня {color=#F0E68C}{b}седьмое{/b}{/color=#F0E68C} чудо света, будто бы очень важное... Представляешь, я его терял и находил, а потом снова терял и находил… и так {color=#F0E68C}{b}семь{/b}{/color=#F0E68C} раз…" 
    ch "Друг, и такое бывает. А потом я его сломал. И да, друг, {color=#F0E68C}{b}семь раз{/b}{/color=#F0E68C} . Возьми его и обязательно используй только с умом! Береги это! Это больше…"

    n "(Горстка кусочков?.. Спасибо тут не скажешь)"
    n "О, хорошо."

    scene black with fade
    show text "{size=40}Хлор немного приподнимается, потягивается, выгибает спинку и задней лапкой чешет за ушком.\n\nЛениво поворачивается, достает из-под коры кусочки ключ-карты и медленно протягивает их Нику." at truecenter with dissolve
    pause 
    hide text with dissolve

    show rules_puzzle at truecenter with dissolve
    pause
    hide rules_puzzle with dissolve

    call start_puzzle_game

    scene bg_forest with fade

    show chlor neutral at Position(xalign=0.7, yalign=0.6)
    show nickel neutral at Position(xalign=0.17, yalign=0.8)
    ch "Поэтому давай… Наши пути здесь, конечно, имеют грани подобия, потому что всё едино… Но я-то тебя прекрасно понимаю, а вот ты меня — вряд ли…"
    ch "Вот и всё, поэтому давай, ступай, в конце леса есть дверь, сам разберёшься, а я пошёл наслаждаться прекрасным."

    hide chlor neutral with dissolve

    n "(Пора идти дальше...)"

    jump scene_5
    return


label scene_5:

    scene black
    with fade

    centered "{size=40}Ник, с собранной ключ-картой в лапах, с трудом добрался до опушки."
    centered "{size=40}Воздух здесь был странно тяжёлым и густым, от него кружилась голова и плыли пятна перед глазами.  
    С трудом различив в листве контуры двери, он приложил карту к панели." 
    centered "{size=40}Дверь бесшумно открылась."
    scene bg_perforator_room_empty
    with fade

    n "Как ярко… Мигают лампочки… Голова все еще кружится…"

    golos "Приветствую! Обнаружен неизвестный пользователь! (^ω^)"
    n "О нет, у меня начались голосовые галлюцинации…"
    golos "Ошибка распознавания ответа. Для взаимодействия посмотрите на центральный монитор."
    n "…"

    scene bg_perforator_room_kasper
    with dissolve

    golos "Уточнение: центральный монитор. Сфокусируйте взгляд на мониторе. (>ω<)"
    n "Кот в телевизоре?.. Я еще не отошел от леса?"
    golos "Ответ распознан. Представление: Меня зовут «Каспер».  
    Я — персональный помощник и антивирусный комплекс данной системы."  
    kasper "Моя функция: обеспечение работоспособности. Сформулируйте ваш запрос."

    n "О, я могу спросить тебя о чем угодно?"
    kasper "Ответ положительный! (•̀ ω <)"

    n "Ты можешь помочь мне выйти из здания?"
    kasper "Обработка запроса… Сканирование разрешений…  
    {b}Ответ отрицательный.{/b} (•̀-•̀)"

    kasper "Обнаружена ошибка. Уровень доступа пользователя не определен.  
    Необходимо выполнить процедуру верификации."

    n "То есть?"
    kasper "Требуется перезагрузка системы безопасности и решение капчи для подтверждения статуса. (•̀-•̀)"

    scene black with fade
    show rules_sudoku at truecenter with dissolve
    pause 10
    hide rules_sudoku with dissolve

    call start_sudoku

    scene bg_perforator_room_kasper with fade


    kasper "Верификация пройдена! Ошибка исправлена. Уровень доступа: «наивысший»! (>ω<)"

    n "Отлично! Так как мне выйти?"

    kasper "Выполняю поиск оптимального маршрута до точки «Выход наружу». Ожидайте."
    kasper "Загрузка...25%%...50%%...99%%...Поиск завершен."
    kasper "Анализ плана. Сканирование окружающей среды."

    kasper "Результат: Для достижения цели «Выход наружу»  
    вам необходим объект: «Коридор с цветами»."

    n "Коридор с… что? Какими цветами? Ты о чем?"

    kasper "Уточнение: Коридор, содержащий 34 растения вида {i}Spathiphyllum{/i},  
    также известного как «Спатифиллум». Координаты: слева от вашего текущего положения."

    n "Хорошо… А как мне добраться до этого коридора?"

    kasper "Прокладываю маршрут:  
    пройдите прямо до конца коридора,  
    сверните налево у красного огнетушителя."  
    kasper "Затем на третьем повороте направо — ваш коридор будет пятой дверью слева."

    n "Понял… вроде бы."

    kasper "Хотите, чтобы я сгенерировал для вас пошаговый путеводитель  
    с голосовым сопровождением? (´•̀ω•̀`)?"

    n "Э-э-э… нет, спасибо! Как-нибудь сам решу. Думаю, я запомнил."

    kasper "Как пожелаете!  
    Однако вы всегда можете обратиться ко мне за помощью.  
    Конец связи. Удачи, пользователь Ник! (•̀ ω - )"

    scene karta_kasper with fade
    pause
    jump scene_6
    return


label scene_6:

    scene black with fade
    centered "{size=40}Ник долго плутал, внимательно считая повороты, и наконец очутился в коридоре, залитом сиреневым цветом, вдоль которого росли цветы.\nНе спатифиллумы…"

    scene corridor_flowers_1 with dissolve

    n "Так это тот самый коридор, о котором говорил Каспер."
    n "(Зеркало? Это что, я?.. Но почему звезда?)"
    n "(Стоит проверить… Пошевелю хвостом... Как же странно это странно.)"

    scene black with fade
    centered "{size=40}После его движения отражение в «зеркале» улыбается.\nНик замирает, понимая, что перед ним — не зеркало, а другой кот, очень на него похожий." with dissolve

    scene corridor_flowers_2 with dissolve

    kin "Удивился? Извини, немного заигрался. Понимаешь, этот коридор принадлежит мне."
    kin "Здесь мои правила. Нужно отгадать загадки, если хочешь пройти."

    call start_riddle_1

    kin "Неплохо. Тогда вот вторая."

    call start_riddle_2

    kin "Слушай, а что ты тут, такой умный, забыл? Куда бежишь?"
    n "Мне сказали, что за этим коридором - выход. Я хочу выбраться отсюда!"
    kin "Тебе солгали. Отсюда нет выхода. Уж я-то знаю, поверь мне. Возвращайся, откуда пришел."
    kin "Пойми, у тебя ничего не выйдет. Все, кого ты встречал — давно сдались."
    kin "Парацетамол с его бредом о змеях? Ртуть с её ракушками? Все смирились. И тебе следует сдаться."
    n "Что?! Откуда ты знаешь все это?!"
    kin "Потому что я — это ты. Я тот, кто уже прошел этот путь от начала до конца. Я знаю, что за последним поворотом тебя ничего не ждёт."
    kin "Ты думаешь, ты сильный? Ты просто напуганный кот, который боится признать, что ему некуда идти."

    n "…"
    n "(Неужели он прав? Неужели дальше за этим коридором ничего нет?)"

    kin "Пора понять, что весь наш мир — это мрачные бесконечные коридоры и комнаты."
    kin "Оставайся с нами и забудь все, что ты знал."

    n "Нет… Всё не может быть таким ужасным!"
    n "Я знаю, что мир не такой!"
    n "Я помню запах и вкус еды! Помню прохладу воды! Мягкую траву под лапами!"
    n "Я не верю тебе! Я справлюсь… Трудные времена создают сильных котят!"

    kin "Ты сам скоро поймёшь, насколько сильно ошибаешься…"
    kin "Последняя загадка."

    call start_riddle_3

    scene black with fade
    centered "{size=40}Едва Ник выдавливает ответ, Кин с яростным шипением бросается на него — и растворяется в воздухе, словно его никогда и не было" with dissolve
    centered "{size=40}Ник стоит, дрожа всем телом. \n Голос Кина продолжает звучать у него в голове: «Ты никуда не денешься от себя...»" with dissolve

    centered "{size=40}Собрав всю волю в лапки, Ник разворачивается и бежит к единственной двери в конце коридора, 
    чувствуя, как паника сжимает ему горло. Сердце бешено колотиться, а в ушах стоит звон." with dissolve

    centered "{size=40}Он подбегает к двери - и видит массивный замок с панелью для кода. \n Ловушка? Или последнее испытание?" with dissolve

    jump scene_7
    return


label scene_7:

    scene lock_background with fade
    n "(Замок? Нужно подобрать код... Но какой?)"
    n "…"
    n "(Тот странный кот в самом начале... Парацетамол... Что он говорил?)"
    n "«Остерегайся числа 4»..."
    n "(Почему четверки? Может, в ней и есть ключ?)"
    call start_code_lock_game
    jump ending_scene


label ending_scene:

    scene black with fade
    centered "{size=40}Замок с глухим щелчком отпирается, и тяжелая дверь медленно отъезжает в сторону.\nНик, не раздумывая, проскальзывает в щель."

    scene forest_morning with dissolve
    n "У меня... получилось..."
    n "Впервые за долгое время я чувствую свежий воздух... Он такой... холодный и настоящий."

    scene forest_morning with fade
    show text "{color=#000000}{size=45} Ник медленно делает несколько шагов вперёд. \n Лапки тонут в мокрой траве." at Position(xalign=0.5, yalign=0.4) with dissolve
    pause 
    hide text with dissolve

    show text "{color=#000000}{size=45}Он замечает у своих лап что-то блестящее — маленькую бирку, \n на которой смутно угадывается слово «Цитрамон»." at Position(xalign=0.5, yalign=0.4) with dissolve
    pause 
    hide text with dissolve

    show text "{color=#000000}{size=45}Но всё это уже не имеет смысла… Он поднимает голову, закрывает глаза,\nподставив мордочку солнцу." at Position(xalign=0.5, yalign=0.4) with dissolve
    pause 
    hide text with dissolve

    show text "{color=#000000}{size=45}Солнечный свет становится всё ярче, почти слепящим.\nФигура кота растворяется в сиянии, сливаясь с утренним лесом.." at Position(xalign=0.5, yalign=0.4) with dissolve
    pause 
    hide text with dissolve

    scene black with fade
    centered "{color=#FFFFFF}{size=50}Вы прошли игру{/b}"

    return


#игра ракушки
init python:
    items_data = {
        "first_shell":   {"image": "images/first_shell.png",   "thumb": "images/first_shell_under_water.png", "focus_mask": "images/first_shell_mask.png", "pos": (916, 622), "found": False, "found_image": "images/hide_first_shell.png", "found_pos": (114, 122)},
        "second_shell":   {"image": "images/second_shell.png",   "thumb": "images/second_shell_under_water.png", "focus_mask": "images/second_shell_mask.png", "pos": (705, 784), "found": False, "found_image": "images/hide_second_shell.png", "found_pos": (117, 265)},
        "third_shell":   {"image": "images/third_shell.png",   "thumb": "images/third_shell_under_water.png", "focus_mask": "images/third_shell_mask.png", "pos": (1317, 710), "found": False, "found_image": "images/hide_third_shell.png", "found_pos": (124, 436)},
        "fourth_shell":   {"image": "images/fourth_shell.png",   "thumb": "images/fourth_shell_under_water.png", "focus_mask": "images/fourth_shell_mask.png", "pos": (648, 376), "found": False, "found_image": "images/hide_fourth_shell.png", "found_pos": (124, 637)},
        "fifth_shell":   {"image": "images/fifth_shell.png",   "thumb": "images/fifth_shell_under_water.png", "focus_mask": "images/fifth_shell_mask.png", "pos": (1081, 177), "found": False, "found_image": "images/hide_fifth_shell.png", "found_pos": (129, 791)},
    }
    hidden_game_bg = "images/find_items_background.png"

    def find_item(item_id):
        if items_data[item_id]["found"]:
            return
        items_data[item_id]["found"] = True
        renpy.restart_interaction()

screen hidden_object_game():

    add hidden_game_bg

    fixed:
        for item_id, data in items_data.items():
            if not data["found"]:
                $ xpos, ypos = data["pos"]
                imagebutton:
                    idle data["thumb"]
                    hover data["thumb"]
                    focus_mask data["focus_mask"]
                    xpos xpos
                    ypos ypos
                    action Function(find_item, item_id)

    for item_id, data in items_data.items():
        if data["found"]:
            add data["found_image"] xpos data["found_pos"][0] ypos data["found_pos"][1]

    if all(data["found"] for data in items_data.values()):
        timer 0.1 action Return()

label start_shells_game:
    call screen hidden_object_game

    show shells_endgame at truecenter with dissolve
    pause 5
    hide shells_endgame at truecenter with dissolve

    return


#игра пазл
init python:
    import random

    pieces_data = [
        { "id": "p0", "img": "images/puzzle/piece_0.png", "target": (588, 320), "placed": False },
        { "id": "p1", "img": "images/puzzle/piece_1.png", "target": (774, 320), "placed": False },
        { "id": "p2", "img": "images/puzzle/piece_2.png", "target": (960, 320), "placed": False },
        { "id": "p3", "img": "images/puzzle/piece_3.png", "target": (1146, 320), "placed": False },
        { "id": "p4", "img": "images/puzzle/piece_4.png", "target": (588, 430), "placed": False },
        { "id": "p5", "img": "images/puzzle/piece_5.png", "target": (774, 430), "placed": False },
        { "id": "p6", "img": "images/puzzle/piece_6.png", "target": (960, 430), "placed": False },
        { "id": "p7", "img": "images/puzzle/piece_7.png", "target": (1146, 430), "placed": False },
        { "id": "p8", "img": "images/puzzle/piece_8.png", "target": (588, 540), "placed": False },
        { "id": "p9", "img": "images/puzzle/piece_9.png", "target": (774, 540), "placed": False },
        { "id": "p10", "img": "images/puzzle/piece_10.png", "target": (960, 540), "placed": False },
        { "id": "p11", "img": "images/puzzle/piece_11.png", "target": (1146, 540), "placed": False },
        { "id": "p12", "img": "images/puzzle/piece_12.png", "target": (588, 650), "placed": False },
        { "id": "p13", "img": "images/puzzle/piece_13.png", "target": (774, 650), "placed": False },
        { "id": "p14", "img": "images/puzzle/piece_14.png", "target": (960, 650), "placed": False },
        { "id": "p15", "img": "images/puzzle/piece_15.png", "target": (1146, 650), "placed": False },
    ]

    for piece in pieces_data:
        piece.setdefault("placed", False)
        piece.setdefault("start", None)
        piece.setdefault("w", 186.06)
        piece.setdefault("h", 110.01)

    def shuffle_start_positions(area=(348, 203, 1576, 921)):
        min_x, min_y, max_x, max_y = area
        for piece in pieces_data:
            sx = random.randint(min_x, max_x)
            sy = random.randint(min_y, max_y)
            piece["start"] = (sx, sy)

    def piece_dragged(drags, drop):
        if not drags:
            return
        drag = drags[0]
        piece_id = drag.drag_name

        if not drop:
            return

        if drop.drag_name == piece_id + "_target":

            piece = next((p for p in pieces_data if p["id"] == piece_id), None)
            if not piece:
                return

            tx, ty = piece["target"]
            drag.snap(tx, ty, delay=0.12)

            piece["placed"] = True

            renpy.restart_interaction()

            if puzzle_completed():
                renpy.hide_screen("puzzle_screen")
                return True

            return

    def puzzle_completed():
        return all(p["placed"] for p in pieces_data)

screen puzzle_screen():
    add "images/puzzle/puzzles_background.png"

    draggroup:
        for piece in pieces_data:
            drag:
                drag_name piece["id"] + "_target"
                draggable False
                droppable True
                xpos piece["target"][0]
                ypos piece["target"][1]
                add Solid("#0000", xysize=(piece["w"], piece["h"]))

        for piece in pieces_data:
            if piece.get("placed"):
                drag:
                    drag_name piece["id"]
                    draggable False
                    droppable False
                    xpos piece["target"][0]
                    ypos piece["target"][1]
                    add piece["img"]
            else:
                drag:
                    drag_name piece["id"]
                    draggable True
                    droppable False
                    dragged piece_dragged
                    xpos piece["start"][0]
                    ypos piece["start"][1]
                    add piece["img"]

    if puzzle_completed():
        timer 1 action Return(True)

label start_puzzle_game:
    python:
        for p in pieces_data:
            p["placed"] = False

    $ shuffle_start_positions(area=(348, 203, 1576, 921))
    call screen puzzle_screen

    show solved_puzzle at truecenter
    pause 3
    hide solved_puzzle at truecenter

    show puzzles_endgame at truecenter with dissolve
    pause 5
    hide puzzles_endgame at truecenter with dissolve

    return


#игра судоку
init python:
    style.num_button = Style(style.default)
    style.num_button.font = "gui/Faithful.ttf"
    style.num_button.size = 28

    style.num_button_text = Style(style.text)
    style.num_button_text.color = "#01134A"
    style.num_button_text.hover_color = "#2A428B"


    sudoku = [
        [3,8,9,0,0,0,5,6,0],
        [0,2,1,9,5,3,0,0,0],
        [7,0,0,8,0,0,3,9,1],
        [2,6,0,1,3,0,0,0,9],
        [0,9,0,0,6,4,8,2,5],
        [5,0,7,2,0,8,0,3,0],
        [9,1,0,3,0,7,6,0,8],
        [0,0,0,6,1,0,2,7,4],
        [4,0,6,0,8,0,9,0,0]
    ]

    original = [row[:] for row in sudoku]

    selected = (0,0)

    def wrong(r,c):
        v=sudoku[r][c]
        if v==0: return False
        if sudoku[r].count(v)>1: return True
        if [sudoku[i][c] for i in range(9)].count(v)>1: return True
        br,bc=(r//3)*3,(c//3)*3
        block=[sudoku[i][j] for i in range(br,br+3) for j in range(bc,bc+3)]
        return block.count(v)>1

label start_sudoku:
    call screen sudoku_screen

    show sudoku_endgame at truecenter with dissolve
    pause 5
    hide sudoku_endgame at truecenter with dissolve

    return

screen sudoku_screen():
    add "images/sudoku_background.png"

    for r in range(9):
        for c in range(9):
            $ x = 844 + c * 26 + (c // 3) * 16 + 3; y=347 + r * 29 + (r // 3) * 14 - 2
            frame:
                xpos x ypos y xsize 26 ysize 29
                background ("#f88" if wrong(r,c) else ("#34AB84" if (r,c)==selected else None))
                if sudoku[r][c]:
                    text str(sudoku[r][c]) font "gui/Faithful.ttf" size 28 color "#01134A"

                button:
                    action SetVariable("selected",(r,c))
                    background None

    vbox:
        xpos 885 ypos 640

        hbox:
            spacing 6
            for n in range(1,10):
                textbutton str(n) style "num_button" action Function(set_num, n)

        imagebutton:
            idle "images/sudoku_check_button.png"
            hover "images/sudoku_check_button_hover.png"
            action Function(try_finish_sudoku)
            xoffset 15

init python:
    def set_num(n):
        r, c = selected
        if original[r][c] == 0:
            sudoku[r][c] = n

    def check_win():
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0 or wrong(r,c):
                    renpy.notify("Есть ошибки!")
                    return False
        renpy.notify("Готово!")
        return True

    def try_finish_sudoku():
        if check_win():
            renpy.end_interaction(True)


#игра загадка 1
default riddle_answer_1 = ""

label start_riddle_1:
    call screen riddle_screen_1
    "Загадка решена!"
    return

init python:
    def try_submit_1():
        ans = riddle_answer_1.strip().lower()
        if ans == "лес":
            renpy.return_statement()
        else:
            renpy.notify("Неверно, попробуй ещё!")
            return

style riddle_input_frame:
    background Frame("#0B0C24", 12, 12)
    outlines [(2, "#ffffff", 0, 0)]

screen riddle_screen_1():

    add "images/riddle_background_1.png"

    frame:
        style "riddle_input_frame"

        xpos 0.448
        ypos 0.605

        xsize 200
        ysize 40

        padding (0, 0)

        input:
            value VariableInputValue("riddle_answer_1")
            pixel_width 200

            font "gui/Faithful.ttf"
            size 30
            color "#ffffff"

            xalign 0.5
            yalign 0.5

    key "K_RETURN" action Function(try_submit_1)
    key "K_KP_ENTER" action Function(try_submit_1)


#игра загадка 2
default riddle_answer_2 = ""

label start_riddle_2:
    call screen riddle_screen_2
    "Загадка решена!"
    return

init python:
    def try_submit_2():
        ans = riddle_answer_2.strip().lower()
        if ans == "рыба":
            renpy.return_statement()
        else:
            renpy.notify("Неверно, попробуй ещё!")
            return

screen riddle_screen_2():

    add "images/riddle_background_2.png"

    frame:
        style "riddle_input_frame"

        xpos 0.448
        ypos 0.577

        xsize 200
        ysize 40

        padding (0, 0)

        input:
            value VariableInputValue("riddle_answer_2")
            pixel_width 200

            font "gui/Faithful.ttf"
            size 30
            color "#ffffff"

            xalign 0.5
            yalign 0.5

    key "K_RETURN" action Function(try_submit_2)
    key "K_KP_ENTER" action Function(try_submit_2)


#игра загадка 3
default riddle_answer_3 = ""

label start_riddle_3:
    call screen riddle_screen_3
    "Загадка решена!"
    return

init python:
    def try_submit_3():
        ans = riddle_answer_3.strip().lower()
        if ans == "тень":
            renpy.return_statement()
        else:
            renpy.notify("Неверно, попробуй ещё!")
            return

screen riddle_screen_3():

    add "images/riddle_background_3.png"

    frame:
        style "riddle_input_frame"

        xpos 0.448
        ypos 0.577

        xsize 200
        ysize 40

        padding (0, 0)

        input:
            value VariableInputValue("riddle_answer_3")
            pixel_width 200

            font "gui/Faithful.ttf"
            size 30
            color "#ffffff"

            xalign 0.5
            yalign 0.5

    key "K_RETURN" action Function(try_submit_3)
    key "K_KP_ENTER" action Function(try_submit_3)


#игра кодовый замок
default code_input = ""

label start_code_lock_game:
    call screen code_lock_game
    "Замок открыт!"
    return

init python:
    def try_unlock():
        ans = code_input.strip().lower()
        if ans == "4734":
            renpy.return_statement()
        else:
            renpy.notify("Неверно, попробуй ещё!")
            return

style code_lock_input:
    background Frame("#C8E590", 12, 12)
    outlines [(2, "#ffffff", 0, 0)]

screen code_lock_game():

    add "images/code_lock_background.png"

    frame:
        style "code_lock_input"

        xpos 0.695
        ypos 0.469

        xsize 200
        ysize 40

        padding (0, 0)

        input:
            value VariableInputValue("code_input")
            pixel_width 200

            font "gui/Faithful.ttf"
            size 30
            color "#0B0C24"

            xalign 0.5
            yalign 0.5

    key "K_RETURN" action Function(try_unlock)
    key "K_KP_ENTER" action Function(try_unlock)
