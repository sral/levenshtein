import unittest

from levenshtein import levenshtein_distance


class TestKnownDistances(unittest.TestCase):

    known_distances = (("kitten", "sitting", 3),
                       ("saturday", "sunday", 3),
                       ("mammoth", "mammoth", 0),
                       ("real", "unreal", 2),
                       ("disco", "duck", 3),
                       ("circle", "square", 5),
                       ("pig", "eye", 3))

    def test_known_distances(self):
        """Test using known distances"""

        for word, target, distance in self.known_distances:
            self.assertEqual(levenshtein_distance(word, target), distance)
