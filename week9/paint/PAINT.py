import pygame

pygame.init()

W = 800
H = 600
active_size = 0
active_color = 'white'

SC = pygame.display.set_mode([W, H])
pygame.display.set_caption("PAINT")
pygame.display.set_icon(pygame.image.load('/Users/firuza/Desktop/PP2/week8/paint/1158164.png'))

painting = []



def draw_menu(size, color):  # brush size
    pygame.draw.rect(SC, 'gray', [0, 0, W, 80])
    pygame.draw.line(SC, 'black', (0, 80), (W, 80), 3)
    l_brush = pygame.draw.rect(SC, 'black', [10, 10, 50, 50])
    pygame.draw.circle(SC, 'white', (35, 35), 22)
    m_brush = pygame.draw.rect(SC, 'black', [70, 10, 50, 50])
    pygame.draw.circle(SC, 'white', (95, 35), 17)
    s_brush = pygame.draw.rect(SC, 'black', [130, 10, 50, 50])
    pygame.draw.circle(SC, 'white', (155, 35), 7)

    brush_list = [l_brush, m_brush, s_brush]

    blue = pygame.draw.rect(SC, (0, 0, 255), [W - 40, 10, 30, 30])
    red = pygame.draw.rect(SC, (255, 0, 0), [W - 40, 40, 30, 30])
    green = pygame.draw.rect(SC, (0, 255, 0), [W - 70, 10, 30, 30])
    yellow = pygame.draw.rect(SC, (255, 255, 0), [W - 70, 40, 30, 30])
    white = pygame.draw.rect(SC, (255, 255, 255), [W - 130, 10, 60, 60])

    color_rect = [blue, red, green, yellow, white]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


# def draw_shapes(cirlce,rectangle,square,equilateral_triangle,right_triangle,hombus):
#     cirlce()
#     circle_pos = pygame.mouse.get_pos()
#     circle_radius = 30
#     pygame.draw.circle(SC, active_color, circle_pos, circle_radius)
#     rectangle()
#     rect_pos = pygame.mouse.get_pos()
#     rect_width = 30
#     rect_height = 50
#     pygame.draw.rect(SC, active_color, (rect_pos, (rect_width, rect_height)))
#     square()
#     sq_pos = pygame.mouse.get_pos()
#     sq_lenght = 60
#     pygame.draw.rect(SC, active_color, (sq_pos, (sq_lenght, sq_lenght)))
#     equilateral_triangle()
#     x, y = pygame.mouse.get_pos()
#     pygame.draw.polygon(SC, active_color, [(x-50, y+50), (x, y), (x+50, y+50)])
#     right_triangle()
#     x, y = pygame.mouse.get_pos()
#     pygame.draw.polygon(SC, active_color, [(x,y), (x+50, y), (x, y-50)])
#     hombus()
#     x, y = pygame.mouse.get_pos()
#     pygame.draw.polygon(SC, active_color, [(x-30, y+20), (x, y), (x+30, y+20), (x, y+40)])


def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(SC, paints[i][0], paints[i][1],
                           paints[i][2])  # [i][0,1,2] active color,mouse,active_size имеет


run = True
circles = []

while run:

    SC.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]  # нажата что именно левая кнопка мышки
    if mouse[1] > 80:
        pygame.draw.circle(SC, active_color, mouse, active_size)
    if left_click and mouse[1] > 70:
        painting.append(
            (active_color, mouse, active_size))  # сохраняем информацию об этом круге что она должна нарисовать

    draw_painting(painting)

    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_e:
        #         rect_width = 50
        #         rect_height = 50
        #         pygame.draw.rect(SC, 'white', (mouse, (rect_width, rect_height)))

        # Rectange (t - от слова төртбұрыш)
        # if event.key == pygame.K_r:
        #     rectangle()
        # #Circle
        # if event.key == pygame.K_c:
        #     cirlce()
        # # Square
        # if event.key == pygame.K_s:
        #     square()
        # if event.key == pygame.K_t:
        #     equilateral_triangle()
        # if event.key == pygame.K_x:
        #     right_triangle()
        # if event.key == pygame.K_b:
        #     rhombus()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    # Если кнопка 'r' нажата, добавляем круг в список
    if keys[pygame.K_r]:
        circles.append(mouse_pos)
    

    # Рисуем все круги из списка
    for circle_pos in circles:
        pygame.draw.circle(SC, active_color, circle_pos, active_size)

    # Обновление экрана
    pygame.display.update()

pygame.quit()
