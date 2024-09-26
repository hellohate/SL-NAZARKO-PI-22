def describe_car(color: str = '', brand: str ='Машину', usage: int = None) -> str:
    output_string = f'Я планую купити {color.lower()} {brand.upper()}'
    if usage:
        output_string += f', витрати пального якого неперевищують {usage}л на 100 км'
    print(output_string)
    return output_string





