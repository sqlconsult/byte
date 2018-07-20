# Implement 16th century algorithm known as the Vigenère cipher. 

Start with a table like this:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

## Example
Given a keyword TRAIN, encode the message ENCODED IN PYTHON as follows:

 - Repeat the keyword and message together such that it is easy to map letters from one to the other:<br>
E N C O D E D I N P Y T H O N
T R A I N T R A I N T R A I N

 - For each letter in the plaintext, find the row that begins with that letter in the table.

 - Find the column with the letter associated with the keyword letter for the chosen plaintext letter.
The encoded character is at the intersection of this row and column.

For example, the row starting with E intersects the column starting with T at the character X. So the first letter in the ciphertext is X. The row starting with N intersects the column starting with R at the character E, leading to the ciphertext XE. C intersects A at C, and O intersects I at W. D and N map to Q while E and T map
to X. The full encoded message is XECWQXUIVCRKHWA.

Decoding basically follows the opposite procedure. First find the row with the character for the shared keyword (the T row) then find the location in that row where the encoded character (the X) is located. The plaintext character is at the top of the column for that row (the E).


## Solution

 - Language: Python 3.5
 - Testing Platform: pytest
 - Unit Test Execution: `$ ./test.sh`
 
 ### Modules
 
 1. cipher.py - Methods required for en/decoding text
 
    - combine_character - Convert plain text and keyword characters to their numerical values, add them together and take the remainder mod 26 to get the cipher text character
    - extend_keyword - Extend the cipher keyword to a specified number of characters
    - separate_character - Decode a single character using keyword
    - _code - Encode plain text or decode encrypted text using combine_func
    - encode - Encodes plain text and returns encoded text
    - decode - Decodes encoded text and returns plain text
 
2. test.sh - Bash script to run automated tests

3. test_cipher.py - Automated tests for cipher.py

    - test_encode - tests encoding an entire string
    - test_encode_character - tests encoding a single character
    - test_encode_spaces - tests encoding a string with spaces
    - test_encode_lowercase - test encoding a lower case string
    - test_combine_character - tests combining encoded plain text characters
    - test_extend_keyword - tests keyword is extended to correct length
    - test_decode_character - tests decoding a single character
    - test_decode - tests decoding an entire string