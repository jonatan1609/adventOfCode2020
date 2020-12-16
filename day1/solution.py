SUM_RESULT = 2020


def file_read(file_name: str, split_by: str = '') -> str:
    with open(file_name) as f:
        con: str = f.read()
    if split_by:
        con: list = con.split(split_by)
    return con


def main() -> int:
    numbers: list[int] = list(map(int, file_read("input", "\n")))
    for i in numbers:
        for j in numbers:
            if i + j == SUM_RESULT:
                return i * j


if __name__ == '__main__':
    print(main())
