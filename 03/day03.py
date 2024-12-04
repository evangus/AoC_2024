import re

def read_input(filename, split = False, convert_to_int = False, sep = '\n'):
    f = open(filename)
    raw = f.read()[:-1]
    f.close()
    data = raw
    if split:
        data = data.split(sep)
    if convert_to_int:
        data = [int(item) for item in data]
    return data

class JumbledProgram:
    def __init__(self, filename) -> None:
        self.memory = read_input(filename)
        pattern = r"mul\(\s*-?\d+\s*,\s*-?\d+\s*\)"
        self.instructions = re.findall(pattern, self.memory)

    @staticmethod
    def mul_instruction(line):
        x,y = [int(a) for a in line[4:-1].split(',')]
        return x*y
    
    def run_part1(self):
        return sum([self.mul_instruction(line) for line in self.instructions])
    
    def run_part2(self):
        pattern = r"mul\(\s*-?\d+\s*,\s*-?\d+\s*\)|do\(\)|don't\(\)"
        status = True
        ans = 0
        text = self.memory
        
        match = re.search(pattern, text)
        
        while match:
            
            if match.group() == "don't()":
                status = False
            elif match.group() == "do()":
                status = True
            elif status:
                ans += self.mul_instruction(match.group())

            text = text[match.span()[-1]:]
            match = re.search(pattern, text)
            
        return ans

print(JumbledProgram('03/input.txt').run_part1())
print(JumbledProgram('03/input.txt').run_part2())
