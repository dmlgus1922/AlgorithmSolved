t = int(input())

buttons = {300:0, 60:0, 10:0}

for button in buttons.keys():
    count = t // button
    t -= count * button
    buttons[button] = count

if not t:
    print(*buttons.values(), sep = ' ')
else:
    print(-1)