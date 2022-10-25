# SortingAndSearching
Sorting and Searching without using any built-in functions

# Project 4: Sorting & Searching

In this assignment we will be implementing the sorting & search functionality
that we have been studying. However, you get to choose which two sorting
algorithms to implement! We **will not** be using _any_ built-in functions other 
than `range`, `append`, `extend`, or `len`. **No credit** will be given for using the built-in python sort or search 
functions (`sort`, `sorted`, `contains`, `index`, etc.), the keyword `in` for search,  or libraries  functions -- you *must* implement your own sort & search functions for credit!

You can test the code by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 iterative_sort.py`
* To run the tests for one problem: `pytest iterative_sort.py`
* To run all the tests prior to submission: `pytest`

**NOTE: Don't run pytest until your main is working**

### Files that should (& shouldn't!) be changed

You **SHOULD** implement your problem solutions in the following files:
* `linear_search.py`
* `binary_search.py`
* `iterative_sort.py`
* `recursive_sort.py`

  

You **SHOULD NOT** modify any `*_test.py` files:
* `linear_search_test.py`
* `binary_search_test.py`
* `iterative_sort_test.py`
* `recursive_sort_test.py`

### Professionalism
In addition to passing the test cases and meeting the specifications / requirements (e.g., only using permitted built-in functions), your code will be assessed in terms of its **_professionalism_**:
* Following naming convetions: meaningful variable names beginning with a lower case letter, class names beginning with an upper case letter
* DRYness: avoiding unnecessary steps or copy & pasting code (use loops & functions instead!)
* Comments: adding comments to explain what lines in longer methods/functions are doing

## Problem 1: Iterative Linear Search
Write a function `linear_search` that takes an unordered array of numbers `a`  and a number to search for `n` as parameters and returns the index of the first occurrence of the number in the array, or -1 otherwise. Your search should be performed using a loop, rather than recursion.

Given `a = [45, 67, -2, 33, -44, 134, -67]`:

| **Example call** | **Returns** |
| -------------- | --------- |
| `linear_search(a, 1)` | `-1` |
| `linear_search(a, 0)` | `-1` |
| `linear_search(a, -1)` | `-1` |
| `linear_search(a, 2)` | `-1` |
| `linear_search(a, -2)` | `2` |
| `linear_search(a, 134)` | `5` |
| `linear_search(a, 67)` | `1` |
| `linear_search(a, -67)` | `6` |


## Problem 2: Recursive Binary Search
Write a recursive function `binary_search` that takes an ordered array of numbers `a`  and a number to search for `n` as  parameters and returns the index of the first occurrence of the number in the array, or -1 otherwise. For full credit, the search should be implemented using recursion, rather than a loop.

Given `a = [-1, 1, 3, 5, 7, 9]`:

| **Example call** | **Returns** |
| -------------- | --------- |
| `binary_search(a, 1)` | `1` |
| `binary_search(a, 0)` | `-1` |
| `binary_search(a, -1)` | `0` |
| `binary_search(a, 2)` | `-1` |
| `binary_search(a, -2)` | `-1` |
| `binary_search(a, 4)` | `-1` |
| `binary_search(a, 5)` | `3` |
| `binary_search(a, 6)` | `-1` |
| `binary_search(a, 7)` | `4` |
| `binary_search(a, 134)` | `-1` |
| `binary_search(a, -67)` | `-1` |


## Problem 3: Iterative Sort

Write an *O(n<sup>2</sup>)* sort function `iterative_sort` that takes an unordered array of numbers as a parameter and returns a sorted array using bubble sort, insertion sort, or selection sort using loops, rather than recursion.

| **Example call** | **Returns** |
| -------------- | --------- |
| `iterative_sort([45, 67, -2, 33, 0, -44, 134, -67])` | `[-67, -44, -2, 0, 33, 45, 67, 134]` |
| `iterative_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |
| `iterative_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` |


## Problem 4: Recursive Sort

Write a less than *O(n<sup>2</sup>)* sort function `recursive_sort` that takes an unordered array of numbers as a parameter and returns a sorted array using merge sort or quick sort with recursion, rather than loops.

| **Example call** | **Returns** |
| -------------- | --------- |
| `recursive_sort([45, 67, -2, 33, 0, -44, 134, -67])` | `[-67, -44, -2, 0, 33, 45, 67, 134]` |
| `recursive_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |
| `recursive_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` |

## 

## Getting started

### Develop online

Click the "Work in Repl.it" button. Edit the file. To run, see the commands below.

### Develop in PyCharm

With this option, you can develop on your laptop. 
You will need to install PyCharm (or another IDE),
git, and pytest. PyCharm has some built-in git 
support.

## Testing
Many of the tests are failing right now because the 
functions
aren't outputting the correct information. Fixing this
will make the tests pass & turn green.

### Setup
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

### Run commands
To run just the main code for one problem:

`python3 file.py`

To run the tests for one problem:

`pytest file_test.py`

To run all the tests prior to submission:

`pytest`

