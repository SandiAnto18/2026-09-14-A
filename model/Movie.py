from dataclasses import dataclass
"""date per data di nascita"""
from datetime import date

@dataclass
class Movie:
    """definisco gli attributi della classe Actor"""
    id: str
    title: str
    year: int
    date_published: date
    duration: int
    country: str
    worlwide_gross_income:str
    languages: str
    production_company: str


      #serve a identificare in modo univoco ogni attore nel grafo."""
    def __hash__(self):
        return hash(self.id)
      #mostro l'output con il titolo del film"""
    def __str__(self):
        return f"{self.title}"