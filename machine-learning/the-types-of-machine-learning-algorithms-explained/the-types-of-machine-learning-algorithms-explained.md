<article class="first">
  <div class="title">
    <h1>The Types of Machine Learning Algorithms Explained</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://github.com/pabloagn/blog/tree/master/version-control) [![category](https://img.shields.io/static/v1?label=Category&message=machine-learning&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://github.com/pabloagn/blog/tree/master/machine-learning) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Python&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/the-types-of-machine-learning-algorithms-explained/)

---

**Machine Learning** is a discipline aimed at designing, understanding and applying computer programs that learn from experience for the purpose of modelling, prediction or control. It has gained significant momentum in recent years because it has forever changed how we look at problem-solving; previous to Machine Learning, if we wanted to tackle a problem, we had to hard-code a solution that would consider every variable and parameter. This becomes increasingly challenging as the amount of generated data also increases. ML algorithms are able to analyze all this data and (_sometimes_) come up with more accurate answers faster than any hard-coded method.

With this new discipline come a variety of models that can be used for different applications; from product recommendations to image, speech & text recognition to sentiment analysis to DNA sequencing to global warming modelling and temperature prediction; the potential applications are vast, and almost every field of study has at least one problem where ML models can help come up with more efficient solutions. ML is here to stay, and it's helpful to know the generalities of the technology to understand its potential applications.

In this article, we will discuss the different Machine Learning algorithm types. We will also qualitatively compare different Machine Learning models to grasp a generalized understanding. We will conclude this segment with some next steps for those interested in diving deeper into this exciting discipline.

We’ll be using Python scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/machine-learning/the-types-of-machine-learning-algorithms-explained).

---

# Table of Contents
- [Machine Learning vs traditional programming](#machine-learning-vs-traditional-programming)
- [Machine Learning algorithm types](#machine-learning-algorithm-types)
	- [Supervised Learning](#1-supervised-learning)
		- [Regression](#11-regression)
		- [Classification](#12-classification)
	- [Semi-Supervised Learning](#2-semi-supervised-learning)
	- [Unsupervised Learning](#3-unsupervised-learning)
	- [Active Learning](#4-active-learning)
	- [Transfer Learning](#5-transfer-learning)
	- [Reinforcement Learning](#6-reinforcement-learning)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Machine Learning vs traditional programming
What's so special about it? Why was it such an important breakthrough in how we think of problem-solving? To explain this, we have to refer to how traditional computation is done. 

Traditional computer programming has been around for more than a century, with the first known computer program dating back to the mid 1800s. It refers to any manually created program that uses input data and executes to produce the output; a programmer creates the program, but without anyone programming the logic, one has to manually formulate rules (*this is what we'll be referring to as hard-coding*).

For example, we can define a function that will do a specific task based on a set of logical rules which we ourselves define. In this case, our function accepts a DataFrame object as input, evaluates each row of the `age` column, and performs a mathematical operation based on each `age` value:

##### **Code**
```Python
# Import modules
import pandas as pd

# Example 1: Hard-coded function

# Declare entries
p0 = ['Saha', 'Howard', 22, 'Secretary', 1300]
p1 = ['John', 'Moore', 32, 'Illustrator', 3000]
p2 = ['Laszlo', 'Kreizler', 35, 'Alienist', 3500]
p3 = ['Willem', 'Van Bergen', 31, 'Pampered Child', 50000]
p4 = ['Libby', 'Hatch', 30, 'Nurse', 1100]
p5 = ['Lucifer', 'Morningstar', 35, 'Club Owner', 100000]
p6 = ['Chloe', 'Decker', 34, 'Detective', 1400]
p7 = ['Dan', 'Espinoza', 36, 'Detective', 1300]
p8 = ['Mazikeen', 'Smith', 35, 'Bounty Hunter', 20000]
p9 = ['Laura', 'Palmer', 22, 'Student', 100]
p10 = ['Dale', 'Cooper', 36, 'FBI Agent', 1800]
p11 = ['Harry', 'S. Truman', 34, 'Sheriff', 1300]
p12 = ['Bobby', 'Briggs', 23, 'Student', 80]
p13 = ['Gordon', 'Cole', 55, 'FBI Agent', 2000]

# Create list of lists
people_list = [p0, p1, p2, p3, p4,
               p5, p6, p7, p8,
               p9, p10, p11, p12,
               p13
               ]

# Declare DataFrame
df = pd.DataFrame(people_list,
                  columns = ['Name', 'Surname', 'Age', 'Job Position', 'Salary'])

# Declare function
def myFun(df):
    '''
    Parameters
    ----------
    df : Pandas DataFrame
        Contains 3 columns: Name, Surname, Age, Job Position, Salary (monthly in USD).

    Returns
    -------
    top_jobs : List
        Contains the top 7 paid job positions for a person between
        25 and 40 years old, sorted by importance.
    '''
    
    df_top = (df.query("`Age` >= 25 and `Age` <= 40").
              groupby('Job Position')['Salary'].mean().
              reset_index(name ='Average Salary').
              nlargest(7, 'Average Salary').
              sort_values(by='Average Salary', ascending=False).
              reset_index(drop=True)
              )
    
    return df_top

# Call function with df
print(myFun(df))
```

##### **Output**
```
     Job Position  Average Salary
0      Club Owner        100000.0
1  Pampered Child         50000.0
2   Bounty Hunter         20000.0
3        Alienist          3500.0
4     Illustrator          3000.0
5       FBI Agent          1800.0
6       Detective          1350.0
```

Apart from the fact that being a club owner or a pampered child could be the key in life, we can see that this method implementation worked because we defined logical rules denoted by our `query` statements. These were explicitly stated and required a logical reasoning behind curtains. 

This was also feasible because we had a very limited set of rules: `age` and `Average Salary`, which we used as features in order to return an output.

The problems surface when we have an extensive set of features we need to consider, are not normalized, or even worst, we don't know which ones could be used leveraged to get the insight we're looking for.

In Machine Learning, the algorithm automatically formulates the rules from its input, and outputs a model which we can use to perform predictions, classifications, or control.

These algorithms can go from extremely simple to extremely complex; it all depends on what we're trying to solve, the input dimensions, and the complexity of our data.

It's important to remember that, as grandiose as it may seem, ML is just another tool in a very extensive toolbox; it's easy to assume that ML can be applied to every possible problem and outperform any traditional algorithm, but the truth is, it does not substitute traditional programming entirely, nor does it do magic.

As with any tool, it has its applications and limitations, and is based on rigorous mathematical and statistical theory. In fact, Machine Learning can be though of as a combination of probability theory, statistics & optimization. We'll see why in a moment.

---

# Machine Learning algorithm types
Machine Learning algorithms can be classified by how they work and what type of data they accept as input. There are 3 main types and some other subclassifications:

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

## 1. Supervised Learning
Supervised Learning uses labeled datasets to train algorithms that to classify data or predict outcomes accurately. We can think of a labeled dataset as one with tags that identify what the data represents.

If we look at our previous example, we used a DataFrame with 5 columns:

##### **Code**
```Python
print(df.columns)
```

##### **Output**
```
Index(['Name', 'Surname', 'Age', 'Job Position', 'Salary'], dtype='object')
```

This means that our data is labeled; it has identifiable tags which we can use to make sense of the information it presents.

More specifically, in the Machine Learning context, a label is the specific vector we're trying to predict or use to classify. This depends on the problem we're trying to solve.

For example, we could use our DataFrame `df` to train a model which predicts a person's Salary based on other attributes such as `Age` and `Job Position`. These attributes would be called features, and the target to predict, in this case `Salary`, would be our label. We could solve this problem either by regression or classification; these are the two main subclasses of Supervised Learning.

### 1.1 Regression
**Regression** is most commonly known since it's taught very early on math courses and has multiple applications; from market analysis to financial analysis to trend forecasting. It requires us to have continuous data points.

The most common and simple type of regression is **Linear Regression** (*LR*), which consists of fitting a straight line to a set of value pairs ($x, y$) in order to predict unseen values of a dependent variable $y$ given an independent variable value $x$. This method uses the general equation of a straight line to fit data:

$$y=m \cdot x+b$$

Where:
- $y$ is the dependent variable.
- $m$ is the slope or gradient (*how steep the line is*).
- $x$ is the independent variable.
- $b$ is the y-intercept (*the value of $y$ when $x=0$*)

Which can be written in terms of Machine Learning notation:

$$h(x) = \theta_0 + \theta_1 x$$

Where:
- $h(x)$ is the label.
- $\theta_0$, $\theta_1$ are weights.
- $x$ is the input feature.

Once we have the basic straight line form, we can start by using random weights and evaluating how well this line fits our data. This is done by using an error function, the most common in Linear Regression being a variation of the Mean Squared Error (*MSE*) function called the **Squared Error Cost Function**.

We can first express the simpler MSE:

$$MSE=\frac{1}{n}\sum_{i=1}^{n}(Y_i-\hat{Y_i})^2$$

Where:
- $n$ are the number of data points.
- $Y_i$ is the observed $i^{th}$ value.
- $\hat{Y_i}$ is the predicted $i^{th}$ value.

And then translate to the Squared Error Cost Function:

$$J(\theta)=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-Y^{(i)})^2$$

Where:
- $m$ are the number of data points.
- $h_{\theta}(x^{(i)})$ is the predicted $i^{th}$ value.
- $Y^{(i)}$ is the observed $i^{th}$ value.

What Linear Regression does, is minimize this function by changing the weights iteratively. This is done by calculating the partial derivatives of $J(\theta_{0}, \theta_{1})$ with respect to $\theta_{0}$ and $\theta_{1}$:

$$\frac{d}{d\theta_0} J(\theta_0,\theta_1)=\theta_0+\theta_1x-Y^{(i)}$$
$$\frac{d}{d\theta_1} J(\theta_0,\theta_1)=(\theta_0+\theta_1x-Y^{(i)})x$$
Where $\theta_{0}$ and $\theta_{1}$ are updated simultaneously on each iteration.

This method we just defined is called **Gradient Descent**, a first-order iterative optimization algorithm for finding a local minimum of a differentiable function. It's widely used in Machine Learning to optimize multiple models.

In the end, we're left with a combination of parameters $(\theta_{0}, \theta_{1})$ which best fit our straight line to the data points.

Of course, Linear Regression, as its name suggests, is used to predict data which presents linear correlation. There are other methods for predicting non-linear continuous data such as Polynomial Regression.

### 1.2 Classification
As its name suggests, this subcategory of Supervised Learning aims to classify 

## 2. Semi-Supervised Learning


## 3. Unsupervised Learning


## 4. Active Learning


## 5. Transfer Learning


## 6. Reinforcement Learning

---

# Conclusions
We have reviewed ...

---
# References
- [IBM, What is supervised learning?](https://www.ibm.com/topics/supervised-learning)
- [IBM, What is unsupervised learning?](https://www.ibm.com/topics/unsupervised-learning)
- [Machine Learning Mastery, What Is Semi-Supervised Learning?](https://machinelearningmastery.com/what-is-semi-supervised-learning/)
- [Towards Data Science, Active Learning in Machine Learning](https://towardsdatascience.com/active-learning-in-machine-learning-525e61be16e5)
- [Analytics Vidhya, Commonly used Machine Learning Algorithms](https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.
