import pygame


class Object:
    _instances = []

    def __init__(self) -> None:
        self._instances.append(self)

    @classmethod
    def set_sizes(cls, screen_width: int, screen_height: int) -> None:
        # if the width is bigger than the ratio, use the height to calculate the width
        if screen_width >= screen_height * 36 // 20:
            height = screen_height
            width = round(height * 36 / 20)
        # otherwise use the width to calculate height
        else:
            width = screen_width
            height = round(width * 20 / 36)

        # use the height and width to calculate other sizes
        cls.unit_size = round(width / 36)
        cls.cell_size = cls.unit_size * 2
        cls.board_size = cls.cell_size * 9
        cls.line_size = max(1, round(cls.cell_size / 64))
        cls.big_line_size = cls.line_size * 3

        # calculate the x_padd and y_padd based on if the height or width was adjusted
        cls.x_padd = (screen_width - width) // 2
        cls.y_padd = (screen_height - height) // 2

        cls.font = pygame.font.SysFont(None, round(cls.cell_size * 0.8))

        # if instance has an update method call it
        for instance in cls._instances:
            if hasattr(instance, "update"):
                instance.update()
