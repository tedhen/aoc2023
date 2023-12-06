from math import sqrt, prod, floor, ceil

def solve_quadratic_eq(a, b, c):
    x1 = (-b - (sqrt(b*b - 4*a*c))) / 2*a
    x2 = (-b + (sqrt(b*b - 4*a*c))) / 2*a

    return (ceil(x1), floor(x2))

def math_time(time, dist):
    #1. dist = s * t_left
    #2. time = t_press + t_left
    #3. s = t_press
    #4. t_press = time - t_left
    #5. dist = (time - t_left) * t_left
    #6. t_left^2 - time * t_left + dist = 0
    #7. dist+1, we must beat the current record
    t_left1, t_left2 = solve_quadratic_eq(1, -int(time), int(dist)+1)
    x = (t_left2 - t_left1) + 1
    return x

def main():
    with open('day6/input.txt', encoding='utf8') as f:
        time = f.readline().strip().split(':')[1].split()
        dist = f.readline().strip().split(':')[1].split()
        puzzle_part1 = list(zip(time,dist))
        solution = [math_time(*x) for x in puzzle_part1]
        print(f"Part1: {prod(solution)}")
        puzzle_part2 = (''.join(time), ''.join(dist))
        print(f"Part2: {math_time(*puzzle_part2)}")

if __name__ == '__main__':
    main()
