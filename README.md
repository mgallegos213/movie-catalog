# Movie Catalog

## Background
The MovieCatalog class uses a combination of Python's dictionary structure and the SortedDict from the `sortedcontainers` library. This allows us to organize movies by genre and year, and optimizes lookup times when querying the movies.

This combined structure enables efficient queries by both genre and year. Because SortedDict is implemented as a self-balancing binary search tree (BST), the lookup times for querying a specific year are O(log n), with n being the number of unique years (keys) in the dataset. In our get_movies method, the time complexity is O(klog n + m), where k is the query range of years, n is the number of unique years, and m is the number of movies in the specified range of years.

## Usage
Run unit test:
```python
python3 -m unittest unit_test.py
```

## Sources used:
- [Introduction to Sorted Containers](https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/)
- [SortedDict Documentation](https://grantjenks.com/docs/sortedcontainers/sorteddict.html)
- [Using Python3 SortedDict Effectively](https://leetcode.com/discuss/study-guide/1515408/using-python3-sorteddict-effectively-floor-ceillings-minimum-maximum-etc)
- [Python Unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [How to Use Unittest to Write a Test Case for a Function in Python](https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python)
