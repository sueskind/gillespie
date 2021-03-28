![gillespie](gillespie.png)

## Gilles... what?

The [Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm) is commonly used to simulate stochastic
processes. Even though it was developed in the context of chemical reactions, this algorithm can be applied to many
fields of research, e.g. chemistry, biology, epidemiology, ...

## Usage

First you must define in what states the populations of your system can be. Then you model your system using three
domains:

#### Initial values

A list of initial values for your states:

```python
initials = [290, 10, 0]
```

*Here we have three states in our population.*

#### Propensities

A list of functions that, given the values of your current states, compute the transition rate of a reaction:

```python
propensities = [lambda s, i, r: 2 * s * i / 300,
                lambda s, i, r: 0.5 * i]
```

*Here we have two reactions that each take current states as input.*

#### Stoichiometry

A list of incremental/decremental values for each reaction for each state:

```python
stoichiometry = [[-1, 1, 0],
                 [0, -1, 1]]
```

*Here the first reaction would decrement the first state and increment the second one. The second reaction would
decrement the second state and increment the third.*

#### Run simulation

```python
import gillespie

times, measurements = gillespie.simulate(initials, propensities, stoichiometry, duration=15)
```

#### Examples

See [examples](examples).

**Note**: `matplotlib` must be installed to run the examples:

```bash
pip install matplotlib
```

## Installation

```bash
pip install gillespie
```