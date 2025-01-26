import random

player = {'x': 1, 'y': 1}
coins = []
score = 0
field_size = 15

def create_coins(num):
    for _ in range(num):
        while True:
            coin = {'x': random.randint(1, field_size), 'y': random.randint(1, field_size)}
            if coin != player:
                coins.append(coin)
                break

def display():
    for y in range(1, field_size + 1):
        for x in range(1, field_size + 1):
            if x == player['x'] and y == player['y']:
                print("U", end=" ")
            elif any(coin['x'] == x and coin['y'] == y for coin in coins):
                print("C", end=" ")
            else:
                print(".", end=" ")
        print()
    print("Score:", score, "| Очки:", score)

def move_player(dx, dy):
    new_x = player['x'] + dx
    new_y = player['y'] + dy
    if 1 <= new_x <= field_size and 1 <= new_y <= field_size:
        player['x'] = new_x
        player['y'] = new_y
        check_for_coins()
    else:
        print("Cannot move outside the field! | Нельзя выйти за пределы поля!")

def check_for_coins():
    global score
    for coin in coins[:]:
        if coin['x'] == player['x'] and coin['y'] == player['y']:
            score += 1
            coins.remove(coin)
            print("Coin collected! | Монета собрана!")

num_coins = int(input("Enter the number of coins to create: | Введите количество монет для создания: "))
create_coins(num_coins)

while True:
    display()
    command = input("Enter command (w/a/s/d to move, q to quit): | Введите команду (w/a/s/d для перемещения, q для выхода): ").strip().lower()

    if command == "w":
        move_player(0, -1)
    elif command == "s":
        move_player(0, 1)
    elif command == "a":
        move_player(-1, 0)
    elif command == "d":
        move_player(1, 0)
    elif command == "q":
        print("Exiting the game. | Выход из игры.")
        break
    else:
        print("Invalid command. Please try again. | Неверная команда. Попробуйте снова.")
