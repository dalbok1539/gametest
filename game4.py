import pygame

pygame.init()
screen_width, screen_height = 960, 640
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("집가고싶다")  # 게임이름

character = pygame.image.load('arm1.png')
character_resized = pygame.transform.scale(character, (int(character.get_width() * 0.1), int(character.get_height() * 0.1)))
char_width = character_resized.get_width()
char_height = character_resized.get_height()

background = pygame.image.load("japan.jpg")
background_width = background.get_width()
background_height = background.get_height()

charX = screen_width // 2
charY = screen_height // 2
move_speed = 10

clock = pygame.time.Clock()

# 충돌 감지 함수
def check_collision(character_rect, background_rect):
    if character_rect.colliderect(background_rect):
        return True
    return False

running = True
moveX = 0
moveY = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 방향키 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -move_speed
            elif event.key == pygame.K_RIGHT:
                moveX = move_speed
            elif event.key == pygame.K_UP:
                moveY = -move_speed
            elif event.key == pygame.K_DOWN:
                moveY = move_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                moveX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                moveY = 0

    # 캐릭터 위치 업데이트
    charX += moveX
    charY += moveY

    # 캐릭터 이동 범위 제한
    if charX < 0:
        charX = 0
    elif charX > background_width - char_width:
        charX = background_width - char_width

    if charY < 0:
        charY = 0
    elif charY > background_height - char_height:
        charY = background_height - char_height

    # 카메라 위치 계산
    cameraX = screen_width // 2 - charX
    cameraY = screen_height // 2 - charY

    # 충돌 감지 및 이동 제한
    character_rect = pygame.Rect(charX, charY, char_width, char_height)
    background_rect = pygame.Rect(0, 0, background_width, background_height)

    if check_collision(character_rect, background_rect):
        # 충돌 발생 시 캐릭터의 이동을 조정
        charX -= moveX
        charY -= moveY

    screen.blit(background, (cameraX, cameraY))  # 배경을 카메라 위치에 맞게 그립니다.
    screen.blit(character_resized, (charX, charY))  # 캐릭터를 화면에 표시합니다.
    pygame.display.flip()  # 업데이트된 화면을 표시합니다.
    clock.tick(60)

pygame.quit()
