Binary Converter
================

In this exercise you will be making functions that convert between base 10 numbers and binary.

Binary notation is based on powers of 2. Each digit is a power of 2. The first digit is 2^0, second 2^1, etc... You then add all of the digits together.

For example, 101 is 5 (4 + 1). 110 is 6 (4 + 2). 1100 is 12 (8 + 4)  
Here is a chart of some base 2 vs base 10 notation numbers:  

		0.....0  
		1.....1  
		10.....2  
		11.....3  
		100.....4  
		101.....5  
		110.....6  
		111.....7  
		1000.....8  
		1001.....9  
		1010.....10  
		1011.....11  
		1100.....12  
		1101.....13


#### Step 1

Write a method that takes binary numbers and outputs a base 10 number.

		binary_to_decimal(1011) ## returns 11

To run the tests for this step execute the following statement from the command line:

```bash
python3 -m unittest test_binary_converter.TestBinaryToDecimal
```
For this to work you must be in the directory `1-binary-converter`.

#### Step 2

Write a method that takes decimal numbers and returns it in binary notation.

		decimal_to_binary(12) ## returns 1100

To run the tests for this step execute the following statement from the command line:

```bash
python3 -m unittest test_binary_converter.TestDecimalToBinary
```
For this to work you must be in the directory `1-binary-converter`.


Resources
----------

[How to Convert Decimal to Binary](http://www.wikihow.com/Convert-from-Decimal-to-Binary)

[CS50 Binary](https://www.youtube.com/watch?v=hacBFrgtQjQ)
