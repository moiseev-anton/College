"""
Используя библиотеку PIL, напишите программу, которая нарисует на
холсте рисунок светофора (использовать различные фигуры, стили, цвета)
"""

from PIL import Image, ImageDraw

def draw_traffic_light():
    # холст с белым фоном
    width, height = 200, 400
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # основа светофора
    rect_x0, rect_y0 = 50, 50
    rect_x1, rect_y1 = 150, 350
    draw.rectangle(
        [rect_x0, rect_y0, rect_x1, rect_y1],
        outline='black',
        fill='gray'
    )

    # радиус каждого сигнала
    radius = 30
    center_x = (rect_x0 + rect_x1) // 2

    # красный сигнал
    red_light_y = rect_y0 + 30
    draw.ellipse(
        [center_x - radius,
            red_light_y,
            center_x + radius,
            red_light_y + 2 * radius],
            fill='red')

    # желтый сигнал
    yellow_light_y = red_light_y + 90
    draw.ellipse(
        [center_x - radius,
            yellow_light_y,
            center_x + radius,
            yellow_light_y + 2 * radius],
            fill='yellow')

    # зеленый сигнал
    green_light_y = yellow_light_y + 90
    draw.ellipse(
        [center_x - radius,
            green_light_y,
            center_x + radius,
            green_light_y + 2 * radius],
            fill='green')

    image.save('traffic_light.png')
    image.show()


if __name__ == '__main__':
    draw_traffic_light()




