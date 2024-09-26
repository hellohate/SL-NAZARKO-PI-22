import src.Task1
import src.Task2


if __name__ == '__main__':
    car_1 = ["Toyota", "Volkswagen", "Ford", "Hyundai", "Honda", "Nissan", "Chevrolet",
             "Kia", "Mercedes", "BMW", "Audi", "Citroen", "Lexus", "Mazda", "Mitsubishi"]
    car_2 = ["Smart", "Seat", "saaB", "mini", "land rover"]
    src.Task1.work_with_lists(car_1, car_2)

    countries = ["argentina", "belgium", "bulgaria", "brazil", "united Kingdom",
                 "greece", "Denmark", "dominican RepubliC", "usa", "Liechtenstein"]
    new_countries = ["Poland", "Brazil", "Portugal", "Belgium", "Romania", "USA",
                     "UK", "Japan", "Brazil"]

    formatted_countries = src.Task2.list_preparation(countries)
    updated_countries = src.Task2.list_concat(formatted_countries, new_countries)
    print(formatted_countries, updated_countries)
