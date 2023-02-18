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

We will not discuss each model in detail since there are too many to cover on one segment. For that, there's a dedicated 3-segment hands-on Guided Project, [Exploratory Data Analysis](https://pabloagn.com/guided-projects/exploratory-data-analysis-pt-1/), which covers all the major classification algorithms along with a detailed comparison by using an example applied on medical data. There will also be future content covering diverse ML model implementations in detail.

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
- [Parametric and Non-Parametric models](#parametric-and-non-parametric-models)
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
**Supervised Learning** uses labeled datasets to train algorithms that to classify data or predict outcomes accurately. We can think of a labeled dataset as one with tags that identify what the data represents.

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
As its name suggests, this subcategory of Supervised Learning aims to classify data by assigning a label to a data input. This method works for linear and non-linear discrete data.

There are multiple classification applications, a very simple case being the classification of Spam Email. Let us look at a simple example.

#### 1.2.1 Binary classification

A Spam detector takes as inputs a number of previously engineered features:

- **Subject Features:**
	- Number of capitalized words.
	- Sum of all the character lengths of words.
	- Number of words containing letters and numbers.
	- Max of ratio of digit characters to all characters in each word.
- **Header Features:**
	- Hour of day when email was sent.
- **URL Features:**
	- The number of all URLs in the email body.
	- The number of unique URLs in the email body.
- **Payload Features:**
	- Number of words containing letters and numbers.
	- Number of words containing only letters.

It then classifies each entry as Spam or Not Spam, so our output would be **binary**:

- **Spam:** 1
- **Not Spam:** 0

Some of the most used binary classification algorithms are:
- Logistic Regression (*LR*)
- k-Nearest Neighbors (*KNN*)
- Decision Trees (*DCT*)
- Support Vector Machines (*SVM*)
- Gaussian Naïve Bayes (*GNB*)
- Bernoulli Naïve Bayes (*BNB*)

#### 1.2.2 Multi-class classification

A classification algorithm can work not just with binary outputs, but multiple ones. This is called a **multi-class** classification algorithm. Let us look at a simple example.

We wish to input different animal descriptors and let our model decide which animal species is it:

- **Physical Attributes:**
	- Haired: `Bool`
	- Feathered: `Bool`
	- Toothed: `Bool`
	- Whiskered: `Bool`
	- Leg Number: `Int`
	- Tail: `Bool`
	- Fins: `Bool`
- **Anatomical Attributes:**
	- Eggs: `Bool`
	- Milk: `Bool`
	- Airborne: `Bool`
	- Aquatic: `Bool`
	- Predator: `Bool`
	- Venomous:  `Int`
- **Physiological / Behavioral Attributes:**
	- Domestic: `Bool`
	- Aggressive: `Int`
	- Supports cold temperatures: `Bool`
	- Supports hot temperatures: `Bool`
	- Tough skin: `Bool`
	- Spiny/horned skin: `Bool`
	- Blends in or camouflages with environment: `Bool`

Our model will intend to classify each entry as a different species, so our output would be **multi-class**, dependent on the number of classes we have for our training set:

- Platypus
- Tiger
- Alpaca
- Horse
- Dog
- Cat
- Guinea pig

Some of the most used multi-class classification algorithms are:
- Decision Tree Classifier (*DCT*)
- Random Forest Classifier (*RF*)
- Extreme Gradient Boosting Ensemble Classifier (*XGBoost*) (*Experimental Support as of Version 1.6*)
- Gaussian Naïve Bayes (*GNB*)
- Bernoulli Naïve Bayes (*BNB*)
- Support Vector Machines (*SVM*)
- Adaptive Boosting Ensemble Classifier (*AdaBoost*)

#### 1.2.3 Managing unbalanced data

For a typical classification algorithm to work without special treatment, we need to have a balanced data set. This means that the ratio of classes must be roughly equal, e.g. from first example, $\approx 50\%$ spam emails, $\approx 50\%$ non spam emails.

We might run into occasions where our data set is unbalanced and we cannot resample from the population. In this case, there are some methods we can use:

- **Under-sampling:** Balances the dataset by reducing the size of the abundant class. This method is used when quantity of data is sufficient. By keeping all samples in the rare class and randomly selecting an equal number of samples in the abundant class, a balanced new dataset can be retrieved for further modelling.

- **Over-sampling:** It's used when the quantity of data is insufficient. It tries to balance dataset by increasing the size of rare samples.

- **Clustering abundant groups:** Instead of relying on random samples to cover the variety of the training samples, we can cluster our abundant class in $r$ groups. For each group, only the medoid (*center of cluster*) is kept. The model is then trained with the rare class and the medoids only.

- **Selecting an appropriate model:** There are classification models that handle unbalanced data particularly well. One example is the **Extreme Gradient Boosting** (*XGBoost*) algorithm.

## 2. Semi-Supervised Learning
**Semi-supervised learning** (*SSL*) involves utilizing both labeled and unlabeled data to enhance the performance of machine learning models, even when only a portion of the dataset has labels. The core concept of this approach is to handle data points differently depending on whether they are labeled or not. For labeled data points, the algorithm employs traditional supervised learning techniques to adjust the model weights, while for unlabeled data points, the algorithm minimizes the variation in predictions between similar training examples.

A typical example where semi-supervised learning can be effective is in text document classification, where obtaining a large number of labeled text documents can be challenging, as it is time-consuming to read through entire documents to assign a classification.

By using a combination of a small number of labeled text documents and a large amount of unlabeled text data, semi-supervised learning enables the algorithm to learn from the labeled data while also classifying the unlabeled data in the training set.

Semi-supervised algorithms achieve this objective by leveraging pseudo-labeling. The model is initially trained using the small set of labeled data in a manner similar to supervised learning until it produces good results. Then, the model is utilized to predict the outputs of the unlabeled data, which creates pseudo labels that might not be entirely accurate. The pseudo labels are then associated with the labeled data, and the inputs in the unlabeled data are linked to the inputs in the labeled data. Finally, the model is retrained using this combined data to minimize errors and increase accuracy.

We can look at a summary of the steps below:

- **Gather labeled and unlabeled data:** Semi-supervised learning algorithms require both labeled and unlabeled data. The labeled data is data that has already been assigned a known label or category, while the unlabeled data is data that does not have an assigned label.
- **Train the model with the labeled data:** The first step in a semi-supervised learning algorithm is to train the model using the labeled data. This is done using traditional supervised learning techniques, where the model is trained to learn the patterns in the labeled data.
- **Use the model to label the unlabeled data:** After the model has been trained on the labeled data, it can be used to make predictions on the unlabeled data. This process is known as inference, and the predicted labels are referred to as pseudo-labels.
- **Combine the labeled and pseudo-labeled data:** The next step is to combine the labeled and pseudo-labeled data. This is done by associating the predicted labels from the unlabeled data with the input data in the labeled data.
- **Retrain the model with the combined data:** The final step is to retrain the model using the combined data. This is done using traditional supervised learning techniques, where the model is trained to learn the patterns in the combined data. The model will now be able to generalize to new data points, including those that were previously unlabeled.
- **Evaluate the model:** After the model has been trained and retrained using the semi-supervised learning algorithm, it is important to evaluate its performance. This can be done by testing the model on a set of validation data or by using other performance metrics, such as accuracy or precision.

There are five main approaches we can use with semi-supervised learning:

### 2.1 Self-training
We can take any supervised method for classification or regression and modify it to work in a semi-supervised manner. This method involves training a model on a small set of labeled data and then using that model to make predictions on the unlabeled data. The most confident predictions are then added to the labeled data set and the model is retrained.

### 2.2 Co-training 
It is used in situations where only a small amount of labeled data is available. It differs from the usual process of training a classifier as it involves training two individual classifiers based on two different views of the data. These views consist of distinct sets of features that offer additional information about each instance, which are independent given the class. Additionally, each view is self-sufficient in that the class of the sample data can be predicted accurately using each set of features separately.

### 2.3 Generative models
Generative models such as the Naïve Bayes algorithm and Gaussian mixture models can be used in semi-supervised learning. These models learn the underlying probability distribution of the data and use this information to make predictions.

### 2.4 Graph-based methods
These methods use the structure of the data to create a graph, where nodes represent instances and edges represent similarity between instances. Graph-based models can use both labeled and unlabeled data to learn the structure of the graph and make predictions.

### 2.5 Deep Learning
Semi-supervised deep learning models such as autoencoders and generative adversarial networks (*GANs*) can use both labeled and unlabeled data to learn the underlying structure of the data and make predictions.

## 3. Unsupervised Learning
Unsupervised learning uses machine learning algorithms to analyze and cluster unlabeled datasets. These algorithms discover hidden patterns or data groupings without the need for human intervention. There are three main uses for unsupervised learning methods: clustering, association and dimensionality reduction.

### 3.1 Clustering
This method groups unlabeled data based on their similarities or differences. We don't require labels. The only thing we require is a set of data points with their features.

Clustering is widely used to study underlying patterns or tendencies not simple at plain sight, and is extremely useful when we have a large volume of apparently uncorrelated data.

#### 3.1.1 Exclusive and Overlapping Clustering
**Exclusive clustering** is a form of grouping that stipulates a data point can exist only in one cluster. This can also be referred to as “*hard*” clustering.

A popular algorithm is the **K-means clustering**, borrowed from signal processing. In this method, the data set is partitioned into $k$ clusters in which each observation belongs to the cluster with the nearest mean (*cluster centers or cluster centroid*), serving as a prototype of the cluster. These clusters are referred to as **Voronoi Cells**:

![Figure 01](https://raw.githubusercontent.com/pabloagn/blog/master/machine-learning/the-types-of-machine-learning-algorithms-explained/images/B007G011_01.png)
###### *Figure 1: Voronoi diagram illustrating how colony area is split into tessellated cells*[^1] 

In the figure above, we can see two different partition sets: The first one denotes a Voronoi diagram with 25 partitions, while the second one has 26 partitions, where one cell splits into two cells (*denoted with the red color*). Typically, each cluster will encapsulate a set of data points; the critical aspect to consider in this method, is to define the correct number of cells so as not to underfit or overfit the model (*i.e. we don't want a single cell for a single data point*)

#### 3.1.2 Hierarchical clustering
**Hierarchical clustering** (*HCA*) algorithms can be classified as agglomerative or divisive. In agglomerative clustering, data points are isolated as separate groupings initially, and then they are merged together iteratively on the basis of similarity until one cluster has been achieved.

There are four main methods to measure similarity:
- **Ward’s linkage:** This method has much in common with the statistical analysis of variance (*ANOVA*); the linkage function specifying the distance between two clusters is computed as the increase in the "error sum of squares" (ESS) after fusing two clusters into a single cluster.
- **Average linkage:** In this method, the linkage function specifying the distance between two clusters is computed as the average distance between objects from the first cluster and objects from the second cluster. The averaging is performed over all pairs of objects.
- **Complete (*or maximum*) linkage:** At the beginning of the process, each element is in a cluster of its own. The clusters are then sequentially combined into larger clusters until all elements end up being in the same cluster. The method is also known as **farthest neighbors clustering**. The result of the clustering can be visualized as a dendrogram, which shows the sequence of cluster fusion and the distance at which each fusion took place.

![Figure 2](https://raw.githubusercontent.com/pabloagn/blog/master/machine-learning/the-types-of-machine-learning-algorithms-explained/images/B007G011_02.png)
###### Figure 2: Dendrogram with data points on the x-axis and cluster distance on the y-axis[^2]

- **Single (*or minimum*) linkage:** This method is based on grouping clusters, at each step combining two clusters that contain the closest pair of elements not yet belonging to the same cluster as each other.

In **divisive clustering**, in contrast, a single data cluster is divided based on the differences between data points.

## 4. Active Learning


## 5. Transfer Learning


## 6. Reinforcement Learning

---

# Parametric and Non-Parametric models
As we have seen, machine learning models can be classified by the types of inputs they accept as well as their functioning. The classification we just reviewed is one way to group similar models, but we can also look at ML algorithms in terms of how they map data points.

## 1. Parametric models
**Parametric models** are based on a mathematical model that defines the relationship between inputs and outputs. A great supervised example is the **Linear Regression** model, which uses the equation of a straight line to fit data points in a plane. Another classification example is the **Logistic Regression** model, which uses the [sigmoid function](https://machinelearningmastery.com/a-gentle-introduction-to-sigmoid-function/) to classify data. These models are based on defined mathematical equations and use them to produce outputs.

Other parametric examples include:
- Perceptrons
- Simple Neural Networks
- Linear Support Vector Machines

Some examples of model parameters include:
- The coefficients of the equation of a straight line in Linear Regression.
- The coefficients of a polynomial in a Non-linear Regression.
- The support vectors in a Support Vector Machine.
- The weights in a Neural Network.

## 2. Non-parametric models
In contrast, **Non-parametric** models do not make strong assumptions about the form of the mapping function; they instead learn from the data itself. An extremely popular  supervised example would be the **Decision Tree Classifier**, which are based on a hierarchical structure. Another example would be 

Other non-parametric examples include:
- A
- A
- A

## 3. Which one to choose?
This question is trickier since it implicates the nature of the problem we're trying to solve. Still, we can summarize both models in a comparative table in order to have a better understanding of the two types:

| Parameter               | Parametric Models                                                                                | Non-Parametric Models                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Parameter usage         | Use a fixed number of parameters to build the model                                              | Use a flexible number of parameters to build the model                        |
| Data assumptions        | Consider strong assumptions about the data                                                       | Consider fewer assumptions about the data                                     |
| Computational effort    | Are usually less computationally expensive                                                       | Are usually more computationally expensive                                    |
| Performance             | Are usually faster performing due to a predefined set of parameters                              | Are usually slower due to undefined parameters                                |
| Data volume requirement | Usually require less data                                                                        | Usually require more data                                                     |
| Simplicity              | Are usually simpler and easier to understand                                                     | Are usually more complex since we don't fully know the underlying model       |
| Flexibility             | Are less flexible since they assume one fixed functional form                                    | Are extremely flexible since there's no predefined functional form            |
| Accuracy                | Can, in some cases, be less accurate if the data is complex or does not fit the underlying model | Can be highly accurate if the data is complex, but can also cause overfitting |


###### Table x: Comparison between Parametric and Non-Parametric ML models

Aaa

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
- [Research Gate, Spam-detection Features](https://www.researchgate.net/figure/Top-5-spam-detection-features-19_tbl2_275647490)
- [KD Nuggets, Managing Unbalanced Data](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html)
- [DataRobot, Semi-supervised Learning](https://www.datarobot.com/blog/semi-supervised-learning/)
- [IBM, Unsupervised Learning](https://www.ibm.com/topics/unsupervised-learning)
- [Laura E. Wadkin, Sirio Orozco-Fuentes, Irina Neganova, The recent advances in the mathematical modelling of human pluripotent stem cells](https://www.researchgate.net/figure/a-Voronoi-diagram-illustrating-how-colony-area-is-split-into-tessellated-cells-b-The_fig5_336013919)

[^1]: Laura E. Wadkin, Sirio Orozco-Fuentes and Irina Neganova at Science Direct, The recent advances in the mathematical modelling of human pluripotent stem cells.
[^2]: DataNovia, Hierarchical Clustering

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.
