#!/usr/bin/env python3
# Created by: Katie G
# Created on: September 28th, 2022
# This program calculates the cost for a pizza
# by getting the diameter of the pizza from
# the user and including HST to give a cost
# in Canadian dollars.
import constants


def main():
    # input
    diameter = float(
        input("Please insert the diameter you’d like your pizza to be in inches: ")
    )

    # process
    subtotal = (
        diameter * constants.INGREDIENTS + constants.RENTAL_COST + constants.LABOUR_COST
    )
    tax_dollars = subtotal * constants.HST
    total = subtotal + tax_dollars

    # output
    print("")
    print("The total cost of your pizza, including HST, is ${:,.2f} CAD.".format(total))


if __name__ == "__main__":
    main()
