import unittest
from unittest import TestCase
import mutantsIdentifier

class mutantsIdentifierTest(unittest.TestCase):

    def setUp(self):
        pass
    def  test_isMutant_ok(self):
        dna = ["CAGCTA","CAGTGC","TAACTG","AAAATG","TCCCTA","TCACTG"]
        result = mutantsIdentifier.isMutant(dna)
        self.assertEqual(result, True)

    def  test_isMutant_ok2(self):
        dna = ["CAGCTA","CCGTGC","TACCTG","AAACTG","TCCCTA","TCACTG"]
        result = mutantsIdentifier.isMutant(dna)
        self.assertEqual(result, True)

    def  test_human_ok(self):
        dna = ["CTGCTA","CAGTGC","TTATGT","AGAAGG","TCCCTA","TCACTG"]
        result = mutantsIdentifier.isMutant(dna)
        self.assertEqual(result, False)

    def test_save(self):
        dna = ["CAGCTA","CAGTGC","TAACTG","AAAATG","TCCCTA","TCACTG"]
        result = False
        saved = mutantsIdentifier.save(dna, result)
        self.assertEqual(saved, None)