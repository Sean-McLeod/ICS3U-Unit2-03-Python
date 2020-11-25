#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can calculate the circumference of a circle with
#    radius entered by users


import constants


def main():
    # This function calculates the circumference of a circle

    # input
    radius = int(input("Enter the radius of the circle (mm):"))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("The circumference of the circle is {}mm".format(circumference))


if __name__ == "__main__":
    main()
