![gillespie](gillespie.png)

## Gilles... what?

The [Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm) is commonly used to simulate stochastic
processes. Even though it was developed in the context of chemical reactions, this algorithm can be applied to many
fields of research, e.g. chemistry, biology, epidemiology, ...

## Installation

Available on [pypi.org](https://pypi.org/project/gillespie/), install via pip:

```bash
pip install gillespie
```

## Usage

First you must define in what states the populations of your system can be. Then you model your system using three
domains:

#### 1. Initial values

A list of initial values for your states:

```python
initials = [290, 10, 0]
```

*Here we have three states in our population.*

#### 2. Propensities

A list of functions that, given the values of your current states, compute the transition rate of a reaction:

```python
propensities = [lambda s, i, r: 2 * s * i / 300,
                lambda s, i, r: 0.5 * i]
```

*Here we have two reactions that each take the three current states as input.*

#### 3. Stoichiometry

A list of incremental/decremental values for each reaction for each state:

```python
stoichiometry = [[-1, 1, 0],
                 [0, -1, 1]]
```

*Here the first reaction would decrement the first state and increment the second one. The second reaction would
decrement the second state and increment the third.*

#### 4. Run simulation

```python
import gillespie

times, measurements = gillespie.simulate(initials, propensities, stoichiometry, duration=15)
```

*Times contains all the time steps where a reaction occured. And measurements is a list of triplets with the SIR measurements in this case.*

## Examples

See [examples](examples).

To run the examples yourself the `gillespie` package is not needed to be installed. However, you will need to install
`matplotlib`:

```bash
pip install matplotlib
```

Then, clone the repo and run an example from the project root directory e.g. via:

```shell
python examples/epidemics/sir.py
```

The output plot will then be created in your working directory.
