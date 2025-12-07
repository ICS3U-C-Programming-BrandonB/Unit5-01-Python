#!/usr/bin/env python3
# Created By: Brandon
# Date: 12/07/2025
# Program allows a user to enter a temperature in degrees Celsius (as a decimal), then converts it to degrees Farenheit and displays the result.


def calculateTemperature():
    # get temperature in celsius from user
    celsius = float(input("Enter the temperature in Celsius: "))

    # convert celsius to farenheit
    farenheit = (celsius * 9 / 5) + 32

    # display the temperature in farenheit
    print("The temperature in Farenheit is: {}°F".format(farenheit))


def main():
    calculateTemperature()


if __name__ == "__main__":
    main()
