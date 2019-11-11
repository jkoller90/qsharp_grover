https://docs.microsoft.com/en-us/quantum/quickstart?view=qsharp-preview&tabs=tabid-python

/* ** Operations are coroutines
Our goal is to prepare two qubits in a specific quantum state, demonstrating how to operate on qubits with Q# to change their state and demonstrate the effects of superposition and entanglement. We will build this up piece by piece to demonstrate qubit states, operations, and measurement.

Overview: In the first code below, we show you how to work with qubits in Q#. We’ll introduce two operations, M and X that transform the state of a qubit.

In this code snippet, an operation Set is defined that takes as a parameter a qubit and another parameter, desired, representing the state that we would like the qubit to be in. The operation Set performs a measurement on the qubit using the operation M. In Q#, a qubit measurement always returns either Zero or One. If the measurement returns a value not equal to a desired value, Set “flips” the qubit; that is, it executes an X operation, which changes the qubit state to a new state in which the probabilities of a measurement returning Zero and One are reversed. To demonstrate the effect of the Set operation, a TestBellState operation is then added. This operation takes as input a Zero or One, and calls the Set operation some number of times with that input, and counts the number of times that Zero was returned from the measurement of the qubit and the number of times that One was returned. Of course, in this first simulation of the TestBellState operation, we expect that the output will show that all measurements of the qubit set with Zero as the parameter input will return Zero, and all measurements of a qubit set with One as the parameter input will return One. Further on, we’ll add code to TestBellState to demonstrating superposition and entanglement.
*/
/*
Operation Set defined such that it takes parameters qubit and desired, representing state that we want the qubit to be in. 
Set performs a measurement on the qubit using M(), which always returns either 0 or 1. If M() returns a desirable value, Set flips the qubit using X()
*/