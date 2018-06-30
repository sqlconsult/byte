#!/usr/bin/env python3

import unittest
import rover


# inherit unittest TestCase for asserts
class TestGrid(unittest.TestCase):

    def test_move_rover_simple(self):
        #
        # test object creation
        #
        print('==> test_move_rover_simple: test #1')
        start_pos = [1, 2, 'N']
        instructions = 'LMLMLMLMM'  # this should put the rover at (3, 2) facing east
        rover_obj = rover.Rover(start_pos, instructions, 5, 5)

        self.assertEqual(rover_obj.x, 1)
        self.assertEqual(rover_obj.y, 2)
        self.assertEqual(rover_obj.direction, 'N')

        self.assertEqual(rover_obj.max_x, 5)
        self.assertEqual(rover_obj.max_y, 5)

        self.assertEqual(rover_obj.instructions, 'LMLMLMLMM')
        #
        # test simple case
        #
        print('==> test_move_rover_simple: test #2')
        start_pos = [1, 2, 'N']
        instructions = 'RMM'   # this should put the rover at (3, 2) facing east
        rover_obj = rover.Rover(start_pos, instructions, 5, 5)
        rover_obj.move_rover()

        self.assertEqual(rover_obj.x, 3)
        self.assertEqual(rover_obj.y, 2)
        self.assertEqual(rover_obj.direction, 'E')

    def test_move_rover_complex(self):
        # test #1
        print('==> test_move_rover_complex: test #1')
        start_pos = [1, 2, 'N']
        instructions = 'LMLMLMLMM'      # this should put the rover at (3, 2) facing east
        rover_obj = rover.Rover(start_pos, instructions, 5, 5)
        new_pos = rover_obj.move_rover()

        self.assertEqual(new_pos['x'], 1)
        self.assertEqual(new_pos['y'], 3)
        self.assertEqual(new_pos['direction'], 'N')

        # test #2
        print('==> test_move_rover_complex: test #2')
        start_pos = [3, 3, 'E']
        instructions = 'MMRMMRMRRM'      # this should put the rover at (5, 1) facing east
        rover_obj = rover.Rover(start_pos, instructions, 5, 5)
        new_pos = rover_obj.move_rover()

        self.assertEqual(new_pos['x'], 5)
        self.assertEqual(new_pos['y'], 1)
        self.assertEqual(new_pos['direction'], 'E')


if __name__ == '__main__':
    unittest.main()
