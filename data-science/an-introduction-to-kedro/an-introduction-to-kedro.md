<article class="first">
  <div class="title">
    <h1>Introduction to Kedro</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Python&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/introduction-to-kedro/)

Writing code can be as simple as importing the required libraries, declaring our variables, functions, and classes as required, including some docstrings here and there, some additional comments, executing, and we're done. While we're at it, let's skip the function & class part and drop everything as is. Even better, let's also save some lines by stripping our file from all comments.

In this Blog Article, we'll

We'll be using Python scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/programming-best-practices-writing-better-code).

---

# Table of Contents
- [Legibility](#legibility)
	- [Authoring](#1-authoring)
	- [Comments](#2-comments)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Assisting

From Zitao Wang to Everyone 08:05 AM
will the recording link be sent over email after the session?
From Juan Luis Cano to Everyone 08:12 AM
Madrid, Developer Advocate
From Pascal Schulz (pmOne) to Everyone 08:12 AM
Germany Data Scientist
From Elaine to Everyone 08:12 AM
Belo Horizonte, Brazil. Data Scientist
From Edgar Hurtado to Everyone 08:12 AM
Bogota - Colombia | Data Engineer
From Ignacio Serrano to Everyone 08:12 AM
Data Scientist. Madrid, Spain
From Me to Everyone 08:12 AM
Mexico City, Data Scientist
From justo van der werf to Everyone 08:12 AM
Netherlands, Data scientist
From Chris Schopp to Everyone 08:12 AM
London, Ontario, Canada.
Simulation Consultant.
From Sara to Everyone 08:12 AM
data analyst from wales :)
From javiersantoma to Everyone 08:12 AM
Barcelona, Data Engineer
From vinicius.sousa to Everyone 08:12 AM
Rio de Janeiro, Brazil - Data Analyst
From Carlos Morente to Everyone 08:12 AM
Málaga (Spain), Data Scientist
From Daniel Jimenez to Everyone 08:12 AM
Data Analyst - Costa Rica SJO
From Viknesh Vivekanandan to Everyone 08:12 AM
Barcelona, Data Analyst
From Ignacio Moya to Everyone 08:12 AM
Madrid, Aeronautical Engineer
From Elena Campillo to Everyone 08:12 AM
Vigo, engineer / researcher
From Lucie Gattepaille to Everyone 08:12 AM
Aix-en-provence, data scientist
From Luca Wetter Sanchez to Everyone 08:12 AM
Data Scientist, UK
From Natthawute Saelim to Everyone 08:12 AM
Japan, Data Scientist
From Emma Saroyan to Everyone 08:12 AM
developer advocate
From Leo Gallegos to Everyone 08:12 AM
Spain Technical PM
From Alborz Babaie Mouziraji to Everyone 08:12 AM
Brussels, Belgium, Data Consultant
From Jo Stichbury to Everyone 08:12 AM
🏴󠁧󠁢󠁷󠁬󠁳󠁿✍️
From Ignacio Amaya to Everyone 08:12 AM
Helsinki, ML engineer
From Jana Staffa to Everyone 08:12 AM
Germany, DS
From Guillermo FB to Everyone 08:12 AM
From Spain, Junior Developer
From nvauquie to Everyone 08:12 AM
Lille in France, VP of Engineering
From Johan Setiawan to Everyone 08:12 AM
Indonesia, system analyst
From Edo Altamura to Everyone 08:12 AM
Manchester UK, Astrophysicist
From Y Chi to Everyone 08:12 AM
Madrid, Business Analytics Student
From Jairo J. Niño to Everyone 08:12 AM
Colombia, Data Science Manager
From Roman Polyachkov to Everyone 08:12 AM
Tashkent, Uzbekistan, network automation engineer
From hector to Everyone 08:12 AM
Hola, Vitoria-Gasteiz, Polymer mechanics researcher
From Túlio Abner de Lima to Everyone 08:13 AM
Brazil, Data engineer
From Carlos Chiri to Everyone 08:13 AM
Bolivia, Data Scientist
From Giuseppe Birardi to Everyone 08:13 AM
Researcher from Italy
From Danilo Gómez to Everyone 08:13 AM
Danilo, Madrid, Software Enginer
From DanielToránMercadé to Everyone 08:13 AM
Barcelona, Data Scientist
From Vanessa Hargreaves to Everyone 08:13 AM
Data Scientist, UK
From Vins Calabrese to Everyone 08:13 AM
i'm from italy, data scientist
From Yetunde Dada (She/Her) to Everyone 08:13 AM
South Africa, Product Manager
From amel omri to Everyone 08:13 AM
amel omri machine learning engineering from tunisia
From Laurent to Everyone 08:13 AM
Belgium, Planning Engineer

# What is Kedro?
- Framework
- Scalability
- Propper engineering foudnations for Data Science code.
- Production quality
- Tailored for ML models that require maintainability production-wise.
- Follows 12-Factor App software engineering philosophy.
- React or Django for ML.
- 8.1k Stars on GitHub
- Donated Kedro to the Linux Foundation
- Committee (Check for this) (Multi-stakeholder)



# Why Kedro?
- Address shortcomings of Jupyter when talking about production code.
- Encourage good software engineering practices.
- 

# The Basics
![[Pasted image 20230504081518.png]]


- Data Catalog: Declarative configuration file to locate files.
	- Abstracted way to refer to datasets.
- Nodes & Pipelines: Based on CLI commands.
- Extensibility: Plugins, extensions.
- Supports orchestration platforms such as Airflow, and others.

# Comparison vs. Other Similar Platforms

![[Pasted image 20230504081926.png]]


# Support & Committee

![[Pasted image 20230504082047.png]]

# Workshop

## Data

Sourced from:

![[Pasted image 20230504082345.png]]

---

# Creating a Kedro Project from Scratch
- Include `kedro~0.18.8` (Released 3 may 2023)
- `catalog.yml` -> Dataset specification

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