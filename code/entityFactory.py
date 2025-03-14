#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.backgorund import Backgorund
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
    #fazer uma lista genérica com o laço for, auxilia a não ter que criar uma lista para cada um dos Backgrounds
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Backgorund(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Backgorund(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg