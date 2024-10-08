import pathlib
import random

import numpy as np
from mpi4py import MPI

from propulate import Propulator
from propulate.propagators.nm import ParallelNelderMead
from propulate.utils import set_logger_config
from propulate.utils.benchmark_functions import (
    get_function_search_space,
    parse_arguments,
)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD

    if comm.rank == 0:
        print(
            "#################################################\n"
            "# PROPULATE: Parallel Propagator of Populations #\n"
            "#################################################\n"
        )

    # Parse command-line arguments.
    config, _ = parse_arguments(comm)

    # Set up separate logger for Propulate optimization.
    set_logger_config(
        level=config.logging_level,  # logging level
        log_file=f"{config.checkpoint}/{pathlib.Path(__file__).stem}.log",  # Logging path
        log_to_stdout=True,  # Print log on stdout.
        log_rank=False,  # Do not prepend MPI rank to logging messages.
        colors=True,  # Use colors.
    )

    rng = random.Random(config.seed + comm.rank)  # Separate random number generator for optimization.
    function, limits = get_function_search_space(config.function)  # Get callable function + search-space limits.

    # Randomly choose a start point from within the limits.
    low = np.array([v[0] for v in limits.values()])
    high = np.array([v[1] for v in limits.values()])
    start_point = np.random.default_rng(seed=config.seed + 235231).uniform(low=low, high=high)
    propagator = ParallelNelderMead(limits, rng=rng, start=start_point)
    # Set up Propulator performing actual optimization.
    propulator = Propulator(
        loss_fn=function,
        propagator=propagator,
        rng=rng,
        propulate_comm=comm,
        generations=config.generations,
        checkpoint_path=config.checkpoint,
    )

    # Run optimization and print summary of results.
    propulator.propulate(logging_interval=config.logging_interval, debug=config.verbosity)
    propulator.summarize(top_n=config.top_n, debug=config.verbosity)
