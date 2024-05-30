# QuizGenerator
Generates and scores any given objective type quiz from the vscode terminal window given an answer key and dict containing Question+Answer pairs(find a sample below)

To get the list of question, heres the ChatGPT prompt that i'm using "Can you please give me an exercise(10 python coding related obective type questions (with 4 options each), intermediate level with answker key)" along with a sample of the format im expecting the GPT output to be e.g.

sample_list = [
    ["What does the `*args` in a function definition signify?", ('A specific number of arguments', 'A list of arguments', 'A tuple of variable number of arguments', 'A dictionary of named arguments')],
    ["Which method checks if all elements in a list are true in a boolean context?", ('all()', 'any()', 'sum()', 'collect()')],
]

correct_answers_key = [1, 3, 2, 2, 1, 2, 1, 1, 3, 2]
