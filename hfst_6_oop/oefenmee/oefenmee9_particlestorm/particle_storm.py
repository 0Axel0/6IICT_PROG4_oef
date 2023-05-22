import pygame
from particle import BoringParticle
import random
from particle import BouncingParticle

# Constantes.
breedte, hoogte = 600,600
fps = 120
aantal_particles = 20

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((breedte,hoogte))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []
for i in range(aantal_particles):
    random_x = (random.random()*2)-1
    random_y = (random.random()*2)-1
    particles.append(BoringParticle(breedte//2,hoogte//2,random_x,random_y))
    particles.append(BouncingParticle(breedte//2,hoogte//2,random_x,random_y))
""" Vul lijst aan... """
    
running = True
while running:
    
    
    
    # Maak scherm schoon.
    scherm.fill((0,0,0))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(fps)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    for particle in particles:
        if type(particle) == BoringParticle:
            particle.bewegen(interval)
            particle.reset(breedte,hoogte)
            pygame.draw.circle(scherm, (particle.color_boring), (int(particle.x),int(particle.y)), 10)
        else:
            particle.bewegen(interval)
            particle.bounce(breedte,hoogte)
            pygame.draw.circle(scherm, (particle.color_bounce), (int(particle.x),int(particle.y)), 10)

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()