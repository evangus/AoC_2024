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

class ReactorReportAnalyzer:
    def __init__(self, filename) -> None:
        self.reports = read_input(filename, split=True)

    @staticmethod
    def check_report(report):
        safe = True
        seq = [int(x) for x in report.split()]
        direction = seq[1] > seq[0]
        safe = (abs(seq[1] - seq[0]) >= 1) * (abs(seq[1] - seq[0]) <= 3)
        if not safe:
            return bool(safe)

        for i in range(1,len(seq)-1):
            safe = ((seq[i+1] > seq[i]) == direction) * (abs(seq[i+1] - seq[i]) >= 1) * (abs(seq[i+1] - seq[i]) <= 3)
            if not safe:
                break
        return bool(safe)
    
    @staticmethod
    def dampened_check_report(report):
        seq = [int(x) for x in report.split()]
        if seq[1] == seq[0]:
            direction = seq[2] > seq[1]
        else:
            direction = seq[1] > seq[0]
        
        for i in range(len(seq)-1):
            safe = ((seq[i+1] > seq[i]) == direction) * (abs(seq[i+1]-seq[i])>=1) * (abs(seq[i+1]-seq[i])<=3)
            if not safe:
                s = ' '.join([str(x) for x in seq[:i+1] + seq[i+2:]])
                safe = ReactorReportAnalyzer.check_report(s)
                if not safe:
                    return bool(safe)
                
        return bool(safe)
        
    
    def run_part1(self):
        return sum([ReactorReportAnalyzer.check_report(report) for report in self.reports])
    
    def run_part2(self):
        return sum([ReactorReportAnalyzer.dampened_check_report(report) for report in self.reports])
