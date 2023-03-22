import unittest
import pytest
from app import multiply

# def test_multiply():
#     values = [(2, 3, 4, 24), (4, 5, 3, 60)]
#     for value in values:
#         try:
#             assert multiply(2, 3, 4) ==24
#         except AssertionError:
#             print('Test Failed')
#         else:
#             print('Test Passed')
#
#
# test_multiply()

# class TestApp(unittest.TestCase):
#
#     def test_multiply(self):
#         values = [(2, 3, 4, 24), (4, 5, 3, 60)]
#         with self.subTest():
#             for value in values:
#                 self.assertEqual(multiply(*value[:-1]), value[-1])

@pytest.mark.parametrize(
    'args, res',
    (
            ((2, 3, 4), 24),
            ((4, 5, 3), 60),
            ((6, 2, 4, 2), 96)
    )
)
def test_multiply(args, res):
    assert multiply(*args) == res


