import pygame
import numpy as np
import time

bg_color = (10, 10, 10)
grid_color = (40, 40, 40)
die_color = (170, 170, 170)
alive_color = (255, 255, 255)

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row,col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = bg_color if cells[row, col] == 0 else alive_color

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = die_color
            elif 2 <= alive <= 3: #stays alive 
                updated_cells[row, col] = 1
                if with_progress:
                    color = alive_color
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = alive_color


        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80)) 
    screen.fill(grid_color)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                cells[y//10, x//10] = 1

                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(grid_color)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()
        
        time.sleep(0.001)

if __name__ == "__main__":
    main()