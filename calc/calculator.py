""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    def addition (tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def subtraction (tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def division (tuple_values: tuple):
        """divide two numbers and store the result"""
        Calculations.add_division_calculation(tuple_values)
        return True