"""


Change in a Foreign Currency
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.
Signature
boolean canGetExactChange(int targetMoney, int[] denominations)
Input
1 ≤ |denominations| ≤ 100
1 ≤ denominations[i] ≤ 10,000
1 ≤ targetMoney ≤ 1,000,000
Output
Return true if it's possible to receive exactly targetMoney given the available denominations, and false if not.
Example 1
denominations = [5, 10, 25, 100, 200]
targetMoney = 94
output = false
Every denomination is a multiple of 5, so you can't receive exactly 94 units of money in this currency.
Example 2
denominations = [4, 17, 29]
targetMoney = 75
output = true
You can make 75 units with the denominations [17, 29, 29].

Python 3
1
import math
2
# Add any extra import statements you may need here
3
​
4
​
5
# Add any helper functions you may need here
6
​
7
​
8
def canGetExactChange(targetMoney, denominations):
9
  # Write your code here
10

11

12
​
13
​
14
​
15
​
16
​
17
​
18
​
19
​
20
​
21
​
22
​
23
# These are the tests we use to determine if the solution is correct.
24
# You can add your own at the bottom.
25
​
26
def printString(string):
27
  print('[\"', string, '\"]', sep='', end='')
28
​
29
test_case_number = 1
30
​
31
def check(expected, output):
32
  global test_case_number
33
  result = False
34
  if expected == output:
35
    result = True
36
  rightTick = '\u2713'
37
  wrongTick = '\u2717'
38
  if result:
39
    print(rightTick, 'Test #', test_case_number, sep='')
40
  else:
41
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
42
    printString(expected)
43
    print(' Your output: ', end='')
44
    printString(output)
45
    print()
46
  test_case_number += 1
47
​
CONSOLE
Remove
Choose the programming language you're most comfortable withLearn about this new feature


"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def canGetExactChange(targetMoney, denominations):


# Write your code here
    pass

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
