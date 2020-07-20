def in_area(image, x, y):
    return x >= 0 and x < len(image) and y >= 0 and y < len(image[0])


# 填充所有
def fill(image, x, y, orig_color, new_color):
    if not in_area(image, x, y):
        return

    if image[x][y] != orig_color:
        return

    if image[x][y] == -1:
        return

    image[x][y] = -1

    fill(image, x, y + 1, orig_color, new_color)
    fill(image, x, y - 1, orig_color, new_color)
    fill(image, x + 1, y, orig_color, new_color)
    fill(image, x - 1, y, orig_color, new_color)

    image[x][y] = new_color


# 填充所有
def fill_boundary(image, x, y, orig_color, new_color, visited):
    if not in_area(image, x, y):
        return 0

    if visited[x][y]:
        return 1

    if image[x][y] != orig_color:
        return 0

    visited[x][y] = True
    surround = fill_boundary(image,
                             x,
                             y + 1,
                             orig_color,
                             new_color,
                             visited) + fill_boundary(image,
                                                      x,
                                                      y - 1,
                                                      orig_color,
                                                      new_color,
                                                      visited) + fill_boundary(image,
                                                                               x + 1,
                                                                               y,
                                                                               orig_color,
                                                                               new_color,
                                                                               visited) + fill_boundary(image,
                                                                                                        x - 1,
                                                                                                        y,
                                                                                                        orig_color,
                                                                                                        new_color,
                                                                                                        visited)

    if surround < 4:
        image[x][y] = new_color
    return 1


def flood_fill(image, x, y, new_color):
    orig_color = image[x][y]
    visited = image.copy()
    for i in range(len(image)):
        visited[i] = [False] * len(image)
    fill_boundary(image, x, y, orig_color, new_color, visited)
    return image


if __name__ == "__main__":
    image = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    x = 1
    y = 1
    new_color = 2
    print(flood_fill(image, x, y, new_color))
