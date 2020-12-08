def main():
    with open('input') as f:
        program = parse_program(f)
        program.execute_until_loop()
        print(f'Accumulator just before the cycle was closed: {program.accumulator()}')

def parse_program(lines):
    instructions = []
    for line in lines:
        instructions.append(parse_instruction(line.strip()))
    return Program(instructions)

class Program:
    def __init__(self, instructions):
        self._instructions = instructions
        self._accumulator = 0
        self._program_counter = 0

    def accumulator(self):
        return self._accumulator

    def execute_until_loop(self):
        executed_instruction_offsets = set()
        while self._program_counter < len(self._instructions):
            if self._program_counter in executed_instruction_offsets:
                break
            if self._program_counter < 0:
                raise RuntimeError(f'Program counter is {self._program_counter}')
            executed_instruction_offsets.add(self._program_counter)
            instruction = self._instructions[self._program_counter]
            instruction.execute(self)

def parse_instruction(string):
    name, argument = string.split(' ')
    return build_instruction(name, int(argument))

def build_instruction(name, operator):
    ctor = {
        'nop': NopInstruction,
        'jmp': JmpInstruction,
        'acc': AccInstruction
    }[name]
    return ctor(operator)

class NopInstruction:
    def __init__(self, _operator):
        pass

    def execute(self, program):
        pass

class JmpInstruction:
    def __init__(self, offset):
        self._offset = offset
    
    def execute(self, program):
        program._program_counter += self._offset

class AccInstruction:
    def __init__(self, integer):
        self._integer = integer

    def execute(self, program):
        program._accumulator += self._integer

if __name__ == '__main__':
    main()
