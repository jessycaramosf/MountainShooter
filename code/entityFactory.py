#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.backgorund import Backgorund


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
    #fazer uma lista genérica com o laço for, auziliza a não ter que criar uma lista para cada um dos Backgrounds
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.apend(Backgorund(f'Level1Bg{i}', (0,0)))
                return list_bg