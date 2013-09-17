from setuptools import setup

setup(name="levenshtein",
      version="0.0.1",
      description="An implementation of the Levenshtein distance algorithm.",
      author="Lars Djerf",
      author_email="lars.djerf@gmail.com",
      url="http://github.com/sral/levenshtein",
      packages=["levenshtein", "levenshtein.tests"],
      test_suite="levenshtein.tests")
