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

    # Variable rebinding
    myvar1 = 3
    IO.puts("Original variable: #{myvar1}")
    myvar1 = myvar1 + 3
    IO.puts("New variable with same label: #{myvar1}")

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

    # Inspect with explicitly defined type (avoids printing mistakes)
    mylist = [1, 2, 3, 4]
    IO.inspect(mylist, label: "Inspect explicitly defining types inside sequence", charlists: :as_lists)

    # Puts
    IO.puts("Puts: #{mylist}")

    # Puts with inspect method inside string interpolation
    mylist = [1, 2, 3, 4, 5]
    IO.puts("Puts with inspect method: #{inspect mylist}")

    # IO.write

    # Define atoms
    myvar1 = :moon
    myvar2 = :sun

    # Write without new line characters
    IO.write("Under the light of the #{myvar1}")
    IO.write("Without the heat of the #{myvar2}")

    # Write including new line characters
    IO.write("Under the light of the #{myvar1}\n")
    IO.write("Without the heat of the #{myvar2}\n")

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
    # Data Types - Atoms
    # --------------------



    # --------------------
    # Data Types - Lists
    # --------------------

    # Define a list
    mylist = [1, 2, 3, 4, 5]
    IO.inspect(mylist, label: "A list of integer values")

    # Concatenating lists

    # Define two lists of atoms
    mylist1 = [:jupyter, :neptune, :mars]
    mylist2 = [:earth, :sun, :moon]

    # Concatenate the two lists
    mylist3 = mylist1 ++ mylist2
    IO.inspect(mylist3, label: "A concatenated list")

    # Insert elements using List.insert
    mylist3 = List.insert_at(mylist3, 6, :saturn)
    IO.inspect(mylist3, label: "Inserted atom at index 6 using insert_at")

    # Subtract items from list
    mylist4 = mylist3 -- mylist1
    IO.inspect(mylist4, label: "Subtracting lists")

    # Verify if item is on list
    IO.puts("Verify if item is in list: #{:neptune in mylist4}")

    # Get head (index 0) and tail (index 1 to -1)
    [head | tail] = mylist4
    IO.puts("Head and tail of list: #{inspect head}, #{inspect tail}")

    # Remove items from list using value
    IO.puts("Remove item using value: #{inspect List.delete(mylist4, :saturn)}")

    # Remove items from list using index
    IO.puts("Remove item using index: #{inspect List.delete_at(mylist4, 0)}")

    # Get first item from list
    IO.puts("Get first item using 'first': #{inspect List.first(mylist4)}")

    # Get last item from list
    IO.puts("Get last item using 'last': #{inspect List.last(mylist4)}")

    # Define list containing key value tuples
    mylist = [home: :earth, closest: :mercury, farthest: :neptune]
    IO.puts("Key - value pairs in list: #{inspect mylist}")

    # --------------------
    # Data Types - Tuples
    # --------------------

    # Define a tuple
    mytuple = {1, 2, 3.0, :mars}
    IO.inspect(mytuple, label: "A tuple containing different types")

    # Perform operations on a tuple

    # Append value
    mytuple = Tuple.append(mytuple, "hello")
    IO.inspect(mytuple, label: "A tuple with appended value")

    # Index tuple
    IO.puts("Indexing on 2: #{elem(mytuple, 2)}")

    # Get tuple size
    IO.puts("Tuple size: #{tuple_size(mytuple)}")

    # Remove item at index
    mytuple = Tuple.delete_at(mytuple, 0)
    IO.inspect(mytuple, label: "A tuple with first value removed")

    # Insert item at index
    mytuple = Tuple.insert_at(mytuple, 1, :jupyter)
    IO.inspect(mytuple, label: "A tuple with atom inserted at index 1")

    # Create a tuple with repeating values (duplicate neptune seven times)
    mytuple2 = Tuple.duplicate(:neptune, 7)
    IO.inspect(mytuple2, label: "A tuple with repeating atoms")

    # Pattern matching with tuples (assign multiple variables in a single line)
    {x, y, z} = {13, 21, 3}
    IO.puts("Multiple variable assignment: #{x}, #{y}, #{z}")


    # --------------------
    # Data Types - Maps
    # --------------------

    # Define a map using strings
    mymap1 = %{"Charles" => "Dickens",
               "Oscar" => "Wilde",
               "Jane" => "Austen",
               "Marcel" => "Proust"}

    IO.puts("A map of strings: #{inspect mymap1}")

    # Define a map using atoms
    mymap2 = %{charles: "Dickens",
                oscar: "Wilde",
                jane: "Austen",
                marcel: "Proust"}

    IO.puts("A map of atoms: #{inspect mymap2}")

    # Methods for map of strings

    # Index by key using get
    IO.puts("Index by key using get (Charles): #{Map.get(mymap1, "Charles")}")

    # Index by key using square brackets
    IO.puts("Index by key using square brackets (Charles): #{mymap1["Charles"]}")

    # Insert element using put_new
    mymap3 = Map.put_new(mymap1, "Virginia", "Woolf")
    IO.puts("Insert element using put_new (Virginia => Woolf): #{inspect mymap3}")

    # Methods for map of atoms

    # Index by key using dot . (Cannot use this method if we have upper-case keys)
    IO.puts("Index by key using dot . (Charles): #{inspect mymap2.charles}")




    # Declare a range
    myrange = 1..100





    # --------------------
    # Logical Operators
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

    # Logical comparisons

    # Define integers
    myint1 = 14
    myint2 = 15
    myint3 = 29

    # Compare conditions
    IO.puts("Less than: #{(myint1 <= myint2) and (myint1 <= myint3)}")
    IO.puts("Greater than (or): #{(myint2 >= myint1) or (myint2 >= myint3)}")
    IO.puts("Greater than (or, not): #{(myint2 >= myint1) and not(myint2 >= myint3)}")

    # Compare boolean values
    mybool1 = true
    mybool2 = false

    # Compare conditions
    IO.puts("True and True: #{mybool1 and mybool1}")
    IO.puts("True and False: #{mybool1 and mybool2}")
    IO.puts("True or True: #{mybool1 or mybool1}")
    IO.puts("True or False: #{mybool1 or mybool2}")
    IO.puts("Not True: #{not(mybool1)}")
    IO.puts("Not False: #{not(mybool2)}")

    # --------------------
    # Flow Control (Conditional constructs)
    # --------------------

    # If else
    # Define some variables
    myvar1 = 14
    myvar2 = 196

    # If else
    if :math.sqrt(myvar2) == myvar1 do
      IO.puts("#{myvar1} is the square root of #{myvar2}.")
    else
      IO.puts("#{myvar1} is not the square root of #{myvar2}.")
    end

    # Define some variables
    myvar1 = 14
    myvar2 = 196

    # Unless else
    unless (:math.sqrt(myvar2) == myvar1) and (rem(myvar2, 2) == 0) do
      IO.puts("Either #{myvar1} is not square root of #{myvar2} or #{myvar2} is an odd number.")
    else
      IO.puts("#{myvar1} is the square root of #{myvar2} and #{myvar2} is an even number.")
    end

    # Cond
    # Define some variables
    myvar1 = 14
    myvar2 = 196

    cond do
      # First case
      (:math.sqrt(myvar2) == myvar1) and not(rem(myvar2, 2) == 0) -> IO.puts("Case 1: #{myvar1} is the square root of #{myvar2}.")

      # Second case
      rem(myvar2, 2) == 0 and not(:math.sqrt(myvar2) == myvar1) -> IO.puts("Case 2: #{myvar2} is an even number.")

      # Third dcase
      (:math.sqrt(myvar2) == myvar1) and (rem(myvar2, 2) == 0) -> IO.puts("Case 3: #{myvar1} is the square root of #{myvar2} and #{myvar2} is an even number.")

      # Fourth case
      not(rem(myvar2, 2) == 0) and not(:math.sqrt(myvar2) == myvar1) -> IO.puts("Case 4: #{myvar1} is not the square root of #{myvar2}, and #{myvar2} is an odd number.")

      # Default case
      true -> IO.puts("Case 5: There was a problem since none of the conditions were met.")
    end

    # Case
    # Define a target variable
    myvar1 = 14

    # Define cases
    case myvar1 do
      14 -> IO.puts("Number is 14")
      15 -> IO.puts("Number is 15")
      16 -> IO.puts("Number is 16")
      _ -> IO.puts("No match among options for number")
    end

    # --------------------
    # Functions - Anonymous Functions
    # --------------------

    # Define anonymous function that exponentiates a given value
    myfun = fn (x, y) -> x**y end

    # Define variables
    x = 7
    y = 2

    # Call anonymous function
    squared_result = myfun.(x, y)

    # Print result
    IO.puts("#{x} to the power of #{y}: #{squared_result}")

    # Define the same anonymous function using short-hand notation
    myfun = &(&1**&2)

    # Call anonymous function
    squared_result = myfun.(x, y)

    # Print result
    IO.puts("#{x} to the power of #{y}: #{squared_result}")

    # Define a function where we do not know the number of expected parameters
    myfun = fn
      # If parameters are x and y, exponentiate
      {x, y} -> x**y

      # If parameters are x, y, and z, calculate product
      {x, y, z} -> x * y * z

      # If parameters are none, return nil
      {} -> nil
    end

    x = 7
    y = 2
    z = 3

    res_1 = myfun.({x, y})
    res_2 = myfun.({x, y, z})
    res_3 = myfun.({})

    # Print results
    IO.puts("Results (cases 1, 2, 3): #{res_1}, #{res_2}, #{res_3}")

    # --------------------
    # Functions - Named functions
    # --------------------

    # Call fun with return to stdout
    mynamedfun1()

    # Call fun with return to variable (assignment)
    myvalue2 = mynamedfun2()
    IO.puts("Value for z is: #{myvalue2}")

    # Call fun with arguments
    myvalue3 = mynamedfun3(7, 2)
    IO.puts("Value for z is: #{myvalue3}")

    # Call fun with default arguments
    myvalue4 = mynamedfun4()
    IO.puts("Value for z is: #{myvalue4}")

    # --------------------
    # Iterators - Enum
    # --------------------

    # Enumerate over lists

    # Define list of integer values
    mylist = [10, 20, 30, 40]

    # Enumerate items using Enum
    Enum.each mylist, fn item ->
      IO.puts(item)
    end

    # --------------------
    # Iterators - Recursion
    # --------------------

    # Define a list of words
    mylist = ["This", "is", "a", "list", "of", "strings"]

    # Call recursive function
    myfun(mylist)

  end

  # Function with return to stdout and no arguments
  def mynamedfun1 do
    x = 7
    y = 2
    IO.puts("Values for x and y are: #{x}, #{y}")
  end

  # Function with return to variable and no arguments
  def mynamedfun2 do
    x = 7
    y = 2
    z = x * y
  end

  # Function with return to variable and arguments
  def mynamedfun3(x, y) do
    z = x * y
  end

  # Function with return to variable and default arguments
  def mynamedfun4(x \\ 7, y \\ 2) do
    z = x * y
  end

  # Recursive function
  def myfun([head|tail]) do
    IO.puts("#{head}")

    # Calls itself with tail as reduced case
    myfun(tail)
  end

  # Base case (empty list)
  def myfun([]), do: nil


end
