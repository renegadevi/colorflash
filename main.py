#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "GREEN": (0, 255, 0),
    "RED":   (255, 0, 0),
    "BLUE":  (0, 0, 255)
}

while True:
    for index, (color, color_value) in enumerate(colors.items()):
        # print(index, ":", color, "\t", color_value)
        screen.fill(color_value)
        pygame.display.flip()
        clock.tick(60)
