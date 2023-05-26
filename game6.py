import pygame

pygame.init()
screen_width, screen_height = 960, 640
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("집가고싶다")  # 게임이름
background = pygame.image.load("japan.jpg")

charX = screen_width // 2
charY = screen_height // 2
move_speed = 5

character = pygame.image.load('arm1.png')
character_resized = pygame.transform.scale(character, (int(character.get_width() * 0.1), int(character.get_height() * 0.1)))

clock = pygame.time.Clock()

# 충돌 감지 함수
def check_collision(character_rect, background_rect):
    if character_rect.colliderect(background_rect):
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 방향키 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        charX -= move_speed
    if keys[pygame.K_RIGHT]:
        charX += move_speed
    if keys[pygame.K_UP]:
        charY -= move_speed
    if keys[pygame.K_DOWN]:
        charY += move_speed

    # 카메라 위치 계산
    cameraX = screen_width // 2 - charX
    cameraY = screen_height // 2 - charY

    # 충돌 감지 및 이동 제한
    character_rect = pygame.Rect(charX, charY, character_resized.get_width(), character_resized.get_height())
    background_rect = pygame.Rect(cameraX, cameraY, screen_width, screen_height)

    if check_collision(character_rect, background_rect):
        # 충돌 발생 시 캐릭터의 이동을 조정
        charX -= move_speed if keys[pygame.K_LEFT] else 0
        charX += move_speed if keys[pygame.K_RIGHT] else 0
        charY -= move_speed if keys[pygame.K_UP] else 0
        charY += move_speed if keys[pygame.K_DOWN] else 0

    screen.blit(background, (cameraX, cameraY))  # 배경을 카메라 위치에 맞게 그립니다.
    screen.blit(character_resized, (screen_width // 2, screen_height // 2))  # 캐릭터를 화면 중앙에 표시합니다.
    pygame.display.flip()  # 업데이트된 화면을 표시합니다.
    clock.tick(120)

pygame.quit()
