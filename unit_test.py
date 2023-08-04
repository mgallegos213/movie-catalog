import unittest
from movie_catalog import MovieCatalog

class TestMovieCatalog(unittest.TestCase):
    def test_get_movies(self):
        catalog = MovieCatalog('catalog.csv')

        # Test query by genre and year range
        movies = catalog.get_movies('Adventure', 2001, 2001)
        # for movie in movies:
        #     print(movie.title)
        self.assertEqual(len(movies), 2)
        self.assertEqual(movies[0].title, 'Harry Potter')
        self.assertEqual(movies[1].title, 'Lord of the Rings')

        # Test query by genre with no matching year
        movies = catalog.get_movies('Adventure', 1990, 1995)
        self.assertEqual(len(movies), 0)

        # Test query by genre and broader year range
        movies = catalog.get_movies('Adventure', 1977, 2001)
        self.assertEqual(len(movies), 3)

        # Test query by non-existent genre
        movies = catalog.get_movies('Comedy', 1977, 2001)
        self.assertEqual(len(movies), 0)

if __name__ == '__main__':
    unittest.main()
