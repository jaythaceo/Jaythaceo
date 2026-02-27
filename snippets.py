# Some quick code snippets

# List Comprehensions
squares = [x**2 for x in range(10)]
print("Squared numbers.",squares)

#lambda functions
add = lambda x, y: x + y
print(add(5, 3))

# Map, Filter, and Reduce Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Filter function filters the items of a sequence based on a function that returns a boolean value.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Reduce function applies a rolling computation to sequential pairs of values in a list. In this case, it multiplies all the numbers together to get the product.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Decorators are a way to modify the behavior of functions or classes. They allow you to wrap another function to extend its behavior without modifying its code.
import time

def timing_decorator(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute.")
    return result
  return wrapper


@timing_decorator
def slow_function():
  time.sleep(2)
slow_function()


# Context manager
from contextlib import contextmanager
@contextmanager
def my_context():
  print("Entering my context")
  yield
  print("Exiting my context")
with my_context():
  print("Inside my context")

# Generators are a type of iterable, like lists or tuples. However, unlike lists, generators do not store their contents in memory. Instead, they generate items on-the-fly as you iterate over them.
def fibonacci(count):
  a, b = 0, 1
  while count > 0:
    yield a
    a, b = b, a + b
    count -= 1

fib = fibonacci(10)
for num in fib:
  print(num)

# Multithreading and Multiprocessing. Python provides the threading and multiprocessing modules to work with threads and processes, respectively. Threads are lightweight, but they have limitations due to the Global Interpreter Lock (GIL) in CPython. Processes, on the other hand, can take full advantage of multiple CPU cores but have higher overhead.

import threading
import urllib.request

urls = [
    'http://www.google.com',
    'http://www.facebook.com',
    'http://www.X.com',
]

def download_file(url):
  urllib.request.urlretrieve(url, url.split("/")[-1])

# Create and start threads 
threads = []
for url in urls:
  t = threading.Thread(target=download_file, args=(url,))
  t.start
  threads.append(t)

# Wait for all threads to complete
for t in threads:
  t.join() 

print("All downloads completed.")
