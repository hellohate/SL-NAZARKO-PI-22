def make_pizza(pizza_size: int = 30, *args: str) -> str:
    output_string = f'Making a {pizza_size}-inch pizza with the following toppings:\n'
    for item in args:
        output_string += f'- {item}\n'
    print(output_string)
    return output_string
