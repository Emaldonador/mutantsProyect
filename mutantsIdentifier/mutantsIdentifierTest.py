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
    
    def  test_novalid_adn(self):
        dna = ["CTGCTA","CAGTGC","TTATGT","AGAAGG","TCXCTA","TCACTG"]
        result = mutantsIdentifier.validateAdn(dna)
        self.assertEqual(result, False)
    
    def test_lambda_human(self):
        event = {'dna':["CTGCTA","CAGTGC","TTATGT","AGAAGG","TCCCTA","TCACTG"]}
        result = mutantsIdentifier.lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 403)

    def test_lambda_mutant(self):
        event = {'dna':["CAGCTA","CAGTGC","TAACTG","AAAATG","TCCCTA","TCACTG"]}
        result = mutantsIdentifier.lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_lambda_no_valid(self):
        event = {'dna':["CTGCTA","CAGTGC","TTATGT","AGAAGG","TCXCTA","TCACTG"]}
        result = mutantsIdentifier.lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 409)

    def test_save(self):
        dna = ["CAGCTA","CAGTGC","TAACTG","AAAATG","TCCCTA","TCACTG"]
        result = False
        saved = mutantsIdentifier.save(dna, result)
        self.assertEqual(saved, None)