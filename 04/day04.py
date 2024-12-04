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

class WordSearcher:
    def __init__(self, filename) -> None:
        self.text = read_input(filename)
        self.line_len = self.text.find('\n')
        self.increments = [(-1)*self.line_len - 2, (-1)*self.line_len - 1, (-1)*self.line_len,
                           -1, 1,
                           self.line_len, self.line_len + 1, self.line_len + 2]

    def run_part1(self):
        ans = 0
        starting_indexes = [i for i in range(len(self.text)) if self.text[i] == 'X']

        for i in starting_indexes:
            for di in self.increments:
                try:
                    if (self.text[i+di] == 'M') & (self.text[i+2*di] == 'A') & (self.text[i+3*di] == 'S') & (i+3*di >= 0):
                        ans += 1
                except IndexError:
                    continue
        return ans
    
    def run_part2(self):
        ans = 0
        starting_indexes = [i for i in range(len(self.text)) if self.text[i] == 'A']

        for i in starting_indexes:
            try:
                x1, x2, x3, x4 = i - self.line_len - 2, i - self.line_len, i + self.line_len, i + self.line_len + 2
                if ((x1>=0) & 
                    (((self.text[x1] == 'M') & (self.text[x4] == 'S')) | ((self.text[x1] == 'S') & (self.text[x4] == 'M'))) & 
                    (((self.text[x2] == 'M') & (self.text[x3] == 'S')) | ((self.text[x2] == 'S') & (self.text[x3] == 'M')))):
                    ans += 1
            except IndexError:
                continue
        return ans


print(WordSearcher('04/input.txt').run_part1())
print(WordSearcher('04/input.txt').run_part2())
