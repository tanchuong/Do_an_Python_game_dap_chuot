import pgzrun
import pygame
import random

# tạo khung hình + tiêu đề game
WIDTH = 1010
HEIGHT = 590
TITLE = 'Game đập chuột'

# thêm hình nền
bg = Actor('background')

#màn hình star game
bg_start = Actor('start_0')
bg_start_1 = Actor('start_1')
bg_start.pos = (505,400)
bg_start_1.pos = (505,400)

#màn hình game over
bg_playagain = Actor('playagain_0')
bg_playagain_1 = Actor('playagain_0')
bg_playagain.pos = (505,450)
bg_playagain_1.pos = (505,450)

# thêm chuột và vị trí lần đầu tiên xuất hiện
mouse = Actor('mouse_0')
mouse.pos = (random.randint(100,900),random.randint(100,500))

#cài đặt thời gian chơi game
choose_time = Actor('time')
choose_time.pos = (350,50)

up_time_0 = Actor('cong_0')
up_time_1 = Actor('cong_1')
up_time_0.pos = (500, 60)
up_time_1.pos = (500, 60)

down_time_0 = Actor('tru_0')
down_time_1 = Actor('tru_1')
down_time_0.pos = (670,60)
down_time_1.pos = (670,60)

# cài đặt mục tiêu chơi game
choose_target = Actor('target')
choose_target.pos = (340,190)

up_target_0 = Actor('cong_target_0')
up_target_1 = Actor('cong_target_1')
up_target_0.pos = (500,190)
up_target_1.pos = (500,190)

down_target_0 = Actor('tru_target_0')
down_target_1 = Actor('tru_target_1')
down_target_0.pos = (670,190)
down_target_1.pos = (670,190)

win = Actor('youwin')
win.pos = (505,300)

lose = Actor('youlose')
lose.pos = (505,300)

# thêm hình búa
player = Actor('hammer_0')

# thêm nhạc nền
sound_background = pygame.mixer.Sound('sounds/ngau_hung.wav')
sound_background.play(-1)
sound_background.set_volume(0.2)

#khai báo điều kiện để bắt đầu và kết thúc game
star_game = False
game_over = False

def mouse_location():
    """
        input: 
            Hình ảnh chuột
            Gọi lại hàm mouse_location sau mỗi 1,5s
        output: 
            Vị trí chuột xuất hiện ngẫu nhiên sau 1,5s
    """
    mouse.image = 'mouse_0' 
    mouse.pos = (random.randint(100,900),random.randint(100,500))
clock.schedule_interval(mouse_location, 1.5)    


def hammer():
    """
        input: 
            Hình ảnh búa ban đầu
        output: 
            Sau khi click thì hàm này 
            được gọi vào hàm on_mouse_move
            và thay thế thành hình búa đập xuống
    """
    player.image = 'hammer_0' 


def on_mouse_move():
    """
        input: 
            Lấy vị trí của con trỏ chuột
        output: 
            - Hiển thị chiếc búa theo vị trí con trỏ chuột
            - Chữ PLAY, chữ PLAYAGAIN, nút tăng giảm thời gian
            và mục tiêu cho game sẽ đổi màu khi trỏ chuột vào
    """
    mouse_x ,  mouse_y = pygame.mouse.get_pos()
    player.pos = (mouse_x, mouse_y)
    
    if bg_start.collidepoint(mouse_x, mouse_y):     #thay hình chữ PLAY
        bg_start.image = 'start_1'
    else:
        bg_start.image = 'start_0'

    if bg_playagain.colliderect(player):        #thay hình chữ Play Again
        bg_playagain.image = 'playagain_1'
    else:
        bg_playagain.image = 'playagain_0'
        
    if up_time_0.collidepoint(mouse_x, mouse_y):   #thay hình dấu cộng time
        up_time_0.image = 'cong_1' 
    else: 
        up_time_0.image = 'cong_0'
    
    if down_time_0.collidepoint(mouse_x, mouse_y):    #thay hình dấu trừ time
        down_time_0.image = 'tru_1' 
    else: 
        down_time_0.image = 'tru_0'
        
    if up_target_0.collidepoint(mouse_x, mouse_y):     #thay hình dấu cộng target
        up_target_0.image = 'cong_target_1'  
    else: 
        up_target_0.image = 'cong_target_0'

    if down_target_0.collidepoint(mouse_x, mouse_y):  #thay hình dấu trừ target
        down_target_0.image = 'tru_target_1' 
    else: 
        down_target_0.image = 'tru_target_0'

#khai báo time,target,score
time_up = 0
target = 0
score = 0
def on_mouse_down():
    """
        input: 
            Các đối tượng cần kiểm tra khi click (chuột, búa và các nút điều khiển trong game)
        output: 
            Khi click để chơi game
            Hình hammer_1 sẽ thay thế cho hình búa ban đầu và 0.2s sẽ trở lại hình búa ban đầu
            Khi va chạm sẽ cộng điểm, tạo ra âm thanh khi va chạm, gọi lại hàm mouse_location ngay sau đó
            Có thể cài đặt thời gian chơi game và mục tiêu theo ý thích hoặc chơi theo mặc định đã cài sẵn trong game
    """
    global score, star_game, game_over, time_count_down, time_up, target
    player.image = 'hammer_1'   
    clock.schedule_unique(hammer, 0.2)  
    
    if mouse.colliderect(player):  
        mouse.image = 'mouse_1' 
        score+=1
        sound = pygame.mixer.Sound('sounds/hammering.wav')
        sound.play()
    
    if up_time_1.colliderect(player):
        time_up+=5
    if down_time_1.colliderect(player):
        time_up-=5
        if time_up <=0:
            time_up = 0
    
    if up_target_1.colliderect(player):
        target+=1
    if down_target_1.colliderect(player):
        target-=1
        if target <=0:
            target = 0
            
    if bg_start_1.colliderect(player) and time_up > 0 and target > 0: #bắt đầu chơi theo thời gian đã chọn
        star_game = True
        game_over = False
        time_count_down = time_up
        score = 0
        bg_start_1.move_ip(10000,10000)
        up_time_1.move_ip(10000,10000)
        down_time_1.move_ip(10000,10000)
        up_target_1.move_ip(10000,10000)
        down_target_1.move_ip(10000,10000)
    
    if bg_start_1.colliderect(player) and time_up == 0 and target == 0:  #mặc định cho game khi ko chọn thời gian là 20s
        star_game = True
        game_over = False
        score = 0
        time_count_down = 20
        bg_start_1.move_ip(10000,10000) 
        up_time_1.move_ip(10000,10000)
        down_time_1.move_ip(10000,10000)
        up_target_1.move_ip(10000,10000)
        down_target_1.move_ip(10000,10000)
        
    if bg_playagain_1.colliderect(player) and time_up > 0 and target > 0: # khi click vào chữ Play again để chơi lại
        star_game = True
        game_over = False
        score = 0
        time_count_down = time_up
        bg_start_1.move_ip(10000,10000) 
        up_time_1.move_ip(10000,10000)
        down_time_1.move_ip(10000,10000)
        up_target_1.move_ip(10000,10000)
        down_target_1.move_ip(10000,10000)


time_count_down = -2
def time():
    """
        input: 
            Truyền vào giá trị time_count_down
            Gọi lại hàm time sau mỗi giây
        output: 
            trả về giá trị time_count_down sau mỗi giây
            khi thời gian về 0 thì kết thúc game
    """
    global time_count_down, game_over
    if True:
        time_count_down -=1
        if time_count_down == 10:
            sound = pygame.mixer.Sound('sounds/count_down.wav')
            sound.play()
    if time_count_down == -1:
        game_over = True
clock.schedule_interval(time, 1)


def update():
    """
        input: 
            Vị trí các nút điều khiển khi kết thúc game
        output: 
            Chuyển vị trí các nút điều khiển ra khỏi màn hình 
            tránh khi click chuột làm thay đổi các thông số
            score, target, time trong quá trình chơi game  
    """
    if game_over == True:
        bg_playagain_1.pos = (505,450)
        up_time_1.pos = (500, 60)
        down_time_1.pos = (670,60)
        up_target_1.pos = (500,190)
        down_target_1.pos = (670,190)
    else:
        bg_playagain_1.move_ip(10000,10000)

def draw():
    """
        input: 
            Các dữ liệu hình ảnh, điểm số, mục tiêu, 
            kiểm tra điều kiện thắng thua của game
        output: 
            Hiển thị dữ liệu hình ảnh, điểm số, mục tiêu ra màn hình
            Màn hình thắng thua khi chơi game
    """
    bg.draw()
    
    if  not star_game and not game_over:
        bg_start.draw()
        choose_time.draw()
        up_time_0.draw()
        down_time_0.draw()
        choose_target.draw()
        up_target_0.draw()
        down_target_0.draw()
        screen.draw.text(str(time_up) ,(570,40), color='red', fontsize=60)
        screen.draw.text(str(target) ,(570,170), color='red', fontsize=60)
    else:
        mouse.draw()
        player.draw()
        screen.draw.text('Score: ' + str(score) ,(100,20), color='yellow', fontsize=60)
        screen.draw.text('Target: ' + str(target) ,(450,20), color='yellow', fontsize=60)
        screen.draw.text('Time: ' + str(time_count_down) ,(800,20), color='red', fontsize=60)
        
    if game_over == True: # khi chơi mặc định thì sẽ ko có win hay lose
        bg.draw()
        choose_time.draw()
        up_time_0.draw()
        down_time_0.draw()
        choose_target.draw()
        up_target_0.draw()
        down_target_0.draw()
        screen.draw.text('Your Score: ' + str(score) ,(280,270), color='red', fontsize=100)
        screen.draw.text(str(time_up) ,(570,40), color='red', fontsize=60)
        screen.draw.text(str(target) ,(570,170), color='red', fontsize=60)
        bg_playagain.draw()
    
    if game_over == True and score >= target and score >0 and target > 0:
        bg.draw()
        choose_time.draw()
        up_time_0.draw()
        down_time_0.draw()
        choose_target.draw()
        up_target_0.draw()
        down_target_0.draw()
        screen.draw.text(str(time_up) ,(570,40), color='red', fontsize=60)
        screen.draw.text(str(target) ,(570,170), color='red', fontsize=60)
        win.draw()
        bg_playagain.draw()
    
    if game_over == True and score < target and score >=0 and target > 0:
        bg.draw()
        choose_time.draw()
        up_time_0.draw()
        down_time_0.draw()
        choose_target.draw()
        up_target_0.draw()
        down_target_0.draw()
        screen.draw.text(str(time_up) ,(570,40), color='red', fontsize=60)
        screen.draw.text(str(target) ,(570,170), color='red', fontsize=60)
        lose.draw()
        bg_playagain.draw()

pgzrun.go()