import sys

def calender(start_day: int, days: int) -> None:

    header = "Sun Mon Tue Wed Thr Fri Sat"
    print(header)

    cells = []
    for _ in range(start_day - 1):
        cells.append("   ")


    for d in range(1, days + 1):
        cells.append(f"{d:>3}")


    for i in range(0, len(cells), 7):
        row = cells[i:i+7]
        print(" ".join(row))


def main() -> int:
    data = sys.stdin.read().strip().split()
    if not data:
        return 0
    start = int(data[0])
    days = int(data[1])
    calender(start, days)
    return 0
