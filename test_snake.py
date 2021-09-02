import unittest
from snake import count_valid_routes

class Snake_tests(unittest.TestCase):

    def test_1(self):
        board =  [4, 3]
        snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
        depth =  3
        
        expected = 7
        computed = count_valid_routes(board, snake, depth)

        self.assertEquals(expected, computed)
        
    def test_2(self):
        board =  [2, 3]
        snake =  [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
        depth =  10

        expected = 1
        computed = count_valid_routes(board, snake, depth)

        self.assertEquals(expected, computed)
        
    def test_3(self):
        board =  [10, 10]
        snake =  [[5,5], [5,4], [4,4], [4,5]]
        depth =  4

        expected = 81
        computed = count_valid_routes(board, snake, depth)

        self.assertEquals(expected, computed)
        
if __name__ == '__main__':
    unittest.main()
