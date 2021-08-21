#
#   An interpreter for the esoteric language BF,
# also known as brainfuck. Note that error handling
# has not been completed (XXX) so if something
# is wrong with the program this may behave
# strangely.
#
#   Also note that this interpreter takes newline
# as a valid character when giving user input (',')
#
from __future__ import print_function

import sys


VALID_BF_COMMANDS = [
    '+', '-', '>', '<', '[', ']', ',', '.'
]

# Use debugging code
DEBUG = [ 'z' ]
DEBUG_ON = False  # True


def print_memory(tape, index=None):
    """Print the contents of the pseudo memory.

    Args:
        tape(list(int)): the ints to  print
        index(int): what cell in the tape is being
            pointed to
    """
    print("")
    if index:
        print("Index:")
        print(index)

    print("Tape:")
    counter = 0
    for cell in tape:
        if index and DEBUG_ON:
            print(counter, cell, "      Character: " + chr(tape[index]))
        else:
            print(counter, cell)
        counter += 1


def plus(tape, index):
    """Add one to the Cell at the given index.

    Args:
        tape(list(int)): the current psuedo memory
        int: what Cell to look at

    Returns:
        list(int): changed psuedo memory
        int: what Cell to look at
    """
    tape[index] += 1
    return tape, index


def minus(tape, index):
    """Add one to the Cell at the given index.

    Args:
        tape(list(int)): the current psuedo memory
        int: what Cell to look at

    Returns:
        list(int): changed psuedo memory
        int: what Cell to look at
    """
    tape[index] -= 1
    return tape, index


def right(tape, index):
    """Move one memory Cell to the right.

    Args:
        tape(list(int)): the current psuedo memory
        index(int): what Cell to look at

    Returns:
        list(int): unchanged psuedo memory
        int: what Cell to look at
    """
    index += 1
    # Initialize Cell to 0 if it didn't exist
    if len(tape) <= index:
        tape.append(0)
    return tape, index


def left(tape, index):
    """Move one memory Cell to the left.

    Args:
        tape(list(int)): the current psuedo memory
        index(int): what Cell to look at

    Raises:
        RuntimeError: If the memory pointer points to
            an index of less than 0

    Returns:
        list(int): unchanged psuedo memory
        int: what Cell to look at
    """
    index -= 1
    if index < 0:
        raise RuntimeError(
            "Tape memory out of bounds. "
            "(before the beginning)")

    return tape, index


def comma(tape, index):
    """put a character input in the Cell at the given index.

    Args:
        tape(list(int)): the current psuedo memory
        int: what Cell to look at

    Returns:
        list(int): changed psuedo memory
        int: what Cell to look at
    """
    # Read one character from stdin
    tape[index] = ord(sys.stdin.read(1))
    return tape, index


def loop_start(tape, index, file_data, command_index):
    """Loop until we find the end of loop character.

    End of loop character: ']'

    Args:
        tape(list(int)): the current psuedo memory
        index(int): what Cell to look at
        file_data(list(char)): the file data
        command_index(int): the index of the command
            to run

    Returns:
        list(int): the pseudo memory
        int: the pointer
        ind: the index of the command to run
    """
    # Move past the begin loop character '['
    command_index += 1

    # If the Cell is already 0 ignore the loop
    if(tape[index] == 0):
        while(file_data[command_index] != ']'):
            command_index += 1

        return tape, index, command_index

    # Save function pointer and memory pointer
    start_of_loop = command_index
    end_of_loop = 0

    # Run the loop the correct number of times
    while(1):
        tape, index, command_index = execute_command(
            tape, index, file_data, command_index)

        command_index += 1

        # Move the function pointer back to the
        #   beginning of the loop if hit end of loop
        if file_data[command_index] == ']':
            end_of_loop = command_index
            command_index = start_of_loop

            # If we hit the end of the loop check
            # to see if the tape at the given index
            # is 0. If it is exist loop
            if tape[index] == 0:
                break

    return tape, index, end_of_loop


def show(tape, index):
    """Print the ASCII at the given Cell.

    Args:
        tape(list(int)): the current psuedo memory
        index(int): what Cell to look at

    Returns:
        list(int): unchanged psuedo memory
        int: what Cell to look at
    """
    print(chr(tape[index]), end='')
    return tape, index


COMMANDS = {
    '+': plus,
    '-': minus,
    '>': right,
    '<': left,
    ',': comma,
    '.': show
}

START_LOOP = '['


def execute_command(tape, index, file_data, command_index):
    """Execute each valid commands.

    Args:
        tape(list(int)): the current psuedo memory
        index(int): what Cell to look at
        file_data(list(char)): the file data
        command_index(int): the index of the command
            to run

    Returns:
        list(int): the pseudo memory
        int: the pointer for the memory cell
        command_index: where in the file_data the given
            command is
    """
    command = file_data[command_index]
    #print(command, end='')

    if command in COMMANDS:
        # Run Command
        tape, index = COMMANDS[command](tape, index)

    elif command == START_LOOP:
        # Start Loop
        tape, index, command_index = loop_start(
            tape, index, file_data, command_index)

    elif command in DEBUG:
        # Print Debugging Information
        print_memory(tape, index)

    return tape, index, command_index


def interpret_commands(file_data):
    """Interpret all valid commands.

    Args:
        file_data(str): the commands to parse
    """
    # Start with a tape with one Cell that is empty
    tape = [0]
    # Start with the tape pointer at 0
    index = 0

    # Pull out only valid BF commands
    commands = []
    for command in file_data:
        if command in VALID_BF_COMMANDS or command in DEBUG:
            commands.append(command)

    # Every command in BF is a single character: execute
    command_index = 0
    while command_index < len(commands):
        tape, index, command_index = execute_command(
            tape, index, commands, command_index)

        command_index += 1


def get_file_data():
    """Get the contents of the file being interpreted.

    Returns:
        str: contents of the file
    """
    if len(sys.argv) < 2:
        raise RuntimeError("No File Provided.")
    else:
        file_data = open(sys.argv[1], "r")
    return file_data.read()


def main():
    """This is an interpreter for the language BP (a.k.a. brainfuck)."""
    file_data = get_file_data()
    interpret_commands(file_data)


if __name__ == "__main__":
    main()
