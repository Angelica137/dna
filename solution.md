Task 1 - Make sure you can run the flask server and get the front end building correctly.

Solution:
The flask server and front end run correctly.

Task 2 - There is a failing test in the backend which needs to be resolved appropriately.

Solution:
The failing test

def test_translation_ends_at_stop_codon(self)

Seemed to fail because the last character was missing.
Looking at the data in constants.py the character corresponding to codon TAG is '\*', for TAA is '_', and TGA is '_'. These last characters were missing from the cases in this test.

Task 3 - Create a tool to allow a wet lab scientist to submit a DNA sequence, indicating the region they
wish to amplify and a desired primer length. Display the resultant primers as well as the melting temperatures
in an appropriate way. - With the example DNA sequence `ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGG`, region to amplify `GGCGAGGAGCTG`
and primer length 4 the tool should return the primers `GGCG`, `CAGC` with melting temperatures 16°C and 14°C
respectively.

Solution:
To simplify the solution, initially, the user is asked to submit the DNA region they wish to amplify.

The design can then be extended to allow the user to begin the task by entering the complete DNA sequence and then indicate the region to amplify.

An assumption here is that the relevant information to produce the primers is the region to be amplified and not the complete DNA sequence, at least at this stage.

Reading the task, it seems that in this problem, when the user specifies the primer length, this is one length for both primers, so it is assumed that, when a user specifies a primer length, this is to be applied to both primers.

Baring in mind it is possible for both primers to take different length requirements, and their calculations are different, the current design keeps the operations needed to design the primers separated by case.

This helps us change requirements in each case in just one place.

Task 4 - Build a separate tool to allow the wet lab scientists to submit a DNA sequence, indicating the region to amplify,
as well as a temperature range, e.g 50°C - 60°C. The tool should return a ranked list of primer pairs subject to the
following constraints: - The primers should be between 6 and 20 nucleotides in length (note that the primers in each pair can have
different lengths from each other). - The primer melting temperatures should both be between the submitted temperature range. - The best primer pair should be the pair which have the most similar melting temperatures.

For this task, we can follow a similar process as above, but instead of specifying a primer length, we specify a range of melting temperatures.

We already have a function to calculate the melting temperature and to calculate the second primer.

We also know that the primers must be between 6 and 20 nucleotides.

Given a region to amplify and temperature range, we can start calculating the first primer by taking the first six characters in our string and checking the temperature.

We then check if this is within the required range if so, we can store the primer-temperature pair in a dictionary.

We can then move on to the next primer using the first seven characters and check the temperature again, and so on until we either reach the maximum 20 characters or the top temperature boundary.

In the case that the temperatures are never within the range, we should return an error.

We can then run a similar process for the second primer applying the rules to calculate it which are more complex than those of the first primer, and we have chosen to keep this as a separate function.

Like we did before, we can now run a separate function to generate the final result.

I was unable to complete all tasks for this tech test. I needed more time to investigate how to find similar values in each dictionary. With the time given, I believe I should have continued to explore "the nearest neighbour problem", but continued research would have taken me longer than the allocated time.

With more time, the code could be refactored to avoid repetition bringing the functions that construct each primer into one depending on the feature the user chooses on the front end.

I would also like to provide a helpful error message to show which temperature threw the error.

I was also unable to do much in the front end in the time given.
