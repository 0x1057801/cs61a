from math import sqrt

def check_year(year):
    top = int(year // 100)
    bottom = int(year % 100)

    return ((top + bottom) * (top + bottom)) == year


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False