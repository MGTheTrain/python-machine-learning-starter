import unittest
from src.data_loader import load_data

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        (x_train, y_train), (x_test, y_test) = load_data()

        # Check data shapes
        self.assertEqual(x_train.shape, (60000, 28, 28, 1))
        self.assertEqual(y_train.shape, (60000,))
        self.assertEqual(x_test.shape, (10000, 28, 28, 1))
        self.assertEqual(y_test.shape, (10000,))

        # Check data normalization
        self.assertTrue((x_train >= 0).all() and (x_train <= 1).all())
        self.assertTrue((x_test >= 0).all() and (x_test <= 1).all())

if __name__ == "__main__":
    unittest.main()
