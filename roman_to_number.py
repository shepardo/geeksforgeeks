
from collections import defaultdict

class RomanToNumber:

    def __init__(self):
        self.map = defaultdict(int)
        self.map['i'] = 1
        self.map['v'] = 5
        self.map['x'] = 10
        self.map['l'] = 50
        self.map['c'] = 100
        self.map['d'] = 500
        self.map['m'] = 1000

    # iii
    # iv
    # xviii
    # ix
    # 42: xlii -> viiil
    # xlii
    def roman_to_number(self, s):
        acc = 0
        prev_n = -1
        for c in s:
            n = self.map[c]
            if n > prev_n:
                acc = n - acc
                prev_n = n
            else:
                acc += n
                prev_n = n
        return acc
        pass



if __name__ == '__main__':
    roman = RomanToNumber()
    print('iii is {0}'.format(roman.roman_to_number('iii')))
    print('iv is {0}'.format(roman.roman_to_number('iv')))
    print('xviii is {0}'.format(roman.roman_to_number('xviii')))
    print('ix is {0}'.format(roman.roman_to_number('ix')))
    print('xlii is {0}'.format(roman.roman_to_number('xlii')))
    pass
