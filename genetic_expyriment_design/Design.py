import os
from typing import Type

from expyriment import design, control, stimuli, misc, io


class Design:
    """
    Class to mount and present the experiment

    Attributes
    ----------

    n_block: int
             number of blocks (runs) of the experiment

    n_trials: int
              number of trials per block

    stim_path: str or path object
               path to the stim files

    stim_list: str or path object
               path to the files with the order for stims to be loaded. There should be one per run

    """

    def __init__(self, exp: Type[design.Experiment], n_block: int, n_trials: int, stim_path: str, stim_list: str):
        self.exp = exp
        self.n_block = n_block
        self.n_trials = n_trials
        self.stim_path = stim_path
        self.stim_list = stim_list

    def mount_design(self):
        """
        Creates a list of expyriment.design.Block objects, creates trials and loads the experimental stim
        according to the class parameters

        Returns
        -------

        exp_design: list of expyriment.design.Block objects
                    list containing the blocks, trials and stimuli ready to run
        """

        block_list = [design.Block(name='run%d' % block + 1 for block in range(self.n_block))]
        run_list = [open(filename) for filename in sorted(os.listdir(self.stim_list))]

        for block in range(self.n_block):
            for line in run_list[block].readlines():
                trial = design.Trial()
                stim = stimuli.TextLine("+")

                trial.add_stimulus(stim)

                block_list[block].add_trial(trial)

            self.exp.add_block(block_list[block])


