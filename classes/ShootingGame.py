from classes import ConfigLoader as configs
import pygame as pygame


class ShootingGame:    
    def __init__(self):        
        pygame.init()        
        self.config = configs.ConfigLoader()    
        

        pygame.display.set_caption(self.config.game_name())
        self.screen = pygame.display.set_mode((self.config.screen_width(), self.config.screen_height()))
        self.player = pygame.image.load(self.config.Player()).convert() # loading player image
        self.background = pygame.image.load(self.config.Background()).convert() # loading Background image
        self.screen.blit(self.background,(0, 0)) 
        self.player_width = 100
        self.player_hight = 100
        self.player = pygame.transform.scale(self.player,(self.player_width,self.player_hight)) # player resizing 
        self.background = pygame.transform.scale(self.background,(self.config.screen_width(), self.config.screen_height())) # background resizing 
        
        pygame.display.set_icon(self.player)
        self.playerX =  self.config.screen_width()/2 - self.player_width
        self.playerY =  self.config.screen_height() - self.player_hight

        print(f'playerX  {self.player.get_width()} and playerY {self.player.get_height()}')
        print(f'screenX  {self.background.get_width()} and ScreenY {self.background.get_height()}')

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
            player_speed = 5
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT]:
                if self.playerX >= -self.player_width/2 :
                    self.playerX -= player_speed
            elif keys[pygame.K_RIGHT]:
                if self.playerX <= self.config.screen_width() - self.player_width/2:
                    self.playerX += player_speed
            
            
            self.screen.fill((0, 0, 0))  
            self.screen.blit(self.background,(0, 0)) 
            self.player.set_colorkey((0, 0, 0)) # to make unwanted color of player transparant          
            self.screen.blit(self.player,(self.playerX, self.playerY))   
                     
            pygame.display.update()

