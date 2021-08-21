[
    Comments. Even valid characters ('<', '>', '+', '-', ',', '.')
        are ignored as the current cell is 0, so the loop is never
        called.
]

+++++++++ # Cell 0 = 9
[
	>++++++++ # Cell 1 = 8
	[
		>+ # Cell 2 plus 1
		>>+ # Cell 4 plus 1
		>+ # Cell 5 plus 1
		< # Back to Cell 4
		<< # Back to Cell 2
		<- # Loop 8 times until Cell 1 is 0
	] # Cell 1 = 0

	<-  # Loop 8 times until Cell 0 is 0
] # Cell 0 = 0
# Cell 2 = 9 * 8 = 72
# Cell 4 = 9 * 8 = 72
# Cell 5 = 9 * 8 = 72

# 0 1  2 3  4  5 6
# 0 0 72 0 72 72 0

>>. # Print Cell 2 = 72 = H

<< # Cell 0
++++ ++++ +++ # Cell 0 = 11
[
	>+++ # Cell 1 = 3
	[
		>+ # Cell 2 plus 1
		>+ # Cell 3 plus 1
		>>+ # Cell 5 plus 1
		<<<<- # Loop 3 times until Cell 1 is 0
	]

	<- # Loop 11 times until Cell 0 is 0
] # Cell 0 = 0
# Cell 2 = 72 plus (3 * 11) = 105
# Cell 3 = (3 * 11) = 33
# Cell 5 = 72 plus (3 * 11) = 105

# 0 1   2  3  4   5 6
# 0 0 105 33 72 105 0 0

>>. # Print Cell 2 = 105 = i
>- # Cell 3 = 33 minus: 1 = 32
. # Print Cell 3 = 32 = space
>++ # Cell 4 = 72 plus 2 = 74
. # Print Cell 4 = 74 = J

# 0 1   2  3  4   5 6
# 0 0 105 32 74 105 0

> # Cell 5 = 105
++++ ++ # Cell 5 = 105 plus 6 = 111
. # Print Cell 5 = 111 = o
++++ # Cell 5 = 111 plus 4 = 115
. # Print Cell 5 = 115 = s
<<< # Cell 2
- # Cell 2 = 105 minus 1 = 104
. # Print Cell 2 = 104 = h
> # Cell 3 = 32
+ # Cell 3 = 32 plus 1 = 33
. # Print Cell 3 = 33 = !
<<< # Cell 0
++++++++++ # Cell 0 = 10
. # Print Cell 0 = 10 = newline

#  0 1   2  3  4   5 6
# 10 0 104 33 74 115 0
