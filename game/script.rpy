# Определяем персонажей
define mc = Character("[player_name]", color="#ffffff")
define n = Character("Ник", color="#ffffff")
define p = Character("Парацетамол", color="#ffff9b")
define rtut = Character("Ртуть", color="#91cdff")
define ch = Character("Хлор", color="#ffbc49")
define golos = Character("Голос из комнаты", color="#42fffc")
define kasper = Character("Каспер", color="42fffc")
define kin = Character("Кин", color="#afff53")


# Начало игры
label start:
    # Первая сцена
    scene black_bg

    # Черный экран
    scene black
    with fade

    # Медленно появляющийся текст
    show text "{size=40}Что произошло?.. Кто я?.. Где я?.. Последнее, что я помню… яркий свет… разные голоса…" with dissolve
    pause 
    hide text with dissolve
 
    # Плавное прояснение сцены (комната глазами кота)
    scene nik_room with fade
    n "Никель?.. Э-э… Я?..."

    # Черный экран с текстом имени
    scene black with fade
    show text "{size=40}Точно. Меня зовут Никель." with dissolve
    pause 
    hide text with dissolve

    # Переход к нормальной сцене с котом
    scene location1_bg with fade

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
    show text "{size=40}Никель осторожно движется по коридору. По стенам — большие аквариумы с причудливыми водорослями, которые подсвечиваются неестественным светом." with dissolve
    pause 
    hide text with dissolve

    # Фон 1 — коридор с аквариумами
    scene corridor_aquariums with fade
    show nickel neutral at Position(xalign=0.2, yalign=0.9) with dissolve

    n "Аквариумы? Растения? Интересно… для чего они тут?.."
    n "Странное чувство, словно за мной кто-то наблюдает..."

    # Смена сцены — напряжённый момент
    scene black with fade
    show text "{size=40}Ник замирает, почувствовав движение в конце коридора." with dissolve
    pause
    show text"{size=40}Сначала он видит лишь две точки света — ярко-зеленые, фосфоресцирующие глаза, отражающие свет аквариумов.\nОни неподвижно смотрят на него из темноты.\nЗатем силуэт кота медленно отделяется от тени и бесшумно приближается." with dissolve
    pause 
    hide text with dissolve

    # Фон 2 — появляется Парацетамол
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
    show text "{size=40}Какой странный кот… Надеюсь, мне еще повезет встретить \nздесь кого-нибудь адекватного… в своём уме." with dissolve
    pause 
    hide text with dissolve

    show text "{size=40}Что за звук? Вода?" with dissolve
    pause 
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
    show text "{size=40}Из воды выплывает выдра." at truecenter with dissolve
    pause 
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
    show text "{size=40}Ник решает помочь Ртути собрать ракушки..." at truecenter with dissolve
    pause 
    hide text with dissolve
    scene black with fade

    #правила игры
    show rules_shells at truecenter with dissolve
    pause 
    hide rules_shells with dissolve

    #!!!!ПОСЛЕ ЭТИХ СЛОВ НАДО ДОБАВИТЬ ИГРУ ПОИСК РАКУШЕК!!!!

    scene pool_bg with fade
    show rtut neutral at Position(xalign=0.27, yalign=0.96) with dissolve
    show nickel neutral at Position(xalign=-0.02, yalign=0.9) with dissolve
    rtut "Отличная командная работа! Теперь моя очередь!"

    # --- Конец сцены ---
    scene black with fade
    show text "{size=40}Ртуть помогла Нику переплыть на другую сторону бассейна. Он отправляется дальше…" at truecenter with dissolve
    pause 
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
    show text "{size=40}Ник идёт дальше.\n\nНеожиданно под лапами начинают попадаться сухие веточки и листья..." at truecenter with dissolve
    pause 
    hide text with dissolve

    show text "{size=40}Он видит приоткрытую дверь, из которой доносится запах свежей травы." at truecenter with dissolve
    pause 
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

    ch "Услышал тебя, друг мой… Есть у меня {color=#F0E68C}{b}седьмое{/b}{/color=#F0E68C} чудо света, будто бы очень важное... Представляешь, я его терял и находил, а потом снова терял и находил… и так {color=#F0E68C}{b}семь{/b}{/color=#F0E68C} раз…" 
    ch "Друг, и такое бывает. А потом я его сломал. И да, друг, {color=#F0E68C}{b}семь раз{/b}{/color=#F0E68C} . Возьми его и обязательно используй только с умом! Береги это! Это больше…"

    n "(Горстка кусочков?.. Спасибо тут не скажешь)"
    n "О, хорошо."

    scene black with fade
    show text "{size=40}Хлор немного приподнимается, потягивается, выгибает спинку и задней лапкой чешет за ушком.\n\nЛениво поворачивается, достает из-под коры кусочки ключ-карты и медленно протягивает их Нику." at truecenter with dissolve
    pause 
    hide text with dissolve

    # --- Системная вставка: начало мини-игры ---
    show rules_puzzle at truecenter with dissolve
    pause
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

    jump scene_5
    return

label scene_5:

    # Черный экран с текстом
    scene black
    with fade

    centered "{size=40}Ник, с собранной ключ-картой в лапах, с трудом добрался до опушки."
    centered "{size=40}Воздух здесь был странно тяжёлым и густым, от него кружилась голова и плыли пятна перед глазами.  
    С трудом различив в листве контуры двери, он приложил карту к панели." 
    centered "{size=40}Дверь бесшумно открылась."
    # ФОН 1 — будка без кота
    scene bg_perforator_room_empty
    with fade

    n "Как ярко… Мигают лампочки… Голова все еще кружится…"

    golos "Приветствую! Обнаружен неизвестный пользователь! (^ω^)"
    n "О нет, у меня начались голосовые галлюцинации…"
    golos "Ошибка распознавания ответа. Для взаимодействия посмотрите на центральный монитор."
    n "…"

    # ФОН 2 — будка с котом на экране
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

    # --- Системная вставка: начало мини-игры ---
    scene black with fade
    show rules_sudoku at truecenter with dissolve
    pause 10
    hide rules_sudoku with dissolve

    # --- здесь появится экран Судоку ---
    #call sudoku_minigame

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

    # Появляется карта
    scene karta_kasper with fade
    pause
    jump scene_6
    return

label scene_6:

    scene black with fade
    centered "{size=40}Ник долго плутал, внимательно считая повороты, и наконец очутился в коридоре, залитом сиреневым цветом, вдоль которого росли цветы.\nНе спатифиллумы…"

    # ФОН 1 — коридор
    scene corridor_flowers_1 with dissolve

    n "Так это тот самый коридор, о котором говорил Каспер."
    n "(Зеркало? Это что, я?.. Но почему звезда?)"
    n "(Стоит проверить… Пошевелю хвостом... Как же странно это странно.)"

    scene black with fade
    centered "{size=40}После его движения отражение в «зеркале» улыбается.\nНик замирает, понимая, что перед ним — не зеркало, а другой кот, очень на него похожий." with dissolve

    # ФОН 2 — коридор с «зеркальным» котом
    scene corridor_flowers_2 with dissolve

    kin "Удивился? Извини, немного заигрался. Понимаешь, этот коридор принадлежит мне."
    kin "Здесь мои правила. Нужно отгадать загадки, если хочешь пройти."

    # -------------------------
    # ПЕРВАЯ ЗАГАДКА
    # -------------------------


    kin "Неплохо. Тогда вот вторая."

    # -------------------------
    # ВТОРАЯ ЗАГАДКА
    # -------------------------

    # ФОН — Ник и Кин

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

    # -------------------------
    # ТРЕТЬЯ ЗАГАДКА

    scene black with fade
    centered "{size=40}Едва Ник выдавливает ответ, Кин с яростным шипением бросается на него — и растворяется в воздухе, словно его никогда и не было" with dissolve
    centered "{size=40}Ник стоит, дрожа всем телом. \n Голос Кина продолжает звучать у него в голове: «Ты никуда не денешься от себя...»" with dissolve

    centered "{size=40}Собрав всю волю в лапки, Ник разворачивается и бежит к единственной двери в конце коридора, 
    чувствуя, как паника сжимает ему горло. Сердце бешено колотиться, а в ушах стоит звон." with dissolve

    centered "{size=40}Он подбегает к двери - и видит массивный замок с панелью для кода. \n Ловушка? Или последнее испытание?" with dissolve


    # Переход к следующей сцене
    jump scene_7
    return

label scene_7:

    scene lock_background with fade
    n "(Замок? Нужно подобрать код... Но какой?)"
    n "…"
    n "(Тот странный кот в самом начале... Парацетамол... Что он говорил?)"
    n "«Остерегайся числа 4»..."
    n "(Почему четверки? Может, в ней и есть ключ?)"

    jump ending_scene


# -----------------------------
# ФИНАЛ
# -----------------------------
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