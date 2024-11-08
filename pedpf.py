import random

# Начальная информация о игре
def print_intro():
    print("Ты оказался в таинственном замке. Твоя цель — выбраться из него, но для этого тебе нужно решить загадки, победить монстров и разобраться в тёмных тайнах этого места.")
    print("В каждой комнате тебя ждёт новая задача, а в некоторых — неожиданные повороты судьбы.\n")

# Вспомогательные функции для отображения инвентаря и здоровья
def show_inventory(inventory):
    print("Твой инвентарь:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Инвентарь пуст.")
    print()

def show_health(health):
    print(f"Здоровье: {health}\n")

# Уровень 1: Найти ключи и открыть дверь
def level_1(inventory):
    print("\nТы находишься в первой комнате. В комнате темно, но ты видишь несколько предметов на столе.")
    print("Ты видишь ключи и записку. На записке написано: 'Ключи от двери, если ты их найдешь.'")
    
    if "ключи" not in inventory:
        action = input("Что ты будешь делать? (взять ключи, осмотреть комнату): ").lower()
        if action == "взять ключи":
            inventory.append("ключи")
            print("Ты взял ключи.")
        else:
            print("Ты осматриваешь комнату, но ничего не нашел.")
    
    if "ключи" in inventory:
        action = input("Теперь ты видишь дверь, но она заперта. Попробуешь открыть её? (да/нет): ").lower()
        if action == "да":
            print("Ты использовал ключи и открыл дверь! Переходишь в следующую комнату.\n")
            return True
        else:
            print("Ты не открыл дверь. Попробуй снова.")
            return False
    else:
        print("Ты не можешь открыть дверь без ключей.")
        return False

# Уровень 2: Победить монстра
def level_2(inventory, health):
    print("\nТы попал во вторую комнату. Темно, и ты слышишь странные звуки.")
    print("Внезапно появляется монстр — Огромный паук!")

    # Если у игрока нет меча, он не может победить монстра
    if "меч" not in inventory:
        action = input("Что ты будешь делать? (исследовать, убежать): ").lower()
        if action == "исследовать":
            # Если игрок решит исследовать, он находит меч
            print("Ты нашел меч! Теперь ты можешь сразиться с монстром.")
            inventory.append("меч")
        elif action == "убежать":
            print("Ты убегал, но паук поймал тебя! Ты теряешь 10 здоровья.")
            health -= 10
            return level_2(inventory, health)  # Возвращаем в начало уровня
        else:
            print("Ты не решился на действия и не сделал ничего.")
            return level_2(inventory, health)  # Возвращаем в начало уровня
    
    # После того, как игрок нашел меч, он может попробовать сразиться с монстром
    if "меч" in inventory:
        action = input("Теперь ты можешь сразиться с монстром. Попробуешь? (да/нет): ").lower()
        if action == "да":
            print("Ты сразился с монстром и победил его с помощью меча!")
            return health  # Возвращаем обновленное здоровье
        else:
            print("Ты не победил монстра. Попробуй снова.")
            return level_2(inventory, health)  # Возвращаем в начало уровня
    else:
        # Если у игрока нет меча, он не может победить монстра
        print("Ты не можешь победить монстра без меча.")
        return level_2(inventory, health)  # Возвращаем в начало уровня

# Уровень 3: Загадка и встреча с NPC
def level_3(inventory, health):
    print("\nТы входишь в третью комнату. Внезапно дверь закрывается, и ты оказываешься в ловушке!")
    print("На стене появляется загадка: 'У меня есть ключ, но ты не можешь меня открыть. Что я?'")
    
    # Игрок решает загадку
    answer = input("Твой ответ: ").lower()
    if answer == "сердце":
        print("Ты правильно разгадал загадку! Старику понравилось твое решение.")
        print("Теперь, когда ты решил загадку, появляется старик...")
        
        # Теперь начинается диалог со стариком
        print("\nТы встречаешь загадочного старика, который сидит у огня и смотрит на тебя своими мудрыми глазами.")
        print("Он говорит: 'Ты на грани решения великой судьбы. Вижу, ты ищешь выход.'")
        
        action = input("Ты решаешь подойти к старику. Он продолжает: 'Ты готов к следующему шагу?' (да/нет): ").lower()
        
        if action == "да":
            print("\nСтарик кидает тебе загадку: 'Я всегда впереди тебя, но ты меня не видишь. Что это?'")
            answer = input("Твой ответ: ").lower()
            
            if answer == "будущее":
                print("Ты правильно разгадал загадку! Старику понравилось твое решение, и он открывает скрытую дверь.")
                print("Ты входишь в скрытую комнату и находишь мощное оружие — магический меч, который значительно улучшает твою атаку.")
                inventory.append("магический меч")
                print("Теперь у тебя есть магический меч! Он может помочь тебе в борьбе с Лордом Замка.")
            else:
                print("Неправильный ответ! Ты теряешь 20 здоровья.")
                health -= 20
        else:
            print("Ты не готов к следующему шагу. Старик исчезает.")
    else:
        print("Неправильный ответ! Ты теряешь 20 здоровья.")
        health -= 20
        return level_3(inventory, health)
    
    return inventory, health


# Уровень 4: Сражение с Лордом Замка
def level_4(inventory, health):
    print("\nТы пришел к последней двери замка. Здесь стоит огромный монстр — Лорд Замка.")
    print("Он предупреждает тебя: 'Ты почти на грани победы, но мне не понравилось, как ты забрал силу от старика.'")
    
    if "магический меч" in inventory:
        action = input("Ты готов сразиться с Лордом Замка? (да/нет): ").lower()
        if action == "да":
            print("Ты сражаешься с Лордом Замка с помощью магического меча!")
            print("Ты одержал победу! Замок разрушен, и ты избежал его ужасных ловушек.")
        else:
            print("Ты не сразился с Лордом Замка. Возможно, ты упустил шанс...")
    else:
        print("Ты не получил магический меч, и Лорд Замка слишком силен для тебя.")
        print("Ты не смог победить Лорда. Замок поглотил тебя.")
    
    return health



# Уровень 5: Финальная битва
def level_5(inventory, health):
    print("\nТы пришел к последней двери замка. Здесь стоит огромный монстр — Лорд Замка.")
    print("Он предупреждает тебя: 'Ты почти на грани победы, но мне не понравилось, как ты забрал силу от старика.'")
    
    if "меч" in inventory:
        action = input("Ты готов сразиться с Лордом Замка? (да/нет): ").lower()
        if action == "да":
            print("Ты сражаешься с Лордом Замка! Битва тяжелая, но ты побеждаешь его.")
            health -= 30  # Урон от босса
            if health > 0:
                print("Ты победил Лорда Замка и открыл последний выход. Ты спасся!")
                return True
            else:
                print("Ты погиб в последней битве.")
                return False
        else:
            print("Ты решил не сражаться. Лорд Замка атакует тебя.")
            health -= 40
            return False
    else:
        print("Ты не можешь победить Лорда Замка без меча.")
        return False

# Главная функция игры
def start_game():
    inventory = []  # инвентарь игрока
    health = 100  # здоровье игрока
    print_intro()
    
    # Уровень 1
    while not level_1(inventory):
        pass

    # Уровень 2
    while health > 0 and not level_2(inventory, health):
        health = level_2(inventory, health)
        if health <= 0:
            print("Ты погиб, не справившись с монстрами.")
            return

    # Уровень 3
    while health > 0 and not level_3(inventory, health):
        health = level_3(inventory, health)
        if health <= 0:
            print("Ты погиб в ловушке.")
            return

    # Уровень 4
    while health > 0 and not level_4(inventory, health):
        health = level_4(inventory, health)
        if health <= 0:
            print("Ты погиб, потеряв здоровье.")
            return

    # Уровень 5 (финальная битва)
    if not level_5(inventory, health):
        print("Ты проиграл в финальной битве.")
    else:
        print("Поздравляю! Ты победил и выбрался из замка!\n")

# Запуск игры
start_game()
