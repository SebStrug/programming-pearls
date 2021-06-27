# Binary Search

Binary search is a foundation for many problem solutions in the first
part of 'Programming Pearls'.

I found this particularly interesting as Bentley writes:
'I was amazed: given ample time, only about ten percent of professional
programmers were able to get this small program right...
Knuth points out that while the first binary search was published
in 1946, the first published binary search without bugs did not appear
until 1962'.

Amazing!

## Notes
1. I wrote a solution in `main.py`. This solution raises a `ValueError`
on invalid input rather than `-1` - does this still count as a valid
solution? The tests check for correct output, rather than the
algorithm running as expected. I wonder how you test algorithms
rather than outputs.
1. Alternative solutions in `alternative/`: one recursive, one iterative.
