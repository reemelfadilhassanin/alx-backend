# Pagination Project

This project implements a RESTful API with pagination capabilities using Python. It demonstrates how to paginate a dataset efficiently and provides a structured approach to handle pagination requests.

## Resources

- **Read or Watch:**
  - [REST API Design: Pagination](#)
  - [HATEOAS](#)

## Learning Objectives

At the end of this project, you should be able to explain the following concepts:

- How to paginate a dataset using simple `page` and `page_size` parameters.
- How to paginate a dataset using hypermedia metadata.
- How to implement pagination in a deletion-resilient manner.

## Requirements

- All your files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3** (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should conform to the **pycodestyle** style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your functions should have documentation that clearly explains their purpose.
- All functions and coroutines must be type-annotated.

## Setup

Use the provided dataset `Popular_Baby_Names.csv` for your project.

## Tasks

### 0. Simple Helper Function

Write a function named `index_range` that takes two integer arguments: `page` and `page_size`. This function should return a tuple of size two containing the start index and end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed.

Example usage:

```python
index_range(1, 7)  # Returns (0, 7)
index_range(3, 15) # Returns (30, 45)
```
