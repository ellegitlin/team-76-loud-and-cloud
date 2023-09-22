import logging
from dataclasses import dataclass
from enum import Enum

#TODO: ADD THINGS YOU NEED FOR STATUS
class GameStatus:
    character_name: str = "Character"
    move_count: int = 0
    running: bool = False
    current_position: tuple = (-100-100)

    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    def create_character(self, character_name: str) -> None:
        pass

    def move(self, direction: Direction) -> None:
        pass
