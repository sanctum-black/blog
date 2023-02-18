<article class="first">
  <div class="title">
    <h1>Julia for Beginners</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Julia&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/julia-for-beginners/)

On our previous article, [What Is Julia, and Why It Matters?](what-is-julia-and-why-it-matters), we discussed why Julia is so relevant today, and made some comparisons between other similar languages such as Python and R. We also mentioned some of its main characteristics and features, and concluded with some next steps in order to get started programming on Julia. 

In this Blog Article, we'll install Julia along with a VS Code extension for it. We'll set up an environment, install some packages, and cover several practical examples, where we will perform a general overview of Julia's main functionalities. We will close this segment by giving some recommendations on how to use Julia as well as next steps for those interested in this bleeding-edge programming language.

We'll be using Julia scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/programming-best-practices-writing-better-code).

---

# Table of Contents
- [Prelude](#prelude)
- Julia in a nutshell
- What makes Julia so special?
- To whom is Julia targeted towards?
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Prelude
I remember some years ago, when Showtime's [Billions](https://www.sho.com/billions) was in its pinnacle, that [Julia](https://pabloagn.com/technologies/julia/) was featured in an episode in which Taylor Mason, the quantitative analyst, mentioned it as a key tool used in the sophisticated quantitative strategies deployed at the fictional [Taylor Mason Capital](https://billions.fandom.com/wiki/Taylor_Mason_Capital).

It seemed interesting, but I didn't pay much attention since my main workhorse at the time was (*and still is)* [Python](https://pabloagn.com/technologies/python/) (*with some specific tasks performed on [R](https://pabloagn.com/technologies/r/)*). This combination basically covers all the data-processing and data-analysis-related functions I perform daily as a Data Scientist and content creator.

Some months ago I came across an interesting TEDx MIT talk: ["A programming language to heal the planet together: Julia"](https://www.youtube.com/watch?v=qGW0GT1rCvs). It immediately grabbed my attention and made me think: How comfortable have I gotten with Python? Maybe too comfortable? I mean, it’s general-purpose, dynamically-typed, descriptive, easy to read and write, has tons of documentation available, a massive community, endless libraries to suit whichever need we may think of, and the list goes on and on. But let’s face the elephant in the room…it’s s l o w and the data volume will only increase in the future.

[Dr. Alan Edelman’s](https://math.mit.edu/~edelman/) conference appeared so convincing to me, that I decided to adopt the language to see if it could substitute Python & R at least to some degree.

For this to work, I first needed to do some preliminary checks:
- Is high-level and mostly dynamically-typed (*or at least has the option to do so*).
- Has a robust and up-to-date set of equivalent libraries.
- Has an active community (*or at least detailed and rigorous technical documentation*).
- Allows to manipulate array-type objects as easily as NumPy or Pandas.
- Has well-maintained support from at least a couple of IDE(s), preferably also [Jupyter](https://pabloagn.com/technologies/jupyter-lab/) or an equivalent notebook-style environment.

I spent a couple of months testing this new programming language, and let me tell you lads, it exceeded my expectations in every possible way.

---

# Julia in a nutshell
If we visit the [official Julia website](https://julialang.org/), we can see some of its key properties:

- Fast
- Dynamic
- Reproducible
- Composable
- General
- Open source

Some of the aspects above are natively covered on other languages such as Python; it's dynamic, has the capacity to generate reproducible environments, is general-purpose, and open-source.

Some of then though, are not covered: Python is not a particularly fast language since it compiles into a format known as byte code. The source code compiled to byte code is then executed in Python’s virtual machine one by one to carry out the operations. Internally, Python code is interpreted during run time rather than being compiled to native code hence it's slower than some other compiled languages such as C, [C++](https://pabloagn.com/technologies/c-plus-plus/) and [Rust](https://pabloagn.com/technologies/rust/).

Also, Python does not natively support multiple-dispatch (*we'll see what that is later on*). We have to install an external library in order to add this functionality.

---

# What makes Julia so special?
As stated in the TEDx MIT Talk we mentioned earlier, Julia is fast; it joined the Petaflop Club in 2017 with the [`Celeste.jl` implementation](https://www.youtube.com/watch?v=uecdcADM3hY). If we take a moment to realize that the other languages currently belonging to this club are C, C++ and Fortran, it really leaves something to think about in terms of where we're heading.

Apart from the fast-performing aspect, Julia is easy to write and read, and this is directly related to the point above; most low-level languages are hard to write simply because of their nature: they are faster-performing, but we also have to be more careful in how we design our programs, requiring a tremendous amount of expertise in computer science and algorithmic design.

As mentioned TEDx MIT Talk:

> The common wisdom for programming languages has always been that we could have an "either" or an "or"; either we can have a programming language that's easy to program, but we'll pay the price (*somehow the programs will execute much more slowly and we will loose out on performance*). The other possibility, a much more difficult endeavor, involves a much higher programming expertise, and then we can get better performance. Julia showed that it wasn't one or the other but that we could have our cake and eat it too.
Dr. Alan Edelman

This quote is fantastic because it summarizes what Julia is all about in a single paragraph: it's fast-performing while at the same time being easy to write and read.

---

# To whom is Julia targeted towards?
Although Julia is defined as a general purpose programming language, it really shines on **scientific computing tasks**; it has a wide variety of scientific libraries covering linear algebra, differential and integral calculus, advanced probabilistic and statistical modeling, discrete and continuous mathematics, analytical geometry and much more. There's even a specific monospaced font called [JuliaMono](https://juliamono.netlify.app/), specifically tailored for scientific computing; we can use font ligatures to produce beautifully written mathematical expressions.

We can also use actual Unicode characters to assign variables:

##### **Code**
```Julia
𝛂, 𝛃 = [1, 2]

println(𝛂)
println(𝛃)
```

##### **Output**
```
1
2
```

##### **Code**
```Julia
if 𝛂 ≥ 𝛃
    println("𝛂 is greated than 𝛃")
else
    println("𝛃 is greated than 𝛂")
end
```

##### **Output**
```
𝛃 is greated than 𝛂
```

If we would like to spice things up a little bit, we could use emojis to assign variables:

##### **Code**
```Julia
🧑 = "We "
❤️ = "love "
⭕ = "Julia"

println(🧑, ❤️, ⭕)
```

##### **Output**
```
We love Julia
```

Or the other way around:

##### **Code**
```Julia
a = "🚀"
b = "👩‍🚀"
c = "🌕"

println(a, b, c)
```

##### **Output**
```
🚀👩‍🚀🌕
```

Fun, right? Well, we're just getting started.

Julia also excels at Data Science tasks; it has multiple libraries covering advanced and dynamic visualization, data querying, data processing and manipulation, problem optimization, machine learning, and more. It's supported by JupyterLab, and even has it's own notebook environment available as a package: `Pluto.jl`.

But that's not all, because Julia is also extremely high performing and capable of parallel computing; it can generate native code for GPUs and has direct integration with the [Spark]() ecosystem.

All of these aspects make Julia extremely versatile and fun to work with.



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