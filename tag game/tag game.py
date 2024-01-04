import pygame
import time 
#import thư viện
  
xx = 400
yy = 300
COORDINATES = [xx, yy]#tuple tọa độ
pygame.init()  #cài thư viện
screen = pygame.display.set_mode(COORDINATES)  #tạo màn hình
done = False  #biến mở chương trình
win = False#biến thắng thua
timer = time.time()#biến giờ
class moveblocks:
    def __init__(self, x, y, up, down, left, right):
         self.x = x    #tọa độ x
         self.y = y    #tọa độ y
         self.up = up    #phím lên
         self.down = down   #phìm xuống
         self.left = left   #phím trái
         self.right = right #phím phải

blue = moveblocks(400-60, 300-60, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
red = moveblocks(0, 0, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

def collide(x1, x2, y1, y2):
        if x1 + 60 >= x2 and x1 <= x2 + 60:
            if y1 + 60 >= y2 and y1 <= y2 + 60:
                return True
        return False  #hàm xác định chạm

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  #nếu bấm dấu x thì tắt
        
    pressed = pygame.key.get_pressed()  
    if pressed[blue.up]: blue.y -= 3  
    if pressed[blue.down]: blue.y += 3  
    if pressed[blue.left]: blue.x -= 3  
    if pressed[blue.right]: blue.x += 3  
    color_blue = (0, 0, 255)#gói gọn điều khiển khối xanh
    
    if pressed[red.up]: red.y -= 3  
    if pressed[red.down]: red.y += 3  
    if pressed[red.left]: red.x -= 3  
    if pressed[red.right]: red.x += 3
    color_red = (255, 0, 0)#gói gọn điều khiển khối đỏ
    time.sleep(0.025)# tick chuyển động
    
    
    black = (0, 0, 0)
    pygame.draw.rect(screen, black, pygame.Rect(0, 0, xx, yy))  
    pygame.draw.rect(screen, color_blue, pygame.Rect(blue.x ,blue.y , 60, 60))  
    pygame.draw.rect(screen, color_red, pygame.Rect(red.x ,red.y , 60, 60))  
    #cập nhật animation
    hit = collide( red.x, blue.x, red.y, blue.y)
    pygame.display.flip()   
    if hit:
        print("red wins")
        time.sleep(1)
        done = True
    timerleft = time.time()
    if timerleft - timer >= 60:
        print("blue wins")
        time.sleep(1)
        done = True
    
        
