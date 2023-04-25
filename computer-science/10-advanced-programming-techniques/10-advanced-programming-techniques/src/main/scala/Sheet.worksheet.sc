import cats._
import cats.implicits._
import cats.instances.list._
import cats.instances.vector._
import scala.annotation.tailrec

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

// 5. Reversed List


// ----------------------
// Higher Order Functions
// ----------------------




// ----------------------
// Currying
// ----------------------


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

// 2. 


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