# -*- coding: utf-8 -*-
"""
Assignment: The objective of this assignment is for you to (a) develop a set of tests for an 
existing triangle classification program, (b) use those tests to find and fix defects in that program, 
and (c) report on your testing results for the Triangle problem
@author: NehharShah
@author: Nihar Shah
Date: 20 September 2022
"""
def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code 
passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer 
values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then 
return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'   
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if not ((a + b > c) or (b + c > a) or (a + c > b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c) or ((c * c) + (b * b)) == (a * a) or ((a * a) + (c * c)) == (b * b):
        return 'Right'
    elif a == b or b == c or a ==c:
        return 'Isosceles'
    else:
        return 'Scalene'