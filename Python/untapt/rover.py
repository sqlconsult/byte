#!/usr/bin/env python3

import constants as const


class Rover:
    def __init__(self, start_pos, instructions, height, width):
        """
        :param start_pos:    rover's starting position
        :param instructions: instructions being executed
        :param height:       maximum grid height
        :param width:        maximum grid width
        """
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.direction = start_pos[2]

        self.max_x = width
        self.max_y = height
        self.instructions = instructions

    def move_rover(self):
        """
        :return: dictionary (x, y, direction) with rover moved to new position based on instructions
        """
        # process rover instructions 1 at a time
        for inst in self.instructions:
            compass_idx = const.COMPASS.index(self.direction)

            # L = rotate left 90 degrees
            if inst == 'L':
                # wrap around if we go past start of list
                # move compass index 1 position to the left
                if compass_idx - 1 < 0:
                    compass_idx = len(const.COMPASS) - 1
                else:
                    compass_idx -= 1
                self.direction = const.COMPASS[compass_idx]

            # R = rotate right 90 degrees
            elif inst == 'R':
                # wrap around if we go past end of list
                # move compass index 1 position to the right
                if compass_idx + 1 > len(const.COMPASS) - 1:
                    compass_idx = 0
                else:
                    compass_idx += 1
                self.direction = const.COMPASS[compass_idx]

            # M = move 1 unit in current direction
            elif inst == 'M':
                x_to_move = const.GRID_MOVES[compass_idx][0]
                y_to_move = const.GRID_MOVES[compass_idx][1]

                # don't move outside grid
                new_x = self.move_in_matrix(self.x, x_to_move, self.max_x)
                new_y = self.move_in_matrix(self.y, y_to_move, self.max_y)

                self.x = new_x
                self.y = new_y

        # return the rovers final position as a dictionary
        ret_val = {'x': self.x,
                   'y': self.y,
                   'direction': self.direction}
        return ret_val

    @staticmethod
    def move_in_matrix(old_value, amt_to_move, max_value):
        """
        :param old_value:    Starting position in matrix
        :param amt_to_move:  Amount to move (+1 or -1)
        :param max_value:    Maximum possible value within matrix
        :return:             New position - 0 if move would be less than 0
                                            max_value if move would be > max value
                                            new position if within bounds
        """
        new_value = old_value + amt_to_move
        if 0 <= new_value <= max_value:
            return new_value
        elif old_value + amt_to_move < 0:
            return 0
        elif old_value + amt_to_move > max_value:
            return max_value
