import pygame as pg

walk_r = pg.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\NoOutline\120x80_PNGSheets\_Run.png")
walk_l = pg.transform.flip(walk_r, True, False)
stay_r =  pg.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\NoOutline\120x80_PNGSheets\_Idle.png")
stay_l = pg.transform.flip(stay_r, True, False)
jump_r = pg.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\Outline\120x80_PNGSheets\_Jump.png")
jump_l = pg.transform.flip(jump_r, True, False)
jump_final = pg.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\Outline\120x80_PNGSheets\_JumpFallInbetween.png")