import pygame
import random
import math


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BTL.06 - Game Câu Ếch (OOP Pygame)")


COLOR_WATER = (30, 144, 255)
COLOR_FROG = (34, 139, 34)
COLOR_FROG_DIVED = (100, 149, 237) 
COLOR_HOOK = (220, 20, 60)
COLOR_TEXT = (255, 255, 255)
COLOR_LINE = (200, 200, 200)

class Wind:
    def __init__(self):
        self.direction = 1  
        self.strength = 0   
        self.change_per_throw()

    def change_per_throw(self):
        self.direction = random.choice([-1, 1])
        self.strength = random.uniform(20, 80) 

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True

    def update(self, dt):
        """Hàm cập nhật logic - Sẽ bị ghi đè bởi class con"""
        pass

    def draw(self, surface):
        """Hàm vẽ - Sẽ bị ghi đè bởi class con"""
        pass

    def get_rect(self):
        """Trả về pygame.Rect để xử lý va chạm"""
        return pygame.Rect(self.x, self.y, 0, 0)

class Frog(GameObject):
    def __init__(self, x, y, speed_multiplier=1.0):
        super().__init__(x, y)
        self.radius = 20
        self.speed_x = random.uniform(-60, 60) * speed_multiplier
        
        self.dive_timer = 0
        self.is_diving = False
        self.dive_duration = random.uniform(2.0, 4.0)

    def update(self, dt):
        self.x += self.speed_x * dt
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            
        self.dive_timer += dt
        if self.dive_timer > self.dive_duration:
            self.is_diving = not self.is_diving
            self.dive_timer = 0
            self.dive_duration = random.uniform(2.0, 4.0)

    def draw(self, surface):
        color = COLOR_FROG_DIVED if self.is_diving else COLOR_FROG
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)
        # Vẽ thêm mắt cho ếch sinh động
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x) - 8, int(self.y) - 12), 5)
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x) + 8, int(self.y) - 12), 5)

    def get_rect(self):
        if self.is_diving:
            return pygame.Rect(0, 0, 0, 0)
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


class Hook(GameObject):
    def __init__(self, x, y, vel_x, vel_y, wind):
        super().__init__(x, y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.wind = wind
        self.gravity = 350 
        self.radius = 8

    def update(self, dt):
        self.vel_y += self.gravity * dt
        self.vel_x += self.wind.direction * self.wind.strength * dt

        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

        if self.y > SCREEN_HEIGHT:
            self.is_alive = False

    def draw(self, surface):
        pygame.draw.circle(surface, COLOR_HOOK, (int(self.x), int(self.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


class Obstacle(GameObject):
    """Tùy chọn vật cản: Chim bay ngang bầu trời làm hỏng lượt câu"""
    def __init__(self, y):
        self.direction = random.choice([-1, 1])
        x = -40 if self.direction == 1 else SCREEN_WIDTH + 40
        super().__init__(x, y)
        self.width = 40
        self.height = 20
        self.speed = random.uniform(80, 150)

    def update(self, dt):
        self.x += self.direction * self.speed * dt
        if self.x < -100 or self.x > SCREEN_WIDTH + 100:
            self.is_alive = False

    def draw(self, surface):
        pygame.draw.rect(surface, (139, 69, 19), (int(self.x), int(self.y), self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Game:
    def __init__(self):
        self.objects = []  
        self.wind = Wind()
        self.score = 0
        self.level = 1
        
        self.rod_pos = (100, 80)
        
        self.mouse_start = None
        self.is_dragging = False

        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.spawn_frogs(5)

    def spawn_frogs(self, count):
        for _ in range(count):
            rx = random.randint(5, SCREEN_WIDTH - 50)
            ry = random.randint(300, SCREEN_HEIGHT - 50)
            speed_multiplier = 1.0 + (self.level - 1) * 0.25
            self.objects.append(Frog(rx, ry, speed_multiplier))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_start = event.pos
                    self.is_dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.is_dragging:
                    mouse_end = event.pos
                    self.is_dragging = False

                    dx = self.mouse_start[0] - mouse_end[0]
                    dy = self.mouse_start[1] - mouse_end[1]
                    
                    vel_x = dx * 2.0
                    vel_y = dy * 2.0

                    self.objects.append(Hook(self.rod_pos[0], self.rod_pos[1], vel_x, vel_y, self.wind))
                    
                    self.wind.change_per_throw()

    def check_collisions(self):
        hooks = [obj for obj in self.objects if isinstance(obj, Hook)]
        frogs = [obj for obj in self.objects if isinstance(obj, Frog)]
        obstacles = [obj for obj in self.objects if isinstance(obj, Obstacle)]

        for hook in hooks:
            for obs in obstacles:
                if hook.get_rect().colliderect(obs.get_rect()):
                    hook.is_alive = False
                    obs.is_alive = False

            for frog in frogs:
                if hook.get_rect().colliderect(frog.get_rect()):
                    hook.is_alive = False
                    frog.is_alive = False  
                    self.score += 1

    def update(self, dt):
        if random.random() < 0.01 and len([o for o in self.objects if isinstance(o, Obstacle)]) < 2:
            self.objects.append(Obstacle(random.randint(120, 250)))

        active_objects = []
        has_frog = False

        for obj in self.objects:
            obj.update(dt)
            if isinstance(obj, Frog):
                has_frog = True
            
            if obj.is_alive:
                active_objects = active_objects + [obj]
        
        self.objects = active_objects
        self.check_collisions()

        if not has_frog:
            self.level += 1
            self.spawn_frogs(5 + self.level * 2) 

    def draw(self):
        screen.fill(COLOR_WATER)
        
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, SCREEN_WIDTH, 280))
        pygame.draw.line(screen, (0, 100, 80), (0, 280), (SCREEN_WIDTH, 280), 3)

        pygame.draw.line(screen, (139, 69, 19), (20, 200), self.rod_pos, 5)

        if self.is_dragging and self.mouse_start:
            curr_pos = pygame.mouse.get_pos()
            dx = self.mouse_start[0] - curr_pos[0]
            dy = self.mouse_start[1] - curr_pos[1]
            target_preview = (self.rod_pos[0] + dx, self.rod_pos[1] + dy)
            pygame.draw.line(screen, COLOR_LINE, self.rod_pos, target_preview, 2)

        for obj in self.objects:
            obj.draw(screen)

        wind_dir_str = "PHẢI" if self.wind.direction == 1 else "TRÁI"
        txt_score = self.font.render(f"Điểm: {self.score}", True, (0, 0, 0))
        txt_level = self.font.render(f"Màn chơi: {self.level}", True, (0, 0, 0))
        txt_wind = self.font.render(f"Gió: Khối {self.wind.strength:.1f} -> {wind_dir_str}", True, (255, 69, 0))

        screen.blit(txt_score, (20, 20))
        screen.blit(txt_level, (20, 50))
        screen.blit(txt_wind, (SCREEN_WIDTH - 250, 20))

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
