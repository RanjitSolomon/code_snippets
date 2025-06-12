# https://www.kdnuggets.com/7-tools-help-write-better-python-code

# 1. Pylint or Ruff – Code Style and Error Detection
# When you're writing code, it's easy to miss small details like unused variables or inconsistent spacing. 
# Pylint is a static code analyzer that catches these issues before they become problems.
# https://pypi.org/project/pylint/

# Pylint reads through your Python code—without running it (that’s what static analyzers do)—and points out style issues, 
# potential errors, and places where your code could be improved.

# Key Features 
# - Checks if your code follows Python's style guide (PEP 8)
# - Spots code that's written but never used
# - Identifies complex code that might need simplifying
# - Finds common programming mistakes
# - Can write custom checkers to match preferences and requirements
# https://pylint.readthedocs.io/en/latest/development_guide/how_tos/custom_checkers.html

# **Note**: You may also want to check out Ruff and use it alongside or in place of Pylint.
# https://github.com/astral-sh/ruff
#======================================================================================

#2. Mypy - Static Type Checking
# Have you ever run your code only to find out that somewhere, you accidentally tried to use a string 
# where you needed a number? Mypy catches these kinds of mistakes before you run your code—saving 
# you time and headaches in debugging.
# https://mypy.readthedocs.io/en/stable/

# Mypy is a static type checker that looks at your code's type hints (those little annotations 
# that tell you what kind of data you're working with) and makes sure everything adds up.

# Key features: 
# - Works with Python's built-in type hints
# - Lets you mix typed and untyped code (perfect when you want to gradually adding types)
# - Catches type-related bugs early
# - Helps document your code's expected inputs and outputs
# - Makes it safer to make significant changes to your code

# To get started, see the mypy cheat sheet and how to use mypy with an existing project.
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://mypy.readthedocs.io/en/stable/existing_code.html

# 3. Pytest - Testing Framework
# How do you know your code works? Really works, not just "seems to work". T
# hat's where testing comes in.

# But writing tests doesn't (always) have to be complicated. Pytest makes it almost 
# fun – seriously! It is a testing tool that helps you write everything from simple 
# checks to complex test suites.

# Key features: 
# - Provides detailed information when tests fail
# - Lets you run specific groups of tests
# - Shares setup code between tests efficiently

# Here are a couple of tutorials from the KDnuggets Python library to help you get started with Pytest:
# - Beginner’s Guide to Unit Testing Python Code with Pytest - https://www.kdnuggets.com/beginners-guide-unit-testing-python-code-pytest
# - Getting Started with Pytest: Effortlessly Write and Run Tests in Python - https://www.kdnuggets.com/getting-started-with-pytest-effortlessly-write-and-run-tests-in-python

# 4. Black - Code Formatter
# Ever spent time wondering if you should put a space after that comma? Black makes these decisions for you.
# So instead of spending time debating about formatting or manually fixing indentation, you can focus on what your code actually does. 
# Given your Python code, Black gives a cleanly formatted version that follows consistent rules.

# Key features: 
# - Auto-formats your code
# - Requires minimal configuration
# - Works with most editors
# - Makes code reviews faster (yeah, no more formatting discussions!)

# Learn to use Black in your project - https://black.readthedocs.io/en/stable/guides/introducing_black_to_your_project.html
# with other tools - https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html

# 5. Bandit - Security Linter
# Security issues in code can be subtle and easy to miss. Bandit helps catch common security mistakes early,
# before they make it into your running application where they could cause real problems.
# https://bandit.readthedocs.io/en/latest/

# Bandit scans your code for common security problems, like using unsafe functions or hardcoded 
# passwords and other sensitive info.

# Key Features: 
# - Identifies common security issues
# - Adjusts warnings based on how serious the issue is
# - Provides clear explanations of potential problems
# - Can use pre-commit to integrates with your version control system

# The getting started guide will help you learn to use Bandit for your projects, create reports, 
# compare them to a baseline, and more. - https://bandit.readthedocs.io/en/latest/start.html


# 6. Coverage.py - Code Coverage Tool
# How much of your code are your tests actually testing? Coverage.py gives you the answer. 
# Because only having tests isn't enough – you need to know they're testing the code right.

# Coverage.py watches your tests run and keeps track of which lines of code they execute. 
# It helps you find code that isn't being tested, so you can add tests where they're needed most.

# Key Features: 
# - Shows which lines of code were run during tests
# - Creates easy-to-read reports
# - Identifies branches in your code that weren't tested
# - Works well with PyTest and other testing frameworks

# This starter guide contains all you need to get started with Coverage.py.
# https://coverage.readthedocs.io/en/7.6.10/#quick-start


# 7. isort - Import Optimizer

# Let's wrap up with a tool that helps keep your code's "front matter" tidy - isort that stands for “import sort”.
# https://pycqa.github.io/isort/

# Well-organized imports make your code easier to read and understand. When you're working with a team, 
# having a consistent way to organize imports helps everyone follow along.

# It sorts imports alphabetically and also by type. So it essentially sorts imports into neat, l
# ogical groups and makes sure they follow a consistent pattern.

# Key features: 
# - Automatically sorts your imports
# - Works with different import styling preferences
# - Works super smoothly with code editors
# - Lets you create custom import sections

# You can check out this quickstart guide to start using the isort Python API.
# https://pycqa.github.io/isort/docs/quick_start/3.-api.html






















