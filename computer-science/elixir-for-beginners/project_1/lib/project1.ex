defmodule Project1 do
  @moduledoc """
  This is a module containing functions to explore the Elixir language.
  """

  @doc """
  Print hello world.
  """
  def main do
    # Our first function
    IO.puts("Hello World")

    # --------------------
    # Variables
    # --------------------
    # Define an integer
    myint = 13

    # Define a floating-point number
    _myfloat = 3.1416

    # Define a string
    _mystring = "Hello World"

    # Define a boolean
    _mybool = true

    # --------------------
    # Printing
    # --------------------
    # Print with parenthesis
    IO.puts(myint)

    # Print without parenthesis
    IO.puts myint

    # Define an integer
    myint = 13

    # Print with string interpolation
    IO.puts("The number is: #{myint}")

    # Define an integer
    myint = 13

    # Print with string concatenation
    IO.puts("The number is: " <> Integer.to_string(myint))

    # Print multiple variables using string interpolation
    myint1 = 13
    myint2 = 14
    IO.puts("Numbers: #{myint1}, #{myint2}")

    # Print multiple variables using string concatenation
    myint1 = 13
    myint2 = 14
    IO.puts("Numbers: " <> Integer.to_string(myint1) <> ", " <> Integer.to_string(myint2))

    # Print the internal representation of a value using IO.inspect
    mylist = [1, 2, 3, 4, 5]

    # Inspect
    IO.inspect(mylist, label: "Inspect")

    # Puts
    IO.puts("Puts: #{mylist}")

    # --------------------
    # Data Types - Check types
    # --------------------
    # Declare variables
    myint = 20
    myfloat = 20.13
    mystring = "Hello"
    mybool = true

    # Check if type is int
    IO.puts("Is #{myint} an integer number?: #{is_integer(myint)}")

    # Check if type is float
    IO.puts("Is #{myfloat} a floating-point number?: #{is_float(myfloat)}")

    # Check if type is string
    IO.puts("Is #{mystring} a string?: #{is_bitstring(mystring)}")

    # Check if type is bool
    IO.puts("Is #{mybool} a boolean?: #{is_boolean(mybool)}")

    # Declare atom without space
    myatom1 = :Hello

    # Declare atom with space
    myatom2 = :"Mexico City"

    # Print atoms
    IO.puts("#{myatom1}, #{myatom2}")

    # Check types
    IO.puts("#{is_atom(myatom1)}, #{is_atom(myatom1)}")

    # --------------------
    # Data Types - Strings
    # --------------------

    # Declare some strings
    mystr1 = "Elixir"
    mystr2 = "is"
    mystr3 = "awesome"

    # Get length of string
    IO.puts("Len: #{String.length(mystring)}")

    # Concatenate strings
    mystr4 = mystr1 <> " " <> mystr2 <> " " <> mystr3 <> "."
    IO.puts("Concatenated: #{mystr4}")

    # Convert to uppercase
    mystr5 = String.upcase(mystr4)
    IO.puts("Upper: #{mystr5}")

    # Go back to lowercase (downcase)
    IO.puts("Lower: #{String.downcase(mystr5)}")

    # Capitalize first characters
    IO.puts("Capitalize: #{String.capitalize(mystr5)}")

    # Check if strings are equal (value and datatype ===)
    IO.puts("Strings are equal?...#{mystr4 === mystr5}")

    # Check if string contains another string
    targetstring = "awesome"
    IO.puts("String contains #{targetstring}?: #{String.contains?(mystr4, targetstring)}")

    # Return first character
    IO.puts("First character: #{String.first(mystr5)}")

    # Index a character inside a string
    IO.puts("Second character: #{String.at(mystr5, 1)}")

    # Get substring using slice (from index 0 to 6)
    IO.puts("String slice: #{String.slice(mystr5, 0, 6)}")

    # Reverse string
    IO.puts("Reverse string: #{String.reverse(mystr5)}")

    # --------------------
    # Data Types - Ints
    # --------------------
    # Define ints
    myint1 = 14
    myint2 = 7
    IO.puts("Ints: #{myint1}, #{myint2}")

    # Arithmetic operations
    IO.puts("Addition: #{myint1 + myint2}")
    IO.puts("Subtraction: #{myint1 - myint2}")
    IO.puts("Product: #{myint1 * myint2}")
    IO.puts("Division returning int or float: #{myint1 / myint2}")
    IO.puts("Division returning int: #{div(myint1, 8)}")
    IO.puts("Remanent: #{rem(myint1, myint2)}")
    IO.puts("Exponentiation: #{myint1**2}")

    # --------------------
    # Data Types - Floats
    # --------------------
    # Define float
    myfloat1 = 1200.0
    IO.puts("Float: #{myfloat1}")

    # Define float using scientific notation
    myfloat2 = 12.0e2
    IO.puts("Float Scientific: #{myfloat2}")










    # Declare a list


    # Declare a tuple


    # Declare a range
    myrange = 1..100

    # --------------------
    # Logical (Comparison) Operators
    # --------------------
    # Define int and float
    myint = 7
    myfloat = 7.0

    # Compare values
    IO.puts("===: #{myint === myfloat}")
    IO.puts("==: #{myint == myfloat}")
    IO.puts("!==: #{myint !== myfloat}")
    IO.puts("!=: #{myint != myfloat}")
    IO.puts(">: #{myint > myfloat}")
    IO.puts("<: #{myint < myfloat}")
    IO.puts(">=: #{myint >= myfloat}")
    IO.puts("<=: #{myint <= myfloat}")


    # Call other functions
    myfun1()

  end

  def myfun1 do

  end

end
