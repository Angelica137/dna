from unittest import TestCase

from app.design_primer import design_primer


class TestDesginPrimer(TestCase):

    def test_return_primer_one(self):
        result = design_primer('GGCGAGGAGCTG', 4)
        expected = 'GGCG'
        self.assertEqual(result, expected)