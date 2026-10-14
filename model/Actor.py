from dataclasses import dataclass

from model import Movie

"""date per data di nascita"""
from datetime import date

@dataclass
class Actor:
    """definisco gli attributi della classe Actor"""
    id: str
    name: str
    height:int
    date_of_birth: date
    known_for_movies:str
    Film:list[Movie]=None
      #serve a identificare in modo univoco ogni attore nel grafo."""
    def __hash__(self):
        return hash(self.id)
      #mostro l'output con il solo Name dell'attore"""
    def __str__(self):
        return f"{self.name}"