#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.backgorund import Backgorund
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            # fazer uma lista genérica com o laço for, auxilia a não ter que criar uma lista para cada um dos Backgrounds
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Backgorund(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Backgorund(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Backgorund(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Backgorund(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
