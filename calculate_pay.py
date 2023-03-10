"""
>>> calculate_pay(10, 10)
100
>>> calculate_pay(50, 10)
600
"""


def calculate_pay(hours, wage):
    if hours <= 0 or wage <= 0:
        pay = 0
        return pay
    elif hours > 40:
        pay = 40 * wage + (hours - 40) * wage * 2
        return pay
    else:
        pay = hours * wage
        return pay


def main():
    example = calculate_pay(20, 0.25)
    print(example)


if __name__ == "__main__":
    main()
