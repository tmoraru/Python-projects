#!/usr/bin/env python

# 1. Input (receive info)
charge_for_food = float(input('\nHow much was charged for food: $'))

# 2. Process (calculate info)
TIP_PERCENTAGE = .20
TAX = .08

def tip (charge_for_food, TIP_PERCENTAGE ):
  return charge_for_food * TIP_PERCENTAGE 

def tax (charge_for_food, TAX ):
  return charge_for_food * TAX 

# For what was charged
print('Tip:', tip(charge_for_food, TIP_PERCENTAGE) )
print(' Tax:', tax(charge_for_food, TAX))

# Task by tmoraru
