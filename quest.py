
def questions():
    data={}

    list = [
    ["What does the `*args` in a function definition signify?", ('A specific number of arguments', 'A list of arguments', 'A tuple of variable number of arguments', 'A dictionary of named arguments')],
    ["Which method checks if all elements in a list are true in a boolean context?", ('all()', 'any()', 'sum()', 'collect()')],
    ["What is the default behavior of the `sort()` method on a list?", ('Sorts the list in ascending order', 'Sorts the list in descending order', 'Randomizes the list', 'Sorts the list numerically then alphabetically')],
    ["What is the output of `bool([])`?", ('True', 'False', 'None', 'Error')],
    ["How can you capture all key-value pairs from a dictionary into separate variables in a single statement?", ('**kwargs', '*args', 'items()', 'unpack()')],
    ["What is the purpose of the `__init__` method in a Python class?", ('Initializes the class attributes', 'Declares the class', 'Compiles the class', 'Documents the class')],
    ["How do you raise a custom exception with a message?", ('raise Exception("Message")', 'error("Message")', 'throw Exception("Message")', 'exception("Message")')],
    ["What does the `@staticmethod` decorator do?", ('Converts a method into a class method', 'Converts a method into a static method not requiring instance reference', 'Makes a method return static values only', 'None of the above')],
    ["What is the result of `set('aabbcc')`?", ('{a, b, c}', '{\'a\', \'b\', \'c\'}', '{\'aa\', \'bb\', \'cc\'}', 'Error')],
    ["Which function is used to combine two lists into a dictionary?", ('zip()', 'map()', 'combine()', 'dict()')]
]
    for key, value in enumerate(list):
        #print(key,value)
        data[key]=value
    #prompt(data)
    return data
