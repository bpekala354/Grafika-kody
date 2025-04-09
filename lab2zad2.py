import pygame

pygame.init()
okno = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")

# paleta barw
KOL_CZERWONY = (255, 0, 0)
KOL_ZIELONY = (0, 255, 0)
KOL_ZOLTY = (255, 255, 0)
KOL_FIOLETOWY = (128, 0, 128)
KOL_AQUA = (0, 255, 255)
KOL_POMAR = (255, 165, 0)
KOL_NIEB = (0, 0, 255)
KOL_SZARY = (128, 128, 128)
KOL_BIALY = (255, 255, 255)

dziala = True
while dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False

    okno.fill(KOL_BIALY)

    # zielony kwadrat
    pygame.draw.rect(okno, KOL_ZIELONY, (150, 150, 300, 300))

    # biały trójkąt
    wierzcholki = [(450, 450), (150, 450), (300, 300)]
    pygame.draw.polygon(okno, KOL_BIALY, wierzcholki)

    pygame.display.flip()
