<article class="first">
  <div class="title">
    <h1>Julia for Beginners</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Julia,%20VS%20Code,%20Pluto,%20PowerShell%207&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/julia-for-beginners/)

On our previous article, [What Is Julia, and Why It Matters?](https://pabloagn.com/blog/what-is-julia-and-why-it-matters/), we discussed why Julia is so relevant today, and made some comparisons between other similar languages such as Python and R. We also mentioned some of its main characteristics and features, and concluded with some next steps in order to get started programming on Julia. 

In this Blog Article, we'll install Julia along with an awesome [VS Code](https://pabloagn.com/technologies/vs-code/) extension that will make programming easier for us. We'll also take a look at two notebook environments:  [`Pluto.jl`](https://pabloagn.com/technologies/pluto/), a great Julia-specific notebook environment, and [JupyterLab](https://pabloagn.com/technologies/jupyter-lab/). We'll set up an environment, install some packages, and cover several practical examples, where we will perform a general overview of Julia's main functionalities. We will close this segment by giving some recommendations on how to use Julia as well as next steps for those interested in this exciting, bleeding-edge programming language.

We'll be using Julia scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/julia-for-beginners). Datasets can also be found in the [`datasets`]() folder inside the repo.

---

# Table of Contents

- What to expect
- Installation
	- Julia
	- VS Code
	- Julia VS Code extension
- Configuring the JuliaMono Typeface
- The Julia REPL
- Creating a Working Environment from the REPL
- Installing packages using pkg from the REPL
- Getting familiar with the VS Code extension
- Getting familiar with JupyterLab
- Getting familiar with Pluto.jl
- Basic syntax
	- Comments
	- Variables
	- Mathematical operators
	- Flow control
		- Logical operators
		- For loop
		- While loop
	- Functions
- Data structures
- Linear algebra
- Data processing
- Multiple dispatch
- Measuring performance
- More useful libraries
- Next steps
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# What to expect
This segment will heavily rely on VS Code since it's the IDE that is currently getting the most support. Some time ago, [Juno](https://junolab.org/) was also well maintained, but efforts have now been transferred entirely to the VS Code extension. We will also use a Julia-specific notebook environment called `Pluto.jl`, as well as JupyterLab. We will be using Microsoft Windows, but a similar installation process applies to other platforms such as macOS & Linux. Although Julia is a fairly new language and doesn't enjoy the vast IDE support that Python has (*yet*), we have limited options, but the options that do exist, are fantastic and well maintained.

Also, we'll assume there is at least some knowledge or background in some programming language since Julia, despite being simple, can get complex quickly; Python should do just fine, since they're very similar syntaxis-wise.

We will not explore all of Julia's functionalities in a rigorous way since there is too much to cover. Instead, we will go over a comprehensive set of hands-on examples in order to start programming in Julia from the very beginning. We will be performing examples mainly targeted towards mathematical operations, linear algebra, and ultimately, Data Science. We will not go deeper into Machine Learning models since that would require at least a couple of additional articles (*in time, we will get there*).

---

# Installation

## 1. Julia
We will first install the latest stable release of the Julia programming language. For this, we can head to the official [Julia Lang website downloads page](https://julialang.org/downloads/). We will select the *Windows 64-bit (installer)*. Once we have it, we'll run the executable and follow the shown steps.

It's important to add Julia to `PATH`, since this will ensure we can start the Julia REPL directly from our terminal without the need to specify the whole absolute path for the executable.

If for some reason we missed this step, it's perfectly fine. We can simply follow the steps below:
1. Open Windows Run by using <kbd>Windows Key</kbd> + <kbd>R</kbd>.
2. Type `rundll32 sysdm.cpl,EditEnvironmentVariables` and hit <kbd>Enter</kbd>.
3. Head to user variables.
4. Find the `Path` variable.
5. Click *Edit*, and then click *New*. 
6. Depending if the installation was performed using administrator permissions or not, we will need to find the Julia executable either in `C:\Program Files (x86)\Julia-1.8.3\bin`, or `C:\Users\ourusername\AppData\Local\Programs\Julia-1.8.5\bin`.
7. Copy the corresponding absolute path and paste it directly in the new `Path` entry.
8. Click *OK* twice.
9. make sure that Julia was added to `Path` by opening the Windows Terminal and typing `Julia`. If everything went smoothly, this command should open the Julia REPL. We can verify this by typing `VERSION` inside the REPL. This should return the version we installed.

## 2. VS Code
If we don't yet have VS Code installed, we can get it from the [official downloads page](https://code.visualstudio.com/download). We need to select the Windows 8, 10, 11 executable and wait for it to download. When the installation is complete, we can verify by opening the Visual Studio Code application directly from the Windows start menu. A detailed configuration guide for VS Code is out of the scope of this article, but can be consulted in the [VS Code official documentation site](https://code.visualstudio.com/docs).

## 3. Julia VS Code extension
Once we have Julia and VS Code installed, we will proceed to install the Julia VS Code Extension:
1. Open VS code and head to the Extensions menu located in the left panel. We can also open the Extensions menu by using the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd>, or by opening the command palette by typing <kbd>F1</kbd> and searching for *Extensions: Install Extensions*.
2. We will then search for Julia which is maintained by *julialang*, install it, and enable it. We can also get the extension by directly using [this link](https://marketplace.visualstudio.com/items?itemName=julialang.language-julia).

Now that everything's in place, we're ready to start configuring our working environment.

---

# Configuring the JuliaMono Typeface
We mentioned the JuliaMono typeface in the last Julia article because it fits perfectly with Julia's scientific philosophy and syntactic style. We will install the font family and make some ligature adjustments so that we have exactly what we want.

To begin, we will head to the [official JuliaMono Typeface website](https://juliamono.netlify.app/). There, we will see all the documentation available for this package.

1. Download the font by heading to the [`cormullion/juliamono`](https://github.com/cormullion/juliamono) repository.
2. Look for the `juliamono-ttf.zip` file and download it.
3. Extract the `.zip` file contents.
4. Open the Fonts menu by using <kbd>Windows Key</kbd> + <kbd>R</kbd>, and typing fonts.
5. Select and drag all the extracted `.ttf` files to the *Fonts* folder and wait for installation to conclude.
6. Once we have the fonts installed, we will head to VS Code, open the command palette with <kbd>R</kbd>, and look for *Preferences: Open Settings (UI)*.
7. We will then search for the *Font Family* option, and locate the *Editor: Font Family* setting.
8. We will change whichever font we had previously designated for `JuliaMono` (*no spaces in between*).
9. We will then close the settings, and open the VS Code command palette again. We will now search for Preferences: Open User Preferences (JSON)
10. We will be presented with a JSON file which handles user-wide VS Code configuration parameters.

Depending if we have already configured something beforehand, we will be presented with different settings. We will need to add an additional JSON entry called `editor.fontLigatures`. Font ligatures are glyphs that combine the shapes of certain sequences of characters into a new form that make for a more harmonious reading experience. A common example is the *fi* ligature, which combines a lowercase *f* and a lowercase *i* into a single glyph so that the shoulder of the *f* doesn’t clash with the dot of the *i*.

The JuliaMono typeface has a selection of ligatures we can choose to enable or not, depending on out specific taste. For the full set of ligatures, we can head to [cormullion's blog](https://cormullion.github.io/pages/2020-07-26-JuliaMono/#contextual_and_stylistic_alternates_and_ligatures). There, we will be presented with all the options we can add, along with some examples.

We will have to select the ligature codes we're interested in, and set them in our user configuration file we previously opened:

```JSON
"editor.fontLigatures": "'zero', 'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'ss07', 'ss08', 'ss11', 'ss12', 'ss13', 'ss14', 'ss15', 'ss20'"
```

We can now save our JSON file and close it.

---

# The Julia REPL
The Julia REPL (*Read-Eval-Print-Loop*) is Julia's shell, which we'll be using extensively in order to configure our environment and download packages.

We can access the REPL using two methods:
- By calling it from PowerShell
- By using it from within VS Code

For opening it in PowerShell, we can simply type Julia:

##### **Code**
```PowerShell
julia
```

We will be presented with the Julia logo, as well as the version we're using and some additional documentation information:

##### **Output**
```
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.8.3 (2022-11-14)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |
```

We can exit the Julia REPL by typing `exit()`.

---

# Creating a Working Environment from the REPL
The first thing we'll do before we install our packages, is set up a working environment similar to a Python virtual environment. For this, we will head to our working folder:

##### **Code**
```PowerShell
cd computer-science/julia-for-beginners
```

We will then access the Julia REPL and use the right bracket <kbd>]</kbd> to access Julia's `pkg` package manager. This will change the prompt and tell us which Julia version we're currently using:

FIGURE 01

We will then type `generate` followed by our `project_name`:

##### **Code**
```Julia
generate project_name
```

##### **Output**
```
Generating  project julia_project:
	julia_for_beginners\Project.toml
	julia_for_beginners\src\julia_project.jl
```

This will create our environment folder containing two files:
- `Project.toml` will contain the environment `name`, the environment `UUID`, the `author`, and the project version (*not to be confused with the Julia version we're using*)
- `julia_for_beginners.jl` will be our main project file (*Julia files have the `.jl` extension*). If we open our file, we can see that we have some information already there:

##### **Output**
```
module julia_project
greet() = print("Hello World!")
end # module julia_project
```

We can then head back to VS Code, select *File*, *Open Folder*, and select our environment folder. We can make sure that we're using the correct environment by opening the VS Code command palette and selecting the *Julia: Change Current Environment* option. this will display all the Julia environments we have currently set up. We can just select the environment name we just created, and it will be set as default for this folder automatically (*if it has not already done so*).

We can make a simple test by opening our `julia_project.jl` file, deleting the existing contents, typing some code, and executing it:

##### **Code**
```Julia
println("This is our first Julia Project!!")
```

##### **Output**
```
This is our first Julia Project!!
```

We can then proceed to install some packages.

---

# Installing packages using pkg from the REPL
Installing packages in Julia is extremely simple. We can directly use the `pkg` package manager from the Julia REPL by following the steps we mentioned earlier.

We may notice that once we're inside `pkg` and inside our project folder, we see that the environment is not active by looking at the left prompt. Before installing our packages, we must activate our environment, else the packages will get installed on the default version and not in the environment we want. For this, we will type the following inside `pkg`:

##### **Code**
```Julia
activate .
```

##### **Output**
```
Activating new project at `C:\Users\username\Documents\computer-science\julia-for-beginners`
```

We are now inside our environment and ready to start installing the packages we'll use throughout this segment.

To install a new package, we can use the following syntax:

##### **Code**
```Julia
add DataFrames
```

##### **Output**
```
Precompiling project...
  9 dependencies successfully precompiled in 37 seconds. 18 already precompiled.
```

Once we install our first package, a new file named `Manifest.toml` will be created. This file is important since it will contain all of the packages currently installed, along with their dependencies, UUIDs and versions.

To install multiple packages at once, we can use a Julia script which calls `Pkg` and installs the required packages. For this, we'll create a new `packages.jl` file inside our environment. We will then include the following, and run it:

##### **Code**
```Julia
pkgs = ["DataFrames", "Symbolics", "Plots", "CSV", "Pluto", "SparseArrays", "LinearAlgebra", "DifferentialEquations", "Distributions", "OhMyREPL", "BenchmarkTools", "IJulia"]

using Pkg

Pkg.add(pkgs)
```

The following packages will be installed:
- `DataFrames`
- `Symbolics`
- `Plots`
- `CSV`
- `Pluto`
- `SparseArrays`
- `LinearAlgebra`
- `DifferentialEquations`
- `Distributions`
- `OhMyREPL`
- `BenchmarkTools`
- `IJulia`

This will take some time, since Julia first needs to download the packages if we still don't have them in our local machine and the precompile them. This is another way of using the `Pkg` library; calling it from inside a Julia script instead of installing from `pkg` using the REPL.

In the end, we should get a similar output:

##### **Output**
```
66 dependencies successfully precompiled in 235 seconds. 396 already precompiled.
```

We can test that our required packages were installed by closing the `packages.jl` script, going back to our `julia_project.jl` file, and loading a couple of random package bu using the `using` command:

##### **Code**
```Julia
using DataFrames
using Plots
using LinearAlgebra

x = range(0, 10, length=100)
y = sin.(x)
plot(x, y)
```

If everything went well, the plot should appear on a new window. It can also be accessed by heading to the Julia Extension menu in the left panel, and expanding the *PLOT NAVIGATOR* menu. we should have our first plot figure `plot_01` there. We can click on it and it will display.

##### **Output**

PLOT_1

---

# Getting familiar with the VS Code extension
Julia's VS Code extension offers multiple functionalities. We can open a Julia REPL that already has our environment activated, by open the VS Code command palette and selecting *Julia: Start REPL*. We can confirm that we're using our current environment by entering into `pkg` by using the right bracket <kbd>]</kbd>; our environment will display on the REPL prompt.

We can directly run a script in the current environment REPL by using the <kbd>ctrl</kbd> + <kbd>F5</kbd> key combination. To clear our REPL we simply use the <kbd>ctrl</kbd> + <kbd>l</kbd> key combination. We can also directly input commands into the environment REPL and they will run.

If we would like to run a single code selection, we can select the code we'd like to run, and use the <kbd>ctrl</kbd> + <kbd>shift</kbd> key combination. This is very useful since we don't have to run the entire script, as previously defined variables will not get deleted upon execution.

We can view our workspace variables by heading to the Julia menu in the left panel, expanding the *WORKSPACE* tab, and expanding the *Julia REPL* tab. This tab will show us all the imported packages for the current session, as well as all the defined variables.

---

# Getting familiar with JupyterLab

---

# Getting familiar with Pluto.jl

---

# Basic syntax

## 1. Comments

## 2. Variables

## 3. Mathematical operators

## 4. Flow control

### 4.1 Logical operators

### 4.2 For loops

### 4.3 While loops

## 5. Functions

---

# Data structures

---

# Linear Algebra

---

# Data processing
For this section, we'll be using some external resources. We will download the [Goodreads-books](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) dataset by [SOUMIK](https://www.kaggle.com/jealousleopard) on Kaggle. The `.csv` dataset is roughly 1.5 MB.

We will then save our `books.csv` file to a new folder inside our project environment, called `datasets`.

## 1. Reading data into a DataFrame
As with Python, we can load files directly into DataFrame objects by using the `DataFrames` & `CSV` packages.

Since we already have those installed, we can simply load them into our current session:

##### **Code**
```Julia
using CSV, DataFrames
```

We can then read our `books.csv` file:

##### **Code**
```Julia

```

---

# Multiple dispatch

---

# Measuring performance

---

# More useful libraries


## 1. Data processing libraries

## 2. Linear Algebra libraries

## 3. Data Science libraries

## 4. Optimization libraries

----

# Next steps

---

# Conclusions

---

# References
- [Talk Julia, Setting Up VS Code for Julia](https://www.youtube.com/watch?v=KesuPOlBB_o)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.