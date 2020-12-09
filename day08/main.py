import copy

def main():
    with open('input') as f:
        program = parse_program(f)

    program.execute_until_loop()
    print(f'Accumulator just before the loop was closed: {program.accumulator()}')

    program_without_loop = fix_loop(program)
    program_without_loop.execute_until_loop()
    print(f'Accumulator after corrected execution: {program_without_loop.accumulator()}')


def parse_program(lines):
    instructions = []
    for line in lines:
        instructions.append(parse_instruction(line.strip()))
    return Program(instructions)

def fix_loop(program):
    copied_program = copy.deepcopy(program)

    fixed_program = try_instruction_swap(copied_program, JmpInstruction, NopInstruction)
    if fixed_program is not None:
        return fixed_program

    fixed_program = try_instruction_swap(copied_program, NopInstruction, JmpInstruction)
    if fixed_program is not None:
        return fixed_program

    raise RuntimeError('Tried replacing all jmp and nop instructions.')

def try_instruction_swap(program, from_cls, to_cls):
    find_predicate = lambda instruction: isinstance(instruction, from_cls)
    index = program.find_instruction(find_predicate)
    while index >= 0:
        program.replace_instruction(index, to_cls)
        if not program.execute_until_loop():
            program.reset()
            return program
        program.replace_instruction(index, from_cls)
        program.reset()
        index = program.find_instruction(find_predicate, start=index + 1)
    return None

class Program:
    def __init__(self, instructions):
        self._instructions = instructions
        self._accumulator = 0
        self._program_counter = 0

    def instructions(self):
        return self._instructions

    def accumulator(self):
        return self._accumulator

    def reset(self):
        self._accumulator = 0
        self._program_counter = 0

    def execute_until_loop(self):
        executed_instruction_offsets = set()
        while self._program_counter < len(self._instructions):
            if self._program_counter in executed_instruction_offsets:
                return True
            if self._program_counter < 0:
                raise RuntimeError(f'Program counter is {self._program_counter}')
            executed_instruction_offsets.add(self._program_counter)
            instruction = self._instructions[self._program_counter]
            instruction.execute(self)
        return False

    def replace_instruction(self, instruction_index, cls):
        existing = self._instructions[instruction_index]
        replacement = cls(existing.argument())
        self._instructions[instruction_index] = replacement

    def find_instruction(self, predicate, start=0):
        for index, instruction in enumerate(self._instructions[start:]):
            if predicate(instruction):
                return start + index
        return -1

def parse_instruction(string):
    name, argument = string.split(' ')
    return build_instruction(name, int(argument))

def build_instruction(name, argument):
    ctor = {
        'nop': NopInstruction,
        'jmp': JmpInstruction,
        'acc': AccInstruction
    }[name]
    return ctor(argument)

class Instruction:
    def __init__(self, argument):
        self._argument = argument

    def argument(self):
        return self._argument

class NopInstruction(Instruction):
    def execute(self, program):
        program._program_counter += 1

class JmpInstruction(Instruction):
    def execute(self, program):
        program._program_counter += self._argument

class AccInstruction(Instruction):
    def execute(self, program):
        program._accumulator += self._argument
        program._program_counter += 1

if __name__ == '__main__':
    main()
