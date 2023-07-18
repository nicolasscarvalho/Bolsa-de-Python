from abc import ABC, abstractmethod


def line(function):

    def wrapper(*args, **kwargs):
        print('-'*60)
        function(*args, **kwargs)

    return wrapper

class PizzeriaDetails(ABC):
    
    @abstractmethod
    def get_dough_ingredients(function):
        
        def wrapper(*args, **kwargs):
            print('Getting dough ingredients...')
            function(*args, **kwargs)

        return wrapper



    @abstractmethod
    def get_sauce_ingredients(function):

        def wrapper(*args, **kwargs):
            print('Getting sauce ingredients')
            function(*args, **kwargs)

        return wrapper



    @abstractmethod
    def get_topping_ingredients(function):
        
        def wrapper(*args, **kwargs):
            print('Getting topping ingredients')
            function(*args, **kwargs)

        return wrapper



    @abstractmethod
    def get_topping_ingredients(function):
        
        def wrapper(ingredients):
            function(ingredients)

        return wrapper



    @abstractmethod
    def prepare_oven(function):
        
        def wrapper(*args, **kwargs):
            print('Preheating oven...')
            function(*args, **kwargs)

        return wrapper





class MakePizza:

    def __init__(self):
        pass

    @line
    @PizzeriaDetails.get_dough_ingredients
    def prepare_dough(self):
        print('Preparing dough...')

    @line
    @PizzeriaDetails.get_sauce_ingredients
    def prepare_sauce(self):
        print('Preparing sauce...')

    @line
    @PizzeriaDetails.get_topping_ingredients
    def add_topping(self):
        print('Adding topping...')

    @line
    @PizzeriaDetails.prepare_oven
    def bake_pizza(self):
        print('Baking pizza...')




pizza_maker: MakePizza = MakePizza()

pizza_maker.prepare_dough()
pizza_maker.prepare_sauce()
pizza_maker.add_topping()
pizza_maker.bake_pizza()