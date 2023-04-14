<article class="first">
  <div class="title">
    <h1>Probability Distributions Explained</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=probability-and-statistics&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/https://pabloagn.com/categories/probability-and-statistics/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=R%20,RStudio&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/probability-distributions-explained/)

Probability distributions are a key concept in probability theory & statistics. They provide a way to model uncertainty & randomness; this can be applied to describing and analyzing data, making predictions, testing hypotheses using statistical inference, inform decision making in many fields, such as finance, engineering, and medicine, and many more applications.

In this Blog Article, we'll define concepts such as probability, discrete and continuous random variables, sample spaces, and events. We'll then define what is a probability distribution, and the types of distributions based on the random variables they describe. We'll complement each example by using R to generate plots for various types of distributions, sample from distributions, and make simple calculations. 

We'll be using R scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/probability-and-statistics/probability-distributions-explained).

---

# Table of Contents
- [Probability distributions](#legibility)
	- [Authoring](#1-authoring)
	- [Comments](#2-comments)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Probability
Probability is a measure of the likelihood or chance of an event occurring. It's a number between 0 and 1, where 0 represents an impossible event (*an event that cannot occur*), and 1 represents a certain event (*an event that will always occur*). For events that are neither impossible nor certain, the probability lies somewhere between 0 and 1.

It's important to note that a given probability cannot be higher than 1. Also, for any event or set of events, the sum of the probabilities of all possible outcomes must be equal to 1. This is known as the Law of Total Probability, and is a pilar in probability theory.

Let us imagine an experiment where we flip a coin $n$ times. A conventional coin has two sides: heads and tails. If the coin is fair (*we will talk about fair and unfair variables later on*), the probability of heads is the same as the probability of tails in a single toss. Thus, we have two possible events with one associated probability each:
- Heads: $p = 0.5$
- Tails: $p = 0.5$

As we can see, the two probabilities sum up to 1, thus, the Law of Total Probability is fulfilled.

No matter how many times we toss the coin, the probabilities of heads or tails will remain the same (*i.e., if we toss the coin 10 times, and we get heads each time, the next toss will have a probability of heads = 0.5, and tails = 0.5*). But we might think, why? Wouldn't a coin toss have higher probability to result in tails after 10 tosses resulting in heads? The answer is: no. This believe is known as the [gambler's fallacy](https://en.wikipedia.org/wiki/Gambler%27s_fallacy), as we'll see further on.

As we saw in our previous example, probability is sometimes unintuitive; if this is our first approach to probabilistic experiments, we may think that probability theorems go against common sense. This is completely normal; our intuitions are often based on small samples or personal experiences, rather than on large datasets or objective evidence. Probability captures the entire frame, providing with powerful modeling and complex decision-making tools.

The coin example includes only 2 possible events. However, our world is not build on black or white; this is where probability distributions come in place.

---

# Random variables, sample space, & events
## 1. Random variables
A **random variable** ($r.v.$) is a variable that takes on different values based on the outcome of a random event or experiment. In other words, it's a quantity that can have different possible values, and the value it takes depends on the outcome of some random process.

In our coin toss experiment, the random variable would be the outcome of the single coin toss.

### 1.1 Discrete random variables
A discrete random variable is a variable that can only take discrete values; takes on a finite or countably infinite set of distinct values.

But what do we mean by countable values? The outcome of a single coin toss can be represented as a discrete $r.v.$, since its possible values $\{\text{heads}, \text{tails}\}$ are finite and countable.

Another example of a discrete random variable would be the outcome of a 6-sided die, where we have six possible outcomes.

### 1.2 Continuous random variables
A continuous random variable is a variable that can take on an infinite number of possible values within a certain range or interval, and the probability of any particular value occurring is always zero.

Let us picture a dartboard in a cartesian coordinate system:

B016A033_dartboard_bg.png

###### *Figure 1. Dart Board Denoting a continuous Probabilistic Space*

We have a set of outcomes limited by the circumference of our circle. What's interesting, is that the set of outcomes is infinite; we could in theory count the number of coordinate pairs, but if we had a dart thin enough, we could not do that, thus, the probability of a single event occurring (*i.e., the dart hitting a specific coordinate pair*), would be 0.

## 2. Sample space
A **sample space** ($S$) is the set of all possible outcomes of the experiment or process, and is typically represented by a list, set, or other collection of values or symbols.

In our coin toss experiment, the sample space variable would be represented by $S = {A, B}$.

## 3. Probabilistic events
A **probabilistic event** ($A$) is an event that has a certain level of uncertainty or randomness associated with it. In other words, it's an event that may or may not occur, and its outcome is not entirely predictable. An event can occur by performing a **probabilistic experiment**, in our case, flipping a coin.

The **probability of an event** is a measure of the likelihood or chance of that event occurring. As we mentioned, this probability is a number between 0 and 1, both inclusive.  The probability of an event A can be expressed as such: $P(A)$.

In our coin toss example, the two possible events would be heads ($A$) or tails ($B$), which we could also denote as $\{1,0\}$.

These three concepts are the foundations of probabilistic theory, and key in understanding probability distributions.

---

# Probability distributions
Probability distributions are mathematical functions that describe the likelihood of different outcomes in a random event or experiment; they describe the possible values a random variable can take, and how frequently they occur.

Let us revisit the coin example, where we have two possible outcomes or events. In this experiment, we toss the coin once.

It would then make sense to express the set of 2 probabilities as such:

$$
  P(X=x) =
  \begin{cases}
    p     & \text{if $x = 1$}, \\
    1 - p & \text{if $x = 0$}.
  \end{cases}
$$

Where:
- $P(X=x)$ denotes the probability of the random variable $X$ taking the value $x$.
- $p$ is the Bernoulli parameter, which can also be thought of as the probability of success in a single coin toss, where the random variable $X = 1$.
- If we have two possible events, it would make sense to express the probability of failure as $1-p$, since we know that the entire sample space must sum to 1. 

The expression we just reviewed is called a **Probability Mass Function** (*PMF*).

## 1. Probability functions
Probability functions are mathematical functions that describe the probability distribution of a random variable. There are different types of probability functions, depending on whether the random variable is discrete or continuous.

The two main probability functions are:
- PMF
- PDF

However, we also have the CDF, which describes the cumulative probability of a $r.v.$ which can be either discrete or continuous.

### 1.1 PMF
A **Probability Mass Function** (*PMF*) is a function that describes the probability distribution of a discrete random variable. The PMF assigns a probability to each possible value that the random variable can take, and is used to calculate the probability of different events or combinations of events.

### 1.2 PDF
A **Probability Density Function** (*PDF*) is a function that describes the probability distribution of a continuous random variable. The PDF assigns a probability density to each possible value of the random variable, and is used to calculate the probability of different events or combinations of events.

### 1.3 CDF
A **Cumulative Distribution Function** (*CDF*) is a function that describes the probability distribution of a random variable, either discrete or continuous. The CDF gives the probability that the random variable $X$ takes on a value less than or equal to a given value $x$.

## 2. Types of distributions
There are multiple probability distributions depending on the random variables we're trying to describe. In the coin toss example, we introduced the Bernoulli distribution, which describes the probability of achieving a “success” or “failure” from a Bernoulli trial. A Bernoulli trial is an event that has only two possible outcomes (*success or failure*).

This means that we can classify the probability distributions by the quantifiable nature of the $r.v.$:
- Discrete distributions
- Continuous distributions

The Bernoulli distribution is discrete by nature, since there are only two possible outcomes we can count. However, there are distributions for all kinds of experiments:
- Bernoulli distribution
- Binomial distribution
- Poisson distribution
- Geometric distribution
- Negative binomial distribution
- Uniform distribution
- Normal (*or Gaussian*) distribution
- Exponential distribution
- Gamma distribution
- Beta distribution
- Student's t-distribution
- Chi-squared distribution
- F-distribution
- Weibull distribution
- Logistic distribution
- Pareto distribution
- Log-normal distribution

In this segment, we'll exclusively focus on the most relevant:
- Bernoulli distribution
- Binomial distribution
- Poisson distribution
- Geometric distribution
- Uniform distribution
- Normal (*Gaussian*) distribution
- Exponential distribution

## Bernoulli distribution


## Binomial distribution


## Poisson distribution


## Uniform distribution


## Normal distribution


## Exponential distribution



---

# Conclusions
We've reviewed multiple yet simple mechanisms we can employ to make our code cleaner, more elegant, modular, usable, scalable and safer. These measures can not only help us become better programmers but better collaborators. It will make reading code a pleasure instead of an agonizing process and instantly boost our credibility.

---

# References
- [Python Documentation, Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Documentation, Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Towards Data Science, What happens when you import a Python module?](https://towardsdatascience.com/what-happens-when-you-import-a-python-module-ad6c0efd2640)
- [Towards Data Science, 3 data structures for faster Python Lists](https://towardsdatascience.com/3-data-structures-for-faster-python-lists-f29a7e9c2f92)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.