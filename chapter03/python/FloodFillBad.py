def in_area(image, x, y):
    return (x >= 0 and x < len(image)) and \
        (y >= 0 and y < len(image[0]))


def is_boundary(image, x, y, orig_color):
    coord = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for tmp_x, tmp_y in coord:
        if in_area(image, tmp_x, tmp_y) and image[tmp_x][tmp_y] != orig_color and image[tmp_x][tmp_y] != -1:
            return True
    return False


def fill(image, x, y, orig_color, new_color):
    if image[x][y] != orig_color:
        return
    if image[x][y] == -1:
        return
    image[x][y] = -1

    coord = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for tmp_x, tmp_y in coord:
        if in_area(image, tmp_x, tmp_y) and \
                (image[tmp_x][tmp_y] == orig_color):
            fill(image, tmp_x, tmp_y, orig_color, new_color)
    image[x][y] = new_color


def fill_boundary(image, x, y, orig_color, new_color):
    if image[x][y] != orig_color:
        return
    if image[x][y] == -1:
        return
    if is_boundary(image, x, y, orig_color):
        image[x][y] = -1
        coord = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for tmp_x, tmp_y in coord:
            if in_area(image, tmp_x, tmp_y) and \
                    (image[tmp_x][tmp_y] == orig_color):
                fill_boundary(image, tmp_x, tmp_y, orig_color, new_color)
        image[x][y] = new_color
    else:
        return

# 把所以连通[x, y]且像素值为origin的像素染成new
def flood_fill(image, x, y, orig_color, new_color):
    if orig_color == new_color:
        return image
    fill_boundary(image, x, y, orig_color, new_color)
    return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    x = 1
    y = 1
    orig_color = image[x][y]
    new_color = 2
    print(flood_fill(image, x, y, orig_color, new_color))
