import pygame
import random
import math
import array

# Khởi tạo Pygame và bộ trộn âm thanh
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2)

# Cấu hình màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BTL.06 - Game Câu Ếch Đồ Họa & Âm Thanh Cao Cấp")

# ==========================================
# HỆ THỐNG MÀU SẮC ĐA DẠNG (PALETTE)
# ==========================================
COLOR_SKY = (212, 241, 244)       # Màu trời sáng
COLOR_WATER = (24, 154, 211)      # Màu nước ao xanh biếc
COLOR_DEEP_WATER = (12, 107, 153) # Nước sâu nửa dưới
COLOR_FROG = (107, 203, 119)      # Xanh lá cây tươi (Ếch nổi)
COLOR_FROG_DIVED = (35, 120, 160) # Màu ẩn dưới nước (Ếch lặn)
COLOR_HOOK = (255, 107, 107)      # Màu cam đỏ nổi bật
COLOR_ROD = (160, 82, 45)         # Màu gỗ cần câu
COLOR_TEXT = (44, 53, 64)         # Màu chữ tối thanh lịch

# ==========================================
# TỰ ĐỘNG SINH ÂM THANH BẰNG CODE (SYNTHESIS)
# ==========================================
def generate_sfx(frequency_start, frequency_end, duration_ms):
    """Tự động tạo hiệu ứng âm thanh dạng sóng sin từ tần số toán học"""
    sample_rate = 22050
    n_samples = int(sample_rate * (duration_ms / 1000.0))
    buf = array.array('h', [0] * n_samples)
    for i in range(n_samples):
        t = float(i) / sample_rate
        # Thay đổi tần số tuyến tính theo thời gian
        current_freq = frequency_start + (frequency_end - frequency_start) * (i / n_samples)
        v = math.sin(2.0 * math.pi * current_freq * t)
        buf[i] = int(v * 32767 * (1.0 - i / n_samples)) # Giảm dần âm lượng về cuối
    return pygame.mixer.Sound(buffer=buf)

# Tạo các âm thanh cần thiết cho game
SFX_THROW = generate_sfx(300, 600, 150)  # Tiếng vút khi ném câu
SFX_CATCH = generate_sfx(800, 200, 200)  # Tiếng chóc khi trúng ếch
SFX_FAIL = generate_sfx(150, 80, 300)    # Tiếng bụp khi trúng chim (hỏng)

# ==========================================
# CONFIG - WIND (GIÓ)
# ==========================================
class Wind:
    def __init__(self):
        self.direction = 1  
        self.strength = 0   
        self.change_per_throw()

    def change_per_throw(self):
        self.direction = random.choice([-1, 1])
        self.strength = random.uniform(10, 60)

# ==========================================
# CLASS BASE - GAME OBJECT
# ==========================================
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True

    def update(self, dt): pass
    def draw(self, surface): pass
    def get_rect(self): return pygame.Rect(self.x, self.y, 0, 0)

# ==========================================
# ĐỒ HỌA NÂNG CAO - HIỆU ỨNG BONG BÓNG NỔ
# ==========================================
class Particle(GameObject):
    """Hiệu ứng bọt nước vỡ tan khi câu trúng"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vel_x = random.uniform(-80, 80)
        self.vel_y = random.uniform(-80, 80)
        self.radius = random.randint(3, 7)
        self.alpha = 255

    def update(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        self.radius = max(0.5, self.radius - dt * 4)
        self.alpha -= dt * 400
        if self.alpha <= 0 or self.radius <= 0.5:
            self.is_alive = False

    def draw(self, surface):
        # Vẽ vòng tròn bọt nước trong suốt nhẹ
        surf = pygame.Surface((int(self.radius*2), int(self.radius*2)), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 255, 255, max(0, int(self.alpha))), (int(self.radius), int(self.radius)), int(self.radius), 1)
        surface.blit(surf, (int(self.x - self.radius), int(self.y - self.radius)))

# ==========================================
# ĐỒ HỌA NÂNG CAO - CON ẾCH CÓ MẮT & MÁ HỒNG
# ==========================================
class Frog(GameObject):
    def __init__(self, x, y, speed_multiplier=1.0):
        super().__init__(x, y)
        self.radius = 22
        self.speed_x = random.uniform(-50, 50) * speed_multiplier
        self.dive_timer = 0
        self.is_diving = False
        self.dive_duration = random.uniform(2.5, 5.0)
        self.wave_anim = 0 # Hiệu ứng dập dềnh trên mặt nước

    def update(self, dt):
        self.x += self.speed_x * dt
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            
        self.dive_timer += dt
        if self.dive_timer > self.dive_duration:
            self.is_diving = not self.is_diving
            self.dive_timer = 0
            self.dive_duration = random.uniform(2.5, 5.0)

        # Tạo độ lắc lư hình sin nhẹ nhàng khi bơi
        self.wave_anim += dt * 4

    def draw(self, surface):
        current_y = self.y + (math.sin(self.wave_anim) * 4 if not self.is_diving else 0)
        color = COLOR_FROG_DIVED if self.is_diving else COLOR_FROG
        
        # 1. Vẽ thân ếch hình Oval mượt
        pygame.draw.ellipse(surface, color, (int(self.x - self.radius), int(current_y - self.radius + 5), self.radius*2, self.radius*1.6))
        
        if not self.is_diving:
            # 2. Vẽ đôi mắt to lồi đặc trưng
            pygame.draw.circle(surface, COLOR_FROG, (int(self.x - 10), int(current_y - 14)), 8)
            pygame.draw.circle(surface, COLOR_FROG, (int(self.x + 10), int(current_y - 14)), 8)
            pygame.draw.circle(surface, (255, 255, 255), (int(self.x - 10), int(current_y - 14)), 5)
            pygame.draw.circle(surface, (255, 255, 255), (int(self.x + 10), int(current_y - 14)), 5)
            pygame.draw.circle(surface, (0, 0, 0), (int(self.x - 10), int(current_y - 14)), 2)
            pygame.draw.circle(surface, (0, 0, 0), (int(self.x + 10), int(current_y - 14)), 2)
            # 3. Má hồng đáng yêu cho game casual
            pygame.draw.circle(surface, (255, 182, 193), (int(self.x - 14), int(current_y)), 3)
            pygame.draw.circle(surface, (255, 182, 193), (int(self.x + 14), int(current_y)), 3)

    def get_rect(self):
        if self.is_diving: return pygame.Rect(0, 0, 0, 0)
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

# ==========================================
# LƯỠI CÂU & VẬT CẢN (CHIM)
# ==========================================
class Hook(GameObject):
    def __init__(self, x, y, vel_x, vel_y, wind):
        super().__init__(x, y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.wind = wind
        self.gravity = 380
        self.radius = 7
        self.trail = [] # Hiệu ứng vệt mờ khi bay kéo dài đằng sau

    def update(self, dt):
        # Lưu vết cũ
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 8: self.trail.pop(0)

        self.vel_y += self.gravity * dt
        self.vel_x += self.wind.direction * self.wind.strength * dt
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

        if self.y > SCREEN_HEIGHT: self.is_alive = False

    def draw(self, surface):
        # Vẽ vệt mờ bay lượn (Motion Blur)
        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 255, 255, alpha // 2), (self.radius, self.radius), self.radius - 2)
            surface.blit(surf, (pos[0]-self.radius, pos[1]-self.radius))

        # Vẽ phao câu / lưỡi câu chính
        pygame.draw.circle(surface, COLOR_HOOK, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius - 3)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

class Obstacle(GameObject):
    def __init__(self, y):
        self.direction = random.choice([-1, 1])
        x = -50 if self.direction == 1 else SCREEN_WIDTH + 50
        super().__init__(x, y)
        self.speed = random.uniform(90, 160)
        self.wing_anim = 0

    def update(self, dt):
        self.x += self.direction * self.speed * dt
        self.wing_anim += dt * 10
        if self.x < -100 or self.x > SCREEN_WIDTH + 100: self.is_alive = False

    def draw(self, surface):
        # Thiết kế đồ họa con chim đang đập cánh
        wing_offset = math.sin(self.wing_anim) * 10
        body_rect = pygame.Rect(int(self.x), int(self.y), 35, 16)
        pygame.draw.ellipse(surface, (214, 90, 49), body_rect) # Thân chim màu cam đất
        # Vẽ đôi cánh đang vỗ up/down
        pygame.draw.line(surface, (150, 60, 30), (int(self.x + 17), int(self.y + 8)), (int(self.x + 10), int(self.y + 8 - wing_offset)), 4)
        pygame.draw.line(surface, (150, 60, 30), (int(self.x + 17), int(self.y + 8)), (int(self.x + 24), int(self.y + 8 - wing_offset)), 4)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 35, 16)

# ==========================================
# CORE GAME LOOP
# ==========================================
class Game:
    def __init__(self):
        self.objects = []
        self.wind = Wind()
        self.score = 0
        self.level = 1
        self.rod_pos = (120, 110) # Đầu cần câu
        self.mouse_start = None
        self.is_dragging = False

        self.font = pygame.font.SysFont("Segoe UI", 22, bold=True)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.spawn_frogs(5)

    def spawn_frogs(self, count):
        for _ in range(count):
            self.objects.append(Frog(random.randint(60, SCREEN_WIDTH - 60), random.randint(320, SCREEN_HEIGHT - 60), 1.0 + (self.level - 1) * 0.3))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_start = event.pos
                self.is_dragging = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.is_dragging:
                self.is_dragging = False
                dx = self.mouse_start[0] - event.pos[0]
                dy = self.mouse_start[1] - event.pos[1]
                
                # Bật âm thanh ném vút câu bay đi
                SFX_THROW.play()
                
                self.objects.append(Hook(self.rod_pos[0], self.rod_pos[1], dx * 2.2, dy * 2.2, self.wind))
                self.wind.change_per_throw()

    def check_collisions(self):
        hooks = [o for o in self.objects if isinstance(o, Hook)]
        frogs = [o for o in self.objects if isinstance(o, Frog)]
        obstacles = [o for o in self.objects if isinstance(o, Obstacle)]

        for hook in hooks:
            for obs in obstacles:
                if hook.get_rect().colliderect(obs.get_rect()):
                    hook.is_alive = obs.is_alive = False
                    SFX_FAIL.play() # Âm thanh va chạm hỏng hóc

            for frog in frogs:
                if hook.get_rect().colliderect(frog.get_rect()):
                    hook.is_alive = frog.is_alive = False
                    self.score += 1
                    SFX_CATCH.play() # Âm thanh câu trúng vui nhộn
                    
                    # Sinh ra 15 hạt bong bóng nước nổ bung xung quanh chú ếch
                    for _ in range(15):
                        self.objects.append(Particle(frog.x, frog.y))

    def update(self, dt):
        if random.random() < 0.008 and len([o for o in self.objects if isinstance(o, Obstacle)]) < 2:
            self.objects.append(Obstacle(random.randint(130, 240)))

        active_objects = []
        has_frog = False
        for obj in self.objects:
            obj.update(dt)
            if isinstance(obj, Frog): has_frog = True
            if obj.is_alive: active_objects.append(obj)
            
        self.objects = active_objects
        self.check_collisions()

        if not has_frog:
            self.level += 1
            self.spawn_frogs(5 + self.level * 2)

    def draw(self):
        # 1. Vẽ nền bầu trời chuyển màu dịu mát
        screen.fill(COLOR_SKY)
        
        # 2. Vẽ mặt ao nước phân cấp độ sâu màu gradient
        pygame.draw.rect(screen, COLOR_WATER, (0, 280, SCREEN_WIDTH, SCREEN_HEIGHT - 280))
        pygame.draw.rect(screen, COLOR_DEEP_WATER, (0, 440, SCREEN_WIDTH, SCREEN_HEIGHT - 440))
        
        # Đường ranh giới ao sắc nét nghệ thuật
        pygame.draw.line(screen, (40, 116, 166), (0, 280), (SCREEN_WIDTH, 280), 4)

        # 3. Vẽ CẦN CÂU uốn cong sống động khi kéo lực
        rod_base = (30, 220)
        if self.is_dragging:
            curr_pos = pygame.mouse.get_pos()
            dx = min(150, max(-150, self.mouse_start[0] - curr_pos[0]))
            dy = min(150, max(-150, self.mouse_start[1] - curr_pos[1]))
            # Tạo hiệu ứng cong đầu cần câu nhẹ theo lực kéo ngược
            flex_end = (self.rod_pos[0] + dx * 0.15, self.rod_pos[1] + dy * 0.15)
            pygame.draw.line(screen, COLOR_ROD, rod_base, flex_end, 6)
            # Vẽ đường chỉ hướng kéo ngắm dứt khoát
            pygame.draw.line(screen, (255, 255, 255), self.rod_pos, (self.rod_pos[0] + dx, self.rod_pos[1] + dy), 2)
        else:
            pygame.draw.line(screen, COLOR_ROD, rod_base, self.rod_pos, 6)

        # 4. Vẽ toàn bộ thực thể game (Ếch, Lưỡi câu, Chim bay, Bong bóng)
        for obj in self.objects:
            obj.draw(screen)

        # 5. Thiết kế UI HUD bóng bẩy, hiện đại góc trên
        panel_rect = pygame.Rect(15, 15, 240, 80)
        # Vẽ một chiếc bảng nhỏ mờ mờ sang trọng đựng thông tin
        surf_ui = pygame.Surface((240, 80), pygame.SRCALPHA)
        surf_ui.fill((255, 255, 255, 180)) 
        screen.blit(surf_ui, (15, 15))
        pygame.draw.rect(screen, (200, 200, 200), panel_rect, 2, border_radius=5)

        screen.blit(self.font.render(f" Score: {self.score}", True, COLOR_TEXT), (20, 22))
        screen.blit(self.font.render(f" Level: {self.level}", True, COLOR_TEXT), (20, 54))

        # Hiển thị thông số Gió sang trọng góc bên phải
        wind_dir_str = " Đông (->)" if self.wind.direction == 1 else " Tây (<-)"
        txt_wind = self.font.render(f"Gió: {self.wind.strength:.1f} m/s |{wind_dir_str}", True, (211, 84, 0))
        screen.blit(txt_wind, (SCREEN_WIDTH - 290, 22))

        pygame.display.flip()

    def loop(self):
        while self.is_running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.loop()
