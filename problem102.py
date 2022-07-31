class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def main():
    origin = Point(0, 0)
    ans = 0
    with open("p102_triangles.txt") as f:
        text = f.read()
        lines = text.split("\n")
        for line in lines:
            if len(line) == 0:
                continue
            coords = line.split(",")
            p1 = Point(int(coords[0]), int(coords[1]))
            p2 = Point(int(coords[2]), int(coords[3]))
            p3 = Point(int(coords[4]), int(coords[5]))
            if point_in_triangle(origin, p1, p2, p3):
                ans += 1
    print(ans)


def point_in_triangle(target_point: Point, p1: Point, p2: Point, p3: Point) -> bool:
    """https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle?answertab=trending#tab-top"""
    denominator = ((p2.y - p3.y) * (p1.x - p3.x)) + ((p3.x - p2.x) * (p1.y - p3.y))
    a = ((p2.y - p3.y) * (target_point.x - p3.x) + (p3.x - p2.x) * (target_point.y - p3.y)) / denominator
    b = ((p3.y - p1.y) * (target_point.x - p3.x) + (p1.x - p3.x) * (target_point.y - p3.y)) / denominator
    c = 1 - a - b
    return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1


if __name__ == "__main__":
    main()
