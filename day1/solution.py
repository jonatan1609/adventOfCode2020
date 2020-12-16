SUM_RESULT = 2020


def file_read(file_name: str) -> list:
    with open(file_name) as f:
        return f.readlines()


def main() -> int:
    numbers: list[int] = [int(x) for x in file_read('input')]
    for i in numbers:
        for j in numbers:
            if i + j == SUM_RESULT:
                return i * j


if __name__ == '__main__':
    print(main())
