local player = {x = 1, y = 1}
local coins = {}
local score = 0
local fieldSize = 15

function createCoins(num)
    for i = 1, num do
        local coin
        repeat
            coin = {x = math.random(1, fieldSize), y = math.random(1, fieldSize)}
        until (coin.x ~= player.x or coin.y ~= player.y)
        table.insert(coins, coin)
    end
end

function display()
    for y = 1, fieldSize do
        for x = 1, fieldSize do
            if x == player.x and y == player.y then
                io.write("U ")
            else
                local coinFound = false
                for _, coin in ipairs(coins) do
                    if coin.x == x and coin.y == y then
                        io.write("C ")
                        coinFound = true
                        break
                    end
                end
                if not coinFound then
                    io.write(". ")
                end
            end
        end
        print()
    end
    print("Очки: " .. score .. " | Score: " .. score)
end

function movePlayer(dx, dy)
    local newX = player.x + dx
    local newY = player.y + dy
    if newX >= 1 and newX <= fieldSize and newY >= 1 and newY <= fieldSize then
        player.x = newX
        player.y = newY
        checkForCoins()
    else
        print("Нельзя выйти за пределы поля! | Cannot move outside the field!")
    end
end

function checkForCoins()
    for i = #coins, 1, -1 do
        if coins[i].x == player.x and coins[i].y == player.y then
            score = score + 1
            table.remove(coins, i)
            print("Монета собрана! | Coin collected!")
        end
    end
end

print("Введите количество монет для создания: | Enter the number of coins to create:")
local numCoins = tonumber(io.read())
createCoins(numCoins)

while true do
    display()
    print("Введите команду (w/a/s/d для перемещения, q для выхода): | Enter command (w/a/s/d to move, q to quit):")
    local command = io.read()

    if command == "w" then
        movePlayer(0, -1)
    elseif command == "s" then
        movePlayer(0, 1)
    elseif command == "a" then
        movePlayer(-1, 0)
    elseif command == "d" then
        movePlayer(1, 0)
    elseif command == "q" then
        print("Выход из игры. | Exiting the game.")
        break
    else
        print("Неверная команда. Попробуйте снова. | Invalid command. Please try again.")
    end
end
