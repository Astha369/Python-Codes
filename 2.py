#A sequence of integers of even length is said to be left-heavy 
# if the sum of the terms in the left-half of the sequence is greater 
# than the sum of the terms in the right half. It is termed right-heavy 
# if the sum of the second half is greater than the first half. 
# It is said to be balanced if both the sums are equal.
#Accept a sequence of comma-separated integers as input. 
# Determine if the sequence is left-heavy, right-heavy or balanced and print this as the output.

seq = list(eval(input()))
l = len(seq)//2

rsum = 0 
lsum = 0
for i in range (l):
    lsum += seq[i]
    rsum += seq[l+i]

if rsum > lsum:
    print("Right-Heavy")
elif lsum > rsum:
    print("Left-Heavy")
else:
    print('Balanced')

    