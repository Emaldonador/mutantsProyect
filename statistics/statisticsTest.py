import unittest
from unittest import TestCase
import statisticsFunction

class statisticsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculate_ok(self):
        response = {"aggregations":{
            "groups": {
                "doc_count_error_upper_bound": 0,
                "sum_other_doc_count": 0,
                "buckets": [
                    {
                        "key": "mutante",
                        "doc_count": 4
                    },
                    {
                        "key": "humano",
                        "doc_count": 2
                    }
                ]
            }
        }
        }
        result = statisticsFunction.calculate(response)
        self.assertEqual(result,{'count_mutant_dna': 4,'count_human_dna':2,'ratio': 2})
