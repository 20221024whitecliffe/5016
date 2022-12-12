# 5016 ReadMe.md
# This repository is for practicing Python coding

Structure of the repository follows sequences of course module. 
Each module composites sample codes in course materials, activity practiced answers with sample answers, 
and extended code blocks where research has been done.

Comments have been added to describe questions, researches, and trials and fails of improved/unfinished/unsolved code blocks for further investigations.

An example is shown in MyFavoriteQuote.py. By doing research and practicing on formating options, methods are 
implemented to achieve different results.

# format is a question, 
# research has been done for different ways to achieve displaying in a block
# method 1: add "\n" after each sentence to change lines
# method 2: use """""" to display however need to be
print('我要你知道，'
      '在这个世界上总有一个人是等着你的，'
      '不管在什么时候，不管在什么地方，'
      '反正你知道，总有这么个人')
""" output = 
我要你知道，在这个世界上总有一个人是等着你的，不管在什么时候，不管在什么地方，反正你知道，总有这么个人
"""

print('我要你知道，\n'
      '在这个世界上总有一个人是等着你的，\n'
      '不管在什么时候，不管在什么地方，\n'
      '反正你知道，总有这么个人\n')
""" output =
我要你知道，
在这个世界上总有一个人是等着你的，
不管在什么时候，不管在什么地方，
反正你知道，总有这么个人
"""

print("""
        我要你知道，
        在这个世界上总有一个人是等着你的，
        不管在什么时候，不管在什么地方，
        反正你知道，总有这么个人
      """)
""" output = 
        我要你知道，
        在这个世界上总有一个人是等着你的，
        不管在什么时候，不管在什么地方，
        反正你知道，总有这么个人
"""

In folder extended, a couple of extended thoughts about some functions during study,
and it was looked into with results. the resources are marked in the codes.

There were found mistakes in sample answers of activities. Best attempts have been made 
to correct them and get them working. However, due to personal capabilities, some faults
were not corrected. They were commented with error messages.

Each of the code has been run and the result or test assertions were added following each 
piece of code.
