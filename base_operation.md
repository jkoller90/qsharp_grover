https://www.youtube.com/watch?v=3WWrQXcktqc

namespace HelloWorld
{
    open Microsoft.Quantum.Intrinsic;

    operation QuantumRandomNumberGenerator() : Result {
      using ( q = Qubit()){
        H(q);
        let r = M(q);
        Reset(q);
        return r;
      }
    }
}
First we start with a qubit initalizated in the state 0 and apply H to create a superposition in which the probabilities for 0 and 1 are the same. Then we measure the qubit and save the output.

  

https://docs.microsoft.com/en-us/quantum/quickstarts/qrng?view=qsharp-preview

When measured, a qubit can only be either 0 or 1. However, during execution the state of the qubit represents the probability of reading either a 0 or a 1 with a measurement. This probabilistic state is known as superposition. We can use this probability to generate random numbers.

In our Q# operation, we introduce the Qubit datatype, native to Q#. We can only allocate a Qubit with a using statement. When it gets allocated a qubit is always in the Zero state.

Using the H operation, we are able to put our Qubit in superposition. To measure a qubit and read its value, you use the M intrinsic operation.

By putting our Qubit in superposition and measuring it, our result will be a different value each time the code is invoked.

When a Qubit is de-allocated it must be explicitly set back to the Zero state, otherwise the simulator will report a runtime error. An easy way to achieve this is invoking Reset.


In the Bloch sphere the north pole represents the classical value 0 and the south pole represents the classical value 1. Any superposition can be represented by a point on the sphere (represented by an arrow). When the closer the end of the arrow to a pole, the higher the probability the qubit collapses into the classical value assigned to that pole when measured. For example, the qubit state represented by the red arrow below has a higher probability of giving the value 0 if we measure it.


Since the outcome of the measurement is completely random, we have obtained a random bit. We can call this operation several times to create integers. For example, if we call the operation three times to obtain three random bits, we can build random 3-bit numbers (that is, a random number between 0 and 7).
