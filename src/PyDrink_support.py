#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 11, 2019 12:32:59 PM EST  platform: Windows NT

import sys
import csv
from .Fridge import Fridge
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
from .Glass import Glass
from . import Cocktails


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fridge = Fridge()
glass = Glass()


def parse_mock():
    """Parses mock data to add to fridge, will be deprecated in A2 once I utilize the LCBO API"""
    with open('data/mock/fridge.csv', newline='') as file:
        """File is formatted:
        Alcoholic
        Name,Price,Description, Alcohol%,Package,Category
        ...
        ...
        ...
        NonAlcoholic
        Name,Price,Description, Carbonated,Sugar Content,Package,Caffiene Content
        ...
        ...
        ...        
        """
        # skip header line
        d_id = 0
        line = file.readline().strip()
        if line == 'Alcoholic':
            next(file)
            fp = csv.reader(file)

            for row in fp:
                if row[0] == 'NonAlcoholic':
                    line = row[0]
                    break

                drink = Alcoholic(d_id, row[0], int(row[1]), row[2], int(row[3]), row[4], row[5])
                fridge.add_drink(drink)
                d_id += 1
        if line == 'NonAlcoholic':
            next(file)
            fp = csv.reader(file)

            for row in fp:
                is_carbonated = True
                if row[3] == 'False':
                    is_carbonated = False

                drink = NonAlcoholic(d_id, row[0], int(row[1]), row[2], is_carbonated, row[4], row[5], row[6])
                fridge.add_drink(drink)
                d_id += 1


def btn_add_glass_lclick(p1, tree, glass_list, success_message):
    print('PyDrink_support.btn_add_glass_lclick')
    print('p1 = {0}'.format(p1))

    """Event triggered when add to glass button is pressed
    1. Empties the Glass TreeView in Glass tab
    2. Repopulates it with all selected Beverages in the Fridge tab"""
    for child in glass_list.get_children():
        glass_list.delete(child)

    # Iterate through all items in TreeView adding all selected items to Glass
    count = 0
    for child in tree.get_children():
        if str(tree.item(child, "values")) == "('Yes',)":
            count += 1
            glass_list.insert('', 'end', text=tree.item(child, "text"), values=tree.item(child, "values"))

    if count > 0:
        success_message.configure(state=tk.NORMAL)

    sys.stdout.flush()


def ntb_open_fridge(p1, tree, textbox_selected, success_message):
    print('PyDrink_support.ntb_open_fridge')
    print('p1 = {0}'.format(p1))

    """Event triggered when the fridge tab is opened
    1. If the fridge is empty, attempt to parse the mock data
    2. Call method to add drinks from the fridge to the TreeView"""

    if fridge.drinks.__len__() == 0:
        parse_mock()
    for drink in fridge.drinks.values():
        print("Drink: %s Selected: %s" % (drink.name, str(drink.selected)))
    success_message.configure(state=tk.DISABLED)
    insert_manager_tree(tree, fridge, textbox_selected, success_message)

    sys.stdout.flush()


def ntb_open_glass(p1, tree, cocktail_tree, textbox_selected):

    print('PyDrink_support.ntb_open_fridge')
    print('p1 = {0}'.format(p1))

    for drink in fridge.drinks.values():
        print("Drink: %s Selected: %s" %(drink.name, str(drink.selected)))

    cocktail_categories = {}
    alcoholic = []
    non_alcoholic = []

    """Iterate through all items in TreeView adding all to dict obj"""
    glass.empty_glass()
    for child in tree.get_children():
        drink = fridge.find_drink('name', tree.item(child, "text"))
        if not glass.has_drink(drink.id):
            glass.add_drink(drink)
        if isinstance(drink, Alcoholic):
            alcoholic.append(drink.category)
        else:
            non_alcoholic.append(drink.name)

    cocktail_categories["Alcoholic"] = alcoholic
    cocktail_categories["NonAlcoholic"] = non_alcoholic
    insert_cocktail_tree(cocktail_tree, Cocktails.find_cocktails(cocktail_categories), textbox_selected)

    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    Cocktails.init()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def insert_manager_tree(tree, obj, textbox_selected, success_message=None):
    """Insertion method."""
    #Clears TreeView
    for child in tree.get_children():
        tree.delete(child)

    for drink in obj.drinks.values():
        selected = 'No'
        if drink.selected:
            selected = 'Yes'
        tree.insert('', 'end', text=str(drink.name),
                    values=selected)
        tree.bind("<Double-1>", lambda e: stv_list_selected_dclick(e, tree, success_message))
        tree.bind("<ButtonRelease-1>", lambda e: stv_select_lclick(e, tree, obj, textbox_selected))


def insert_cocktail_tree(tree, obj, textbox_selected):
    """Insertion method."""
    # Clears TreeView
    for child in tree.get_children():
        tree.delete(child)

    for cocktail in obj:
        tree.insert('', 'end', text=str(cocktail.name),
                    values='No')
        tree.bind("<ButtonRelease-1>", lambda e: stv_cocktail_selected(e, tree, textbox_selected))


def stv_select_lclick(p1, tree, obj, textbox_selected):
    """Update Description of selected frame"""
    print('PyDrink_support.stv_list_selected_dclick')
    print('p1 = {0}'.format(p1))
    item = tree.selection()[0]
    drink = obj.find_drink('name', tree.item(item, "text"))

    if drink is not None:
        # 1 - line 0 - coloumn
        textbox_selected.delete('1.0', tk.END)
        textbox_selected.insert('1.0', str(drink))


def stv_cocktail_selected(p1, tree, textbox_selected):
    """Update Description of selected frame"""
    print('PyDrink_support.stv_cocktail_selected')
    print('p1 = {0}'.format(p1))
    item = tree.selection()[0]
    cocktail = Cocktails.get_cocktail(tree.item(item, "text"))

    if cocktail is not None:
        # 1 - line 0 - coloumn
        textbox_selected.delete('1.0', tk.END)
        textbox_selected.insert('1.0', "Glass: %s\nMain Alcohol: %s\nOther Alcohols: %s\nMixes: %s\nGarnish: %s\n"
                                % (cocktail.glass, cocktail.main_alcohol, cocktail.other_alcohols, cocktail.mixes,
                                   cocktail.garnish))


def stv_list_selected_dclick(p1, tree, success_message):
    """Update Selection of drink in fridge"""
    print('PyDrink_support.stv_list_selected_dclick')
    print('p1 = {0}'.format(p1))
    item = tree.selection()[0]
    drink = fridge.find_drink('name', tree.item(item, "text"))

    # Flip sign of selected
    if tree.item(item, "values")[0] == 'No':
        tree.item(item, values='Yes')
        drink.selected = True
    else:
        tree.item(item, values='No')
        drink.selected = False

    if success_message is not None:
        success_message.configure(state=tk.DISABLED)


if __name__ == '__main__':
    import PyDrink
    PyDrink.vp_start_gui()




