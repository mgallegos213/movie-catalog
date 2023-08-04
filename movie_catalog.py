import csv
from sortedcontainers import SortedDict
from typing import Iterable

from movie import Movie

class MovieCatalog:
    def __init__(self, filename: str):
        self.catalog = {}
        self.parse_movies(filename)

    def parse_movies(self, filename: str):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip header
            for row in reader:
                id, title, year, genres = row
                genres = genres.split('|')
                movie = Movie(id, title, int(year), genres)
                for g in genres:
                    # If the genre is not in the catalog, create an entry with a SortedDict
                    if g not in self.catalog:
                        self.catalog[g] = SortedDict()
                    
                    # If the year is not in the SortedDict for the genre, create a list
                    if movie.year not in self.catalog[g]:
                        self.catalog[g][movie.year] = []
                    
                    # Append the movie to the list for the corresponding year
                    self.catalog[g][movie.year].append(movie)
                # print(self.catalog)


    # Queries movies by genre and year range.
    # Time Complexity: O(klog(n) + m) => k is range of years, n is total years, m is number of movies in that range
    # We are returning the combined array of movies for that genre[year] list
    # Have to iterate over each year's result and combine it to our returned result []
    # Space Complexity: O(1)
    def get_movies(self, genre: str, start_year: int, end_year: int) -> Iterable[Movie]:
        result = []
        if genre not in self.catalog:
            return result
        for year in self.catalog[genre].irange(start_year, end_year):
            movies = self.catalog[genre][year]
            result.extend(movies)
        return result
