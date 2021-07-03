import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont('cambria', 28)
font2 = pygame.font.SysFont('cambria', 40)
username1 = ""
text2 = font.render("Enter your username: ", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username1 = username1[:-1]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_RETURN:
                if username1 == "":
                    default = "Anonymous"
                    username1 = default
                running = False
            else:
                username1 += event.unicode
    screen.fill((0, 0, 0))
    text3 = font.render(username1, True, (150, 0, 0))
    screen.blit(text3, (730, 500))
    screen.blit(text2, (430, 500))
    font1 = pygame.font.Font('freesansbold.ttf', 150)
    font2 = pygame.font.SysFont('cambria', 40)
    text = font1.render("Game Over", True, (255, 255, 255))
    from game import level, score
    text1 = font2.render("Your score was "+str(level*100 + score), True, (255, 255, 255))
    screen.blit(text, (220, 180))
    screen.blit(text1, (460, 400))
    pygame.display.flip()
