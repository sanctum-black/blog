<article class="first">
  <div class="title">
    <h1>An Introduction to RegEx</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Python,%20Bash&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/an-introduction-to-regex/)

Regular Expressions, also known as RegEx, is a pattern-matching tool used to find patterns in strings. We can think of RegEx as the powerful version of search-and-replace or [wildcards](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm), where we can look for specific substrings, and replace accordingly.

RegEx can be used to search for patterns and/or replace patterns with other strings, numbers or characters. It's such a powerful tool, that many programming languages support their own RegEx flavor.  

In this Blog Article, we'll start by discussing what RegEx is, providing some historical context, explaining why it's useful, providing a comprehensive list of the most popular flavors available, and going through the basic syntax of RegEx expressions.

We'll then review RegEx syntactic elements such as literal characters, metacharacters & shorthand notations, character sets, ranges, negations, alternations, and modes or flags. We'll step things up a little by exploring anchors & boundaries, quantifiers & repetitions, greedy & lazy operation modes, capturing & non-capturing groups, named groups, backreferences, and positive & negative lookarounds., all while providing detailed examples throughout the entire segment, and a mini-project involving a client's database cleaning using more advanced regular expressions.

We'll close this segment by providing some next steps for those interested in practicing RegEx composing.

We'll be using Python scripts & RegEx expressions which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/an-introduction-to-regex).

---

# Table of Contents
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# What is RegEx?
RegEx is an extremely powerful tool for searching simple to very complex patterns. It's mostly used in text validation and searching throughout large bodies of text.

It's so powerful, that there are specific flavors (*implementations*) for multiple programming languages, and is widely adopted among software developers, data analysis, Linux sysadmins, and much more.

## 1. An introduction
RegEx can do two main things:
- Look through a body of text.
- Match and replace one or more instances using RegEx patterns.

A body of text includes anything that has literal characters, digits, or special characters inside. For example, RegEx can be used to search the following, among many others:
- HTML code
- IP Addresses
- Passwords
- Physical Addresses
- Dates
- Structured / unstructured datasets
- User inputs

This is just a small subset of what RegEx can search, because it can virtually search any body of text we can think of.

Depending on our use case, we can use RegEx in multiple platforms:
- A shell prompt such as [PowerShell](https://pabloagn.com/technologies/powershell-7/) or Bash.
	- Actually, Bash has multiple commands that support POSIX RegEx out of the box.
- Bash scripts.
- The find-and-replace feature in VS Code.
- A JavaScript script.
- A [Python](https://pabloagn.com/technologies/python/) script.
- A [Rust](https://pabloagn.com/blog/rust-for-beginners/) application.
- Simple validation using debuggers such as [RegEx101](https://regex101.com/).
- The RegEx feature in [Bulk Rename Utility](https://www.bulkrenameutility.co.uk/).

This is just a reduced list, but the number of platforms supporting RegEx is extense.

## 2. Visualizing RegEx
Let us illustrate what RegEx is by using a visualizer. A RegEx visualizer is a tool that lets us visualize our RegEx pattern in a railroad diagram. Great visualizers include:
- [regex-vis](https://regex-vis.com)
- [Debuggex](https://www.debuggex.com/)
- [Regulex](https://jex.im/regulex/#!flags=&re=)

We can write a simple RegEx expression that searches for email domains:

##### **Code**
```RegEx
(?<=@)\w+(?=\.\w{2,3})
```

A railroad diagram would look like such:

B019A036_regex_vis_01

We can see that there's a train-like diagram, where each RegEx step is explained in detail, including:
- Which literal character is being searched for.
- How many times (*repetitions*) are we searching for the given character.

We'll discuss what each of those characters are in more detail, but for now, we must understand that RegEx operates character-wise, and we can add repetitions to repeat the pattern to more than one character, or sets to include a range of possible characters.

---

# Historical context
Regular expressions, or RegEx, have their roots in theoretical computer science and formal language theory, dating back to the early 20th century. The concept of formal languages and their grammars was introduced by mathematician [Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky) in the 1950s, and this laid the foundation for the development of RegEx.

In the 1960s and 70s, RegEx was used extensively in the development of the [Unix](https://en.wikipedia.org/wiki/Unix) operating system, which is still widely used today. The `grep` command, which is used to search for patterns in text files, was one of the earliest implementations of regex and remains an important tool for developers and system administrators.

As computing power and storage capacity increased, RegEx became more widely used in a variety of applications, including data validation, text processing, web scraping, and network security. Today, RegEx is a fundamental tool for anyone working with text data or programming, and is supported by virtually all programming languages and many software tools.

---

# Why is it useful?
As we mentioned, there are thousands of applications where RegEx can be useful. However, there are some main use cases usually employed by programmers.

## 1. Searching & replacing complex patterns
If we've ever tried searching for a substring in any editor such as VS Code, Spyder, R Studio, or PyCharm, we may remember that the search patterns we were able to include were very limited.

Let us imagine we have a set of 4 email addresses, and would like to find and replace all domains using a conventional search-replace method:

```
johndoe@email.com
james_johnson@email.com
olivia_lee@email.com
markwilson@email.com
```

Easy, right? We would search for `email`, and replace for the required domain. But what would happen if the target emails have different domains?

```
johndoe@gmail.com
james_johnson@yahoo.com
olivia_lee@protonmail.com
markwilson@gmail.com
```

Well, this becomes more complicated, because we have no exact matches to look for. In short, we would have to look for each domain separately, and replace for the required new domain.

This is not a deal-breaker, since we only have 4 addresses, but what happens when we have a database of 1,000,000 records? The manual approach becomes impossible.

This is where RegEx comes into play. We can use regular expressions to search for extremely complex patterns, and replace with a new value accordingly.

The great thing about RegEx, is that it's extremely simple in nature, but can become as complex as we would like it to be, meaning we have the flexibility to build complex expressions with simple components, and keep building on top of that, until we get what we were looking for.

## 2. Validating user inputs
We've probably heard of SQL injections. They are a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed.

When we enter a website that asks for username and password, we normally type our username and our password, without thinking what goes behind curtains; in reality, the moment we enter our password and press enter, our data is most probably validated in an SQL database, where the algorithm searches for our entry, and returns `TRUE` if our username and password match. If they do not match, it returns `FALSE` and we get an "*incorrect password*" message.

If someone were to include an SQL query in the input (*SQL injection*) instead of the expected username and password, a lot of bad things such as deleting records, changing passwords, and forcing an entry could happen.

This can be easily solved using input validation techniques with RegEx: The username and password fields are expecting a specific combination of characters, so that an error would be returned if we were to try something like this:

##### **Code**
```SQL
SELECT * FROM Users WHERE UserId = 105 OR 1=1;
```

Or even simpler:

##### **Code**
```SQL
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

These are actually two extremely simplified versions of an SQL injection that can be avoided by using RegEx as an input validation mechanism.

---

# Why is it hard?
RegEx has certain fame associated with it; people often times see RegEx as a bunch of characters without any sense whatsoever, and that's because RegEx is not written as a conventional programming language (*there's no explicit instruction given using conventional programming language-style syntaxis*); instead, it uses a set of basic characters, metacharacters and modifiers to build complex search patterns that, at first glance, look unintelligible.

This expression, for example, validates IPv4 addresses:

##### **Code**
```RegEx
/
^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$
/
gm
```

Apart from the numeric characters, there's nothing that would remotely make sense at first glance; it looks like a bunch of random characters resembling what we get when we open a binary file in a text editor:

##### **Code**
```
8@4@;rE9=*A|=*Ae~mEtVtQtKuQ@@t
```

The thing is that, with RegEx, each character has a very specific purpose that we will soon learn.

---

# RegEx Flavors
As mentioned, there are a number of RegEx flavors depending on the language and/or their version.

Below are the most common flavors currently available:
- **POSIX Basic and Extended Regular Expressions:** POSIX (*Portable Operating System Interface*) defines two flavors of regular expressions: Basic Regular Expressions (BRE) and Extended Regular Expressions (*ERE*). They are used in various UNIX-based systems and tools such as grep, sed, and awk.
- **Perl-Compatible Regular Expressions (PCRE):** PCRE is a popular RegEx library used in many programming languages such as PHP, Python, and Ruby. It provides powerful features such as lookaheads, backreferences, and non-capturing groups.
- **JavaScript Regular Expressions:** JavaScript supports RegEx natively, and its flavor is similar to PCRE, but with some differences, such as the lack of support for lookbehinds.
- **.NET Regular Expressions:** The .NET framework provides a RegEx class that supports a flavor similar to PCRE, with some additional features such as named groups and balancing groups.
- **Python Regular Expressions:** Python also has a native RegEx module that supports a flavor similar to PCRE, but with some differences, such as the use of a raw string for RegEx patterns and the lack of support for atomic groups.
- **Java Regular Expressions:** Java provides a RegEx library that supports a flavor similar to .NET, with some differences, such as the lack of support for lookbehinds in the default mode.

Additionally, more flavors for emerging languages have been recently created:
- Golang
- Rust

---

# Preparing our environment
For this segment, we'll be using two main tools:
1. **[RegEx101](https://regex101.com/):** A powerful regular expression tester with syntax highlighting, explanation, cheat sheet for PHP/PCRE, Python, GO, JavaScript, Java, C#/.NET, Rust.
2. Python RegEx in VS Code: 

---

# Basic syntax & rules
RegEx syntax is comprised of a base of characters, metacharacters and modifiers that we can use to compose complex expressions.

We must take into account that each RegEx flavor has slight variations, but the general syntax is very similar throughout.

A basic RegEx syntax is defined as follows:

##### **Code**
```RegEx
/cat/gi
```

Where:
- Forward slashes `/` delimit the regular expression.
- Inside the slashes, we include our expression, which in this case is the literal word `cat`.
- Outside of the slashes, we include the mode(s) or flag(s), which can change the way RegEx operates on our target. In this example, the `g` flag stands for "global", while the `i` flag stands for "case-insensitive".

Throughout this segment, we'll write regular expressions without the forward slashes to make it more efficient. However, when we're using Python, we'll need to change to forward slashes and quotations: `'/regex_pattern/'`.

We will also denote the outputs enclosed by double asterisk `**` signs: `**regex_output**`.

It's important to note that regular expressions are case-sensitive unless specified otherwise. This means that if we look for `K`, it will return `K` and not `k`. Also, they operate on a per-character basis, and by default, only the first character found is returned, so if we define the following:

##### **Code**
```RegEx
/cat/
```

Only the first `cat` appearance will be returned. If we would like to return all the matches, we need the include the `g` flag.

## 1. Modes / flags
Modes & flags refer to the optional operation mode we can pas to RegEx. We've already seen two of them. However, there are more we can use:
- **`i` (*case-insensitive*):** This flag indicates that the pattern should be matched in a case-insensitive manner. For example, `/cat/i` would match '`cat`', '`Cat`', or '`CAT`'.  
- **`g` (*global*):** This flag indicates that the pattern should be matched multiple times within the text string, rather than just the first occurrence.  
- **`m` (*multiline*):** This flag changes the behavior of anchors such as `^` and `$` to match the beginning and end of individual lines within the text string, rather than just the beginning and end of the whole string.  
- **`s` (*single-line*):** This flag changes the behavior of the dot (.) special character to match any character, including newlines.  
- **`x` (*verbose*):** This flag allows for the use of whitespace and comments within the regex pattern, making it easier to read and understand.

We can use combinations of flags by using the following syntax:

##### **Code**
```RegEx
/cat/gim
```

## 2. Literal characters
A literal character is a single string character that can be used to match in a larger string. It matches the first occurrence of that character in the string. For example, `a` would be a literal character.

As we mentioned, literal character matching is case-sensitive.

We can also use a collection of literal characters to match full words:

##### **Code**
```RegEx
paul

Where is **paul**
```

There are special characters, such as `.` and `?`, that cannot be matched using literal characters alone.

## 3. Metacharacters list
There are 11 main metacharacters that are special in RegEx. Each metacharacter (*without escape*) has a specific function:
1. `.` (*dot*): Matches any single character except for newline characters.
2. `*` (*asterisk*): Matches zero or more occurrences of the preceding character or group.
3. `+` (*plus*): Matches one or more occurrences of the preceding character or group.
4. `?` (*question mark*): Matches zero or one occurrence of the preceding character or group.
5. `^` (*caret*): Matches the beginning of a line.
6. `$` (*dollar sign*): Matches the end of a line.
7. `[ ]` (*square brackets*): Defines a character class that matches any single character within the brackets.
8. `|` (*pipe*): Specifies alternative patterns to be matched.
9. `()` (*parentheses*): Groups characters or patterns together, and can be used with quantifiers.
10. `{ }` (*curly braces*): Specifies the number of occurrences of the preceding character or group to match.
11. `\` (*backslash*): Escapes special characters, allowing them to be matched as plain text.

We also have other special metacharacters:
- Digits, words, and whitespaces:
1. `\d` - Matches any digit character.
2. `\D` - Matches any character that is not a digit character.
3. `\w` - Matches any word character (_alphanumeric & underscore_). Only matches low-ascii characters (_no accented or non-roman characters_).
4. `\W` - Matches any character that is not a word character (_alphanumeric & underscore_).
5. `\s` - Matches any whitespace character (_spaces, tabs, line breaks_).
6. `\S` - Matches any character that is not a whitespace character.

- Non-printable characters
8. `\t` - Matches a TAB character.
9. `\n` - Line Feed: Matches a newline character
10. `\r` - The carriage return character moves the cursor to the beginning of the line without advancing to the next line.
11. `\f` - Form feed is a page-breaking ASCII control character. It forces the printer to eject the current page and to continue printing at the top of another page.

If we want to search for any of these literally, we have to translate the metacharacter into a literal character (_escape it_). We do this using the backslash `\`.

Escaping metacharacters:

##### **Code**
```RegEx
\+

This **+** is a plus sign
```

We can look at metacharacters as operators in any other programming language; they perform a given operation on the character before it.


# Main metacharacters
The main metacharacters are used as base to compose more complex metacharacters. Let us review each one in more detail.

## 1. The dot metacharacter *(.)*
The dot metacharacter matches any single character, without caring what the character is. The only exceptions are line break characters (_by default, but we can add a flag and it will now match even line breaks_).

The dot metacharacter will also match other metacharacters:

##### **Code**
```RegEx
.is

Th**is** is a sentence with a special character **?is**
```

So what we're doing here, is matching any character before `is`, and `is` itself.



## 5. Quantifiers & repetitions *(+, *)*
We mentioned that RegEx works on a per-character basis. This means that if we want to match a repetition of characters, we need to use an operator that lets us do that.

The asterisk `*` is used to attempt to match the preceding token zero or more times. The plus `+` is used to attempt to match the preceding token once or more times. A token in the RegEx context is a single character or metacharacter we're trying to match.

## 4. Character sets


## 5. Ranges


## 6. Negations


## 7. Alternations


---

# Advanced components

## 1. Anchors & boundaries


## 2. Quantifiers & repetitions


## 3. Greedy & lazy operation modes


## 4. Capturing & non-capturing groups


## 5. Named groups


## 6. Backreferences


## 7. Lookarounds
Lookarounds are special metacharacters that allow us to specify patterns that must match (*or must not match*) before or after the main pattern you are trying to match.

There are 4 main lookaround implementations in RegEx:
- Positives
	- Lookbehind
	- Lookahead
- Negatives
	- Lookbehind
	- Lookahead

The positive variations allow us to match if a pattern is before or after the main pattern, while the negative variations allow us to match if a pattern is not before or after the main pattern.

A lookbehind checks for the pattern before the main pattern (looks behind), while a lookahead does the inverse; looks ahead the main pattern.

We can illustrate this a little bit better with a railroad diagram:

##### **Code**
```RegEx
(?<=before)target(?=after)
```

B019A036_regex_vis_02

As we can see, there is a `before` (*Preceded by*), and an `after` (*Followed by*). This diagram refers specifically to the positive variants, but we can do a similar diagram for the negative versions by using the negation metacharacter:

##### **Code**
```RegEx
(?<!before)target(?!after)
```

B019A036_regex_vis_03

Let us define a simple example that will serve to understand better:

```
Mr. Oleg Smith
Mrs. Danna Pereia
```

Also, we'll use the `gm` flags for all lookaround examples, so we need to make sure we include that in our expressions.

### 7.1 Positive lookbehind
A positive lookbehind is telling RegEx to match `b` if `a` exists; it's looking behind `b`, and returning `b` if the pattern behind (`a`) matches.

The basic syntax is as follows:

##### **Code**
```RegEx
(?<=before)target
```

Where:
- `before` is the pattern behind our target.
- `target` is the pattern that will be returned if `before` exists.

From our previous example:

##### **Code**
```RegEx
(?<=Mr\. )\w+

Mr. **Oleg** Smith
Mrs. Danna Pereia
```

### 7.2 Positive lookahead
A positive lookbehind is telling RegEx to match `a` if `b` exists; it's looking ahead `a`, and returning `a` if the pattern ahead (`b`) matches.

The basic syntax is as follows:

##### **Code**
```RegEx
target(?=after)
```

Where:
- `target` is the pattern that will be returned if `after` exists.
- `after` is the pattern ahead of our target.

From our previous example:

##### **Code**
```RegEx
\w+(?= Smith)

Mr. **Oleg** Smith
Mrs. Danna Pereia
```

### 7.3 Negative lookbehind
A positive lookbehind is telling RegEx to match `b` if `a` does not exist; it's looking behind `b`, and returning `b` if the pattern behind (`a`) does not match.

The basic syntax is as follows:

##### **Code**
```RegEx
(?<!before)target
```

Where:
- `before` is the pattern behind our target.
- `target` is the pattern that will be returned if `before` does not exist.

From our previous example:

##### **Code**
```RegEx
(?<!Danna )\b\w+$

Mr. Oleg **Smith**
Mrs. Danna Pereia
```

This one is slightly more elaborate, so let us break it down:
1. Define a negative lookbehind that checks if `Danna ` does not exist. Note that we add a single space ` ` after the name.
2. Define a word boundary. This tells RegEx that we only want to match `\w+` if it's a word boundary (*meaning the complete surname*)
3. Match any alphanumeric using `\w` repeated until the end of the line using `$`.

### 7.4 Negative lookahead
A positive lookbehind is telling RegEx to match `a` if `b` does not exist; it's looking ahead `a`, and returning `a` if the pattern ahead (`b`) does not match.

The basic syntax is as follows:

##### **Code**
```RegEx
target(?!after)
```

Where:
- `target` is the pattern that will be returned if `after` does not exist.
- `after` is the pattern ahead of our target.

From our previous example:

##### **Code**
```RegEx
^\w+s?\.(?! Oleg)

Mr. Oleg Smith
**Mrs.** Danna Pereia
```

Let us break it down:
1. Define the start of the line with `^`.
2. Match any alphanumeric word `\w+` followed by an optional `s` (*including `Mrs.`*) and a literal dot `\.`.
3. Assert if next word is not `Oleg`, preceded by a space ` `.

---

# RegEx in Python
Up until now we've only seen regular expressions in a debugger, but RegEx is too powerful to just play around with it, and not do actual work in a programming language.

Python supports RegEx via two main libraries:
- The `re` built-in library.
- The `regex` third-party library.

The first one provides a more limited set of functions for working with regular expressions. It can be used to search for patterns in strings, split strings using regular expressions, and replace parts of strings with new text.

The second one has a more powerful set of functions for working with regular expressions. It can do everything that the `re` module can do, but it also provides additional features such as the ability to perform advanced searches using multiple regular expressions at the same time, and the ability to match overlapping patterns.

In this segment we'll work with both. We'll start by installing the `regex` library it if we don't have it already. The `re` library is already included with our Python installation:

##### **Code**
```PowerShell
pip install regex
```

We'll now open our favorite IDE, and import the modules:

##### **Code**
```Python
import re
import regex
```

## 1. Using re
We can start by declaring a simple string:

##### **Code**
```Python
mystring = """
Mr. John Smith
Mrs. Catherina Jones
Mr. Kali Smith
Mrs. Jenneth Smith
"""
```

If we print our string, this is what we get:

##### **Code**
```Python
print(mystring)
```

##### **Output**
```
Mr. John Smith
Mrs. Catherina Jones
Mr. Kali Smith
Mrs. Jenneth Smith
```

Which actually translates to:

##### **Output**
```
\nMr. John Smith\nMrs. Catherina Jones\nMr. Kali Smith\nMrs. Jenneth Smith\n
```

Now we can declare a pattern that will search for any name beginning with `Mrs.`:

##### **Code**
```Python
pattern = re.compile("^Mrs\. \w+ \w+", re.M)
```

A couple of details to remember:
- A RegEx expression can be enclosed in single `''` or double `""` quotes.
- It can contain as many flags as we'd like. In `re`, flags are defined using a `re.F` syntax, where `F` is any supported flag.
- Flags in `re` have different syntaxis as in POSIX RegEx, for example.

Below are all the supported flags in `re`, with their long and short names (*we can use whichever we like*):
- `re.IGNORECASE` (or `re.I`): Perform case-insensitive matching.
- `re.MULTILINE` (or `re.M`): Allow `^` and `$` to match at the beginning and end of each line, in addition to the beginning and end of the entire string.
- `re.DOTALL` (or `re.S`): Allow the `.` metacharacter to match any character, including newlines.
- `re.UNICODE` (or `re.U`): Enable full Unicode matching.
- `re.ASCII` (or `re.A`): Perform ASCII-only matching.
- `re.VERBOSE` (or `re.X`): Enable verbose mode, which allows the use of whitespace and comments within the regex pattern.
- `re.DEBUG`: Display debugging information about the regex pattern and the matching process.

### 1.1 Using finditer
We can try to match our string using the `finditer` method, which will return match objects instead of the simple match:

##### **Code**
```Python
# Match & print
matches = pattern.finditer(mystring)
[x for x in matches]
```

The `pattern.finditer` method returns an iterable `re.Match` object, which is why we need to use a loop to print out all the values.

##### **Output**
```
[<re.Match object; span=(16, 36), match='Mrs. Catherina Jones'>, <re.Match object; span=(52, 70), match='Mrs. Jenneth Smith'>]
```

Where:
- `span`: Start and end position of the occurrence (*zero-based index, upper bound exclusive*)
- `match`: The actual full match, including all characters defined in our `pattern`.

If we want to match a pattern directly without compiling the actual expression first, we can also do so. The only change we'll make is the flag position, which we'll put at the end of the expression:

##### **Code**
```Python
# Match without compiling
matches = re.finditer("^Mrs\. \w+ \w+", mystring, re.M)
[x for x in matches]
```

##### **Output**
```
[<re.Match object; span=(16, 36), match='Mrs. Catherina Jones'>, <re.Match object; span=(52, 70), match='Mrs. Jenneth Smith'>]
```

Sometimes, we'll be including special characters in our RegEx expressions, so it'll be best to use the raw string indicator `r`:

##### **Code**
```Python
pattern = re.compile(r"^Mrs\. \w+ \w+", re.M)
```

This will tell Python to treat everything inside our string (*including everything with a backslash `\` character*) as a literal string.

### 1.2 Using findall
If we do not want the whole `re.Match` object, and instead just want the actual matches, we can use the `findall` method:

##### **Code**
```Python
matches = pattern.findall(mystring)
matches
```

This method will actually return a list of matches, without anything else:

##### **Output**
```
['Mrs. Catherina Jones', 'Mrs. Jenneth Smith']
```

### 1.3 Using match
The `match` method determines if the pattern matches at the beginning of the string. It will only return one `re.Match` object if it exists, and `None` otherwise.

##### **Code**
```Python
mystring = "Hello World"
pattern = re.compile(r"[A-Za-z]+ [A-Za-z]+")
match = pattern.match(mystring)
print(match)
```

##### **Output**
```
<re.Match object; span=(0, 11), match='Hello World'>
```

### 1.4 Using search
If we want to search if a pattern exists at least once in a body of text, we can use the search method, which will return a `re.Match` object for the first match if it exists, and `None` otherwise:

##### **Code**
```Python
mystring = """
Mr. John Smith
Mrs. Catherina Jones
Mr. Kali Smith
Mrs. Jenneth Smith
"""

pattern = re.compile(r"^Mrs\. \w+ \w+", re.M)
match = pattern.search(mystring)
print(match)
```

##### Output
```
<re.Match object; span=(16, 36), match='Mrs. Catherina Jones'>
```

### 1.5 Operating on re.Match objects
We mentioned that some of the methods in `re` return a `re.Match` object instead of the actual match. This is useful when we want to perform additional operations on our matches.

There are two main methods we can use on these objects:
- `group`
- `start`
- `end`
- `span`

Let us illustrate with some examples where we want to operate on phone numbers from some client's database:

##### **Code**
```Python
# Declare a string
mystring = r"""
John Doe, johndoe@email.com, (123) 456-7890, 123 Main St.
Jane Smith, jane.smith@email.com, (234) 567-8901, 456 Elm St.
Robert Johnson, robert.johnson@email.com, (345) 678-9012, 789 Oak Ave.
Sarah Lee, sarah_lee@email.com, (456) 789-0123, 234 Pine St.
Michael Brown, michael.brown@email.com, (567) 890-1234, 567 Maple Dr.
Lisa Davis, lisa.davis@email.com, (678) 901-2345, 890 Cedar Rd.
David Rodriguez, david.rodriguez@email.com, (789) 012-3456, 1234 Willow Way
Emily Kim, emily.kim@email.com, (890) 123-4567, 5678 Birch Blvd.
James Johnson, james_johnson@email.com, (901) 234-5678, 9012 Pine St.
"""

# Declare a regular expression
pattern = re.compile(r"(?<=\.com\, )\(\d{3}\) \d{3}\-\d{4}\b", re.M)

# Match using finditer()
matches = pattern.finditer(mystring)

# Print matches
for match in matches:
    # Print complete phone numbers
    print(f"Full re.Match object: {match}\n")

    # Print match locations in body of text
    #  (returns tuple)
    print(f"Match Location: {match.span()}\n")

    # Print start and end of each match
    print(f"Start Index: {match.start()} ; End Index: {match.end()}\n")

    # Print length
    print(f"Phone Number Length: {match.end() - match.start()}\n")

    # Print the actual phone number
    print(f"Phone Number: {match.group()}\n")
```

##### **Output**
```
Full re.Match object: <re.Match object; span=(30, 44), match='(123) 456-7890'>

Match Location: (30, 44)

Start Index: 30 ; End Index: 44

Phone Number Length: 14

Phone Number: (123) 456-7890

Full re.Match object: <re.Match object; span=(93, 107), match='(234) 567-8901'>

Match Location: (93, 107)

Start Index: 93 ; End Index: 107

Phone Number Length: 14

Phone Number: (234) 567-8901

Full re.Match object: <re.Match object; span=(163, 177), match='(345) 678-9012'>

Match Location: (163, 177)

Start Index: 163 ; End Index: 177

Phone Number Length: 14

Phone Number: (345) 678-9012

Full re.Match object: <re.Match object; span=(224, 238), match='(456) 789-0123'>

Match Location: (224, 238)

Start Index: 224 ; End Index: 238

Phone Number Length: 14

Phone Number: (456) 789-0123

Full re.Match object: <re.Match object; span=(293, 307), match='(567) 890-1234'>

Match Location: (293, 307)

Start Index: 293 ; End Index: 307

Phone Number Length: 14

Phone Number: (567) 890-1234

Full re.Match object: <re.Match object; span=(357, 371), match='(678) 901-2345'>

Match Location: (357, 371)

Start Index: 357 ; End Index: 371

Phone Number Length: 14

Phone Number: (678) 901-2345

Full re.Match object: <re.Match object; span=(431, 445), match='(789) 012-3456'>

Match Location: (431, 445)

Start Index: 431 ; End Index: 445

Phone Number Length: 14

Phone Number: (789) 012-3456

Full re.Match object: <re.Match object; span=(495, 509), match='(890) 123-4567'>

Match Location: (495, 509)

Start Index: 495 ; End Index: 509

Phone Number Length: 14

Phone Number: (890) 123-4567

Full re.Match object: <re.Match object; span=(568, 582), match='(901) 234-5678'>

Match Location: (568, 582)

Start Index: 568 ; End Index: 582

Phone Number Length: 14

Phone Number: (901) 234-5678
```



## 2. Using regex

---

# Unit testing

---

# Worked-out examples

---

# Mini-project: Cleaning a client's database
A house rental company has a brand new relational database they would like to populate with new user's information. They currently have the data in a rudimentary and weird format that cannot be parsed by using formats such as `.tsv` or `.csv` (*their engineer messed up and inputted the data separated by weird inconsistent characters*).

Our job is to extract four key fields in this dataset, which will then be used to systematically harass their clients via invasive phone calls and targeted publicity:
- User's first name.
- User's last name.
- User's phone number (*validated*).
- User's email address.

Since this company is dubious, they also recollected their customers' IP Addresses in IPv4 format. However, we have mentioned that their engineer has certain opportunities, so they're skeptical as to weather these addresses are even valid.

We then have three rules:
- If the phone number is not valid, we must not include it, since this will only stall their process.
- If the IP Address is not valid, we must not include it.
- If the email address is not valid, we must not include it.

The dataset's head can be found below:

```
Christopher Brown%%% cbrown@gmail.com%}%% (567) 890-1234%%% 890 Cedar Rd.%%% 192.268.0.3
Ashley Johnson%%% ashleyjohnson@yahoo.com%%% (678) 901-2345%%% 1234 Willow Way%%% 10.0.0.5
Andrew Lee%%% andrewlee@hotmeil.com%%% (789) 012-3456%%% 5678 Birch Blvd.%%% 172.16.1.3
Sarah Davis%%% sarah.davis@gmail.com%%% (890) 123-4567%%% 9012 Pine St.%%% 192.268.1.4
Robert Kim%%% robert_kim@yahoo.com%$$% 2345 Oak Ave.%%% 10.0.0.6
Emily Smith%%% emilysmith@gmail.com%%% (123) 456-7890%%% 456 Elm St.%%% 172.16.0.4
Michael Davis Jr.%%% michael.davis.jr@yahooo.com%%% (234) 567-8901%%% 789 Oak Ave.%%% 192.268.0.4
L. Kim Jr.%%% lkimjr@hotmeil.com%%% (345) 678-9012%% 10.0.0.7
```

The dataset link can be consulted [here]().

Let's get started, shall we?

## 1. Making sense of the data
From our dataset's head, we can notice some details:
- The attributes appear to be separated by multiple percentage signs `%` (*no idea why*), or other weird characters.
- The percentage signs are not always consistent (*some have double, and some have triple characters*).
- Some IP addresses appear to be invalid.
- Some email domains appear to be invalid.
- Some first names are denoted by an acronym (*`L. Kim`*).
- Some customers have middle name, which we do not want.
- All email addresses appear to end in `.com`, and have commercial domains, meaning we have a limited set of options that we can use to validate.
- All phone numbers have exactly the same structure:
	- `(aaa) ddd-dddd`: `a` is the area code, and `d` is a digit between `0` and `9`.

So, in summary, this database is a mess. However, RegEx is so powerful, that we'll be able to perform all the tasks and return a pristine version to our client.

## 2. First names
This one is fairly simple. We need to 

## 3. Last names


## 4. Validated phone numbers


## 5. Validated email addresses


## 6. Validated IPv4 addresses

## 7. Matching the database
After all the previous steps, we should end up with something like such:

##### **Code**
```RegEx
^(?P<first_name>\w+)(?:\.? )(?P<last_name>\w+)(?P<suffix> Jr\.|Sr\.)?(\.?)(?:[\%\$\{\}]{1,3} )?(?P<email_Address>(?P<email_name>\w+)(?P<email_second_name>\.\w+)?(?P<email_third_name>\.\w+)?\@(?P<email_domain>hotmail|gmail|aol|outlook|yahoo|protonmail)(?:\.com))?(?:[\%\$\{\}]{1,3} )?(?P<phone>\(\d{3}\) \d{3}\-\d{4})?(?:[\%\$\{\}]{1,3} )(?P<address>\d+ (?:\w+ ?){1,}\.?)(?:[\%\$\{\}]{1,3} )?(?P<ip_addr>(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))$
```

We can now translate our pattern to our Python script, and perform the matches using our input dataset:

##### **Code**
```Python
# -----------------------
# Import modules
# -----------------------
import re

# -----------------------
# Clean database
# -----------------------

# Define a multi-line RegEx expression
pattern = re.compile(
    r"^(?P<first_name>\w+)(?:\.? )(?P<last_name>\w+)"
    r"(?P<suffix> Jr\.|Sr\.)?(\.?)(?:[\%\$\{\}]{1,3} )?"
    r"(?P<email_address>(?P<email_name>\w+)(?P<email_second_name>\.\w+)?"
    r"(?P<email_third_name>\.\w+)?\@(?P<email_domain>hotmail|gmail|aol|outlook|yahoo|protonmail)(?:\.com))?"
    r"(?:[\%\$\{\}]{1,3} )?(?P<phone>\(\d{3}\) \d{3}\-\d{4})?(?:[\%\$\{\}]{1,3} )"
    r"(?P<address>\d+ (?:\w+ ?){1,}\.?)(?:[\%\$\{\}]{1,3} )?"
    r"(?P<ip_address>(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))$",
    re.M
)

# Read database
rdir = "src/inputs/advanced_set.txt"

with open(rdir, 'r') as file:
    database = file.read()
    matches = pattern.finditer(database)

for match in matches:
    print(f'NAME: {match.group("first_name")}, {match.group("last_name")}')
    print(f'EMAIL ADDRESS: {match.group("email_address")}')
    print(f'IP ADDRESS: {match.group("ip_address")}')
    print('')
```

##### **Output**
```
NAME: Jane, Smith
EMAIL ADDRESS: jane.smith@yahoo.com
IP ADDRESS: 10.0.0.1

NAME: Robert, Johnson
EMAIL ADDRESS: robert.johnson.jr@gmail.com
IP ADDRESS: 172.16.0.1

NAME: Michael, Brown
EMAIL ADDRESS: mbrown@aol.com
IP ADDRESS: 10.0.0.2

NAME: Lisa, Davis
EMAIL ADDRESS: lisa.davis@outlook.com
IP ADDRESS: 172.16.1.1

NAME: Emily, Kim
EMAIL ADDRESS: emily.kim@yahoo.com
IP ADDRESS: 10.0.0.3

NAME: Mark, Wilson
EMAIL ADDRESS: markwilson@gmail.com
IP ADDRESS: 172.16.1.2

NAME: Samantha, Smith
EMAIL ADDRESS: samantha.smith@yahoo.com
IP ADDRESS: 172.16.0.3

NAME: Emily, Smith
EMAIL ADDRESS: emilysmith@gmail.com
IP ADDRESS: 172.16.0.4

NAME: David, Smith
EMAIL ADDRESS: david.smith@yahoo.com
IP ADDRESS: 172.16.1.4

NAME: James, Davis
EMAIL ADDRESS: jdavis@hotmail.com
IP ADDRESS: 10.0.0.8

NAME: Olivia, Johnson
EMAIL ADDRESS: ojohnson@yahoo.com
IP ADDRESS: 172.16.0.5

NAME: Christopher, Kim
EMAIL ADDRESS: christopher.kim@yahoo.com
IP ADDRESS: 172.16.1.5

NAME: John, Smith
EMAIL ADDRESS: john.smith@gmail.com
IP ADDRESS: 10.0.0.10

NAME: M, Brown
EMAIL ADDRESS: mbrown@gmail.com
IP ADDRESS: 172.16.0.7

NAME: E, Johnson
EMAIL ADDRESS: ejohnson@yahoo.com
IP ADDRESS: 172.16.1.7

NAME: R, Davis
EMAIL ADDRESS: rdavis@gmail.com
IP ADDRESS: 10.0.0.14

NAME: E, Smith
EMAIL ADDRESS: esmith@yahoo.com
IP ADDRESS: 172.16.0.8

NAME: J, Kim
EMAIL ADDRESS: jkim@gmail.com
IP ADDRESS: 10.0.0.15

NAME: J, Brown
EMAIL ADDRESS: jbrown@aol.com
IP ADDRESS: 172.16.1.8

NAME: L, Lee
EMAIL ADDRESS: llee@yahoo.com
IP ADDRESS: 172.16.0.9

NAME: J, Kim
EMAIL ADDRESS: jkim@yahoo.com
IP ADDRESS: 172.16.1.9

NAME: R, Smith
EMAIL ADDRESS: rsmith@yahoo.com
IP ADDRESS: 172.16.0.10

NAME: S, Lee
EMAIL ADDRESS: slee@gmail.com
IP ADDRESS: 10.0.0.19

NAME: R, Rodriguez
EMAIL ADDRESS: rrodriguez@yahoo.com
IP ADDRESS: 10.0.0.20

NAME: D, Kim
EMAIL ADDRESS: dkim@gmail.com
IP ADDRESS: 172.16.0.11

NAME: K, Davis
EMAIL ADDRESS: kdavis@yahoo.com
IP ADDRESS: 172.16.1.11

NAME: D, Johnson
EMAIL ADDRESS: djohnson@yahoo.com
IP ADDRESS: 172.16.0.12

NAME: K, Lee
EMAIL ADDRESS: klee@yahoo.com
IP ADDRESS: 172.16.1.12

NAME: S, Kim
EMAIL ADDRESS: skim@yahoo.com
IP ADDRESS: 10.0.0.24

NAME: J, Johnson
EMAIL ADDRESS: jjohnson@gmail.com
IP ADDRESS: 172.16.0.13

NAME: M, Rodriguez
EMAIL ADDRESS: mrodriguez@yahoo.com
IP ADDRESS: 10.0.0.25

NAME: L, Kim
EMAIL ADDRESS: lk@yahoo.com
IP ADDRESS: 172.16.1.13

NAME: J, Lee
EMAIL ADDRESS: jlee@aol.com
IP ADDRESS: 172.16.0.14

NAME: E, Rodriguez
EMAIL ADDRESS: erodriguez@yahoo.com
IP ADDRESS: 10.0.0.27

NAME: L, Davis
EMAIL ADDRESS: ldavis@aol.com
IP ADDRESS: 10.0.0.28

NAME: S, Johnson
EMAIL ADDRESS: sjohnson@yahoo.com
IP ADDRESS: 172.16.0.15

NAME: K, Johnson
EMAIL ADDRESS: kjohnson@yahoo.com
IP ADDRESS: 172.16.1.15

NAME: S, Lee
EMAIL ADDRESS: slee@yahoo.com
IP ADDRESS: 172.16.0.16

NAME: L, Smith
EMAIL ADDRESS: lsmith@yahoo.com
IP ADDRESS: 10.0.0.31

NAME: D, Rodriguez
EMAIL ADDRESS: drodriguez@aol.com
IP ADDRESS: 172.16.1.16

NAME: M, Davis
EMAIL ADDRESS: mdavis@gmail.com
IP ADDRESS: 10.0.0.32

NAME: J, Johnson
EMAIL ADDRESS: jjohnson@yahoo.com
IP ADDRESS: 172.16.0.17

NAME: S, Brown
EMAIL ADDRESS: sbrown@yahoo.com
IP ADDRESS: 10.0.0.33
```

---

# Next steps



---

# Conclusions
We've reviewed 

---

# References
- 

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.