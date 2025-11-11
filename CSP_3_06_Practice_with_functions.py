#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    return (a+b+c)/2

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s,a,b,c):
    return s*(s-a)*(s-b)*(s-c)

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    mult = multiplyDifferences(s,a,b,c)
    return root(mult)


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(n):
    return n*2

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(b,y):
    newB = -b
    return newB+y, newB-y
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    return (b**2)-(a*c*4)

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(x,y,z):
    return plusMinus(y,root(mainCalc(x, y, z)))[0] / denominator(x), plusMinus(y, root(mainCalc(x, y, z)))[
        1] / denominator(x)