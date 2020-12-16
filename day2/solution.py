from re import compile

PATTERN = compile(r"(?P<from>\d+)-(?P<up_to>\d+) (?P<letter>\w): (?P<password>\w+)")


def file_read(file_name: str) -> list:
    with open(file_name) as f:
        return f.readlines()


def main() -> int:
    passwords = file_read('input')
    counter = 0
    for password in passwords:
        if match := PATTERN.match(password):
            groups = match.groupdict()
            if int(groups['from']) <= groups['password'].count(groups['letter']) <= int(groups['up_to']):
                counter += 1
    return counter


if __name__ == '__main__':
    print(main())
