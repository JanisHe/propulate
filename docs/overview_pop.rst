.. _overview_pop::

Overview
========

Population-based algorithms are a class of optimization and search algorithms inspired by concepts from biological
evolution and natural selection. These algorithms maintain an entire set (or *population*) of candidate solutions where
each solution corresponds to a unique point in the search space of the problem. They are designed to solve complex
optimization problems by iteratively evolving this population of candidate solution over multiple generations.
The goal is to find the best solution within a given search space without exhaustively evaluating
every possible solution. The core idea behind population-based algorithms is to mimic the process of evolution, where
candidates with better traits have a higher chance of surviving and reproducing, passing on their advantageous traits
to the next generation. Similarly, in optimization problems, the solutions that exhibit better performance with respect
to the optimization objective are favored and used to generate new candidate solutions.

There are several popular population-based algorithms, each with its own variations and characteristics:

Evolutionary Algorithms (EAs)
    Evolutionary algorithms work by maintaining a population of potential solutions (individuals) representing
    the parameters of a solution. In each generation, individuals are selected for reproduction based on their fitness
    (how well they solve the problem). The selected individuals are then combined through crossover
    (exchange of genetic material) and mutation (random changes to genes) operations to
    produce new offspring for the next generation. Over time, the population evolves towards better solutions.

Particle Swarm Optimization (PSO)
    PSO is inspired by the behavior of bird flocks or fish schools. Each solution is represented as a "particle" that
    moves through the search space. Particles adjust their positions based on their personal best solution and the best
    solution found by any particle in the population. This encourages exploration of the search space while converging
    towards better solutions.

Covariance Matrix Adaption Evolution Strategy (CMA-ES)
    CMA-ES, or Covariance Matrix Adaptation Evolution Strategy, is an optimization algorithm designed to solve complex
    problems by efficiently searching through a solution space. It achieves this by estimating the optimal search
    direction, step size, and shape of the search space, using past solutions' performance. CMA-ES generates new
    candidate solutions based on these estimates and iteratively refines them to converge towards an optimal solution.
    It is particularly effective in challenging optimization scenarios where the landscape is irregular or difficult to
    navigate.

Differential Evolution (DE)
    Differential evolution maintains a population of candidate solutions. New solutions are generated by combining and
    perturbing the differences between different individuals. This process aims to encourage diversity in the population
    while gradually refining the solutions.

Ant Colony Optimization (ACO)
    ACO is inspired by the foraging behavior of ants. The algorithm models the search space as a graph, where solutions
    are paths through the graph. Artificial "ants" traverse the graph, depositing pheromones on paths. Solutions with
    higher pheromone concentrations are more likely to be chosen by subsequent ants, leading to the emergence of good
    solutions over time.

Cuckoo Search (CS)
    Cuckoo search simulates the behavior of cuckoo birds' reproduction strategy. Each solution corresponds to a cuckoo
    egg, and each nest represents a potential solution. Cuckoos lay eggs in nests, and the nests with better eggs
    (solutions) survive and reproduce. The algorithm involves creating new solutions by combining existing ones and
    occasionally replacing solutions to maintain diversity.
