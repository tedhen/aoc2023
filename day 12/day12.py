import re

def find_arrangement(report, groups):

    arrangements = 0

    if len(report) == 0 and len(groups) > 0:
        return 0
    elif len(report) == 0 and len(groups) == 0:
        return 1
    elif len(report) > 0 and len(groups) == 0:
        return 0

    cur = report[0]
    if cur == '.':
        arrangements = find_arrangement(report[1:], groups)
    elif cur == '?':
        operational = '.' + report[1:]
        damaged = '#' + report[1:]
        arrangements = find_arrangement(operational, groups) + find_arrangement(damaged, groups)
    elif cur == '#':
        g = groups[0]
        damaged = [ True for x in report[:g] if x == '#']

        #count number of #
        # if less than g
            # and next ., then return 0
            # or next ?, then replace with # and retry function 
        # if equal then pop groups and amount matching
        # if more than g, return 0

        try:
            if all(damaged) and report[g] != '#':
                arrangements = find_arrangement(report[g:], groups[1:])
        except IndexError:
            pass

    else:
        raise ValueError('Unknown type of char')

    return arrangements

def main():
    with open('day 12/test_input.txt', encoding='utf8') as f:
        puzzel_input = []
        for l in f:
            report = re.match(r"[.?#]*", l).group(0)
            groups = re.findall(r'\d', l)
            puzzel_input.append((report, list(map(int,groups))))
        


    x = find_arrangement(*puzzel_input[0])
    print(x)


if __name__ == '__main__': 
    main()