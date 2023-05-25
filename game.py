import pygame


pygame.init()
screen_width, screen_height = 960, 640
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("집가고싶다") #게임이름
background = pygame.image.load("japan.jpg")


charX = 0
charY = 0
move_speed = 10

character = pygame.image.load('arm1.png')
character_resized = pygame.transform.scale(character, (int(character.get_width() * 0.1), int(character.get_height() * 0.1)))



clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
    
        #방향키 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            charX = -move_speed
        if keys[pygame.K_RIGHT]:
            charX = +move_speed
        if keys[pygame.K_UP]:
            charY = -move_speed
        if keys[pygame.K_DOWN]:
            charY = +move_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                moveX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                moveY = 0

 
    # 카메라 위치 계산
    cameraX = charX - screen_width // 2
    cameraY = charY - screen_height// 2


    # 화면 업데이트 처리
    screen.blit(background, (0, 0))
    screen.blit(character_resized, (charX - cameraX , charY - cameraY))  # 캐릭터를 화면에 표시합니다.
    pygame.display.flip()  # 업데이트된 화면을 표시합니다.
    
    # 초당 프레임 설정
    clock.tick(60)
              



pygame.quit()

