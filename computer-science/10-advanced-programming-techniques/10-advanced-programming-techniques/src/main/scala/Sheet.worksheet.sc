// Cats
import cats._
import cats.implicits._
import cats.instances.list._
import cats.instances.vector._

// Tail Recursion
import scala.annotation.tailrec

// Asynchronous CPS
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.{Promise, Await, Future}
import scala.concurrent.duration._

// ----------------------
// Tail recursion
// ----------------------

// 1. Sum of a list
def recursiveSum(list: List[Int]): Int = {
    @tailrec
    def sumItems(list: List[Int], counter: Int): Int = {
        if (list.isEmpty) counter
        else sumItems(list.tail, counter + list.head)
    }
    sumItems(list, 0)
}

// Simple call
recursiveSum(List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

// Extense call
recursiveSum(List.range(1, 100000))

// Even bigger call
// recursiveSum(List.range(1, 1000000000))

// ----------------------

// 2. Factorial calculation
def factorialCalc(n: Int): BigInt = {
    @tailrec
    def factorialItems(n: Int, counter: BigInt): BigInt = {
        if (n == 0) 1
        else if (n == 1) counter
        else factorialItems(n-1, n * counter)
    }
    factorialItems(n, 1)
}

// Edge case call
factorialCalc(0)

// Small integer call
factorialCalc(4)

// Extense call
factorialCalc(10)

// Even bigger call
factorialCalc(100)

// ----------------------

// 3. Fibonacci sequence
def FibCalc(n: Int): BigInt = {
    @tailrec
    def fibItems(n: Int, next: BigInt, current: BigInt): BigInt = {
        if (n == 0) current
        else fibItems(n-1, next + current, next)
    }
    fibItems(n, 1, 0)
}


// Edge case call
FibCalc(0)

// Small integer call
FibCalc(5)

// Extense call
FibCalc(10)

// Even bigger call
FibCalc(1000)

// ----------------------

// 4. Exponentiation
def ExpCalc(base: Int, exp: Int) : BigInt = {
    @tailrec
    def ExpItems(base: Int, exp: Int, counter: BigInt): BigInt = {
        if (base == 0) 0
        else if (exp == 0) 1
        else if (exp == 1) counter
        else ExpItems(base, exp - 1, base*counter)
    }
    ExpItems(base, exp, base)
}

// Edge case call
ExpCalc(0, 0)

// Small integer call
ExpCalc(2, 2)

// Extense call
ExpCalc(8, 4)

// Even bigger call
ExpCalc(14328, 5)

// ----------------------
// Higher-Order Functions
// ----------------------

// 0. Basic syntax

// Higher-order function
def myfun(f: Int => Boolean, n: Int): Boolean = {
    f(n)
}

// Parameter function
def f(n: Int): Boolean = {
    n >= 1
}

// Higher-order function call
myfun(f, 1)

// 1. Single verification of a list
def checkList(checkerEven: Int => Boolean, list: List[Int]): Int = {
    def countElements(checkerEven: Int => Boolean, list: List[Int], counter: Int): Int = {
        if (list.isEmpty) counter
        else {
            if (checkerEven(list.head)) countElements(checkerEven, list.tail, counter + 1)
            else countElements(checkerEven, list.tail, counter)
        }
    }
    countElements(checkerEven, list, 0)
}

def checkerEven(target: Int): Boolean = {
    target % 2 == 0
}

checkList(checkerEven, List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


// 2. Variation of a summation
def sumNumbers(applyProduct: (Int, Int) => Int, applyAddition: (Int, Int) => Int, a: Int, b: Int, x: Int): Int = {
    if (a > b) 0
    else applyProduct(applyAddition(a, x), x) + sumNumbers(applyProduct, applyAddition, a + 1, b, x)
}

def applyProduct(n: Int, x: Int): Int = {
    n * x
}

def applyAddition(n: Int, x: Int): Int = {
    n + x
}

sumNumbers(applyProduct, applyAddition, 2, 3, 2)

// ----------------------
// Currying
// ----------------------

// 1. A curried addition function

// Define a curried function
def sumNums(x: Int)(y: Int): Int = {
    x + y
}

// Partial call
val first_call = sumNums(7) _

// Complete call
val second_call = first_call(3)

// 2. A curried call using two functions

// Define curried function
def sumInts(squareInt: Int => Int)(x: Int, y: Int): Int = {
    squareInt(x + y)
}

// Define helper function
def squareInt(a: Int): Int = {
    a*a
}

// Direct call
sumInts(squareInt)(2, 3)

// Partial call
val applySumSquare = sumInts(squareInt) _

// Complete partial call
applySumSquare(2, 3)

// ----------------------
// Monads
// ----------------------

// 1. An undefined operation

// Unsafe division one
def unsafeDivOne(UnsafeDivTwo: (Double, Double)  => Double, a: Double, b: Double, d: Double): Double = {
    UnsafeDivTwo(a, b) / d
}

// Unsafe division two
def UnsafeDivTwo(a: Double, b: Double): Double = {
    a / b
}

// Call 1
unsafeDivOne(UnsafeDivTwo, 12, 2, 3)

// Call 2
unsafeDivOne(UnsafeDivTwo, 12, 0, 3)


// Safe division one
def safeDivOne(SafeDivTwo: (Double, Double) => Option[Double], a: Double, b: Double, d: Double): Option[Double] = {
    if (b != 0 & d != 0) {
        safeDivTwo(a, b).flatMap(result => safeDivTwo(result, d))
    }
    else None
}

// Safe division two
def safeDivTwo(a: Double, b: Double): Option[Double] = {
    if (b != 0) Some(a / b)
    else None
}

safeDivOne(safeDivTwo, 12, 0, 3)

// ----------------------
// Pattern Matching
// ----------------------

// Basic syntax

// Define a pattern-matching construct
def patternMatch(x: Int): Unit = {
  x match {
    case 14 => println("The number is 14")
    case 15 => println("The number is 15")
    case _ => println("The number is not 15 nor 16")
  }
}

// Define simple integer variables
val simple_int_1: Int = 14
val simple_int_2: Int = 15
val simple_int_3: Int = 16

// Call function
patternMatch(simple_int_1)
patternMatch(simple_int_2)
patternMatch(simple_int_3)

// ----------------------

// 1. Handle a division by zero
def checkDivide(result: Option[Double]) = {
    result match {
    case Some(value) => println(s"Division result: $value")
    case None        => println("Division by zero is not allowed")
    }
}

// Checking
checkDivide(safeDivOne(safeDivTwo, 12, 2, 3))
checkDivide(safeDivOne(safeDivTwo, 12, 0, 3))

// ----------------------

// 2. Animal classification

// Define an animal checker
def checkAnimal(animal: String): String = {
    animal match {
        case ("Elephant" | "Whale" | "Dog") => "Mamal"
        case ("Parrot" | "Eagle" | "Penguin") => "Bird"
        case ("Lizard" | "Tortoise" | "Snake") => "Reptile"
        case _ => "Animal is not in DB, sorry."
    }
}

// Define an animal
val my_animal = "Snake"

// Call function
checkAnimal(my_animal)

// ----------------------

// 3. Type checking

// Implement using pattern matching
def checkType1(x: Any): String = x match {
  case _: Int => "Int"
  case _: String => "String"
  case _: Boolean => "Boolean"
  case _ => "Unknown"
}

// Implement using a if-else constructs
def checkType2(x: Any): String = {
  if (x.isInstanceOf[Int]) "Int"
  else if (x.isInstanceOf[String]) "String"
  else if (x.isInstanceOf[Boolean]) "Boolean"
  else "Unknown"
}

// Call functions
checkType1(1)
checkType2(1)

checkType1("A String")
checkType2("A String")

// ----------------------
// Extractors
// ----------------------

// 1. Extractors with a custom class

// Define our custom class
class PositiveInt(val value: Int)

// Define an object
object PositiveInt {
  def unapply(value: Int): Option[PositiveInt] =
    if (value > 0) Some(new PositiveInt(value)) else None
}

// Define a checker that includes an extractor
def checkNum(x: Int) = x match {
  case PositiveInt(positiveInt) => println(s"The number ${positiveInt.value} is positive.")
  case _ => println(s"The number ${x} is not positive.")
}

checkNum(7)
checkNum(-10)

// ----------------------
// Lazy evaluation
// ----------------------

// 1. Defining a simple lazy variable

// Define an eager list and a lazy list
val my_list:List[Int] = List(1, 2, 3, 4, 5)
lazy val my_lazy_list:List[Int] = List(1, 2, 3, 4, 5)

// ----------------------
// Implicits
// ----------------------

// Define a function with implicit parameter x
def findInt(implicit x: Int) = x

// Define an implicit value
implicit val my_int: Int = 10
// implicit val my_int_2: Int = 7
implicit val my_string: String = "A String"

// Call function without argument
findInt

// ----------------------
// Type classes
// ----------------------

// 1. Value formatter

// Define a type class
trait Formatter[T] {
  def format(value: T): String
}

// Define a Formatter object, including two
// implicit objects: String and Int
object Formatter {
  implicit object IntFormatter extends Formatter[Int] {
    def format(value: Int): String = s"The integer value is $value"
  }

  implicit object StringFormatter extends Formatter[String] {
    def format(value: String): String = s"The string value is $value"
  }
}

// Define the formatter method
def printFormatted[T](value: T)(implicit f: Formatter[T]): Unit = {
    println(f.format(value))
}

// Format an int and a string
printFormatted(777)(Formatter.IntFormatter)
printFormatted("a string")(Formatter.StringFormatter)

// ----------------------
// Continuation-Passing Style (CPS)
// ----------------------

// Definition: Example

// Conventional Style

// Define an addition function
def addInts(x: Int, y: Int): Int = {
    x + y
}

// Define a multiplication function
def multiplyInts(d: Int, z: Int): Int = {
    d * z
}

// Declare test variables
val x1 = 7
val y1 = 14
val z1 = 21

// Call both functions
println(s"($x1 + $y1) * $z1 = ${multiplyInts(addInts(x1, y1), z1)}")


// CPS Style

// Define an addition function
def addIntsCPS(x: Int, y: Int, k: Int => Unit): Unit = {
    k(x + y)
}

// Define a multiplication function
def multiplyIntsCPS(d: Int, z: Int, k: Int => Unit): Unit = {
    k(d * z)
}

// Declare test variables
val x2 = 7
val y2 = 14
val z2 = 21

addIntsCPS(x2, y2, sum => {
  multiplyIntsCPS(sum, z2, product => {
    println(s"($x2 + $y2) * $z2 = $product")
  })
})

// 1. Sum and product of list of integers
def sumListCPS(list: List[Int], k: Int => Unit): Unit = k(list.sum)

def productListCPS(list: List[Int], k: Int => Unit): Unit = k(list.product)

val numbers = List(7, 14, 21, 28, 35)

sumListCPS(numbers, sum => {
  println(s"Sum: $sum")

  productListCPS(numbers, product => {
    println(s"Product: $product")
  })
})

// ----------------------
// Futures and Promises
// ----------------------

// 1. One asynchronous calculation

// Define Promise
def sumAsync(a: Int, b: Int): Future[Int] = {
  val promise = Promise[Int]()

  // Start an asynchronous task to calculate the sum of the integers
  val task = new Runnable {
    override def run(): Unit = {
      val result = a + b

      // Fulfill the promise with the result of the calculation
      promise.success(result)
    }
  }

  // Start the task on a separate thread
  new Thread(task).start()

  promise.future
}

// Assign sumAsync to variable
val future = sumAsync(1, 2)

// Call using Await API
val result = Await.result(future, 10.seconds)
println(s"Sum: $result")

// ----------------------

// 2. Two asynchronous calculations

// Define operation 1
def addAsync(a: Int, b: Int): Future[Int] = Future {
  a + b
}

// Define operation 2
def multiplyAsync(a: Int, b: Int): Future[Int] = Future {
  a * b
}

// Define task
val resultFuture = for {
  sum <- addAsync(7, 5)
  product <- multiplyAsync(7, 5)
} yield (sum, product)

// Call task
val result_2 = Await.result(resultFuture, 10.seconds)

// ----------------------
// Higher-Kinded Types
// ----------------------

// 1.1 A higher-kinded type for lists and vectors

// 1. Define the higher-kinded type called Box
trait Box[F[_]] {
  def first[A](fa: F[A]): Option[A]
}

// 2. Define how the Box type should work with Lists
class ListBox extends Box[List] {
  def first[A](list: List[A]): Option[A] = list.headOption
}

// 3. Define how the Box type should work with Vectors
class VectorBox extends Box[Vector] {
  def first[A](vector: Vector[A]): Option[A] = vector.headOption
}

// 4. Implement a function findFirst that works with instances of our higher-kinded type
def findFirst[F[_], A](box: Box[F], container: F[A]): Option[A] = {
  box.first(container)
}

// 5. Create an instance of ListBox and use it to find the first element in a list
val listBox = new ListBox()
val myList = List(1, 2, 3)
val firstElementList = findFirst(listBox, myList)

// 6. Create an instance of VectorBox and use it to find the first element in a Vector
val vectorBox = new VectorBox()
val myVector = Vector(4, 5, 6)
val firstElementVector = findFirst(vectorBox, myVector)

// Print both values
println(firstElementList)
println(firstElementVector)

// 1.2 A generic implementation of the Box trait
// that can handle different container types
// based on the type constructor provided

// 1. Define a generic implementation using Foldable and reduceLeftOption
class GenericBox[F[_]: Foldable] extends Box[F] {
  def first[A](container: F[A]): Option[A] = {
    Foldable[F].reduceLeftOption(container)((a, _) => a)
  }
}

// 2. Create an instance of ListBox and use it to find the first element in a list
val genericListBox = new GenericBox[List]
val myList2 = List(1, 2, 3)
val firstElementList2 = genericListBox.first(myList2)

// 3. Create an instance of VectorBox and use it to find the first element in a Vector
val genericVectorBox = new GenericBox[Vector]
val myVector2 = Vector(4, 5, 6)
val firstElementVector2 = genericVectorBox.first(myVector2)


println(firstElementList)
println(firstElementVector)