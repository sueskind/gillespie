# Chemical reactions

The Gillespie algorithm originates from this field of research. For chemical reactions we can assume a well-mixed
substance of molecules and model them with a count variable.

# Simple equilibrium reaction

We have two chemical elements `X` and `Y` that reversibly react to an `XY` molecule:

```
X + Y -> XY
XY    -> X + Y
```