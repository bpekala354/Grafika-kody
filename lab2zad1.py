import pygame
import math

pygame.init()
okno = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zmieniony Hexagon")

# Kolory w RGB
KOLORY = {
    "czerwony": (255, 0, 0),
    "zielony": (0, 255, 0),
    "zolty": (255, 255, 0),
    "fiolet": (128, 0, 128),
    "jasny_niebieski": (0, 255, 255),
    "pomarancz": (255, 165, 0),
    "niebieski": (0, 0, 255),
    "szary": (128, 128, 128)
}

# Parametry początkowe
promien = 150
srodek_x = 300
srodek_y = 300
obrot_stopnie = 0

# Przełączniki transformacji
obracajXY = False
skalujX = False
skalujY = False

# Funkcja rysująca sześciokąt
def rysuj_szesciokat(x, y, r, kat_obrotu):
    wierzcholki = []
    for i in range(6):
        kat_rad = math.radians(i * 60 + kat_obrotu)
        px = x + r * math.cos(kat_rad)
        py = y + r * math.sin(kat_rad)

        if skalujX:
            wsp = 0.2
            px += wsp * py
        if skalujY:
            wsp = 0.2
            py += wsp * px
        if obracajXY:
            px, py = py, px

        wierzcholki.append((px, py))
    return wierzcholki

# Pętla główna
dziala = True
while dziala:
    okno.fill((0, 0, 0))
    punkty_hex = rysuj_szesciokat(srodek_x, srodek_y, promien, obrot_stopnie)
    pygame.draw.polygon(okno, KOLORY["zolty"], punkty_hex)

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            klawisz = zdarzenie.key
            if klawisz == pygame.K_1:
                promien += 10
            elif klawisz == pygame.K_2:
                obrot_stopnie += 20
            elif klawisz == pygame.K_3:
                obrot_stopnie += 180
            elif klawisz == pygame.K_4:
                skalujX = not skalujX
            elif klawisz == pygame.K_5:
                srodek_y -= 10
            elif klawisz == pygame.K_6:
                skalujY = not skalujY
            elif klawisz == pygame.K_7:
                obracajXY = not obracajXY
                obrot_stopnie += 180
            elif klawisz == pygame.K_8:
                promien -= 10
            elif klawisz == pygame.K_9:
                obracajXY = not obracajXY
                obrot_stopnie += 180
                skalujX = not skalujX

    pygame.display.flip()
