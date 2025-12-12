CodeChef Streak

CodeChef offers a feature called streak count. A streak is maintained if you solve at least one problem daily.
Om and Addy actively maintain their streaks on CodeChef. Over a span of N consecutive days, you have observed the count of problems solved by each of them.

Your task is to determine the maximum streak achieved by Om and Addy and find who had the longer maximum streak.
## Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N — the number of days.
The second line of each test case contains N space-separated integers, the i th of which is A i, representing the problems solved by Om on the i thday.
The third line of each test case contains N space-separated integers, the i thof which is B i, representing the problems solved by Addy on the i th day.
## Output Format
For each test case, output:
OM, if Om has longer maximum streak than Addy;
ADDY, if Addy has longer maximum streak than Om;
DRAW, if both have equal maximum streak.
You may print each character in uppercase or lowercase. For example, OM, om, Om, and oM, are all considered the same.
## Constraints
1≤T≤10^5 

1≤N≤10^5

0≤Ai,Bi≤10^9

The sum of N over all test cases won't exceed 6⋅10^5
 
Sample 1:
## Input
3

6

1 7 3 0 2 13

0 2 3 4 5 0

3

1 3 4

3 1 2

5

1 2 3 0 1

1 2 0 2 3
## Output
Addy

Draw

Om
## Explanation:
Test case 1: Om has a maximum streak of 3 days, while Addy has a maximum streak of 4 days.

Test case 2: Both have the same maximum streak of 3 days.

Test case 3: Addy has a maximum streak of 2 days and Om has a maximum streak of 3 days.
