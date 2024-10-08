from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	generator = []
	random.seed(seed)
	for i in range(number):
		generator.append(i)
	random.shuffle(generator)
	return generator
	pass

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	pass

	array = gen_random_int(number, seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	array_str = ", ".join(map(str, array)) + "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	numbers = document.getElementById("generate").innerHTML 
	str_list = numbers.split(',')
	int_list = list(map(int, str_list))
	sorted_list = bubble_sort(int_list)
	converted_list = map(str, sorted_list)
	array_str = converted_list
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	str_list = value.split(',')
	str_list.replace(" ","")
	int_list = list(map(int, str_list))
	sorted_list = bubble_sort(int_list)
	converted_list = map(str, sorted_list)
	array_str = converted_list


	document.getElementById("sorted").innerHTML = array_str

def bubble_sort(array):
	n = len(array)
	swapped = True
	while swapped == True:
		swapped = False
		new_n = 0
		for inner_i in range(1,n-1):
			first = array[inner_i - 1]
			second = array[inner_i]
			if first > second:
				array[inner_i - 1], array[inner_i] =  array[inner_i], array[inner_i - 1]
				swapped = True
				new_n = inner_i
		n = new_n
	return array
