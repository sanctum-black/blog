// Importing libraries & modules

use std::io;
use std::cmp::Ordering;
use rand::Rng;

// Commenting
// This is a single line comment.
// Which can also be continued in the next line.

/*
This is a multiline comment
where we can include multiple lines
without having to comment each line.
*/

// The main function

// Define constant outside main function
const HELLO: &str = "Constant Hello";

// Define an immutable variable outside main function
// let mystring_immut = 7;

fn main() {
    // Print a string in same line
    print!("Hello ");
    print!("World");

    // Print a string in newline
    println!("Hello");
    println!("World");

    // Print an integer using a string literal format argument
    println!("{}", 7);

    // Format output with additional text
    println!("The number is: {}", 7);

    // Multiple placeholders
    println!("The numbers are: {} and {}", 7, 4);

    // Print variable
    let intvar = 7421;
    println!("{}", intvar);

    // Immutable variable
    let mystring_immut = 7;
    println!("{}", mystring_immut);

    // Mutable variable
    let mut mystring_mut:String = String::new();

    // Accept user input
    io::stdin().read_line(&mut mystring_mut)
    .expect("Didn't Receive Input");

    println!("You wrote: {}", mystring_mut);

    // Print constant
    println!("{}", HELLO);                                                            

    // Using variables as placeholders
    let _myplaceholder:i32 = 34;

    // Using underscores as separators
    let mynum_immut: i32 = 7_000_000;
    println!("{}", mynum_immut);

    // Some arithmetic operators
    let mut myvar1: i32 = 14;
    let mut myvar2: i32 = 16;

    // Arithmetic operations
    println!("Addition: {}", myvar1 + myvar2);
    println!("Subtraction: {}", myvar1 - myvar2);
    println!("Product: {}", myvar1 * myvar2);
    println!("Division: {}", myvar1 / myvar2);


    // Arithmetic operations with assignment
    myvar1 += 1;
    myvar2 /= 2;
    println!("Addition with assignment: {}", myvar1);
    println!("Division with assignment: {}", myvar2);

    // Define boolean variable
    let boolean_var:bool = true;
    println!("{}", boolean_var);

    // Define an integer variable
    let mynum_i32:i32 = 2000;
    let mynum_f32:f32 = 3.1416;
    println!("{}, {}", mynum_i32, mynum_f32);

    // Get maximum number for a given data type
    println!("Max size for u8 is: {}", u8::MAX);

    // Define a char variable
    let _mychar:char = 'a';

    // Define a string variable
    let _mystring:&str = "string";
    
    // Multiple variable assignment
    let (myvar1, myvar2, myvar3) = (1, 2, 3);
    println!("{} {} {}", myvar1, myvar2, myvar3);


    // Shadowing
    // let var1: i32 = 10;
    // let var1: f32 = 10.0;
    // println!("{}", var1);

    // Random number generation
    let myrandnum = rand::thread_rng().gen_range(1..11);
    println!("Random number is: {}", myrandnum);

    // Conditional control
    let firstnum:i32 = 7;
    let secondnum:i32 = 15;
    let thirdnum:i32 = 14;

    if (secondnum > firstnum) && (secondnum > thirdnum) {
      println!("Number {} is the biggest one of the series.", secondnum);
    } else if (firstnum > secondnum) && (firstnum > thirdnum) {
      println!("Number {} is the biggest one of the series.", firstnum);
    } else {
      println!("Number {} is the biggest one of the series.", thirdnum);
    }

    if (firstnum % 2 == 0) || (secondnum % 2 == 0) || (thirdnum % 2 == 0) {
      println!("There is at least one even number here.");
    }

    // Conditional control using variables
    let base:i32 = 7;
    let fourthnum:i32 = 49;
    let power: u32 = 2;
    let numbertest:bool = if base.pow(power) == fourthnum {true} else {false};
    println!("{}", numbertest);
    let elevated:i32 = base.pow(power);
    println!("{}", elevated);

    // Conditional control using match
    let mynum:u32 = 14;
    let mynum_reminder:u32 = mynum%2;
    match mynum_reminder {
      0 => println!("The number {} is even.", mynum),
      1 => println!("The number {} is odd.", mynum),
      _ => println!("{} is not a number.", mynum),
    };

    let mynum1:u32 = 14;
    let mynum2:u32 = 15;
    match mynum1.cmp(&mynum2) {
      Ordering::Less => println!("{} is less than {}.", mynum1, mynum2),
      Ordering::Greater => println!("{} is greater than {}.", mynum1, mynum2),
      Ordering::Equal => println!("{} is equal to {}.", mynum1, mynum2),
    };

    // Arrays
    let myarr:[i32; 10] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
    // Index the first element
    println!("{}", myarr[0]);

    // Get its length
    println!("{}", myarr.len());

    // Multiply the first element by a scalar
    println!("{}", myarr[0] * 10);

    // Define a mutable array
    let mut myarr_mut:[i32; 10] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];

    // Print the original array
    println!("Original: {:?}", myarr_mut);

    // Substitute a value
    myarr_mut[0] = 1000;

    // Print the mutated array
    println!("Mutated: {:?}", myarr_mut);

    // Iterables with iter

    // Define an array
    let myarray:[i32; 5] = [1,2,3,4,5];

    // Define an iterable set
    let myarray_iter = myarray.iter();
    for mynum in myarray_iter {
        println!("Number = {:?}", mynum);
      }

    // Iterables with loop

    // Define an array
    // let myarray:[i32; 5] = [1,2,3,4,5];   

    // Define a counter as a mutable variable
    // let mut mycounter:usize = 0;

    // // Define loop (without counter condition check)
    // loop {
    //   println!("{}", myarray[mycounter]);

    //   // Increase counter
    //   mycounter += 1;
    // }

    // Define loop (with counter condition check)

    // Define an array
    let myarray:[i32; 5] = [1,2,3,4,5];   

    // Define a counter as a mutable variable
    let mut mycounter:usize = 0;

    // Define loop (without counter condition check)
    loop {
      // First, check condition. If it's true, break
      if mycounter >= myarray.len() {
      break;
      }

      // If condition is false, execute code
      println!("{}", myarray[mycounter]);

      // Increase counter
      mycounter += 1;
    }

    // Define a while loop

    // Define an array
    let myarray:[i32; 5] = [1,2,3,4,5];   

    // Define a counter as a mutable variable
    let mut mycounter:usize = 0;

    // Define loop
    while mycounter < myarray.len() {

      println!("{}", myarray[mycounter]);

      // Increase counter
      mycounter += 1;
    }

    // Define a for loop with a range
    let myarray:[i32; 5] = [1,2,3,4,5];

    // Define loop
    for i in 0..myarray.len() {
      println!("{}", myarray[i]);
    }

    // Define a for loop using an iterator set
    let myarray:[i32; 5] = [1,2,3,4,5];

    // Define an iterable set
    let myiter = myarray.iter();

    // Define loop
    for i in myiter {
      println!("{}", i)
    }

    // Define an array
    let myarray:[i32; 5] = [1,2,3,4,5];

    // Define loop including iterable set
    for i in myarray.iter() {
      println!("{}", i)
    }

    // Define a for loop using an iterator and enumerate

    // Define an array
    let myarray:[i32; 5] = [1,2,3,4,5];

    // Define loop including iterable set and enumerate
    for (index, item) in myarray.iter().enumerate() {
      println!("{}: {}", index, item);
    }

    // Define an immutable tuple
    let mytuple: (i32, i32, &str, f32, bool) = (12, 14, "16", 18.0, true);

    println!("{}", mytuple.0);

    // Define a mutable tuple
    let mut mytuple_mut: (i32, i32, &str, f32, bool) = (12, 14, "16", 18.0, true);

    println!("Original: {:?}", mytuple_mut);

    // Mutate the tuple
    mytuple_mut.0 = 14;

    println!("Mutated: {:?}", mytuple_mut);

    // Define a string using String
    let mut mystring1 = String::new();

    // Insert a character
    mystring1.push('X');

    // Insert a string
    mystring1.push_str("Y Z");

    // Iterate over words by splitting at whitespaces 
    for i in mystring1.split_whitespace() {
      println!("{}", i);
    }

    // Replace a string
    let mystring2: String = mystring1.replace("X", "W X");
    println!("{}", mystring2);

    // Slice a string

    // First convert to heap-allocated string
    let myheapstring: String = mystring2.to_string();
    println!("Heap: {}", myheapstring);

    // Then index
    let mysubstring2 = &myheapstring[1..6];
    println!("Substring: {}", mysubstring2);

    // Create a non-empty string using String
    let mystring3 = String::from("This is is a non-empty string");
    
    // Remove duplicates from a String

    // First convert to vector
    let mut myvec1: Vec<String> = mystring3.split_whitespace().map(str::to_string).collect();
    println!("{:?}", myvec1);

    // Then remove duplicates
    myvec1.dedup();
    println!("{:?}", myvec1);

    // Slices of other types

    // Declare an array
    let myarr1: [i32; 5] = [1, 2, 3, 4, 5];

    // Slice an array from index 1 to 4
    let myslice1 = &myarr1[1..4];
    println!("Slice 1: {:?}", myslice1);

    // Slice an array from beginning to 4
    let myslice2 = &myarr1[..4];
    println!("Slice 2: {:?}", myslice2);    

    // Slice an array from index 1 to end
    let myslice3 = &myarr1[1..];
    println!("Slice 3: {:?}", myslice3);  

    // Slice an array from beginning to end
    let myslice4 = &myarr1[..];
    println!("Slice 4: {:?}", myslice4);  

    // Mutable slice from mutable array

    // Declare mutable array
    let mut myarr2: [i32; 5] = [1, 2, 3, 4, 5];

    // Declare mutable slice
    let myslice5 = &mut myarr2[1..4];

    // Mutate slice
    myslice5[0] = 100;
    println!("Slice 5: {:?}", myslice5);    

    // Casting
    let myfloat: f32 = 32.7;
    println!("{}", myfloat);
    let myint: i32 = myfloat as i32;
    println!("{}", myint);

    // Collecting an iterator

    // Define a range iterator
    let myrange = 1..12;

    // Collect iterator to vector
    let mycollectedrange: Vec<i32> = myrange.collect();
    println!("{:?}", mycollectedrange);

    // Defining vectors

    // Define an empty vector
    let myvector1: Vec<i32> = Vec::new();
    println!("{:?}", myvector1);

    // Define a populated immutable vector
    let myvector2: Vec<i32> = vec![10, 20, 30, 40];
    println!("{:?}", myvector2);

    // Define a populated mutable vector and perform some operations
    let mut myvector3: Vec<i32> = vec![50, 60, 70, 80];

    // Append number
    myvector3.push(90);

    // Index first component
    println!("{}", myvector3[0]);

    // Verify if a given value exists
    match myvector3.get(1) {
      Some(60) => println!("Number 60 is in the vector."),
      _ => println!("Number 60 is not in the vector."),
    };

    // Print length of vector
    println!("{:?}", myvector3.len());

    // Defining a block
    let var_outsideblock = 49;
    {
        // Inside a block
        let var_insideblock = 7;
        println!("Inside 1: {}", var_insideblock);
        println!("Inside 2: {}", var_outsideblock);
    }

    // Outside a block
    println!("Outside: {}", var_outsideblock);

    // Call myfun1
    myfun1();

    // Call myfun2
    myfun2(21, 22.3);

    // Assign output of myfun3
    let myoutput3: i32 = myfun3(7, 7);
    println!("{}", myoutput3);

    // Assign output of myfun4
    let myoutput4: i32 = myfun4(7, 7);
    println!("{}", myoutput4);

}

// Defining our own function

fn myfun1() {
    let myint: i32 = 100;
    println!("{}", myint);
}

fn myfun2(myarg1: i32, myarg2: f32) {
    println!("{}, {}", myarg1, myarg2);
}

fn myfun3(myarg1: i32, myarg2: i32) -> i32 {
    myarg1 * myarg2
}

fn myfun4(myarg1: i32, myarg2: i32) -> i32 {
    let op1: i32 = myarg1 - 2;
    let op2: i32 = myarg2 - 4;
    let op3: i32 = op1 * op2;

    return op3;
}