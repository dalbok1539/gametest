import pygame

pygame.init()
screen = pygame.display.set_mode([960, 640])
pygame.display.set_caption("집가고싶다")  # 게임 제목
background = pygame.image.load("japan.jpg")

charX = 0
charY = 0

character = pygame.image.load('arm1.png')
character_resized = pygame.transform.scale(character, (int(character.get_width() * 0.1), int(character.get_height() * 0.1)))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 방향키 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                charY -= 10
            elif event.key == pygame.K_s:
                charY += 10
            elif event.key == pygame.K_a:
                charX -= 10
            elif event.key == pygame.K_d:
                charX += 10

    screen.blit(background, (0, 0))  # 배경을 다시 그립니다.
    screen.blit(character_resized, (charX, charY))  # 캐릭터를 화면에 표시합니다.
    pygame.display.flip()  # 업데이트된 화면을 표시합니다.
    clock.tick(60)

pygame.quit()
