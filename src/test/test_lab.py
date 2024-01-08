import unittest
from src.main.lab import nerExercise
class TestNERExercises(unittest.TestCase):
    def test_ner_exercise(self):
        result = nerExercise()
        result_tag_dict = {}
        for node in result:
            if hasattr(node, 'label'):
                result_tag_dict[node.label()] = node.leaves()

        self.assertTrue('PERSON' in result_tag_dict)
        self.assertTrue('ORGANIZATION' in result_tag_dict)

if __name__ == '__main__':
    unittest.main()