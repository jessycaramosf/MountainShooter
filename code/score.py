import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.const import C_YELLOW, SCORE_POS, MENU_OPTION


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()  # metodo para inserir imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # metodo insere retangulo onde a imagem vai ser inserida
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.text(48,'You Win!', C_YELLOW, SCORE_POS['Title'] )
            if game_mode == MENU_OPTION[0]:
                text = 'Player 1 enter your name (4 characters)'
            pygame.display.flip()
            pass

    def text(self, text_size: int, txt: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(txt, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass