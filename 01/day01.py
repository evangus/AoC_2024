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

class ChiefHistorianNotes:
    def __init__(self, filename):
        self.list_1 = []
        self.list_2 = []
        for line in read_input(filename, split=True):
            pair = [int(x) for x in line.split()]
            self.list_1.append(pair[0])
            self.list_2.append(pair[1])
        self.total_distance = 0
        self.similarity_score = 0
        
    def calc_total_distance(self):
        self.total_distance = 0
        self.list_1.sort()
        self.list_2.sort()
        self.total_distance = sum([abs(x-y) for (x,y) in zip(self.list_1,self.list_2)])

    def calc_similarity_score(self):
        self.similarity_score = 0
        self.numbers_frequency = dict.fromkeys(set(self.list_1),0)
        for key in self.numbers_frequency:
            self.numbers_frequency[key] = sum([a == key for a in self.list_2])
        self.similarity_score = sum([key * self.numbers_frequency[key] for key in self.list_1])

    def run_part1(self):
        self.calc_total_distance()
        return self.total_distance
    
    def run_part2(self):
        self.calc_similarity_score()
        return self.similarity_score

print(ChiefHistorianNotes('input.txt').run_part1())
print(ChiefHistorianNotes('input.txt').run_part2())
