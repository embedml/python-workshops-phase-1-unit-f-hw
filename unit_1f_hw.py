'''
In this file you will fill in each class and method.

Try to follow naming exactly in the file, otherwise it 
may result in a false failure. Each method and class 
name is case and space sensitive. 
'''


'''

For Unit 1F you will practice what you practice below:

- Classes
    - Creating an object 
    - Creating the init function
    - setting attributes with the init function
    - Creating more functions in the same class


'''



##### Create a Class Below #######
'''
Create a class called Car, create an __init__ method (constructor) that takes in 
`miles_per_gallon`, and assigns it to the attribute `mpg`. Have it take in `car_name` and assigns
it to the attribute `name`.

'''

##################################

##### Create a Class Below #######
'''
Create a class called Dog, create an __init__ method (constructor) that takes in `breed`, and assigns
it to the attribute `breed`. Have __init__ also take in `weight`, an assign it to the attribute `weight`.

Then create a method (aka class function) called `get_breed`. It should return the
`breed` attribute. 

Then create a method called `get_weight`. It should return the `weight` attribute.

Note: The get_x functions should not have an input. Ex: def get_weight(self):

'''

##################################


##### Create a Class Below #######
'''
Create a class called Math_Operations

Create a method called `add`, that takes in `a` and `b`, adds them together (a+b) and returns the value. 

Create a method called `sub`, that takes in `a` and `b`, then subtracts b from a (a-b), and returns the value.

Create a method called `slope_intercept`, that takes in an `m`, `x`, and `b`. Then 
returns the output based on the slope equation (y = m * x + b)

Create a method called `pythagorean`, which takes in `a` and `b`, squares `a` and `b`, takes the sum then returns 
the square roots the summed values. (output = sqrt(a^2 + b^2))

HINT: Use ** instead of ^ for python exponents.
HINT HINT: You can raise variable and numbers to a fractional (or decimal) exponent for roots!
Note: Even though we will not be using self in this class, dont forget to include it as the first
argument in the method definitions. 
'''
##################################

#### Solve the problem below ####
'''
Solve the following problem in the function 'getting_pythags` below:

Create a object that is from the Math_Operations class. 

Create an empty list called `pythags`.

Using a for loop and the Math_Operations class, iterate through 
the `a_list` and `b_list` performing the pythagorean theorem on each item 
from each list respectively. `a_list` items should go into the `a` parameter and 
`b_list` items should go into the `b` parameter. Append each result into 
the `distances` list. 

At the end return the `pythags` list.

'''
def getting_pythags():
    a_list = [0, -2, 1, 4, 10, -3, 2, 5, 2]
    b_list = [1, 2, -3, 14, -1, 0, 1, 5, 1]
    #### Put your code below #####


    ###############################



##################################



##### Create a Class Below #######
'''
Create a class called Garage.

In the class' constructor it should take in a parameter called `num_spots` and assign it to the attribute `num_spots`.

Have the class also start with a attribute called `cars` which has an empty list assigned to it. 

It should also have a method called `add_car()`. This should add a `car` parameter to the `cars` list. This should decrement the
`num_spots` attribute since adding a car means we have one less spot. I`f there are enough spots it should return true.

In the `add_car()` method, it should check to see if there are enough spots left. If there are not enough spots it should 
return False and not add the car to the list. 

Create a method in the class called `show_cars()`. This should return the `cars` list attribute. This method should return the list
of cars that are currently in the garage.

'''


#################################

#### Solve the problem below ####

'''
Do the following in the `garage_problem` function below:

Create a Garage object that has 3 spots.

Create 4 Car objects. 

The first car object should be named "Toyota Tacoma" with 13 miles per gallon.
The second car object should be named "Nissan Altima" with 22 miles per gallon.
The third car object should be named "Volkswagon Beetle" with 23 miles per gallon.
The fourth car object should be named "Ferrari Enzo" with 7 miles per gallon.

Using the car object. Store each car one by one into the garage object you created. 
Hint: Use the "add_car" method in the garage object.
Print the output of the `add_car` method each time you use it. 


Then return the list of cars you added to the garage, as well as the garage object. 
The list should be the first thing returned and the garage object the second
Print the list of cars before returning it in the function.

'''

def garage_problem():
    #### Put your code below ####


    #############################


############################

'''
Do you have any suggestions for this homework? Leave them below! 


'''
