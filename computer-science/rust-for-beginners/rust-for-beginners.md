<article class="first">
  <div class="title">
    <h1>Rust for Beginners</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Rust,%20VS%20Code,%20PowerShell%207&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/rust-for-beginners/)

Rust is a multi-paradigm, low-level, statically-typed, general-purpose programming language which emphasizes performance, type safety, and concurrency. Despite being a low-level language, it provides safety features that many high-level counterparts also present. Simply put, Rust has better safety standards in comparison to other low-level languages (*C, C++*), mainly in the memory management department; Rust has a robust set of garbage collection tools which include null pointer dereferencing prohibition, pointer aliasing enforcement, and much more.

Of course, Rust is still a low-level language meant to provide direct interaction with the hardware, and thus provides an unsafe counterpart also called unsafe Rust.


We'll be using Rust scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/rust-for-beginners).

---

# Table of Contents
- [To Love or Not to Love](#to-love-or-not-to-love)
- [What to expect](#what-to-expect)
- [Installation](#installation)
	- [Rust](#1-Rust)
	- Microsoft C++ Build Tools]()
	- [VS Code](#2-vs-code)
	- [Rust VS Code extension](#3-julia-vs-code-extension)

- [Next steps](#next-steps)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# To Love or Not to Love
According to recent Stack Overflow surveys, Rust has maintained itself as the most loved programming language for some years now; yes, even more loved than Python. It's sometimes thought of as a niche language, but has been steadily gaining popularity over the recent years. 


## 1. Low-level control
- It offers access to the raw bits.
- Byte-level access is risky
- Systems programming language

## 2. Garbage collection
- Memory errors often lead to security breaches.
- 

## 3. Concurrency
- At compile time, many potential concurrent processing problems are pointed out.
- Robust compiler

## 4. Asynchronous processing


## 5. Backward compatibility


## 6. Debugging
- Easy-to-understand errors.

## 7. Community & development
Rust is still a fairly new programming language. Still, people love it so much that the existing community is enthusiastic and eager to contribute to the Rust project. Even so, that they have their own name; Rustaceans.

---

# What to expect
Aaa

Additionally, the installation and configuration process will be tailored towards the Windows operating system, although the steps are similar and straightforward for other platforms. 

---

# Installation
For this segment, we will need to install three main components:
- The Rust programming language.
- Visual Studio Code.
- The Visual Studio Code Rust extension.

We will also install some packages, which will come later when we get to the package manager.

## 1. Rust
There are two main methods we can use to install the Rust programming language:
- Via the `rustup` installer.
- Via standalone installers in the form of tarballs (*`.tar.gz`*) for Unix-like environments, a Windows installer (*`.msi`*), or a macOS installer (*`.pkg`*).

We'll stick `rustup`, the recommended method in the official documentation; it has a 6-week rapid release process and supports a variety of platforms. The complete installer documentation can be found [here](https://rust-lang.github.io/rustup/).

To install Rust, we will follow the steps below:
1. Head to the [Rust language installation page](https://www.rust-lang.org/tools/install).
2. Download the 64-bit executable.
3. Run the executable.
4. Take note of the Cargo home directory displayed in the installation prompt (*usually located in  `C:\Users\username\.cargo`*).
5. Wait for the following prompt to appear: `You can uninstall at any time...`.
6. Hit <kbd>Enter</kbd>.
7. Wait for the following prompt to appear: `Rust is installed now. Great!`.
8. Hit <kbd>Enter</kbd>.
9. Open a new shell and input the following: `rustc --version`
10. If the installed `rustc` version appeared, it means the installation was successful.

If instead we got an error such as `rustc command not found`, it most probably means that the `.cargo/bin` directory was not added to the `Path` environment variable. To fix this, we will need to add it manually by following the steps below:
	1. Open the Windows run command window by typing <kbd>WIN</kbd>+<kbd>r</kbd>.
	2. Input the following: `"C:\Windows\system32\rundll32.exe" sysdm.cpl,EditEnvironmentVariables`
	4. Select `Path`.
	5. Click `Edit...`.
	6. Click `New`.
	7. Input the following: `C:\Users\username\.cargo\bin`.
	8. Click `OK`.
	9. Click `OK`.
	10. Try to execute the `rustc --version` command again.

## 2. Microsoft C++ Build Tools
In order to be able to compile Rust code, we will need to install the Microsoft C++ Build Tools. It is probable that we already have this installed. If we don't, we can follow the steps below:
1. Head to the [Microsoft Visual Studio Downloads Page](https://visualstudio.microsoft.com/downloads/).
2. On *All Downloads*, look for `build tools`.
3. Download the *Build Tools for Visual Studio 2022* installer.
4. Install the Microsoft C++ Build Tools.

## 3. VS Code
If we don't yet have VS Code installed, we can get it from the [official downloads page](https://code.visualstudio.com/download). We need to select the Windows 8, 10, 11 executable and wait for it to download. When the installation is complete, we can verify by opening the Visual Studio Code application directly from the Windows start menu. A detailed configuration guide for VS Code is out of the scope of this article but can be consulted on the [VS Code official documentation site](https://code.visualstudio.com/docs).

## 4. Rust VS Code extension
Once we have Rust and VS Code installed, we will proceed to install the Rust VS Code Extension:
1. Open VS code and head to the Extensions menu in the left panel. We can also open the Extensions menu by using the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd> or by opening the command palette by typing <kbd>F1</kbd> and searching for *Extensions: Install Extensions*.
2. We will search for `rust-analyzer`, maintained by *rust-lang.org*, install it, and enable it. We can also get the extension by using [this link](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer).

Now that everything's in place, we're ready to start configuring our working environment.

---

# Creating a project
The first thing to do after installation is create a Rust project. This is handled by the `cargo` package manager.

There are two options for creating a new project:
- Creating a new project folder.
- Using an existing folder as project folder.

If we want to create a project from scratch, we can first head to our project directory:

##### **Code**
```PowerShell
cd Projects
```

We will then initialize our project:

##### **Code**
```PowerShell
cargo new rust-for-beginners
```

Conversely, if we want to use the current directory as project folder, we can simply change directories to our target folder and initialize it as our project:

##### **Code**
```PowerShell
cd rust-for-beginners
cargo init
```

This command will create two components:
- A `src` folder: Contains our project's source code.
- A `Cargo.toml` file: Is the project's manifest and contains metadata that is needed to compile our package, such as project name and required dependencies.

Once we're at it, we can mention that the `.toml` file format is fairly popular among the Rust developer ecosystem notably being used by Cargo; it is mainly used for configuration purposes.

We can optionally install a VS Code extension that will make our life easier when dealing with this file format:
1. Open VS code and head to the Extensions menu in the left panel. We can also open the Extensions menu by using the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd> or by opening the command palette by typing <kbd>F1</kbd> and searching for *Extensions: Install Extensions*.
2. We will search for `Even Better TOML`, maintained by *tamasfe*, install it, and enable it. We can also get the extension by using [this link](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml).

This extension is backed by [taplo](https://taplo.tamasfe.dev/) and will provide TOML syntax support.

## 1. The project manifesto
If we open our `Cargo.toml` file, we will see that it contains some boilerplate metadata about our newly-created project:
- `package`: Defines a package.
	- `name`: The name of the package.
	- `version`: The version of the package (*not the Rust release*).
	- `edition`: The Rust edition.
- `dependencies`: Package library dependencies.

A `.toml` file general structure consists of sections and key-value pairs, similar to a Python dictionary; a `Cargo.toml` file section groups similar variables together, depending on their functionality.

The full set of sections and key-value pairs can be consulted [here](https://doc.rust-lang.org/cargo/reference/manifest.html).

Once we start including dependencies into our project, we will also start working with our manifesto. Once the file is generated, the `Cargo.toml` manifesto is meant to be edited by us.

## 2. Including dependencies
As we mentioned, Rust dependencies are handled by Cargo. There are three main concepts that we should be aware of:
- **Module / Struct:** A module is a way to organize code and data into logical units. A module can contain functions, structs, enums, constants, types, and other modules.
- **Crate:** A crate is a compilation unit in Rust that produces a binary or a library. It contains one or more modules that define functions, structs, enums, traits, and other Rust language constructs. A crate can be compiled into a binary executable or a library that can be used by other programs.
- **Library:** A library is a special kind of crate that is intended to be used by other programs. It provides a collection of reusable code that can be linked into other Rust programs. A library can be either a dynamic library (`.so` or `.dll`) or a static library (`.a` or `.lib`). Rust libraries can be organized into modules, which are similar to namespaces in other languages.
- **Package:** A package is a set of one or more crates that are built and tested together. A package contains a `Cargo.toml` file that specifies the package's name, version, authors, dependencies, build script, and other metadata. A package can be published to the Rust package registry ([*crates.io*](https://crates.io/)) to be used by other Rust developers.

Let us head to VS Code and open our `main.rs` source file. Once we open it, we'll notice that two new items are created in our project folder:
- A `Cargo.lock` file: Contains exact information about our dependencies. It is maintained by Cargo and should not be manually edited.
- A `target` folder: Where the output of a build is stored.
	- A `debug` folder: Where the debug build is stored.
	- A `.rustc_info.json` file: Contains metadata about the compilation process and the target platform for which the code was compiled.
	- A `CACHEDIR.TAG` file: Marks a directory as a cache directory. Tools that recognize the signature inside this file will treat the directory as a cache directory and may take appropriate action, such as excluding it from backups or indexing.

We'll discuss these files & folders in more detail as we move on. For now, we will focus on the `main.rs` file.

We will start by importing the following modules into our main file:
- `std::io`: Standard input/output module.
- `std::io::{Write, BufReader, BufRead, ErrorKind}`: PENDING TO EXPLAIN
- `use std::fs::File`: PENDING TO EXPLAIN
- `std::cmp::Ordering`: PENDING TO EXPLAIN
- `rand::Rng`: Random number generator module.

##### **Code**
```Rust
use std::io;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use rand::Rng;
```

If we pay close attention, we can see that we used the keyword `use` to import a library followed by a double colon `::`, the required module(s), nested imports in the case of `std::io` enclosed in curly braces `{}`, and a semicolon `;` termination.

We can also see that two alerts pop up:
- An unused import alert for `std::io`: Rust knows that we have not used the module in our code, hence it raises an alert.
- An unresolved import for `rand`: We have not specified a version for the `rand` library, hence Rust raises an error.

The first alert does not require further action; we will eventually make use of this module. For the second one, we will head to our `Cargo.toml` manifesto and include the library version under `[dependencies]`:

##### **Code**
```Rust
[dependencies]
rand = "0.8.5"
```

Once we do this, the error should disappear.

## 3. The main function
As we will see later on, every executable Rust program requires a `main` function. The main function serves as the entry point to our program.

Whenever we create a new Rust project, this main function will be written by default in our `main.rs` file:

##### **Code**
```Rust
fn main() {
    println!("Hello, world!");
}
```

If we leave this as is, our program will simply print `Hello, world!` to `stdout`.

## 4. Compiling the project
Compiling and running a Rust project can be done using Cargo, and consists of 3 main steps:
- Navigate to the project directory.
- Build the project.
- Run the project.

##### **Code**
```PowerShell
# Navigate to the project directory
cd rust-for-beginners

# Build the project
cargo build

# Run the project
cargo run
```

If the project was built successfully, we'll get the build confirmation as well as the string from our `println!()` statement inside our `main` function:

##### **Output**
```
Compiling rust-for-beginners v0.1.0 (C:\Users\username\Documents\rust-for-beginners)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s

Hello, world!
```

 Else, we'll get a build error:
 
##### **Output**
```
Compiling rust-for-beginners v0.1.0
error: Compilation Error Message
```

---

# Commenting
Comments are fragments of code that are not included for execution during built and running. There are multiple ways to comment in Rust, although we will only review the two most used:
- **Line Comment:** Single line.
- **Block Comment:** Multiline.

## 1. Line comment
We can comment a single line by prepending our comment with a double slash `//`:

##### **Code**
```Rust
// This is a single line comment.
// Which can also be continued in the next line.
```

## 2. Block comment
We can comment a block by enclosing our comment in slash asterisk symbols `/* */`:

##### **Code**
```Rust
/*
This is a multiline comment
where we can include multiple lines
without having to comment each line.
*/
```

---

# Pointers, references and ownership
Before we dive any deeper, it's worth spending some time understanding what pointers are and how memory, ownership and references work in Rust. This is because these concepts are key in understanding not just Rust's architecture, but any low-level language such as C and C++, plus, it will save us a lot of frustration when we get to variables and data types.

## 1. Pointers
Formally, a pointer is a derived data type that can store the memory address of other variables. It allows us to manipulate and reference data stored in memory by directly accessing its location in memory.

Let us represent a generic block of memory using an array-like structure:

| Address | Value    |
| ------- | -------- |
| 0x0000  | 01100110 |
| 0x0001  | 00100001 |
| 0x0002  | 10110100 |
| 0x0003  | 11001010 |
###### *Figure N: Representation of A Memory Block using An Array-Like Structure*

Where:
- The **address** is the location inside the memory block.
- The **value** is the data that is stored at that particular address.

In this example, the memory block contains four consecutive memory locations starting at address 0x0000. Each memory location stores a byte of data represented by a sequence of 8 bits. The values in this example are binary values, but they can also be represented in hexadecimal or decimal notation.

If we convert our binary sequences to decimal numbers, we get the following:

| Address | Value    |
| ------- | -------- |
| 0x0000  | 102 |
| 0x0001  | 33 |
| 0x0002  | 180 |
| 0x0003  | 202 |
###### *Figure N: Binary Characters Converted to Decimal numbers*

If we look closer, the addresses in our memory block are simply numbers represented in hexadecimal form; the `0x` character preceding all the address values denotes we're talking about a hexadecimal value, where the number following would be the actual hexadecimal value.

To convert it to decimal, we simply solve for the following:

$$0x0001 = 0 x 16^3 + 0 x 16^2 + 0 x 16^1 + 1 x 16^0$$

Simplifying:

$$0x0001 = 0 x 4096 + 0 x 256 + 0 x 16 + 1 x 1$$

Thus, our decimal number would be 1.

Following this logic, we could define a value in our memory block to be an address; this is the definition of a pointer: a value that happens to be an address in memory.

If we substitute the value corresponding to the memory address 0x0002 for another address within the same block and convert the remaining binary representations to hexadecimal 0x notation, we would end up with the following:

| Address | Value  |
| ------- | ------ |
| 0x0000  | 0x0066 |
| 0x0001  | 0x0021 |
| 0x0002  | 0x0001 |
| 0x0003  | 0x00CA |

###### *Figure N: Memory Block Containing a Pointer at Address 0x0002, Referencing Address 0x0001, or Value 0x0021*

Now we have a pointer, but, why is this relevant? Well, in Rust we have 3 types of pointers:
- References
- Raw pointers
- Smart pointers

We'll focus on the most common type: references.

## 2. References
In Rust, a reference is a type of pointer that lets us borrow values without taking ownership of them. This means that we can include an additional layer of abstraction (*e.g., referencing a value without directly interacting with it*), which allows us to borrow values without copying them.

This can be much more efficient than making copies of large data structures, and is especially important in performance-critical code, where reducing memory usage can improve program speed and reduce resource consumption.

As we will see, references in Rust are created using the ampersand `&` operator. For example, if we want to define a reference to the `str` data type and assign it to a variable, we can use the following syntax: 

##### **Code**
```Rust
let _mystring:&str = "string";
```

Not to worry. We'll dive deeper into variable declarations when we get to variables.

## 3. Ownership
We've already seen an example of borrowing by using a data type reference (*i.e., the `str` data type has an owner, and we borrow it from that owner to define a new variable*). This concept is part of a wider idea called ownership. 

Ownership in Rust is based on the concept of a unique owner for each value. When a value is created, it is associated with a unique owner, which is responsible for managing the value's memory allocation and lifetime. The owner can be a variable, a function, or a data structure.

Apart from borrowing, we can also transfer ownership using Rust's `move` semantics; when a value is assigned to another owner, the original owner is said to have "*moved*" the value. The new owner takes over responsibility for the value's memory allocation and lifetime, and the original owner becomes invalid.

With this concept, we've also introduced another key idea in Rust: memory safety.

In short, ownership ensures that there is always exactly one owner for the value, and that the owner is responsible for managing the value's memory allocation and lifetime. When an owner goes out of scope or is no longer needed, Rust automatically frees the memory associated with the value. This ensures that Rust programs are memory safe, efficient, and free from common low-level programming errors such as [dangling pointers](https://en.wikipedia.org/wiki/Dangling_pointer), [use-after-free](https://encyclopedia.kaspersky.com/glossary/use-after-free/), and [data races](https://www.mathworks.com/products/polyspace/static-analysis-notes/what-data-races-how-avoid-during-software-development.html).

Now that we have a general understanding of pointers, references and ownership, we can discuss variables.

---

# Variables
There are a number of different variable types depending on their structure. In a general way, we use `let` to define a variable under the current scope.

We have to remember that Rust cares about unused variables; if we declare a variable and we don't reference it anywhere in our code, the compiler will throw an error, unless we prepend our variable name with an underscore `_`. This tells Rust that the defined variable is meant to be used as a placeholder, and thus the compiler will ignore it:

##### **Code**
```Rust
let _myplaceholder:i32 = 34;
let myplaceholder:i32 = 34;
```

The first declaration will not throw an error if left unreferenced, while the second one will.

We can also use underscores `_` in between digits when dealing with numeric variables in order to denote thousand separators; this will increase legibility while not having any consequence during compilation:

##### **Code**
```Rust
fn main() {
    // Using underscores as separators
    let mynum_immut = 7_000_000;
    println!("{}", mynum_immut);
}
```

##### **Output**
```
7000000
```

As expected, the value will be printed without the underscore characters.

If we recall, we installed a Rust extension for VS Code. This extension provides helpful features such as data type inference upon declaring a variable. We cannot see it directly in our code, but the extension is including the following:

##### **Code**
```Rust
fn main() {
    // Using underscores as separators
    let mynum_immut: i32 = 7_000_000;
    println!("{}", mynum_immut);
}
```

Note the `i32` specification after the name of our variable.

## 1. Immutable variables
Variables in Rust are immutable by default; when a variable is immutable, once a value is bound to a name, we can’t change that value. The reason this is default behavior, is for security purposes; we don't have to keep track of the variables ad how they change throughout our program if they cannot be changed in the first place, unless we explicitly decide to do so.

The simplest way to define a mutable variable inside a function is as follows:

##### **Code**
```Rust
let mystring_immut:&str = "Hello World";
```

Where:
- `mystring_immut` is the variable name.
- `&str` is the borrowed form of the `str` type.
- `Hello World` is the value assigned to the variable.

## 2. Mutable variables
Mutable variables can change throughout our code. The simplest way to define a mutable variable inside a function is as follows:

##### **Code**
```Rust
let mut mystring_mut:String = String::new();
```

Where:
- `mut` refers to the variable being mutable.
- `mystring_mut` refers to the variable name.
- `String` refers to the data type.
- `new()` tells Rust to create this as a new variable.

## 3. Static variables
Static variables `static` are a different type of variable in Rust.


## 4. Variable bindings

### 4.1 Mutability

### 4.2 Scope
As we have mentioned, variable bindings in Rust have a scope. Scopes are important since they indicate to the compiler when borrows are valid, when resources can be freed, and when variables are created or destroyed.

A block or block expression is a control flow expression and anonymous namespace scope for items and variable declarations.

A block can be defined by using curly brackets:

##### **Code**
```Rust

```

Variables defined inside a block using `let` will not be accessible outside of that block. However, variables defined outside a block using `let` will be accessible from within a given block.

### 4.3 Shadowing
Variables in Rust can be shadowed, meaning we can declare two variables under the same scope using the same variable name, but with different data types. 

---

# Constants
Constants in Rust are different to immutable variables in that they are computed at compilation time (*and can be used in other compile-time computation*) and hence the run time is faster, as it does need to compute it again; immutable variables are always computed at run time (*all `const` occurrences will be replaced by the value assigned on compilation*). Additionally, immutable variables are defined under the current scope (*are not defined globally*), while constants are global.

Let us elaborate further by using an example:

##### **Code**
```Rust
// Define constant outside main function
const HELLO: &str = "Constant Hello";

fn main() {
	// Print constant from inside main function
    println!("{}", HELLO);
}
```

As we might have noticed, we define a `const` using uppercase letters.

##### **Output**
```
Constant Hello
```

Conversely, if we try to do the same for an immutable variable, the compiler won't even let us declare it outside our function:

##### **Code**
```Rust
// Define an immutable variable outside main function
let mystring_immut = 7;

fn main() {
	println!("{}", mystring_immut);
}
```

##### **Output**
```
consider using `const` or `static` instead of `let` for global variables
```


---

# Printing
There are multiple ways we can use to print values in Rust. Below are the two most commonly used:
- `print!()`
- `println!()`

We might have noticed the exclamation mark `!` at the end of each statement; this is because both printing methods are macros (*we'll discuss macros later on*).

Printing a string literal in Rust can be achieved using the `print!()` macro without any additional arguments:

##### **Code**
```Rust
fn main() {
    // Print a string in same line
    print!("Hello ");
    print!("World");
}
```

##### **Output**
```
Hello World
```

This method will not include a newline at the end of each print statement, so it's sometimes best to use the `println!()` macro instead:

##### **Code**
```Rust
fn main() {
    // Print a string in newline
    println!("Hello");
    println!("World");
}
```

##### **Output**
```
Hello
World
```

However, if we would like to print other data types different than string literals, such as integer literals, float literals or variables, we need to include a string literal format argument using curly brackets `{}`, which is just a placeholder for our variable(s).

##### **Code**
```Rust
fn main() {
    // Print an integer using a string literal format argument
    println!("{}", 7);
}
```

##### **Output**
```Rust
7
```

We can add multiple placeholders, with the arguments to print separated by a comma `,`:

##### **Code**
```Rust
fn main() {
    // Multiple placeholders
    println!("The numbers are: {} and {}", 7, 4);
}
```

##### **Output**
```
The numbers are: 7 and 4
```

We can also add text with the placeholder to format our output:

##### **Code**
```Rust
fn main() {
    // Format output with additional text
    println!("The number is: {}", 7);
}
```

If we want to print variables, we can do so by including the same string literal format argument as before:

##### **Code**
```Rust
fn main() {
    let intvar = 7421;
    println!("{}", intvar);
}
```

##### **Output**
```
7421
```

---

# Data types
We mentioned that Rust is a statically-typed language. This means that all data types must be explicitly known to the interpreter before compiling. We have two options when dealing with data types:
- To explicitly define the data type.
- To let the Rust compiler fill in a default data type based on the variable's assigned value.

When working with data types in Rust, there are some core concepts we need to take into account:
- If you have a variable of some type `T`, it means that we own the data associated with `T`. If we have a variable of type `&T`, then we don't own the data, we're borrowing it.

There are 17 main data types in Rust, which can in turn be divided into six categories:

## 1. Primitive types
Primitives refer to the basic data types that are built into the language and are not defined in terms of other data types. There are four main primitive data types in Rust:
- Boolean - `bool`
- Numeric - integer `i` (*signed or unsigned*) and float `f`
- Textual - `char` and `str`
- Never - `!`

### 1.1 Boolean
The boolean type can take one of two possible values:
- `true`: Has the bit pattern `0x01`
- `false`: Has the bit pattern `0x00`

We can define a simple boolean variable:

##### **Code**
```Rust

```

#### 1.1.2 Boolean logic 
Boolean values can be operated on using boolean logic or boolean operators. There are five main boolean operators in Rust. Given two variables, `a` and `b`, we can define them as follows:
- Logical not: `!a`
- Logical or: `a | b`
- Logical and: `a & b`
- Logical xor: `a ^ b`
- Logical comparisons:
	- Equal to: `a == b`
	- Greater than: `a > b`
	- Greater than or equal to: `a >= b`
	- Less than: `a < b`
	- Less than or equal to: `a <= b`

### 1.2 Integer
As mentioned, there are signed and unsigned integer types. The main difference between the two is that:
- A signed integer can hold negative values.
- An unsigned integer can hold a larger positive value and no negative value.

An integer type can also be classified based on its minimum and maximum number of bits (*capacity*), e.g., `i8` (*signed*) will accept a number from -128 to 127, while `i16` (*signed*) will accept a number from -32,768 to 32,767.

This does not just apply to Rust, but is common to all programming languages (*its just that dynamically typed languages handle this automatically for us*) and directly related to the computer hardware and how a system stores information in memory.

Below is the complete list of signed integer data types:

| Type   | Minimum             | Maximum            |
| ------ | ------------------- | ------------------ |
| `i8`   | \-(2<sup>7</sup>)   | 2<sup>7</sup>\-1   |
| `i16`  | \-(2<sup>15</sup>)  | 2<sup>15</sup>\-1  |
| `i32`  | \-(2<sup>31</sup>)  | 2<sup>31</sup>\-1  |
| `i64`  | \-(2<sup>63</sup>)  | 2<sup>63</sup>\-1  |
| `i128` | \-(2<sup>127</sup>) | 2<sup>127</sup>\-1 |
###### [Table n: Signed integer types With their respective minimum and maximum values](https://doc.rust-lang.org/reference/types/numeric.html)

As well as their unsigned counterparts:

| Type   | Minimum | Maximum            |
| ------ | ------- | ------------------ |
| `u8`   | 0       | 2<sup>8</sup>\-1   |
| `u16`  | 0       | 2<sup>16</sup>\-1  |
| `u32`  | 0       | 2<sup>32</sup>\-1  |
| `u64`  | 0       | 2<sup>64</sup>\-1  |
| `u128` | 0       | 2<sup>128</sup>\-1 |
###### [Table n: unsigned integer types With their respective minimum and maximum values](https://doc.rust-lang.org/reference/types/numeric.html)

It's important to note that the default type for any Rust program will be `i32` (*i.e., if we define an integer numeric variable without explicitly stating its data type, the compiler will most probably suggest `i32` as its data type*).

We can define an integer variable under the current scope:

##### **Code**
```Rust
let mynum_i32:i32 = 2000;
```

We can also directly check the maximum number possible for a given data type using the following syntax:

##### **Code**
```Rust
println!("Max size for u8 is: {}", u8::MAX);
```

##### **Output**
```
Max size for u8 is: 255
```

If we try to define a variable with a data type where our value is out of its range, we will get the following error:

##### **Code**
```Rust
let mynumber:u8 = 256;
```

##### Output
```
literal out of range for `u8`
```

### 1.3 Float
Similar to integers, floating-point values can be classified by their bit size and are defined by the [IEEE 754 standard](https://en.wikipedia.org/wiki/IEEE_754). The only difference is that there are only two different types we can declare:
- `f32`: "[*binary32*](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)" type is 32 bits in size and has single precision.
- `f64`: "[*binary64*](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)" type is 64 bits in size and has double precision.

We can define a floating-point variable under the current scope:

##### **Code**
```Rust
let mynum_f32:f32 = 3.1416;
```

As with integer types, there is a default floating-point type suggested previous to compilation time; the default type for any Rust program will be `f64` (*i.e., if we define a floating-point numeric variable without explicitly stating its data type, the compiler will most probably suggest `f64` as its data type*).

We mentioned precision when discussing the floating-point types available in Rust. This is an attribute common to all floating-point types denoting the number of digits after the [radix point](https://en.wikipedia.org/wiki/Decimal_separator#Radix_point).

Single precision means that there is a limited set of possible numbers after the radix point, while double precision means more possible numbers.

More concretely, single-precision floating-point numbers provide roughly 6 to 7 significant decimal digits, while double-precision numbers provide approximately 14.

### 1.4 String
Strings are slightly different in terms of how we use them in Rust; strings and slices are only accessible via references (*borrowing*), thus when we declare a string using the `str` data type, for example, we will have to prepend our data type with an ampersand `&`.

A reference consists of a pointer into memory which cannot be changed directly by the owner of the reference, since the owner is not the actual owner of the underlying type.

There are two types of strings in Rust:
- `String`: Is stored as a vector of bytes, but guaranteed to always be a valid UTF-8 sequence.
- `&str`: Is a slice that always points to a valid UTF-8 sequence, and can be used to view into a `String`.

### 1.5 Character
A character `char` is similar to a string, the main difference the first is always four-bytes, while the latter doesn't have to be composed of just four-byte chunks.

We can declare a char under the current scope by using single quotes `''`:

##### **Code**
```Rust
let mychar:char = 'a';
```

If we try to include more than one character, we will get an error:

##### **Code**
```Rust
let mychar:char = 'ab';
```

##### **Output**
```
character literal may only contain one codepoint
Syntax Error: Literal must be one character long
```

### 1.6 Never
The never type `!` is a type with no values, representing the result of computations that never complete. Expressions of type `!` can be coerced into any other type. As of Rust 1.68.2 (*current version as of April 2023*) the `!` type can only appear in function return types.

## 2. Sequence types
There are 3 main sequence data types in Rust:
- Tuple - `( Type_1 , Type_2, Type_n )`
- Array - `[ Type ; Expression ]`
- Slice - `[ Type ]`

### 2.1 Tuple
A tuple can have members of different types, but cannot change in size.


### 2.2 Array
An array is strictly implemented; it has to be defined at compile time (*using literals*), be of a single data type, and cannot change in size.


### 2.3 Slice
A slice is a dynamically sized type representing a "*view*" into a sequence of elements of type `T`. The slice type is written as `[T]`.


## 3. User-defined types


## 4. Function types


## 5. Pointer types



## 6. Trait types

---

# Other data structures
We already discussed three sequence data types: tuple, array and slice.

Data structures or collections:
- Vector
- Hash map

---

# Operators
https://doc.rust-lang.org/book/appendix-02-operators.html

---

# Random LEFT HERE
At the beginning of this segment, we imported the `rand::Rng` random number generator module. There are multiple ways to generate random numbers in Rust, though we'll only discuss a couple.

https://www.youtube.com/watch?v=ygL_xcavzQ4

---

# Iterators
Iterators in Rust are patterns that allow sequential access to a collection of values, one at a time. They are similar in concept to iterators from other languages such as `for` and `while` loops in Python, but are defined differently.

In order to loop through a collection of values using Rust, we first have to define an iterable set, for example, by using a previously-defined array:

##### **Code**
```Rust
use std::iter;
```

##### **Code**
```Rust
// We create an array
let myarray = [27,35,40,10,19];

// We create an iterable

```

- range
- for

---
# Functions
Functions in Rust can be declared by using the following syntax:

##### **Code**
```Rust
fn myfun(args) {
    function_body;
}
```

Where:
- `args` represents the arguments we will pass to our function.
- `function_body` represents our function's content, terminated by a semicolon `;` (*content should be indented using 4 spaces*).

### 5.1 Main function
In Rust, the main function is used to signal the start of program execution and control flow throughout the program. It does not accept any arguments, and should be included as the first function in our program.

A typical main function syntax is shown below:

##### **Code**
```Rust
fn main() {
    function_body;
}
```

---

# Macros
Macros in Rust are a way of writing code that writes other code. In simpler terms, a macro expands to produce more code than the code we’ve written manually.

All macros are terminated using an exclamation mark `!`.

A simple macro example is `println!(arg)`, which prints `arg` in a newline. 

---

# User input
We can accept user inputs using the `std::io` module. The simplest way to define a user input is as follows:

##### **Code**
```Rust
use std::io;

fn main() {
    // Mutable variable
    let mut mystring_mut:String = String::new();

    // Accept user input
    io::stdin().read_line(&mut mystring_mut)
    .expect("Didn't Receive Input");
}
```

Where:
- `read_line` is a method belonging to the `std::io::BufRead` method, which reads a line of input, appending it to the specified buffer.
- `&mut` is denoting a mutable reference to our previously declared binding variable.
- `mystring_mut` is the binding variable name.
- `expect`: The `read_line` method will return a result of type `enum` (*provide a way of saying a value is one of a possible set of values*), where the result will be either `Ok` or `Err`. If the input reading fails, the `read_line` method will return `Err`, along with the error message  inside the `expect` method.

If the return value is `Ok`, the user input will be stored in our variable `mystring_mut`, which we can use in our code as with any other variable of the same type.




---

# Next steps
We covered a tiny sample of what Julia can do. This language has endless potential and can be used by many professionals and enthusiasts looking for a high-performance, bleeding-edge alternative to the current options.

Now that we know the basics of the Julia programming language, there are multiple paths we can choose to follow:
- **Data Science & Machine Learning:** [Julia for Data Scientists]() would be a great next step for those interested in using this language for big data processing & parallelization, Machine Learning algorithm design & deployment, statistical analysis, and more.
- **Optimization:** [Julia for Optimization and Learning](https://juliateachingctu.github.io/Julia-for-Optimization-and-Learning/stable/) imparted by the [Czech Technical University](https://www.cvut.cz/en/) in Prague, provides excellent introductory material for those interested in Optimization & Machine Learning techniques. 
- **Linear Algebra:** Julia stands up when performing linear algebra-related operations. There is a huge collection of packages and documentation available. A great first step would be [Basic Linear Algebra in Julia](https://www.youtube.com/watch?v=IFkQ0aB6eHs), imparted by the extremely well-versed [Dr. Jane Herriman](https://twitter.com/janeherriman).
- **Integral & Differential Calculus:** No scientific language is complete without a robust set of calculus methods, and Julia, of course, is no exception. There is a [great series of articles](https://jverzani.github.io/CalculusWithJuliaNotes.jl/) by [jverzani](https://github.com/jverzani) aiming to cover the basics of calculus using Julia, ranging from simpler undergraduate concepts to more intermediate topics.
- **Documentation:** Julia can also be used for documentation purposes. In particular, the [`Documenter.jl`](https://documenter.juliadocs.org/stable/) package offers excellent capabilities to write in [Markdown](https://pabloagn.com/technologies/markdown/) offering a simple and easy-to-understand interface.

---

# Conclusions
In this segment, we installed the Julia programming language from scratch along with Visual Studio as an IDE and the Visual Studio Julia extension as a handy tool. We also reviewed two great notebook environment options: JupyterLab and `Pluto.jl`.

Once we had our installations ready, we learned to use the Julia REPL from the Windows Terminal and from within VS Code using the Julia extension. We also learned how to create project environments, install packages within our environment, manage them appropriately, and write our first Julia program.

Finally, we introduced some of Julia's core concepts, accompanied by hands-on examples using `Pluto.jl` and `PlutoUI`.

Julia is a language that has been gaining consistent popularity throughout the last few years. It was introduced as a fresh approach to scientific programming and is sure to become a building block for aspiring Data Scientists in the near future. It has so many innovative features that it's hard to look the other way and continue using the well-established Data Science languages we have been using for several years.

Julia allows us to stop and think if what we're doing and how we're doing it is the most optimal way. It's an ambitious project that aims to change how we look at high-performance scientific computing.

One thing to consider is that Julia is fast-evolving; each iteration brings on new changes, which might be small but can also consist of a complete refactoring of base functionality. This is critical because a library that worked yesterday with a given syntax might not work the same way today. Still, this is always part of the process of any programming language, and really, the most exciting one; witnessing a group of passionate people build the foundations for the future is always inspiring.

---

# References
- [Peter Wayner, 7 reasons to love the Rust language—and 7 reasons not to](https://www.infoworld.com/article/3675391/7-reasons-to-love-the-rust-language-and-7-reasons-not-to.html)
- [Rust Official Documentation, Safe & Unsafe Rust](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html)
- https://codilime.com/blog/rust-vs-cpp-the-main-differences-between-these-popular-programming-languages/
- https://codilime.com/blog/why-is-rust-programming-language-so-popular/
- https://www.techrepublic.com/article/the-most-loved-and-most-disliked-programming-languages-revealed-in-stack-overflow-survey/
- https://www.youtube.com/watch?v=ygL_xcavzQ4
- https://forge.rust-lang.org/infra/other-installation-methods.html#rustup
- https://doc.rust-lang.org/cargo/reference/manifest.html
- https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html
- https://doc.rust-lang.org/reference/types.html
- https://blog.logrocket.com/rust-iterators-closures-deep-dive/

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.