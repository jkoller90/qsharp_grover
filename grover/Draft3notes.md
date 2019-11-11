https://docs.microsoft.com/en-us/quantum/quickstarts/search?view=qsharp-preview&tabs=tabid-python

Grover's algorithm asks whether an item in a list is the one we are searching for. It does this by constructing a quantum superposition of the indexes of the list with each coefficient, or probability amplitude, representing the probability of that specific index being the one you are looking for.

At the heart of the algorithm are two steps that incrementally boost the coefficient of the index that we are looking for, until the probability amplitude of that coefficient approaches one.

The number of incremental boosts is fewer than the number of items in the list. This is why Grover's search algorithm performs the search in fewer steps than any classical algorithm.




end:

The ReflectAboutMarked operation is called only four times, but your Q# program was able to find the "01010" input amongst 25=32 possible inputs!