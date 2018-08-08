#!/usr/bin/python

# This script is meant to take in a protein sequence with none protein letters \and return a corrected protein sequence

# We will read in the seq from a file stored somewhere in the computer and specify \that it is a string
#protein = input('Please give a protein sequence: ')

protein = 'JUJSDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'

print("The input protein is ", protein)

# We will initialise the corrected protein as an empty string
corr_protein = ' '

# Initialise count
count = 0

# We create a for loop test to iterate through the entire length of the input protein \sequence
for i in range(len(protein)):

	# Store the amino acid alphabets in a variable
	aa = 'ABCDEFGHIKLMNPQRSTVWXYZ'

	# Create a boolean test to check presence of alphabet in the 20 amino alphabets
	if protein[i] not in aa:

		# Let's print out the none-aa alphabet removed and its position
		print('The letter %s has been detected at position %d as a none-aa and removed!' % (protein[i], i))

		# Changing count to capture detected none-aa
		count += 1

		# To prevent the loop from stoping when test results is false
		continue

	# We store the corrected seq by extending corr_protein at each iteration
	corr_protein += protein[i]

# To check if the entire seq is not a protein seq we use another if test
if count == len(protein):
	print('The supplied sequence was not a protein sequence!')

# To check whether entire seq given was a true protein seq
if (len(corr_protein)-1) == (len(protein)):
	print('The supplied sequence was entirely a protein sequence!')

# Put a control so that only a corrected or correct input seq is printed as output and not a fully none protein seq
if len(corr_protein) > 1:

	# When the for loop has fully cycled, we ask that the corrected protein sequence be printed out in full
	print('The corrected/output protein sequence is: %s' % corr_protein)

	# Print out the number of deleted alphabets
	print('A total of %d alphabets have been deleted from the input sequence' % count)
