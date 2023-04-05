// Importing libraries & modules

use std::io;
// use std::io::{Write, BufReader, BufRead, ErrorKind};
// use std::fs::File;
// use std::cmp::Ordering;
// use rand::Rng;

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
    
    // Shadowing
    // let var1: i32 = 10;
    // let var1: f32 = 10.0;
    // println!("{}", var1);


    // Iterables
    let myarray:[i32; 5] = [1,2,3,4,5];
    let myarray_iter = myarray.iter();
    for mynum in myarray_iter {
        println!("Number = {:?}", mynum);
      }

    // // Defining a block
    // let var_outsideblock = 49;
    // {
    //     // Inside a block
    //     let var_insideblock = 49;
    //     println!("{}", var_insideblock);
    //     println!("{}", var_outsideblock);
    // }

    // println!("{}", var_outsideblock);

    // myfun1();

}


// fn myfun1() {

// }



