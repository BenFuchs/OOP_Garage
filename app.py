from abc import ABC, abstractmethod
from enum import Enum


class Options(Enum):
    ADD = 1
    DELETE = 2
    UPDATE = 3
    DISPLAY = 4
    EXIT = 5


class Garage:
    car_list = []

    @classmethod
    def display_cars(cls):
        if not cls.car_list:
            print("No cars in the garage.")
        else:
            for idx, car in enumerate(cls.car_list, 1):
                print(f"{idx}. {car.to_json()}")


class Vehicle(ABC):
    @abstractmethod
    def modelInput(self):
        pass

    @abstractmethod
    def yearInput(self):
        pass

    @abstractmethod
    def colorInput(self):
        pass


class Car(Vehicle):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    def modelInput(self, input_value):
        if input_value and len(input_value) > 1:
            self.__model = input_value

    def yearInput(self, input_year):
        if input_year > 0:
            self.__year = input_year

    def colorInput(self, input_color):
        if len(input_color) > 0:
            self.__color = input_color

    def to_json(self):
        return {"model": self.__model, "year": self.__year, "color": self.__color}


def menu():
    while True:
        for option in Options:
            print(f'{option.name} - {option.value}')
        try:
            user_input = int(input("Please select an option: "))
            if user_input in Options._value2member_map_:
                return user_input
            else:
                print("Invalid option. Please select a valid number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


class Actions:
    @staticmethod
    def add():
        model = input("Input car model: ")
        color = input("Input car color: ")
        try:
            year = int(input("Input car year: "))
        except ValueError:
            print("Invalid year. Please enter a valid integer.")
            return
        Garage.car_list.append(Car(model, year, color))
        print(f"Car {model} added to the garage.\n")

    @staticmethod
    def display():
        Garage.display_cars()

    @staticmethod
    def delete():
        if not Garage.car_list:
            print("No cars to delete.")
            return
        Garage.display_cars()
        try:
            index = int(input("Enter the number of the car to delete: ")) - 1
            if 0 <= index < len(Garage.car_list):
                removed_car = Garage.car_list.pop(index)
                print(f"Car {removed_car.to_json()['model']} has been removed from the garage.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    @staticmethod
    def update():
        if not Garage.car_list:
            print("No cars to update.")
            return
        Garage.display_cars()
        try:
            index = int(input("Enter the number of the car to update: ")) - 1
            if 0 <= index < len(Garage.car_list):
                model = input("Input new car model: ")
                try:
                    year = int(input("Input new car year: "))
                except ValueError:
                    print("Invalid year input. Please enter a valid integer.")
                    return
                color = input("Input new car color: ")
                Garage.car_list[index] = Car(model, year, color)
                print(f"Car {index + 1} has been updated.\n")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    @staticmethod
    def exit():
        print("Exiting program.")
        exit()


if __name__ == "__main__":
    actions_map = {
        Options.ADD.value: Actions.add,
        Options.DISPLAY.value: Actions.display,
        Options.DELETE.value: Actions.delete,
        Options.UPDATE.value: Actions.update,
        Options.EXIT.value: Actions.exit,
    }

    while True:
        selected_option = menu()
        action = actions_map.get(selected_option)
        if action:
            action()
        else:
            print("This option is not yet implemented.")
