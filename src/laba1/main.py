from src.Task3 import describe_car
from src.Task4 import count_expression
from src.Task6 import make_pizza


def main():
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
    f1 = describe_car('Червону', 'audi', 12)
    f2 = count_expression()
    print(str(f2) + ',\n' + f1)

if __name__ == '__main__':
    main()