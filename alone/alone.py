import pygame, sys
from pygame.locals import *


largura = 900
altura = 400
cor_foda =(2,77,98)
grama = (34, 177, 76)
chao_foda = pygame.Surface((900, 400))

class personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.personagem = pygame.image.load('Personagens\caveirinha xd.png')
        self.rect = self.personagem.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 50
        self.velocidade = 20
        self.vida = True
    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900                        
    def pular(self):
        #dps faço
        pass
    def acenar(self):
        #dps faço
        pass
    def bater(self):
        #bater isnt cool in the moment xd
        pass
    def matar(self):
        # D:
        pass
    def colocar(self, superficie):
        superficie.blit(self.personagem, self.rect)
def testgame():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("alone beta")
    jogador = personagem()
    jogando = True
    pygame.mixer.music.load('musiquinhatrist.mp3')
    pygame.mixer.music.play()

    while True:
        jogador.movimento()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jogador.rect.left -= jogador.velocidade
                if evento.key == K_RIGHT:
                    jogador.rect.right += jogador.velocidade
        tela.fill(cor_foda)
        chao_foda.fill(grama)
        tela.blit(chao_foda, [0,270])
        jogador.colocar(tela)
        pygame.display.update()
testgame()
