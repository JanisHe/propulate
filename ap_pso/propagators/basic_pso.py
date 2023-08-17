"""
This file contains the first stateful PSO propagator for Propulate.
"""
from random import Random
from typing import Dict, Tuple, List

import numpy as np

from ap_pso import Particle, make_particle
from propulate.propagators import Propagator


class BasicPSOPropagator(Propagator):

    def __init__(self, w_k: float, c_cognitive: float, c_social: float, rank: int,
                 limits: Dict[str, Tuple[float, float]], rng: Random):
        """
        Class constructor.
        :param w_k: The learning rate ... somehow
        :param c_cognitive: constant cognitive factor to scale p_best with
        :param c_social: constant social factor to scale g_best with
        :param rank: the rank of the worker the propagator is living on in MPI.COMM_WORLD
        :param limits: a dict with str keys and 2-tuples of floats associated to each of them
        :param rng: random number generator
        """
        super().__init__(parents=-1, offspring=1)
        self.c_social = c_social
        self.c_cognitive = c_cognitive
        self.w_k = w_k
        self.rank = rank
        self.limits = limits
        self.rng = rng
        self.laa: np.ndarray = np.array(list(limits.values())).T  # laa - "limits as array"

    def __call__(self, particles: List[Particle]) -> Particle:
        old_p, p_best, g_best = self._prepare_data(particles)

        new_velocity: np.ndarray = self.w_k * old_p.velocity \
                                   + self.rng.uniform(0, self.c_cognitive) * (p_best.position - old_p.position) \
                                   + self.rng.uniform(0, self.c_social) * (g_best.position - old_p.position)
        new_position: np.ndarray = old_p.position + new_velocity

        return self._make_new_particle(new_position, new_velocity, old_p.generation + 1)

    def _prepare_data(self, particles: List[Particle]) -> Tuple[Particle, Particle, Particle]:
        """
        Returns the following particles in this very order:
        1.  old_p: the current particle to be updated now
        2.  p_best: the personal best value of this particle
        3.  g_best: the global best value currently known
        """
        if len(particles) < self.offspring:
            raise ValueError("Not enough Particles")

        own_p = [x for x in particles if x.rank == self.rank]
        old_p = max(own_p, key=lambda p: p.generation)

        if not isinstance(old_p, Particle):
            old_p = make_particle(old_p)
            print(
                f"R{self.rank}, Iteration#{old_p.generation}: Type Error. "
                f"Converted Individual to Particle. Continuing.")

        g_best = min(particles, key=lambda p: p.loss)
        p_best = min(own_p, key=lambda p: p.loss)

        return old_p, p_best, g_best

    def _make_new_particle(self, position: np.ndarray, velocity: np.ndarray, generation: int):
        """
        Takes the necessary data to create a new Particle with the position dict set to the correct values.
        :return: The newly created Particle object
        """
        new_p = Particle(position, velocity, generation, self.rank)
        for i, k in enumerate(self.limits):
            new_p[k] = new_p.position[i]
        return new_p
