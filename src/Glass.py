#!/usr/bin/python

from .DrinkStorage import DrinkStorage
from .Alcoholic import Alcoholic
import csv
import re


class Glass(DrinkStorage):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user is planning on using for cocktails"""
    _cocktails = {}

    def __init__(self):
        super().__init__()
        with open('data/cocktails.csv', newline='') as file:
            # skip header line
            next(file)
            fp = csv.reader(file)
            self.parse(fp)

    @property
    def cocktails(self):
        """Get list of all cocktails parsed from data"""
        return self._cocktails

    @cocktails.setter
    def cocktails(self, value):
        """Set list of all cocktails parsed from data"""
        self._cocktails = value

    # Pre: File must be a valid file location
    # Post: Stores cocktails in list of cocktails
    def parse(self, fp):
        """Parse cocktail file trying to grab elements
           (csv not made very well some aspects missing,
           therefore try catches)"""
        c_id = 0
        for row in fp:
            c = Cocktail()
            fields = Glass.parse_row(row)
            c.name = fields[0]
            c.glass = fields[1]
            c.main_alcohol = fields[2]
            c.other_alcohols = fields[3]
            c.mixes = fields[4]
            c.garnish = fields[5]
            self.cocktails[c_id] = c
            c_id += 1

    # Pre: row must be a valid list of strings from csv data
    #      row should have 6 elements
    # Post: Returns a list of string fields that were
    #       successfully extracted from the row list
    @staticmethod
    def parse_row(row):
        CONST_MAX_ROWS = 6  # Constant Number of rows that doesn't change in mock data
        fields = []
        for i in range(0,CONST_MAX_ROWS):
            try:
                attr = row[i]
                fields.append(attr)
            except IndexError:
                fields.append('')
        return fields

    # Pre: name must be valid string
    # Post: Returns parameter from dictionary if found
    def get_cocktail(self, name):
        """Find cocktail by name and return cocktail object"""
        for cocktail in self.cocktails.values():
            if getattr(cocktail, 'name', False) == name:
                return cocktail

    # Pre: N/A (suggested use requires drinks to be in Glass
    # Post: Returns list of cocktails that can be made satisfying all requirements of each cocktail with the categories
    #       provided
    def find_cocktails(self):
        """Find cocktails that meet all category requirements -
               only cocktails whose main_alcohol, other_alcohols, and mixes
               are in the categories list (list of drinks in fridge)"""

        alcoholic = []
        non_alcoholic = []
        for drink in self.drinks.values():
            if isinstance(drink, Alcoholic):
                alcoholic.append(drink.category)
            else:
                non_alcoholic.append(drink.desc)

        result = []
        for cocktail in self.cocktails.values():
            has_main_alcohol = False
            has_other_alcohol = False
            has_mix = False
            main_alcohol = getattr(cocktail, 'main_alcohol', False).lower()
            other_alcohol = getattr(cocktail, 'other_alcohols', False).lower()
            mixes = getattr(cocktail, 'mixes', False).lower()

            main_alcohol_list = main_alcohol.split(',')
            other_alcohol_list = other_alcohol.split(',')
            mixes_list = mixes.split(',')

            for main_requirement in main_alcohol_list:
                requirement_list = re.findall(r"[\w']+|[.,!?;]", main_requirement)
                if len(requirement_list) != 0:
                    found = False
                    for categoryList in alcoholic:
                        for attribute in categoryList:
                            if str(attribute).lower() != "none":
                                if any(x in str(attribute).lower() for x in requirement_list):
                                    found  = True
                                    break
                        if found:
                            break

                    if found:
                        has_main_alcohol = True
                    else:
                        has_main_alcohol = False
                        break
                else:
                    has_main_alcohol = True

            for other_requirements in other_alcohol_list:
                requirement_list = re.findall(r"[\w']+|[.,!?;]", other_requirements)
                if len(requirement_list) != 0:
                    found = False
                    for categoryList in alcoholic:
                        for attribute in categoryList:
                            if str(attribute).lower() != "none":
                                if "vermouth" in str(attribute).lower() and any("vermouth" for x in requirement_list):
                                    if "dry" in str(attribute).lower() and not "dry" in str(requirement_list).lower():
                                        continue
                                    elif "sweet" in str(attribute).lower() and not "sweet" in str(requirement_list).lower():
                                        continue
                                if any(x in str(attribute).lower() for x in requirement_list):
                                    found = True
                                    break
                        if found:
                            break

                    if found:
                        has_other_alcohol = True
                    else:
                        has_other_alcohol = False
                        break
                else:
                    has_other_alcohol = True
                    break

            for mix_requirements in mixes_list:
                if len(mix_requirements) != 0:
                    found = False
                    for attribute in non_alcoholic:
                        if str(attribute).lower() != "none":
                            if str(attribute).lower() in mix_requirements or mix_requirements in str(attribute).lower():
                                found = True
                                break
                    if found:
                        has_mix = True
                    else:
                        has_mix = False

                else:
                    has_mix = True

            if cocktail not in result and has_main_alcohol and has_other_alcohol and has_mix:
                result.append(cocktail)

        return result


class Cocktail:
    """Class containing all cocktail requirements: main-alcohol, other alcohols, mixes, and garnishes."""

    def __init__(self, name='', glass='', main_alcohol='', other_alcohols='', mixes='', garnish=''):
        self._name = name
        self._glass = glass
        self._main_alcohol = main_alcohol
        self._other_alcohols = other_alcohols
        self._mixes = mixes
        self._garnish = garnish

    @property
    def name(self):
        """Get Name of cocktail"""
        return self._name

    @name.setter
    def name(self, name):
        """Set Name of cocktail"""
        self._name = name

    @property
    def glass(self):
        """Get Glass type of cocktail"""
        return self._glass

    @glass.setter
    def glass(self, glass):
        """Set Glass type of cocktail"""
        self._glass = glass

    @property
    def main_alcohol(self):
        """Get main alcohol needed for cocktail"""
        return self._main_alcohol

    @main_alcohol.setter
    def main_alcohol(self, main_alcohol):
        """Set main alcohol needed for cocktail"""
        self._main_alcohol = main_alcohol

    @property
    def other_alcohols(self):
        """Get other alcohols needed for cocktail"""
        return self._other_alcohols

    @other_alcohols.setter
    def other_alcohols(self, other_alcohols):
        """Set other alcohols needed for cocktail"""
        self._other_alcohols = other_alcohols

    @property
    def mixes(self):
        """Get mixes needed for cocktail"""
        return self._mixes

    @mixes.setter
    def mixes(self, mixes):
        """Set mixes needed for cocktail"""
        self._mixes = mixes

    @property
    def garnish(self):
        """Get garnish needed for cocktail"""
        return self._garnish

    @garnish.setter
    def garnish(self, garnish):
        """Set garnish needed for cocktail"""
        self._garnish = garnish

    # Pre: None
    # Post: Returns string of Vital information from Cocktail object instance
    def __str__(self):
        return "Glass: %s\nMain Alcohol: %s\nOther Alcohols: %s\nMixes: %s\nGarnish: %s\n" % \
               (self.glass, self.main_alcohol, self.other_alcohols, self.mixes, self.garnish)

