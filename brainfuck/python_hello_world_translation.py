C0 = 0
C1 = 0
C2 = 0
C3 = 0
C4 = 0
C5 = 0
C6 = 0

C0 = 8
for num in range(0, C0):

	C1 = 4
	for new_num in range(0, C1):
		C2 += 2
		C3 += 3
		C4 += 3
		C5 += 1

		# End of for loop
		C1 -= 1

	C2 += 1
	C3 += 1
	C4 -= 1
	C6 += 1


	# End of for loop
	C0 -= 1
print chr(C2)
C3 -= 3
print chr(C3)
C3 += 7
print chr(C3)
print chr(C3)
C3 += 3
print chr(C3)
print chr(C5)
C4 -= 1
print chr(C4)
print chr(C3)
C3 += 3
print chr(C3)
C3 -= 6
print chr(C3)
C3 -= 8
print chr(C3)
C5 += 1
print chr(C5)
C6 += 2
print chr(C6)

print "Results"
print (0, C0)
print (1, C1)
print (2, C2)
print (3, C3)
print (4, C4)
print (5, C5)
print (6, C6)
