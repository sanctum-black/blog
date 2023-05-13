<article class="first">
  <div class="title">
    <h1>Scala 3 for Beginners</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Scala,%20VS%20Code,%20PowerShell&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/programming-best-practices-writing-better-code/)

Scala is a strong statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. It was developed by [Martin Odersky](https://en.wikipedia.org/wiki/Martin_Odersky) & a group of computer scientists at EPFL in Switzerland.

In this Blog Article, we'll discuss some historical background regarding Scala, the main advantages & disadvantages of the language, and provide an introduction to functional programming and its main traits. We'll then go over installation & configuration using [VS Code](https://pabloagn.com/technologies/vs-code/) & the powerful [Metals](https://scalameta.org/metals/docs/editors/vscode/) extension, and creating, compiling & running projects using [sbt](https://www.scala-sbt.org/).

We'll create our first Scala project, and use it to discuss Scala's main features, general syntax, main constructs, and main types. We'll close this segment with some next steps for those interested in learning more about Scala & functional programming in general.

We'll be using Scala 3 scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/scala-3-for-beginners).

---

# Table of Contents
- What is Scala?
	- A brief historical overview
	- The foundations
- Why Scala?
	- Functional Programming
	- Object-Oriented Programming
	- Strong static typing
- What to expect
- Preparing our environment
	- Installing Scala 3 & sbt using Coursier
	- Installing VS Code
	- Installing Metals for VS Code
- Creating a new project
- Basic syntax
	- Commenting
	- Variables
		- Lazy
		- Eager
	- Optional braces
	- Optional semicolons
	- Indentation
	- Functions
	- Blocks
- Basic data types
	- Type hierarchy structure
	- Numeric types
	- Textual types
	- Boolean type
	- Unit type
	- Null & nothing types
	- Any and AnyVal types
- Control structures
	- Conditionals
	- Loops
		- while and do-while loops
		- for loop and for comprehensions
		- Iterating with collections
	- Pattern matching & extractors
	- Exception handling
	- Collections and higher-order functions
		- Higher-order functions
		- map
		- filter
		- reduce
- Type system
	- Intersection and union types
	- Opaque type aliases
	- Type lambdas
	- Type covariance & variance
- Metaprogramming
	- Macros
	- Inline methods
	- Quotes & splices
- Object-Oriented Programming
	- Classes
		- Non-abstract classes
		- Abstract classes
		- Constructors and initialization
	- Objects
	- Traits
	- Inheritance & polymorphism
		- The Liskov Substitution Principle
- Simplified implicits
	- New given/using syntax
	- Extension methods
	- Type class derivation
	- Context functions
- Enums and ADTs
	- Enumerations
		- Basic enums
		- Parameterized enums
	- Algebraic Data Types (ADTs)
		- Sealed traits and case classes
		- Match types
- Packaging
	- Understanding packages and package hierarchy
	- Declaring packages
	- Importing & using packages
- Unit testing
- Next steps
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# What is Scala?
Scala, which stands for Scalable Language, is a strong statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. It was mainly developed for data-intensive applications in mind, and is built on top of Java, which means that Scala actually compiles to Java bytecode and is executed by the **Java Virtual Machine** (*JVM*).

Scala was built with on


## 1. A brief historical overview

## 2. The foundations
Scala is built on top of Java; it uses the entire Java's typeset, as well as the JVM for compilation & execution. This means that a lot of the concepts in Scala will be familiar if we are already familiar with Java or a similar language.



---

# Why Scala?


---

# What to expect
Scala leverages multiple core functionalities such as a rich type system, implicits, advanced pattern matching, powerful abstraction capabilities, and much more, to execute in a safely and highly-performant manner. However, this makes Scala a difficult language to learn, even when discussing introductory topics.

Because of this, we must set realistic expectations: Scala takes time getting used to, since the way of thinking for writing proper Scala code is different to other languages; it elegantly combines functional & OOP to create powerful abstractions; this means that we might have to think of how to approach problems in a different way.

## 1. The Scala way of thinking
We can, of course, write Scala code as if it were Python (*with some exceptions, of course*), but we would not be leveraging the full power that this language has in store for us. In order to properly write a Scala application, we must think the Scala way.

This encompasses one main rule of thumb: Scala seamlessly combines two [programming paradigms](https://pabloagn.com/blog/programming-paradigms-explained/), while enforcing the key components of each one, unlike other languages that can be though of as more "*relaxed*":
- **Functional**: Immutability, higher-order functions, pattern matching, for comprehensions, collections, and functional transformations.
- **Object-Oriented**: Classes and objects, traits, inheritance and polymorphism, and encapsulation.

So, what does this mean? Well, in practical terms, the Scala way of thinking can be summarized in six core concepts:

### 1.1 Embracing immutability
It's easy to reassign variables as we write our code, but this takes a significant hit on compile-time, execution performance, and safety. Thinking in terms of immutability forces us to be creative when approaching problems: one excellent example is using recursion in favor of loops.

### 1.2 Using pattern matching and deconstruction
Pattern matching can be though of as the more powerful brother of if-else statements: this technique can be used for checking types, and deconstructing complex data structures.

### 1.3 Adjusting to a type-driven development
If there's one fundamental aspect that can some take time getting used to when coming from other dynamically-typed languages, is type-driven development. It lets us think of our code in a less ambiguous manner; we don't have to guess the expected input & output types in a function, because we closely delimit the rules of what can and cannot be done.

For this, we can use multiple techniques such as type annotations, type inheritance, bounds, and higher-kinded types.

### 1.4 Favoring composition over inheritance
Although Scala supports inheritance, it encourages the use of composition and traits to promote code reuse and modularity.


### 1.5 Using powerful abstractions
Scala enables the creation of powerful abstractions, such as type classes, implicit conversions, and context bounds. While Python has some similar features, such as decorators and context managers, Scala's features are more versatile and expressive.


### 1.6 Taking advantage of concurrency and parallelism
This one is not applicable to all Scala applications, but is one characteristic deeply rooted in the Scala ecosystem. It provides excellent support for concurrent and parallel programming through libraries like [Akka](https://akka.io/), [Spark](https://spark.apache.org/), [Cats Effect](https://typelevel.org/cats-effect/), and [Monix](https://monix.io/). This differs from Python, which has the **Global Interpreter Lock** (*GIL*) that can limit parallelism.

### 1.7 Unit testing
Unit testing is relevant in most modern programming languages, but is particularly prevalent in Java & Scala: it ensures that individual units of code (*such as functions, methods, or classes*) work correctly and helps maintain code quality, catch regressions, and improve the overall robustness of the software.

Scala has an entire ecosystem dedicated to unit testing, something we might have not done extensively in other languages; we can design & build entire test suites that, thanks to Metals, are extremely easy to execute and debug.

## 2. Versioning and IDEs
Also, we'll be using VS Code along with the Metals extension for this segment. However, there are more options for writing Scala code:
- [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [ScalaIDE for Eclipse](http://scala-ide.org/)
- [GNU Emacs](https://www.gnu.org/software/emacs/)
- [Vim-Scala](https://github.com/derekwyatt/vim-scala)
- [NetBeans](https://netbeans.apache.org/)
- [Atom](https://github.com/atom)

Although we can also use Scala 2 for some of the examples covered in this segment, it's best to use Scala 3, since the latter contains a wide variety of powerful improvements over Scala 2.

---

# Preparing our environment
Although environment setup in Scala is not as straightforward as in other languages, we have some great tools to aid us in the process: we will make sure to have the following components ready before starting to write code:
- The **Scala 3** language.
- A Scala 3 build tool, in this case, **sbt**.
- An IDE supporting Scala 3 syntax (*in this case, **VS Code***).
- An IDE productivity tool, in this case, **Metals**.

## 1. Installing Scala 3 & sbt using Coursier
For Scala 3 installation, we'll use a special tool called `Coursier`. This tool is a package & artifact manager that will:
- Install a JVM if none is present.
- Update the `JAVA_HOME` and `PATH` environment variables.
- Add `~\AppData\Local\Coursier\data\bin` to `PATH`.
- Install the following packages:
	- `ammonite`
	- `cs`
	- `coursier`
	- `scala`
	- `scalac`
	- `scala-cli`
	- `sbt`
	- `sbtn`
	- `scalafmt`
- Download & install the **Simple Build Tool** (*sbt*).

To begin, we'll:
1. Download the [latest release of `Coursier`](https://github.com/coursier/coursier/releases) matching our operating system.
2. Execute the installer.
3. Add `Coursier` to `PATH` in case we missed it.
4. Setup our Scala environment running the following in PowerShell:

##### **Code**
```PowerShell
cs setup --jvm adopt:11
```

To verify our installation, we can use the following commands:

##### **Code**
```PowerShell
java -version
scala --version
sbt about
```

Which should print the following:

##### **Output**
```
java version "20.0.1" 2023-04-18
Java(TM) SE Runtime Environment (build 20.0.1+9-29)
Java HotSpot(TM) 64-Bit Server VM (build 20.0.1+9-29, mixed mode, sharing)

Scala code runner version 3.2.2 -- Copyright 2002-2023, LAMP/EPFL

This is sbt 1.8.2
```

Now that our installation is complete, we can install our IDE.

## 2. Installing VS Code
If we don't yet have VS Code installed, we can get it from the [official downloads page](https://code.visualstudio.com/download). We need to select the Windows 8, 10, 11 executable and wait for it to download. When the installation is complete, we can verify by opening the Visual Studio Code application directly from the Windows start menu. A detailed configuration guide for VS Code is out of the scope of this article but can be consulted on the [VS Code official documentation site](https://code.visualstudio.com/docs).

## 3. Installing Metals for VS Code
Once we have Scala 3, sbt, and VS Code installed, we will proceed to install the Metals VS Code Extension:
1. Open VS code and head to the Extensions menu in the left panel. We can also open the Extensions menu by using the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd> or by opening the command palette by typing <kbd>F1</kbd> and searching for *Extensions: Install Extensions*.
2. We will search for `Scala (Metals)`, maintained by *[Scalameta](https://scalameta.org/)*, and install and enable it. We can also get the extension using [this link](https://marketplace.visualstudio.com/items?itemName=scalameta.metals).

Now that everything's in place, we're ready to start configuring our working environment.

---

# The Scala REPL
As with many programming languages, Scala provides a **REPL** (*Read-Evaluate-Print-Loop*), a tool for evaluating expressions in Scala.

A Scala REPL can be opened from anywhere by using the following command:

##### **Code**
```Scala
scala
```

##### **Output**
```
Welcome to Scala 3.2.2 (11, Java OpenJDK 64-Bit Server VM).
Type in expressions for evaluation. Or try :help.
```

We can then input any expression we'd like to evaluate:

##### **Code**
```Scala
println("Hello Scala")
```

##### **Output**
```
Hello Scala
```

Although most of the code we'll be writing will be inside Scala files, we can also use the REPL to quickly evaluate any expression on-the-fly.

---

# Creating a new project
A typical Scala 3 generalized workflow consists of the following steps:
1. Create a project folder.
2. Create a project using sbt and a selected template (*can be external or our own*).
3. Import the main `build.sbt` file to our project.
4. Write our Scala 3 code in a file appended by the `.scala` extension.
5. Compile & run our Scala 3 source file using sbt.
6. Test our source code if we have a test suite included in our project.
7. Debug as per required.

We'll follow each step in detail.

## 1. Creating a project
The first step is to create a project folder, where our project will reside:

```PowerShell
cd Documents

New-Item -ItemType Directory -Path scala-for-beginners

cd scala-for-beginners
```

We can then create our project using a predefined template. Templates in `sbt` are pre-defined project structures or scaffolding that can be used as a starting point for new projects. Templates provide a convenient way to set up common project configurations, directory structures, and build settings.

There are several templates available for Scala `sbt`, including:
- **Basic Template:** This template provides a simple project structure with minimal configuration.
- **Giter8 Template**: Giter8 is a project templating tool that generates projects from templates hosted on GitHub. It allows us to choose from a wide range of community-maintained templates.  
- **Play Framework Template**: Play Framework is a web development framework for Scala. This template sets up a Play project with the necessary configurations and directory structure.

For this segment, we'll be using the basic template. Once we're in our project folder, we can execute the following command in PowerShell:

##### **Code**
```PowerShell
sbt new scala/scala3.g8
```

This will create a new project based on the Scala 3 seed template. It's important to use `scala3`. Otherwise, a project using Scala 2 will be created.

We will then need to provide a name for our project when prompted:

##### Code
```PowerShell
name [Scala 3 Project Template]: scala-for-beginners
```

This will create one main folder with the name of our project, as well as multiple subfolders.

## 2. The directory structure
If we take a look inside our main project folder, we'll see the following directory structure:

```
scala-for-beginners/
│
├── project/
│   ├── build.properties
│   └── plugins.sbt
│
├── src/
│   ├── main/
│   │   ├── resources/
│   │   └── scala/
│   │       └── Main.scala
│   │
│   └── test/
│       ├── resources/
│       └── scala/
│           └── MainSpec.scala
│
├── build.sbt/
├── .gitignore/
└── README.md
```

Let us explore each component in detail:
- `scala-for-beginners/`: Is the root directory of our sbt project, named after the project name.
- `project/`: Contains sbt build configuration files.
	- `build.properties`: Specifies the sbt version to be used for the project.
	- `plugins.sbt`: Contains sbt plugin dependencies for the project.
- `src/`: The source code directory, containing both main and test code.
	- `main/`: Contains the main application code and resources.
		- `scala/`: Contains the main Scala source code files.
			- `Main.scala`: A sample Scala source file (*not required to be named `Main`; it's just convention to call the file containing the main methods as `Main.scala`*).
	- `test/`: Contains the test code and resources.
		- `scala/`: Contains the Scala test source code files.
			- `MainSpec.scala/`: A sample Scala test source file.
- `build.sbt`: The main sbt build configuration file, where we define project settings, the Scala version we're using, library dependencies, and other build-related configurations. This file is extremely important, and should always be located under the root directory.
- `.gitignore/`: A sample `.gitignore` file if we're working with code versioning tools such as GitHub or GitLab.
- `README.md`: A sample `readme` file that should be included as an entry point to our project.

There are three directories/files we'll usually modify during a project development:
- `src/`: This directory is meant to be modified, and contains our source code.
- `build.sbt`: This file is intended to be modified if required.
- `.gitignore`, `README.md`: These of course are intended to be modified, since the already provided are just templates.

Apart from this base structure, there is one additional element that we'll include. For this, we will head to `scala-for-beginners/src/` and create a new folder called `worksheets`. We will then `cd` into our new directory, and create a new file called `MyExamples.worksheet.sc`; we'll see what this is in a moment.

## 3. Basic build configuration
When we created our project, a `build.sbt` file was also generated; this is the main build file for our application, and contains a structure like such:

##### **Code**
```Scala
val scala3Version = "3.2.2"

lazy val root = project
  .in(file("."))
  .settings(
    name := "scala-for-beginners",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test
  )
```

This file is intended to be modified; here, we'll be able to add dependencies, packages, and the Scala version we're using for this particular project.

Let us break this down in more detail:
- `scala3Version`: The scala version we're using for our project.
- `libraryDependencies`: The key denoting the packages we plan to install in our project. A dependency can be added by simply appending a new `key := dependency` entry:

##### **Code**
```Scala
libraryDependencies += "org.typelevel" %% "cats-core" % "2.7.0"
```

Where:
- `org.typelevel`: Is the organization or group ID of the library, typically representing the package structure. In our case, it's the group ID for the Cats library.
- `%%`: Is an `sbt`-specific shorthand that automatically appends the Scala binary version (*e.g., 3.20 for Scala 3.20*) to the library's name. This helps us fetch the correct version of the library that is compatible with our project's Scala version.
- `cats-core`: Is the library name or artifact ID. In our case, it's the core module of the Cats library.
- `%`: Separates the library's organization, name, and version in the dependency definition. It's used to build the complete dependency string.
- `2.7.0`: Is the library version we want to include in our project. It represents the specific release of the Cats library we'll be using.

## 4. Working with Scala worksheets
A couple of minutes ago, we created a new file called `MyExamples.worksheet.sc`. This file is a worksheet Scala file, and will let us evaluate Scala code snippets incrementally as if we were using the Scala REPL.

Scala Worksheets use the `.sc` extension, and unlike a typical `.scala` file, they're not compiled, and instead are run by the interpreter on real time.

Worksheet files can be located in the following directory:

```
projectname/src/worksheet/MyExamples.worksheet.sc
```

The name structure must be the following:
- Start with the parent directory name, followed by a dot.
- Include worksheet `keyword`.
- End with `.sc` extension.

Whenever we write code in the `worksheet.sc` file and save it, the Scala interpreter will automatically run the code and produce the output inside the file.

Let us write a simple line in our newly-created worksheet and check its output:

##### **Code**
```Scala
println("Hello, World")
```

##### **Output**
```
println("Hello, World")
// Hello, World
```

If there's any problem with our code, the compiler will throw an error.

## 5. Working with Scala source files
Scala files have the `.scala` extension and are compiled when we run the project if a main class exists.

We can have multiple `.scala` files with multiple classes, objects and methods inside, but there will be one main class required for each project. This class should be treated as the entry point to our application.

### 5.1 Programs
We'll see classes & objects in more detail later on, but for now, we must know that a main class can be defined using three different ways:
- Using a `Main` object with Java-like syntax.
- Using a `Main` object which extends App, and saves us the Java-like syntax.
- Using the `@main` annotation.

#### 5.1.1 Using a Main object with Java-like syntax
This method includes a `Main` object along with a `main` method sticking to Java syntax:

##### **Code**
```Scala
object Main {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
  }
}
```

If we compare this with a Java main Class & method, we can see it's very similar:

##### **Code**
```Java
public class Main {
	public static void main(String[] args){
		System.out.println("Hello, World!");
	}
}
```

This way of declaring `Main` objects is too verbose, and defeats one of Scala's purposes when compared to Java: To create a more concise language.

#### 5.1.2 Using a Main object extending App
This is a more concise version of the above, since we can effectively save the Java-like syntactic verbosity, but we still declare a `Main` object:

```Scala
object Main extends App {
  println("Hello, world!")
}
```

As we'll see later on, the `extends` keyword extends the behavior of `A` with `B`, in this case `App` with `Main`; by extending the `App` trait, we automatically get a `main` method for our application, so we don't need to define it ourselves. We can write our application's code directly within the `Main` object body, and the `App` trait takes care of executing it.

One thing to note is that when using `object Main extends App`, our application's code will be executed when the `Main` object is run. This approach was commonly used in Scala 2, but it's worth noting that the `App` trait relies on the `DelayedInit` feature, which is deprecated in Scala 3. For new Scala 3 projects, it is recommended to use the `@main` annotation to define a main method or implement a `main` method within an object, as these approaches are more concise and do not rely on deprecated features.

#### 5.1.3 Using the @main annotation
This is the more concise method, since we don't even need to define a Main object or method explicitly:

##### **Code**
```Scala
@main def hello(): Unit = {
  println("Hello Scala")
}
```

When we annotate a method with `@main`, the Scala 3 compiler automatically generates a wrapper object with a `main` method that calls our annotated method. This wrapper object serves as the entry point for our application and does not require any explicit `main` method declaration.

If we're wondering which one to use, it's really up to us to decide. However, the preferred method is the last one, since it's more concise and extremely easy to read.

## 6. Opening our project in VS Code
We will need to open our project in the root directory. This directory can be found by locating the `build.sbt` file, which will be the main build file for our project. We can then simply open VS Code, and select import build:


7392838_scala-for-beginners-01.png

###### Figure n: Import Build Prompt by metals

When we import the main build, some additional folders will be created in our root directory:

```
scala-for-beginners/
│
├── .bloop/
├── .bsp/
├── .metals/
└── plugins.sbt
```

We'll not be working directly with these folders. However, it's important to know that they belong to the Metals extension and the `sbt` compiler.

## 7. Compiling and running a Scala project
If we have our `.scala` file, we can compile it and run it using sbt:
1. Go to our project's main directory.
2. Initialize an `sbt` prompt.
3. Execute the `run` command.

This command will run inly if we have a main class associated with our project. Else, it will throw an error.

We can try this command on our `Main.scala` predefined template, which should look like such:

##### **Code**
```Scala
@main def hello: Unit =
  println("Hello world!")
  println(msg)

def msg = "I was compiled by Scala 3. :)"
```

##### **Code**
```SBT
run
```

##### **Output**
```
[info] running hello
Hello world!
I was compiled by Scala 3. :)
[success] Total time: 0 s, completed May 12, 2023, 5:34:12 PM
```

This should run our main source file, and create a new directory under our project's root folder:

```
scala-for-beginners/
│
└── target/
```

The `target/` folder contains all the information produced from the compiler on our first compile. This includes the Java Bytecode files, which are under `scala-for-beginners\target\scala-3.2.2\classes`.

Files with the `.class` extension are Java Bytecode files that can directly run on the JVM.

## 8. Working with the SBT shell
The build tool we installed earlier (*`sbt`*) provides a shell we can access in order to perform several operations on our scala project, such as compiling, executing, testing, debugging, and more. We can access the `sbt` shell whenever we're under an existing `sbt` project (*that is, under the root folder of our project*).

An `sbt` instance can be executed by using the following command:

##### **Code**
```PowerShell
sbt
```

##### **Output**
```
[info] welcome to sbt 1.8.2 (Oracle Corporation Java 11)
[info] loading project definition from C:\Users\Pablo\OneDrive\Documents\Blog\computer-science\scala-3-for-beginners\scala-for-beginners\project
[info] loading settings for project root from build.sbt ...
[info] set current project to scala-for-beginners (in build file:/C:/Users/Pablo/OneDrive/Documents/Blog/computer-science/scala-3-for-beginners/scala-for-beginners/)
[info] sbt server started at local:sbt-server-6ea3b4cc30af6310f6a2
[info] started sbt server
sbt:scala-for-beginners>
```

Any command we execute inside of this shell will be in reference to our newly-created project.

There are two main commands we'll be using extensively throughout this segment:
- `run`: Compiles and runs a main class, passing along arguments provided on the command line.
- `test`: Executes all tests.

If we have questions about any command in sbt, we can execute the following command:

##### **Code**
```SBT
help <command_name>
```

For example:

##### **Code**
```SBT
help project
```

##### **Output**
```
project

        Displays the name of the current project.

project name

        Changes to the project with the provided name.
        This command fails if there is no project with the given name.

project {uri}

        Changes to the root project in the build defined by `uri`.
        `uri` must have already been declared as part of the build, such as with Project.dependsOn.

project {uri}name

        Changes to the project `name` in the build defined by `uri`.
        `uri` must have already been declared as part of the build, such as with Project.dependsOn.

project /

        Changes to the initial project.

project ..

        Changes to the parent project of the current project.
        If there is no parent project, the current project is unchanged.

        Use n+1 dots to change to the nth parent.
        For example, 'project ....' is equivalent to three consecutive 'project ..' commands.
```

We can also consult the full `sbt` documentation [here](https://www.scala-sbt.org/1.x/docs/)

---

# Basic data types
- Type hierarchy structure
- Numeric types
	- Integers: `Byte`, `Short`, `Int`, `Long`
	- Floating-point: `Float`, `Double`
- Textual types
	- `Char`
	- `String`
- Boolean type
- Unit type
- Null & nothing types
	- `Null`
	- `Nothing`
- Any and AnyVal types
	- `Any`
	- `AnyVal`


---

# Next steps
Scala is feature-packed and has thousands of built-in more advanced functionalities. 

Checking out the [10 Advanced Programming Techniques](https://pabloagn.com/blog/10-advanced-programming-techniques/) blog, where we use Scala 3 to dive into 10 fascinating programming concepts with hands-on examples, including:
- Tail recursion
- Higher-order functions
- Currying
- Monads
- Pattern matching & extractors
- Lazy evaluation
- Implicits & type classes
- Continuation-passing style (CPS)
- Futures and Promises
- Higher-kinded types


YouTube Channels:
- **[DevInsideYou](https://www.youtube.com/@DevInsideYou)**: The 


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