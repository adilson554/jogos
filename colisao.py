# -*- coding: utf-8 -*-
"""
Colisão entre retângulos.
"""

import pygame
import random

largura = 600
altura = 400

VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

heroi_x = random.randint(50, largura-50)
heroi_y = random.randint(50, altura -50)
maca_x = random.randint(50, largura-50)
maca_y = random.randint(50, altura -50)
gilo_x = random.randint(50, largura-50)
gilo_y = random.randint(50, altura -50)

pontos = 0
fonte = pygame.font.SysFont("liberationmono", 40)

fechar = False
while not fechar:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar = True
    
    
    maca = pygame.draw.rect(tela, VERDE, (maca_x, maca_y, 50, 50))
    gilo = pygame.draw.rect(tela, AZUL, (gilo_x, gilo_y, 50,50))
    heroi = pygame.draw.rect(tela, VERMELHO, (heroi_x, heroi_y, 50, 50))
    
    if pygame.key.get_pressed()[pygame.K_a]:
        if heroi_x <= 0:
            heroi_x = 0
        else:
            heroi_x = heroi_x - 5
            
    if pygame.key.get_pressed()[pygame.K_d]:
        if heroi_x >= largura-50:
            heroi_x = largura -50
        else:
            heroi_x = heroi_x + 5
    if pygame.key.get_pressed()[pygame.K_w]:
        if heroi_y < 0:
            heroy_y = 0
        else:
            heroi_y = heroi_y - 5
    if pygame.key.get_pressed()[pygame.K_s]:
        if heroi_y > altura-50:
            heroi_y = altura - 45
        else:
            heroi_y = heroi_y + 5
            
            
    if heroi.colliderect(maca):
        maca_x = random.randint(50, largura-50)
        maca_y = random.randint(50, altura -50)
        gilo_x = random.randint(50, largura-50)
        gilo_y = random.randint(50, altura -50)
        pontos = pontos + 1
        
    if heroi.colliderect(gilo):
        gilo_x = random.randint(50, largura-50)
        gilo_y = random.randint(50, altura -50)
        pontos = pontos -2
        
    if maca.colliderect(gilo):
        gilo_x = random.randint(50, largura-50)
        gilo_y = random.randint(50, altura -50)
            
    texto = f'pontos = {pontos}'
    texto_formatado = fonte.render(texto, True, (50,100,50))
    tela.blit(texto_formatado, (300,30))
    # update
    pygame.display.update()
    tela.fill((0,0,50))


pygame.quit()
