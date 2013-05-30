__author__ = 'Paultimate'

import pygame


class imgHandlr():
    """Lets handle those images like a boss"""

    def renderImg(self, img):
        """Constructor for imgHandlr"""
        return pygame.image.load(img).convert()
