xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

def dxdy(dx, dy):
    if dx == 0 and dy != 0:
        return 0, 1
    elif dx != 0 and dy == 0:
        return 1, 0
    elif (dx, dy) == (0, 0):
        return 0, 0
    
    dx_, dy_ = map(abs, (dx, dy))

    if dx_ < dy_:
        dx_, dy_ = dy_, dx_

    while True:
        temp = dx_ % dy_
        if temp == 0:
            return dx // dy_, dy // dy_
        else:
            dx_, dy_ = dy_, temp

dx, dy = dxdy(dx, dy)

def distance(xe, xs, ye, ys):
    return ((xe - xs) ** 2 + (ye - ys) ** 2) ** 0.5

dis = distance(xe, xs, ye, ys)
while True:
    xe += dx
    ye += dy
    dis_ = distance(xe, xs, ye, ys)

    if dis_ < dis:
        dis = dis_
    else:
        xe -= dx
        ye -= dy
        break
    
print(xe, ye)
