# Programing Best Practices: Writing Better Code
Writing code can be as simple as importing the required libraries, declaring our variables, functions and classes as per required, including some docstrings here and there, some additional comments, executing, and we're done. While we're at it, lets skip the function & class part and just drop everything as is. Even better, lets also save some lines by stripping our file from all comments.

The result? A piece of code with absolutely no indication of what it does or how it does it, with the impossibility to modularize & scale in any useful way. In short, a beautiful, useless creation made by us, just for us.

In this section, we will review some simple methods which will immediately bring clarity & credibility to our code, being thus able to share it with other people, understand it ourselves when re-reading some weeks or months after, and not perishing in the process.

We will use Python as an example, but most of the steps will apply to any programming language.  

We'll be using Python scripts which can be found in the [Blog Article Repo](https://github.com/pabloaguirrenck/blog/tree/master/big-data/6-big-data-file-formats-compared).

---

## Table of Contents
- Legibility
	- Authoring
	- Comments
		- Simple commenting
		- Over-commenting
		- Breaking comments in a newline
		- Section definition
	- Docstrings
	- Indentation
	- Line breaks & parenthesis
		- Line breaks
		- Parenthesis
	- Appropriate variable naming
	- Spacing
- Modularization & scalability
	- Modularization
	- Scalability
- Performance
	- Aaa
	- Aaa
- Testing & debugging
	- Exception handling
	- Print statements
- Dependency specifications

---

## Legibility
If we were to chose one step to try and write better code, this would be the one. We can write code without any functions whatsoever, or even deliver underperforming software, but if the people reading our code don't even know what its for, what it's supposed to do, where to look and what to change in order to optimize its performance, they're better off writing the code by themselves.

Legibility is not just about filling our script with comments of every step we do (*maybe when we're trying to explicitly teach something, it might be a good idea*). Legibility is about making our code understandable to ourselves, and to anyone with little to no context of what we're trying to achieve.

The good thing is, if we are to improve legibility, we have some very simple and extremely useful mechanisms additional to commenting that we can use.

### 1. Authoring
This is the first step we will cover, and a crucial one when sharing our material. It provides the creator with a way to assume authorship of the creation. It also provides readers and consumers with a way to contact the creator in case of any question. We can get our hands on a beautifully written and extremely useful program, but who the heck does this code belong to? Was it written by ChatGPT?

It is also important to include authoring and contact information as metadata in the code we write, specially in a working environment, so that people will know who to blame when things go wrong (*just kidding, sort of*). Jokes aside, this is true, and happens more often than not. We want to be able to provide a way for other collaborators to reach out if our code doesn't work as expected. After all, we're assuming responsability when submitting code to other people.

Authoring, as with several of the commenting techniques, comes down to personal preference, though we should include at least the date of creation, our name, and some type of contact information.

Typically, we enclose this metadata at the top of our script in a docstring using single `'` or double `"` triple quotes: 

##### **Code**
```Python
'''
Created on: Wed Jan 18 20:48:18 2023
@author: Lucifer Morningstar
contact: lucifermorningstar@gmail.com
'''
```

We can of course complement this information by specifying additional fields, such as last modification date, Python version used, and more.

The nice thing about authoring, is that several IDEs have the option to customize & introduce these lines by default when creating a new blank document.

### 2. Comments
#### 2.1 Simple commenting
Commenting is always encouraged when working with code. It lets us re-read and understand the procedures we used some time ago, and also give context to other people reading our material.

We can comment a single line by using the hash symbol `#`:

##### **Code**
```Python
# This is a comment.
```

#### 2.2 Over-commenting
The caveat of commenting is that it is often abused to the point of replicating line by line what the code is doing. Again, this is fine if we're teaching someone, but to the experienced programmer, this will not be necessary, and will in turn introduce too many reading breaks which are not required. We can think of over-commenting as abusing punctuation; it breaks the flow, and impedes clear reading.

Fortunately, there are two simple rules to avoid over-commenting:
- Use comments as a way to explain the why, not the how.
- Only write a comment when it's absolutely necessary.

Both statements are important because some times, the code is self-explanatory. This would make writing the following comment unnecessary:

##### **Code**
```Python
# Declare a while loop that prints 'Hello', and stops after 8 iterations
i = 0
while i < 8:
    print('Hello')
    i += 1
```

#### 2.3 Breaking comments in a newline
Comments are meant to be read as clearly, easily and fast as possible, but the truth is, sometimes they can get extense.

In some IDEs, this can cause the comment to overflow, looking unprofessional:

##### **Code**
```Python
# Declare a list variable that will serve to store dictionaries. This is crucial since we won't be able to retrieve the objects otherwise.
mylist = []
```

Breaking the comment in two or more lines improves readability:

##### **Code**
```Python
# Declare a list variable that will serve to store dictionaries.
# This is crucial since we won't be able to retrieve the objects otherwise.
mylist = []
```

We can also use a docstring if the comment is too long. We just have to make sure to keep format consistency across our annotations:

##### **Code**
```Python
'''
Declare a list variable that will serve to store dictionaries.
This is crucial since we won't be able to retrieve the objects otherwise.
'''
mylist = []
```

#### 2.4 Section definition
When working with long scripts, we can also use the hash symbol `#` to define section separators and divide our code blocks by including some kind of delimiter along with the comment.

The format used is purely based on personal preference, but should generally be a collection of uniform characters typically used to delimit:

##### Code
```Python
# -------------------------------
# -------------------------------
# This denotes a section start point
# -------------------------------
# -------------------------------

# -------------------------------
# -------------------------------
# This denotes a section end point
# -------------------------------
# -------------------------------

# -------------------------------
# This denotes a subsection start point
# -------------------------------

# -------------------------------
# This denotes a subsection end point
# -------------------------------

# This denotes a subtitle
# -------------------------------
```

We can also use a different, more emphatic character combination to denote a centered title:

##### Code
```Python
# +-----------------------------------------+
# |      This denotes a centered title      |
# +-----------------------------------------+
```

The important thing to remember, is not to overcrowd our code. Otherwise, it could become illegible.

Also, setting a section spacing standard can help.

### 3. Docstrings
We already used docstrings as a way to insert simple comments, but the main reason they were created were to be used inside functions as a way to explain what the object does, and its expected inputs & outputs.

This is especially relevant when writing extense code. Also, it provides a way for other people, or even ourselves, to use the function as a modular object and know exactly what to expect from a function call.

We can include a docstring inside a function by using the same format as before:

##### **Code**
```Python
def addAges(age1, age2, age3):
    '''
    Parameters
    ----------
    age1 : int
        Age 1, from 1 to 10.
    age2 : int
        Age 2, from 11 to 20.
    age3 : int
        Age 3, from 21 to 30.

    Returns
    -------
    sumOfAges : int
        Sum of ages 1, 2 and 3.
    '''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges
```

One crucial detail to remember, is that docstrings are indentation-sensitive, meaning an impropperly indented docstring will throw an `IndentationError` upon execution:

##### **Code**
```Python
def addAges(age1, age2, age3):
'''
Parameters
----------
age1 : int
    Age 1, from 1 to 10.
age2 : int
    Age 2, from 11 to 20.
age3 : int
    Age 3, from 21 to 30.

Returns
-------
sumOfAges : int
    Sum of ages 1, 2 and 3.
'''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges
```

##### **Output**
```
IndentationError: expected an indented block after function definition on line 1
```

### 4. Indentation
Indentation is used in all programming languages, and has two main purposes depending on the language used:
- As a way to improve code readability
- As part of the actual syntaxis

Python uses indentation as part of its syntaxis. This is why the `IndentationError` above was raised.

Even though Python code is generally not executed without the propper indentation, we still can indent incorrectly in some cases without an error being raised. This is common when using argument continuation in newlines:

##### **Code**
```Python
mylist1 = [1, 2, 3, 4,
     5, 6, 7, 8]

mylist2 = [1, 2, 3, 4,
		    5, 6, 7, 8]
```

The above code runs fine, but doesn't look fine. In fact, it looks as if something were off. The reason is that, even though Python does not raise an `IndentationError`, the indentation is incorrect in both cases.

We can propperly indent our lists by aligning parenthesis, or in this case, brackets:

##### **Code**
```Python
mylist1 = [1, 2, 3, 4,
           5, 6, 7, 8]

mylist2 = [1, 2, 3, 4, 
           5, 6, 7, 8]
```

### 5. Line breaks, parenthesis, brackets & curly brackets
#### 5.1 Line breaks
Line breaks are useful but not that common, and often reduce the code legibility. They can also lead to syntax errors if not used propperly.

We can use them for specific cases, *e.g. whenever we are presented with a variable containing multiple characters*.

A line break can be achieved by adding a backslash `\` to the section we want to break:

##### **Code**
```Python
myvar = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + \
        9 + 10 + 11 + 12
```

#### 5.2 Parenthesis
A better alternative to backslashes would be to enclose our variable arguments in a parenthesis. This also allows us to continue writing on a newline:

##### **Code**
```Python
myvar = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 +
        9 + 10 + 11 + 12)
```

### 5.3 Brackets & curly brackets
As we saw before, we can enclose arguments in a parenthesis to be able to continue writing on a newline.

We can also continue arguments on a newline if we're dealing with other objects such as lists, arrays or dictionaries.

This is extremely useful, when for example, we have to specify a high-dimension array with multiple nested brackets.

If we were to attempt a one-liner, the code would become challenging to read:

##### **Code**
```Python
import numpy as np

# Declare a 3-dimensional numpy array
myarr = np.array([[[10,20,30,40], [50,60,70,80]]])
```

We could use line continuation to break each specific dimension into a newline:

##### **Code**
```Python
import numpy as np

myarr = np.array([
                    [
                        [10,20,30,40],
                        [50,60,70,80]
                    ]
                ])
```

Another example would be a JSON-like formatted object:

##### Code
```Python
schema = {'type': 'record','name': 'dataset','namespace': 'dataset','doc': 'This schema consists of 1 int type and 7 string types','fields': [{'name': 'Name', 'type': 'string'},{'name': 'Age', 'type': 'int'},{'name': 'Occupation', 'type': 'string'},{'name': 'Country', 'type': 'string'},{'name': 'State', 'type': 'string'},{'name': 'City', 'type': 'string'}]}
```

This is frankly unpleasant, and overflows the document width by about 3 times.

We can do better by using line continuation:

##### **Code**
```Python
schema = {
    'type': 'record',
    'name': 'dataset',
    'namespace': 'dataset',
    'doc': 'This schema consists of 1 int type and 7 string types',
    'fields': [
        {'name': 'Name', 'type': 'string'},
        {'name': 'Age', 'type': 'int'},
        {'name': 'Occupation', 'type': 'string'},
        {'name': 'Country', 'type': 'string'},
        {'name': 'State', 'type': 'string'},
        {'name': 'City', 'type': 'string'}
    ]
}
```

### 6. Appropriate variable naming
When we start writing lengthier programs, its inevitable to start losing count of the variables we declare. Or maybe we have really good memorization skills and don't really care what names we use, but then Juan from Engineering, the poor guy responsible for deploying our code, sends us an email begging to send a variable definition document, because he cannot understand a thing:

##### **Code**
```Python
msw = (3, 1, 4.3, 6.5, 2)
kEla = [4, 3, 5, 6, 7, 3]
thePanty = [1, 2, 3, 4, 5]
theOtherpanty = [4, 3, 6, 7, 8, 2]
mthBreather = [8, 7, 1, 4, 5, 6]
xyz = 3.1416

for w in range(len(mthBreather)):
    theOtherpanty.append(w)
    for d in thePanty:
        print(xyz)
    copyofthePanty = thePanty.copy()
```

Plain and utter awfullness, right?

We can do much better, and give Juan a break:

##### **Code**
```Python
myTuple = (3, 1, 4.3, 6.5, 2)
myList = [4, 3, 5, 6, 7, 3]
myList_2 = [1, 2, 3, 4, 5]
myList_3 = [4, 3, 6, 7, 8, 2]
myList_4 = [8, 7, 1, 4, 5, 6]
pi = 3.1416

for constants in range(len(myList_4)):
    myList_3.append(constants)
    
    for items in myList_2:
        print(pi)
    
    myList_2_copy = myList_2.copy()
```

### 7. Spacing
Lastly, spacing propperly will always improve our code. Spacing creates a sense of separation and independence, and instantly provides a better reading experience.

Python does not require for us to insert spaces between characters, but if leave our code without spacing, or even worse, with inconsistent spacing, it will be much harder to read:

##### **Code**
```Python
myList = [1,2,3,4,5,6,  7, 8,9,10, 11]
```

The line above generates our list object successfully and without spaces in between of course, but the reading is a challenge in its own.

This is why its always good practice to be consistent about the spaces we use, how we use them, and why we use them.

We can implement single spaces between our list arguments:

##### **Code**
```Python
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

We can also implement newlines to make distinctions between different segments or operations:

##### **Code**
```Python
def myFun(x, y, z):
    x =+ 1
    y *= 1
    z -+ 1
    t = 3
    
    for i in range(x):
        t -= x

    return t
```

---

## Modularization & scalability

### 1. Modularization
Code is meant to be modular. Sure, we can write a single script to bulk-rename *n* number of files. That script would only be used for that purpose, and would not require any dependence or be required by any other program.

But the reality is, most of the code that is written is meant to be used in conjunction with other code; it's meant to work as part of a bigger system. This is called modularization, and is an extremely powerful concept in programming.

In Python, modularization can be achieved by using different levels of abstraction such as functions, classes and other scripts.

Let's take an example where we want to calculate the sum of all numbers inside a list object:

##### **Code**
```Python
nums = [1, 2, 3, 4, 5]

total = 0

for x in nums:
    total += x
    
print(f'Sum of values is: {total}')
```

##### **Output**
```
Sum of values is: 15
```

This code performs as expected:
- It first defines our list of integer numbers.
- It then defines our initial counter `total`, and sets it to 0.
- It then iterates over all elements of our `nums` list, adding each element to our counter `total`.
- Finally, it prints some string along with the sum of all numbers.

But it presents the following disadvantages:
- The code is only usable inside the script itself, meaning we cannot call it from another script.
- We have to re-define our `nums` object each time we want to perform a different calculation.
- We cannot assign the `total` calculation to another variable unless we explicitly copy the `total` variable. 
- There's no way for the user to input a custom list of numbers if the script is run from a shell.

This code can be modularized by refactoring it to a function:

##### **Code**
```Python
def getSum(nums):
    total = 0

    for x in nums:
        total += x
        
    print(f'Sum of values is: {total}')
    
    return total
```

We can then call our function and assign the returned variable `total` to *n* number of variables:

##### **Code**
```Python
nums_1 = [1, 2, 3, 4, 5]
nums_2 = [6, 7, 8, 9, 10]
nums_3 = [11, 12, 13, 14, 15]
nums_4 = [16, 17, 18, 19, 20] 

total_1 = getSum(nums_1)
total_2 = getSum(nums_2)
total_3 = getSum(nums_3)
total_4 = getSum(nums_4)

print(total_1, total_2, total_3, total_4)
```

##### **Output**
```
Sum of values is: 15
Sum of values is: 40
Sum of values is: 65
Sum of values is: 90
15 40 65 90
```

Finally, we can also call our function from an entirely different script, by simply importing `getSums()` as a custom method. For this, we need to create a new Python script `my_fun.py` in the same directory as our current script, and include our `getSum` function:

##### **Code**
```Python
from my_fun import getSum

nums_5 = [-3, -2, -1, 0, 1, 2, 3] 
total_5 = getSum(nums_5)
```

##### **Output**
```
Sum of values is: 0
```

We can even rename our `getSum` function upon importing:

##### **Code**
```Python
from my_fun import getSum as sumVals

nums_6 = [-3, -2, -1, 0, 1, 2, 3] 
total_5 = sumVals(nums_6)
```

##### **Output**
```
Sum of values is: 0
```

This is just scratching the surface of what abstraction can do. A more detailed study of other objects is out of the scope of this article.

### 2. Scalability
A scalable code does not require frequent modifications to maintain performance when handling varying workloads. This can be achieved from several viewpoints, and strongly depends on what the code is intended to perform.

When handling large data sets for example, it is important to think of the following:
- Properly define the file format(s) to be used.
- Properly define a schema to be used, and keep consistency.
- Properly define the objects that will be used to store the information.
- Properly define the aggregation levels that will be taking place.
- Manage memory according to the expected data set size.
	- A simple `del` after using an object will clear it from memory.

Further information on Big Data file formats can be found on my 3-article series [6 Big Data File Formats Compared](https://pabloagn.com/blog/6-big-data-file-formats-compared-pt-1/).

This is just one example, but there are multiple measures that can be taken in order to secure scalability and execution integrity.

---

## Performance
Although this area requires a little bit of experience and additional knowledge in algorithmic design & computational complexity, we can manage to at least perform the basics in order to ensure our code does what its supposed to, in the least ammount of time possible, consuming the least ammount of resources.

Of course, there are countless variables we can optimize such as using another programming language for starters. Nontheless, we can focus on the most basic mechanisms we can implement.

### 1. 

### 2. 

### 3. 

---

## Testing & debugging

### 1. Exception handling
If we go back to the [Docstrings](#2-docstrings) section and take a closer look at the function we defined, there is nothing in the code impeding the user from inputting a wrong parameter. Sure, we defined a docstring telling the user what to do, but we did nothing to ensure how the function would behave if the user gave an integer number out of the specification bounds as input, or even worse, the wrong type.

In the best-case scenario, the user reads the docstring and understands what to do. In the worst-case scenario, the user doesn't even know what a data type is, and inputs something like this:

##### **Code**
```Python
def addAges(age1, age2, age3):
    '''
    Parameters
    ----------
    age1 : int
        Age 1, from 1 to 10.
    age2 : int
        Age 2, from 11 to 20.
    age3 : int
        Age 3, from 21 to 30.

    Returns
    -------
    sumOfAges : int
        Sum of ages 1, 2 and 3.
    '''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges

addAges('1', '1', '0')
```

What would happen? Well, the first thing to bear in mind is that if we input garbage, we get garbage. That is, if we don't have a handler for these types of slips (*which happens often, and can easily break a precarious program*).

Fortunately, with this particular input, the program would not break. Instead, it would simply concatenate the three ages (*not sure what's worse*):

##### **Output**
```
'110'
```

We can see that not only is the intended operation wrong, but the returned object is a string.

The user could slip in a more subtle way and input something like this:

##### **Code**
```Python
addAges('1', 2, 3)
```

##### **Output**
```
TypeError: can only concatenate str (not "int") to str
```

And there we have it folks, the user broke our program in 2 tries. He even got upset because "*some unintelligible giberish appeared on his screen, even though he did everything right*". Good luck explaining that to our boss.

The thing is, we could've avoided this by using exception handlers.

These handy methods allow us to redirect errors such as the one we encountered, and do something productive with them.

...

### 2. Print statements
Print statements allow us to make less typing and logical mistakes, by outputting useful messages about specific sections. We can use print statements either to debug, or to output mesages to the anxious user.

Even though we sometimes feel like printing every step just to ensure we're not losing it, we should moderate ourselves and not go too bananas, otherwise, we might turn an anxious user into an angry user.

...

---

## Dependency handling
Last but not least, dependencies play a huge roll in avoiding execution errors and ensuring maintainability. There are multiple mechanisms we can put into place in order to ensure that our code will run smoothly across environments:

- Specify the dependencies required in a readme file, and pack it along with our code. Also, add it to the project repository if we're using version control.
- Create a yaml file to specify and handle the required environment.
- Make sure the packages we're using are actively maintained.
	- This is not always fully possible, but we can try to include the least ammount of unmaintained packages in our code to ensure the least ammount of conflicts.
- If we created a proprietary package that we're using for some project, we need to keep the file handy and if possible, upload to a version control software such as [GitHub](https://pabloagn.com/technologies/github/).
- Make sure we're using the correct methods, and that they'll not be deprecated soon.
	- This is an easy one. Most methods output a warning if they're about to be deprecated in future versions. We need to be proactive with these warnings and substitute the old methods in favor of updated ones before it's too late and our angry user turns into an excstatic user.

...

---

## Conclusions
We've reviewed multiple yet simple mechanisms we can employ to make our code cleaner, more elegant, modular, usable and scalable. These measures can not only help us be better programmers, but better collaborators.



---

## References
- [Geeks for Geeks, Working with csv files in Python](https://www.geeksforgeeks.org/working-csv-files-python/)
- [Stack Exchange, Why do we keep using CSV?](https://softwareengineering.stackexchange.com/questions/47838/why-do-we-keep-using-csv)
