 #!/usr/bin/env python3

import datetime
from functools import wraps

def spent_time_logging_decorator(function):
	@wraps(function)
	def wrapper(*args):
		start = datetime.datetime.now()
		result = function(*args)
		end = datetime.datetime.now()
		spent_time = end - start
		print("spent {} microseconds in {} with arguments {}. Result was: {}".format(spent_time.microseconds, function.__name__, str(args), result))
		return result 
	return wrapper


def is_palindrome(string_value):
	char_array = list(string_value)
	size = len(char_array)
	half_size = int(size / 2)
	for i in range(0, half_size):
		if char_array[i] != char_array[size - i - 1]:
			return False
	return True

@spent_time_logging_decorator
def convert_to_palindrome(v):
	def action(string_value, chars):
		chars_to_append = list(string_value)[0:chars]
		chars_to_append.reverse()
		new_value = string_value + "".join(chars_to_append)
		if not is_palindrome(new_value):
			new_value = action(string_value, chars + 1)
		return new_value

	return action(v, 0)
	