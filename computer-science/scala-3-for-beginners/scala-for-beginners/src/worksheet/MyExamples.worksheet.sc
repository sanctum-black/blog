import mdoc.document.CompileResult.TypeError
// ----------------------
// Commenting
// ----------------------

// Single commenting

/*
Multi-line
commenting
*/

// ----------------------
// Variables
// ----------------------

// Lazy Evaluation
def mylazyvar = 21

// Eager evaluation using val
val myeagerval = 31

// Eager evaluation using var
var myeagervar = 32

// Reassign variable
myeagervar = 33

// Print final evaluation
println(myeagervar)

// ----------------------
// Printing
// ----------------------

// Declaring a simple variable
val myString = "Howdy hey"

// Using println
println(myString)
println(myString)

// Using print
print(myString)
print(myString)

// Using string interpolation

// Declaring a simple variable
val myImportantVal = 1000

// Print using string interpolation
println(s"This is one very important value: ${myImportantVal}")

// ----------------------
// Optional braces & semicolons
// ----------------------

// Declaring a function including braces & semicolons
def myFun1 = {
    7 * 7;
}

// Declaring a function omitting braces & semicolons
def myFun2 = 
    7 * 7


// ----------------------
// Indentation
// ----------------------
def myUnindentedFun(a: Int): Unit = 
println(a)

def myIndentedFun(a: Int): Unit = 
    println(a)

myIndentedFun(7)
myUnindentedFun(7)

val myUnindentedVar: Int = 
{
val a = 1
a
}

val myIndentedVar: Int = 
    {
        val a = 1
        a
    }


// ----------------------
// Functions
// ----------------------

// Declaring a function without arguments
def simpleFun = 7 * 7

// Declaring a function with arguments
def moreElaborateFun(x: Int, y: Int) = x * y

// Declaring a multi-line function
def multilineFunction(x: Int, y: Int) = 
    val myvar_1 = 14
    val myvar_2 = 7
    x + y + (myvar_1 * myvar_2)

multilineFunction(5, 5)

// ----------------------
// Anonymous Functions
// ----------------------

val myNewInt = (a: Int, b: Int) => a * b
println(myNewInt(5, 7))


// ----------------------
// Blocks
// ----------------------

// Declare a block
{
    val inside_1 = 14
    val inside_2 = 21
}

// Try to reference inside variable outside block
// inside_2

// Declare a variable using blocks
val my_extense_var = {
    val a = 5 * 4
    val b = 7 * 2
    b
}

// ----------------------
// Type declaration
// ----------------------

// Declaring a variable with its type
val myval_1: Int = 14

// Declaring a function with its type
def myfun_1: Int = 7 * 7

// Declaring a function with its type, including its arguments
def myfun_2(x: Int, y: Int): Int = x * y


// ----------------------
// Type System
// ----------------------

// Declare a Byte
val myByte: Byte = 127

// Impossible operations with Byte
// val myByte_2: Byte = myByte - 7
// val myByte_3: Byte = (myByte - 7.toByte)

// Possible operations with Byte
val myByteToInt = myByte - 7
val myByte_2: Byte = (myByte - 7).toByte

// Declare a Short
val myShort: Short = 32767

// Declare an Int with explicit type
val myIntExp: Int = 1

// Declare an Int with inferred type
val myIntInf = 1

// Declare a Long type with suffix
val myLong: Long = 9223372036854775807L

// Declare a Long type without suffix
// val myLong_2: Long = 9223372036854775807

// Declare a Float number using decimal notation
val myFloat: Float = 3.141592653589793238462643383279502884197

// Declare a Float number using scientific notation
val myFloat_2: Float = 2.102030E1

// Declare a Double number using decimal notation
val myDouble: Double = 3.141592653589793238462643383279502884197

// Declare some chars
val myChar_1: Char = 'a'
val myChar_2: Char = 'b'
val myChar_3: Char = '1'

// Perform arithmetic operations with chars
myChar_1 > myChar_2
myChar_1 < myChar_2
myChar_1 >= myChar_2
myChar_1 <= myChar_2
myChar_1 != myChar_2
myChar_1 + myChar_2
myChar_1 - myChar_2
myChar_1 * 1
myChar_2 * 1
myChar_3 * 1

// Convert Char to Int
myChar_1.toInt

// Boolean types
val myBoolTrue: Boolean = true
val myBoolFalse: Boolean = false

// AND Operator
myBoolTrue && myBoolTrue
myBoolTrue && myBoolFalse
myBoolFalse && myBoolTrue
myBoolFalse && myBoolFalse

// OR Operator
myBoolTrue || myBoolTrue
myBoolTrue || myBoolFalse
myBoolFalse || myBoolTrue
myBoolFalse || myBoolFalse

// Unit type
def myFun_3(x: Int, y: Int): Unit = 
    val a = x + y
    println(a)

myFun_3(1, 2)

// Null type



// Nothing type

def myErrorFun(x: Int): Nothing = x match {
    case x:Int => throw new IllegalArgumentException(s"{s} is not of the correct type.")
}

// myErrorFun(1)

// ----------------------
// Conditionals
// ----------------------

def getBiggest(x: Int, y: Int): Int = 
    if (x >= y) x
    else y

getBiggest(1, 2)
getBiggest(4, 1)

def checkInBetween(x: Int, y: Int, z: Int): Boolean = 
    if ((y > x) & (y < z)) true
    else false

checkInBetween(2, 3, 4)
checkInBetween(3, 2, 4)

def checkSmallest(x: Int, y: Int, z: Int): Int = 
    if ((x <= y) & (x <= z)) x
    else if ((y <= x) & (y <= z)) y
    else z

checkSmallest(1, 2, 3)
checkSmallest(5, 2, 10)
checkSmallest(1, 1, 2)

// ----------------------
// Pattern Matching
// ----------------------

// Using an anonymous function
val match_using_anonymous = (x: Int) => x match {
    case 1 => s"${x} is equals to 1"
    case 2 => s"${x} is equals to 2"
    case _ => s"${x} is neither 1 nor 2"
}

match_using_anonymous(1)
match_using_anonymous(10)

// Using a class hierarchy

// Define abstract Animal class with unimplemented methods
abstract class Animal:
    val name: String
    val age: Int
    val species: String
    def salutes: Unit

    def feedAnimal(subject: Animal): String = subject match
        case subject: Doggo => s"Here you go ${subject.name} big boy, take some bacon!"
        case subject: Human => s"Hey my friend ${subject.name}, that bacon's not for you. Hands off please!"
        case _ => "I don't know who or what you are, kindly leave my house or I'll call the police, my good sir."
end Animal

// Define Human class extending Animal
class Human(val name: String, val age: Int) extends Animal:
    val species: String = "human"
    def salutes =
        println(s"Hi, my name is ${this.name}, I'm ${this.age} years of age, and I'm a proud ${this.species}.")
end Human

// Define Doggo class extending Animal
class Doggo(val name: String, val age: Int) extends Animal:
    val species: String = "doggo"
    def salutes = 
        println(s"Woof woof!!, My name is ${this.name}, I'm ${this.age} years of age, and I'm a happy big ${this.species}.")
end Doggo

// Define a weird Animal subclass
class WeirdGuy(val name: String, val age: Int) extends Animal:
    val species: String = "weird guy"
    def salutes =
        println(s"Howdy doody, partner! I'm ${this.name}, ${this.age} olde, and I'm somewhat of a ${this.species}. Why don't ya grab yerself a cold one and sit a spell, ya hear?")

// Instanciate
val Chad = new Human("Chad", 23)
Chad.salutes

val Napoleon = new Doggo("Napoleon", 5)
Napoleon.salutes

val Skeeter = new WeirdGuy("Skeeter", 20)
Skeeter.salutes

// Declare feeding function (is not a method, since it does not belong to Animal or any of its subclasses)
def feedAnimal(subject: Animal): String = subject match
    case subject: Doggo => s"Here you go ${subject.name} big boy, take some bacon!"
    case subject: Human => s"Hey my friend ${subject.name}, that bacon's not for you. Hands off please!"
    case _ => "I don't know who or what you are, kindly leave my house or I'll call the police, my good sir."

// Feed the dog animals only
feedAnimal(Napoleon)
feedAnimal(Chad)
feedAnimal(Skeeter)

// ----------------------
// Loops
// ----------------------

// Declare a simple integer mutable variable
var y: Int = 100

// Declare a while loop
while (y % 2 == 0)
    println(s"${y} is still even")
    y  /= 2

// Declare a functional-style equivalent
def checkEven(y: Int): Unit = 
    if (y / 2 % 2 != 0) println(s"${y} is still even")
    else checkEven(y / 2)

checkEven(100)

// Declare a for loop
for (x <- 1 to 10)
    println(x)

// Declare a functional-style equivalent
def printInteger(x: Int): Unit = 
    if (x == 10) println(x)
    else printInteger(x + 1)

printInteger(1)

// ----------------------
// for Comprehensions
// ----------------------

// Declare a list
val mynumbers: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)

// Apply squared and create new list
val mynumbers_squared: List[Int] = for (n <- mynumbers) yield n * n

// for comprehensions with conditions
val numbers: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)

// Apply modulus and filter by odd & even numbers
val numbers_odd: List[Int] = for (n <- numbers if n % 2 != 0) yield n
val numbers_even: List[Int] = for (n <- numbers if n % 2 == 0) yield n

// ----------------------
// Exception handling
// ----------------------

def parseStringToInt(x: String): Unit = 
    try
        val parsed: Int = x.toInt
        println(parsed)
    catch
        case e: NumberFormatException => println(s"Couldn't parse '${x}' to an integer.")

parseStringToInt("7")
parseStringToInt("a")

// ----------------------
// Collections
// ----------------------

// List
val myIntList: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)
val myStringList: List[String] = List("a", "a", "b", "b", "c", "c")
val myFloatList: List[Float] = List(1f/2f, 1f/4f, 1f/8f)
val myMixedList: List[Matchable] = List(1, "2", 3.0)

// Array

// Declare array
val myArray: Array[Int] = Array(1, 2, 3, 4, 5)

// Print string representation
print(myArray)

// Change array value
myArray(0) = 0

// Print array elements using foreach
myArray.foreach(println)

// Set
val mySet: Set[Int] = Set(1, 2, 3, 4, 5)
println(mySet)

// Map
// Declare Map of Int -> String
val myMapInt: Map[Int, String] = Map(1 -> "one", 2 -> "two", 3 -> "three")

// Index Map by Int key
myMapInt(1)

// Declare Map of String -> Int
val myMapString: Map[String, Int] = Map("one" -> 1, "two" -> 2, "three" -> 3)

// Index Map by String key
myMapString("two")

// Tuple

// Declare a tuple using a single type
val myTupleSingle: Tuple = (1, 2, 3, 4, 5)

// Declare a tuple using multiple but explicitly declared types
val myTupleMulti: (String, Int, String, String, Int) = ("1", 2, "3", "4", 5)

// Declare a tuple using multiple inferred types
val myTupleMulti_2 = (1, "2", 3, "4", "5", '6', 7)

// Option
val personAge = Map("John" -> 30, "Amy" -> 25)

def getAge(name: String): Option[Int] = {
    personAge.get(name)
}

val johnAge = getAge("John")
val amyAge = getAge("Amy")
val unknownAge = getAge("Unknown")

def checkAge(age: Option[Int]): Unit = age match
    case Some(age) => println(s"The age is: ${age}")
    case None => println(s"Sorry! Person does not exist.")

checkAge(johnAge)
checkAge(unknownAge)

// Vector
val myVector: Vector[Int] = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9)

// ----------------------
// Higher-order functions
// ----------------------

// Defining a list of values to operate on
val myTargetList: List[Int] = List(1, 2, 3, 4)

// Define the summation function
def sumList(l: List[Int], f: Int => Int): Int = 
    def sumNumbers(h: Int, t: List[Int], f: Int => Int): Int = 
        if (t.isEmpty) f(h)
        else f(h) + sumNumbers(t.head, t.tail, f)
    sumNumbers(l.head, l.tail, f)

def intSquared(x: Int): Int = 
    x*x

// Call function
sumList(myTargetList, intSquared)

// ----------------------
// Higher-order methods - Map
// ----------------------

// Declare a simple list of integer values
val myList: List[Int] = List(1, 2, 3, 4, 5)

// Declare a squared method
def squaredInts(x: Int): Int = 
    x*x

// Use Map on list
myList.map(squaredInts)

// Perform the same operation using an anonymous function
myList.map((x: Int) => x * x)

// Double numbers using placeholder
myList.map(_ * 2)

// Define a list of lists
val listOfLists: List[List[Float]] = List(
                                     List(1, 2, 3, 4, 5),
                                     List(6, 7, 8, 9, 10),
                                     List(11, 12, 13, 14, 15)
                                     )

// Declare single list average function
def averageOfLists(x: List[Float]): Float = 
    val listLen = x.length
    def calculateAverage(h: Float, t: List[Float], cum: Float): Float = 
        if (t.isEmpty) (cum + h)/listLen
        else calculateAverage(t.head, t.tail, h + cum)
    calculateAverage(x.head, x.tail, 0)

// Apply average function to list of lists using map
listOfLists.map(averageOfLists)

// Chaining map functions
listOfLists.flatten.map(x => x + 1).map(x => x * 2)

// ----------------------
// Higher-order methods - flatMap
// ----------------------

// Define a collection of words
val myWordCollection: List[String] = List("Hello", "there", "my", "dear")

// Map & flatten
myWordCollection.flatMap(x => x.toList)

// Define a list of lists
val listOfLists_2: List[List[Float]] = List(
                                       List(1, 2, 3, 4, 5),
                                       List(6, 7, 8, 9, 10),
                                       List(11, 12, 13, 14, 15)
                                       )

// Calculate averages for each nested list
listOfLists_2.flatMap(x => List(x.sum / x.length))

// ----------------------
// Higher-order methods - filter
// ----------------------

// Define a new list
val myRawList: List[Int] = List.range(1, 100)

// Filter even numbers
val myFilteredList: List[Int] = myRawList.filter(x => x % 2 == 0)

// ----------------------
// Higher-order methods - reduce
// ----------------------

// Define a new list
val myAlphabetList: List[String] = List("a", "b", "c", "d")

// Reduce left
myAlphabetList.reduceLeft(_ + _)

// Declare a list of lists
val listOfLists_3: List[List[Float]] = List(
                                       List(1, 2, 3, 4, 5),
                                       List(6, 7, 8, 9, 10),
                                       List(11, 12, 13, 14, 15)
                                       )

// Calculate averages by reducing
listOfLists_3.map(x => x.reduceLeft(_ + _) / x.length)

// Invert a list
myAlphabetList.reduceLeft((x,y) => y+x).toList



// ----------------------
// Recursion
// ----------------------

def mySumFun(a: Int, b: Int): Int = 
    def accumulatorFun(a: Int, b: Int, acc: Int): Int = 
        if (a > b) acc
        else accumulatorFun(a + 1, b, acc + a)
    accumulatorFun(a, b, 0)

mySumFun(1, 10)