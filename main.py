import json

ROW = 0
COL = 1


def parse_into_matrix(arg):
    return [s.split(" ") for s in arg]


with open("./input.json", "rt", encoding="utf-8") as file:
    content = file.read()
    obj = json.loads(content)

matrix = parse_into_matrix(obj["matrix"])
target = parse_into_matrix(obj["target"])
cols = zip(*matrix)
visited = [[False] * len(a) for a in matrix]


def main():
    start = 0
    dir = ROW

    for a in matrix:
        print(a)

    print(target)


if __name__ == "__main__":
    main()
