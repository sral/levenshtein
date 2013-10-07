import unittest

from levenshtein import levenshtein_distance, levenshtein_distance_recursive


class TestKnownDistances(unittest.TestCase):

    known_distances = (("kitten", "sitting", 3),
                       ("saturday", "sunday", 3),
                       ("mammoth", "mammoth", 0),
                       ("real", "unreal", 2),
                       ("disco", "duck", 3),
                       ("circle", "square", 5),
                       ("pig", "eye", 3))

    def test_known_distances_recursive(self):
        """Test iterative algorithm using known distances"""

        for word, target, distance in self.known_distances:
            self.assertEqual(levenshtein_distance_recursive(word, target),
                             distance)

    def test_known_distances_iterative(self):
        """Test iterative algorithm using known distances"""

        for word, target, distance in self.known_distances:
            self.assertEqual(levenshtein_distance(word, target), distance)
