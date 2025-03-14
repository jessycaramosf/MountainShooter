#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC): # Classe Abstrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.sur = pygame.image.load('./asset' + name + '.png')
        self.rect = self.sur.get_rect(left=position[0],top=position[1])
        self.speed = 0

    @abstractmethod # @ decorator
    def move(self, ):
        pass
