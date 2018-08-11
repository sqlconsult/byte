# Stride Coding Challenge


## The Problem

There is a chocolate store that sells white, dark, milk and sugar free
chocolate bars. When a shopper places an order for chocolate, store
staff specify the price of the chocolate and the number of wrappers that
must be returned in order to receive free chocolates. The price of the
chocolate and the number of wrappers required to receive a free
chocolate changes with every order as the shop is still experimenting
with how the promotion should work.

### Promotion Rules

- When a shopper trades the required number of:
  - `milk` wrappers they will receive one complimentary `milk` chocolate
    and one complimentary `sugar free` chocolate.
  - `white` wrappers they will receive one complimentary `white`
    chocolate and one complimentary `sugar free` chocolate.
  - `sugar free` wrappers they will receive one complimentary `sugar
    free` chocolate and one complimentary `dark` chocolate.
  - `dark` wrappers they will receive one complimentary `dark`
    chocolate.

### The Orders File

Orders placed by different shoppers can be found in the CSV file
`input/orders.csv`. The first line of this file contains header
information, each subsequent line represents an order. The header format
is:

    cash, price, wrappers needed, type

- Cash: the amount of cash the shopper has to spend on chocolate.

- Price: the price of a single chocolate.

- Wrappers needed: is the number of wrappers that must be traded in, in
  order to receive free chocolate. This number applies to each type of
  wrapper being turned in (e.g. a value of 3 means that 3 milk or 3 white
  wrappers may be redeemed at once) and is independent of the type of
  chocolate being ordered.

- Type: the type of chocolate the shopper is buying in that order.

There are four orders in the `input/orders.csv` file. Every line in
`input/orders.csv` is a separate order with a different `price` and
number of `wrappers needed`. Orders are independent of each other, the
`cash`, `price` and `wrappers needed` of one order does not affect any
other order.

## Solution

 - Language: Python 3.5
 - Input: `input/orders.csv`
 - Output: `output/redemptions.csv`
 - Execution: `$ ./run.sh`
 - Entry Point: `file: controller.py method: main`
 - Unit Test Execution: `$ ./test.sh`
 
 ### Application Modules
 
1. candy.py - used to compute number of wrappers and bonus wrappers  for each order

    - bonus_candy - determines number of free chocolate wrappers user gets by candy type
    - candy_calc - calculates the amount of candy the user can purchase + free promotional candy
 
2. constants.py - global constants used through out the solution
 
3. controller.py - controls application flow

    - display_invalid_orders - displays invalid input orders with error messages
    - files_exist - validates input and output files and directories exist
    - main - main processing logic
    - process_valid_orders - process valid orders to determine number of wrappers
    - read_order_file - read and validate input source file
    - write_output_orders_file - writes target output order file
  
4. model.py - application interface for file operations

    - is_number - returns true if input string is a valid integer or floating point number
    - read_file - for a given input file path, read and validate the file.  Returns list of valid and invalid orders
    - validate_input_order - for a given input order, validate each field.  Returns true if valid, else false
    - write_orders - write calculated number of wrappers to output file
 
5. order.py - class definitions for reading and validating the input source file

    - InputOrder - input line, as is.  No validation, type conversion, all strings
    - ValidOrder - properly validated and converted input order (integers)
    - InvalidOrder - any input order that fails validation with error messages
 
6. view.py - application interface to display information to the user

    - display_msg - displays message to user
 
 ### Bash scripts

1. run.sh - Bash script to execute the application
 
2. test.sh - Bash script to run automated tests
 
 ### Testing Modules
 
1. test_candy - candy wrapper calculation tests

    - test_bonus_candy - for a given input candy type, test that correct bonus candy is allocated
    - test_candy_calc - for given cash, price, wrappers needed for exchange and candy type test that the number of wrappers and bonus wrappers are correctly allocated
 
2. test_controller - controller method tests

    - test_display_invalid_orders - tests invalid orders are displayed
    - test_process_valid_orders - tests valid orders are correctly processed

3. test_file_exists - test method to validate input and output directories and files exist

    - test_files_and_dirs_exist - tests case when input and output directories and files exist
    - test_inp_dir_not_exists - tests case when output directory does not exist
    - test_inp_file_not_exists - tests case when input file does not exist
    - test_out_dir_not_exists - tests case when output directory does not exist

4. test_isnumber - test method to validate strings are valid integers or floats

    - test_int - tests valid and invalid integers
    - test_float - tests valid and invalid floats
    - test_invalid_type - invalid string types (i.e., not float or integer)
    
5. test_read - read and validate input file unit tests

    - test_main_read_order_file - tests controller.read_order_file
    - test_model_read_file - tests model.read_file
    - test_model_validate_input_order - tests model.validate_input_order
    - test_model_input_order - tests order.InputOrder
 
6. test_write - write output unit tests

    - test_controller_write_file - tests controller.write_file
    - test_model_write_file - tests model.write_file
    

 