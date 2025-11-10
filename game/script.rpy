# Определяем персонажей
define mc = Character("[player_name]", color="#ffffff")
define n = Character("Ник", color="#ffffff")
define p = Character("Парацетамол", color="#ffff9b")
define rtut = Character("Ртуть", color="#91cdff")
define ch = Character("Хлор", color="#ffbc49")


# Начало игры
label start:
    # Первая сцена
    scene black_bg

    # Черный экран
    scene black
    with fade

    # Медленно появляющийся текст
    show text "Что произошло?.. Кто я?.. Где я?.. Последнее, что я помню… яркий свет… разные голоса…" with dissolve
    pause 4
    hide text with dissolve
 
    # Плавное прояснение сцены (комната глазами кота)
    scene location1_bg with fade
    pause 2

    show text "Никель?.. Э-э… Я?..." with dissolve
    pause 3
    hide text with dissolve

    # Черный экран с текстом имени
    scene black with fade
    show text "Точно. Меня зовут Никель." with dissolve
    pause 3
    hide text with dissolve

    # Переход к нормальной сцене с котом
    scene location1_bg with fade
    show nickel neutral at left with dissolve

    # Реплики кота
    n "Какое-то странное место… Металлические стены, пахнет химией?... И эти провода свисают с потолка..."
    n "Всё вокруг кажется таким холодным и... брошенным. Надо срочно выбираться отсюда."

    
    jump scene_1
    return


# scene_1.rpy
label scene_1:

    # Черный экран
    scene black with fade

    # Текст-описание
    show text "Никель осторожно движется по коридору. По стенам — большие аквариумы с причудливыми водорослями, которые подсвечиваются неестественным светом." with dissolve
    pause 4
    hide text with dissolve

    # Фон 1 — коридор с аквариумами
    scene corridor_aquariums with fade
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    n "Аквариумы? Растения? Интересно… для чего они тут?.."
    n "(Странное чувство, словно за мной кто-то наблюдает...)"

    # Смена сцены — напряжённый момент
    scene black with fade
    show text "Ник замирает, почувствовав движение в конце коридора.\n\nСначала он видит лишь две точки света — ярко-зеленые, фосфоресцирующие глаза, отражающие свет аквариумов.\nОни неподвижно смотрят на него из темноты.\nЗатем силуэт кота медленно отделяется от тени и бесшумно приближается." with dissolve
    pause 6
    hide text with dissolve

    # Фон 2 — появляется Парацетамол
    scene corridor_aquariums_paracetamol with fade
    pause 2
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
    p "О, ну другое дело, Ник! Только меня выход не интересует. Однако запомни одну вещь: бойся змей. А, блин, две вещи! И остерегайся числа 4."

    # --- Системное уведомление ---
    scene black with fade
    show system_notice at truecenter with dissolve
    pause 5
    hide system_notice with dissolve

    # Возврат к разговору
    scene corridor_aquariums with fade
    show paracetamol neutral at Position(xalign=0.68, yalign=0.6)
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    n "…"
    n "Спасибо... Я, пожалуй, пойду тогда."
    p "Налево иди!"

    # --- Внутренний монолог ---
    scene black with fade
    show text "Какой странный кот… Надеюсь, мне еще повезет встретить \nздесь кого-нибудь адекватного… в своём уме." with dissolve
    pause 6
    hide text with dissolve

    show text "Что за звук? Вода?" with dissolve
    pause 3
    hide text with dissolve

    jump scene_2
    return

label scene_2:

    # --- Локация: бассейн ---
    scene pool_bg with fade
    show nickel neutral at Position(xalign=0.0, yalign=0.9) with dissolve

    n "Бассейн? Мяу… Я не люблю воду."
    n "Похоже, на той стороне есть дверь. Как же мне туда добраться?.."
    n "Мне показалось, или только что какая-то тень проплыла?.. Надо подойти поближе."

    # --- Темнота и появление выдры ---
    scene black with fade
    show text "Из воды выплывает выдра." at truecenter with dissolve
    pause 2
    hide text with dissolve

    # --- Появляется Ртуть ---
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
    show text "Ник решает помочь Ртути собрать ракушки..." at truecenter with dissolve
    pause 2
    hide text with dissolve
    scene black with fade

    #правила игры
    show rules_shells at truecenter with dissolve
    pause 5
    hide rules_shells with dissolve

    #!!!!ПОСЛЕ ЭТИХ СЛОВ НАДО ДОБАВИТЬ ИГРУ ПОИСК РАКУШЕК!!!!
    call start_hidden_game

    scene pool_bg with fade
    show rtut neutral at Position(xalign=0.27, yalign=0.96) with dissolve
    show nickel neutral at Position(xalign=-0.02, yalign=0.9) with dissolve
    rtut "Отличная командная работа! Теперь моя очередь!"

    # --- Конец сцены ---
    scene black with fade
    show text "Ртуть помогла Нику переплыть на другую сторону бассейна. Он отправляется дальше…" at truecenter with dissolve
    pause 2
    hide text with dissolve

    jump scene_3
    return

label scene_3:

    # --- Локация: коридор ---
    scene corridor_green with fade
    show nickel neutral at Position(xalign=0.65, yalign=0.6) with dissolve:
            zoom 0.8

    n "(Не знаю, куда мне стоит пойти дальше…)"

    # --- Переход: чёрный экран и повествование ---
    scene black with fade
    show text "Ник идёт дальше.\n\nНеожиданно под лапами начинают попадаться сухие веточки и листья..." at truecenter with dissolve
    pause 3
    hide text with dissolve

    show text "Он видит приоткрытую дверь, из которой доносится запах свежей травы." at truecenter with dissolve
    pause 3
    hide text with dissolve

    # --- Переход к следующей локации ---
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

    ch "Услышал тебя, друг мой… Есть у меня {b}{i}седьмое{/i}{/b} чудо света, будто бы очень важное... Представляешь, я его терял и находил, а потом снова терял и находил… и так {b}{i}семь{/i}{/b} раз…" 
    ch "Друг, и такое бывает. А потом я его сломал. И да, друг, {b}{i}семь раз{/i}{/b} . Возьми его и обязательно используй только с умом! Береги это! Это больше…"

    n "(Горстка кусочков?.. Спасибо тут не скажешь)"
    n "О, хорошо."

    scene black with fade
    show text "Хлор немного приподнимается, потягивается, выгибает спинку и задней лапкой чешет за ушком.\n\nЛениво поворачивается, достает из-под коры кусочки ключ-карты и медленно протягивает их Нику." at truecenter with dissolve
    pause 5
    hide text with dissolve

    # --- Системная вставка: начало мини-игры ---
    show rules_puzzle at truecenter with dissolve
    pause 5
    hide rules_puzzle with dissolve
    #!!!ПОСЛЕ ЭТОГО ВСТАВИТЬ МИНИ ИГРУ ПАЗЗЛЫ
    # call puzzle_game

    scene bg_forest with fade

    show chlor neutral at Position(xalign=0.7, yalign=0.6)
    show nickel neutral at Position(xalign=0.17, yalign=0.8)
    ch "Поэтому давай… Наши пути здесь, конечно, имеют грани подобия, потому что всё едино… Но я-то тебя прекрасно понимаю, а вот ты меня — вряд ли…"
    ch "Вот и всё, поэтому давай, ступай, в конце леса есть дверь, сам разберёшься, а я пошёл наслаждаться прекрасным."

    hide chlor neutral with dissolve

    n "(Пора идти дальше...)"

    scene black with fade
    return

label chapter1_menu:
    menu:
        "Какую задачу хочешь решить первой?"
        
        "Решить судоку":
            jump sudoku_game
            
        "Собрать пазл":
            jump puzzle_game
            
        "Найти спрятанные предметы":
            jump find_items_game
            
        "Сыграть в три в ряд":
            jump match3_game
            
        "Ввести код от замка":
            jump code_lock_game

label after_minigame:
    paracetamol "Отлично справился! Что будем делать дальше?"
    jump chapter1_menu

label code_lock_game:
    scene bg safe
    $ code_input = ""
    $ correct_code = "1234"
    
    paracetamol "Нужно ввести код от сейфа. Попробуй угадать!"
    
    while code_input != correct_code:
        $ code_input = renpy.input("Введите 4-значный код (подсказка: [correct_code]):", length=4)
        
        if code_input == correct_code:
            paracetamol "Ура! Сейф открыт!"
            $ renpy.notify("Сейф открыт! +10 очков")
        else:
            paracetamol "Код не подошел. Попробуй еще раз."
    
    jump after_minigame

# Мини-игра "Поиск предметов"
label find_items_game:
    scene bg library
    $ found_items = []
    $ needed_items = ["ключ", "книга", "очки"]
    
    paracetamol "Найди все спрятанные предметы в библиотеке: ключ, книгу и очки."
    
    call screen find_items_screen
    
    paracetamol "Молодец! Нашел все предметы!"
    jump after_minigame

screen find_items_screen():
    # Добавляем скрытые зоны для клика
    imagemap:
        ground "bg library"  # Ваше фоновое изображение
        
        # Определяем зоны, где можно кликать (координаты x1, y1, x2, y2)
        hotspot (100, 200, 150, 250) action [AddToSet(found_items, "ключ"), Return()]
        hotspot (300, 150, 350, 200) action [AddToSet(found_items, "книга"), Return()]
        hotspot (500, 300, 550, 350) action [AddToSet(found_items, "очки"), Return()]
    
    # Показываем найденные предметы
    vbox:
        xalign 0.1
        yalign 0.1
        text "Найдено: [len(found_items)]/3 предметов"
        for item in found_items:
            text "[item]"

label sudoku_game:
    scene bg desk
    $ sudoku_solved = False
    
    paracetamol "Реши судоку! Заполни все клетки цифрами от 1 до 4."
    
    call screen sudoku_screen
    
    if sudoku_solved:
        paracetamol "Поздравляю! Судоку решено!"
    else:
        paracetamol "В следующий раз получится!"
    
    jump after_minigame

screen sudoku_screen():
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 20
        ypadding 20
        
        vbox:
            text "Мини-судоку 2x2" xalign 0.5
            
            # Простая сетка 2x2 для начала
            grid 2 2:
                spacing 10
                
                for i in range(4):
                    textbutton str(i+1):
                        action [SetVariable("sudoku_solved", True), Return()]
                        xminimum 50
                        yminimum 50

label puzzle_game:
    scene bg table
    $ pieces_placed = 0
    
    paracetamol "Собери пазл из 4 кусочков!"
    
    call screen puzzle_screen
    
    paracetamol "Отлично! Картинка собрана!"
    jump after_minigame

screen puzzle_screen():
    draggroup:
        # Целевые позиции для кусочков
        for i in range(2):
            for j in range(2):
                $ x_pos = 400 + j * 100
                $ y_pos = 200 + i * 100
                drag:
                    drag_name "target_[i]_[j]"
                    xpos x_pos
                    ypos y_pos
                    xsize 100
                    ysize 100
                    draggable False
        
        # Драг-элементы (кусочки пазла)
        for i in range(2):
            for j in range(2):
                $ x_pos = 100 + j * 110
                $ y_pos = 200 + i * 110
                drag:
                    drag_name "piece_[i]_[j]"
                    child "puzzle_piece_[i]_[j]"  # Ваши изображения кусочков
                    xpos x_pos
                    ypos y_pos
                    droppable True
                    dragged pieces_dragged

init python:
    items_data = {
        "first_shell":   {"image": "images/first_shell.png",   "thumb": "images/first_shell_under_water.png", "focus_mask": "images/first_shell_mask.png", "pos": (916, 622), "found": False},
        "second_shell":   {"image": "images/second_shell.png",   "thumb": "images/second_shell_under_water.png", "focus_mask": "images/second_shell_mask.png", "pos": (705, 784), "found": False},
        "third_shell":   {"image": "images/third_shell.png",   "thumb": "images/third_shell_under_water.png", "focus_mask": "images/third_shell_mask.png", "pos": (1317, 710), "found": False},
        "fourth_shell":   {"image": "images/fourth_shell.png",   "thumb": "images/fourth_shell_under_water.png", "focus_mask": "images/fourth_shell_mask.png", "pos": (648, 376), "found": False},
        "fifth_shell":   {"image": "images/fifth_shell.png",   "thumb": "images/fifth_shell_under_water.png", "focus_mask": "images/fifth_shell_mask.png", "pos": (1081, 177), "found": False},
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

    if all(data["found"] for data in items_data.values()):
        timer 0.1 action Return()

label start_hidden_game:
    call screen hidden_object_game

    show shells_endgame at truecenter with dissolve
    pause 5
    hide shells_endgame at truecenter with dissolve

    return