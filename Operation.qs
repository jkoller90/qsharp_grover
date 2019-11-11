namespace Quantum
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

    