#!/usr/bin/env python3

import model
import rover
import view


def read_input_file(file_path):
    # read input file
    lines = []
    read_successful = True
    try:
        lines = model.read_input_file(file_path)

    except FileNotFoundError as ex:
        msg = 'FileNotFoundError (check file path) occurred while reading {path}.  Exception=[{exception}'. \
            format(path=file_path, exception=ex)
        view.display_msg(msg)
        read_successful = False

    except StopIteration:
        msg = 'StopIteration (check file size) occurred while reading {path}.'. \
            format(path=file_path)
        view.display_msg(msg)
        read_successful = False

    finally:
        return lines, read_successful


def main():
    # read input file
    file_path = 'input.txt'
    input_lines, read_flag = read_input_file(file_path)

    # first line contains grid size
    input_fields = input_lines[0].split()
    width = int(input_fields[0])
    height = int(input_fields[1])

    # process each input line 1 at a time
    for line_num in range(1, len(input_lines), 2):
        # split input line into each field
        input_fields = input_lines[line_num].split()

        # get rover starting position within the grid
        start_pos = [int(input_fields[0]), int(input_fields[1]), input_fields[2]]

        # rover instructions are on following line
        instructions = input_lines[line_num + 1]

        # initialize the rover object
        rover_obj = rover.Rover(start_pos, instructions, height, width)

        # move rover and display final position & direction
        final_pos = rover_obj.move_rover()
        print(final_pos['x'], final_pos['y'], final_pos['direction'])


if __name__ == '__main__':
    main()
