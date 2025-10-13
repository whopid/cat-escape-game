# Определяем персонажей
define mc = Character("[player_name]", color="#ffffff")
define paracetamol = Character("Парацетамол", color="#000000")


# Начало игры
label start:
    # Первая сцена
    scene bg room day
    show paracetamol happy at center
    
    paracetamol "Привет, Никель!"
    paracetamol "Сегодня нам предстоит решить несколько головоломок."
    
    jump chapter1_menu

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