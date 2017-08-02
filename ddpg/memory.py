from collections import deque
from logging import Logger
from numpy import random


class Memory:
    def __init__(
        self, minlen=0, maxlen=2**16, batch_size=2**5, validator=None
    ):
        self.buffer     = deque([], maxlen=maxlen)
        self.full       = False

        self.batch_size = batch_size
        self.minlen     = minlen
        self.maxlen     = maxlen
        self.validator   = validator or (lambda x: True)

    def __len__(self):
        return len(self.buffer)

    def all(self):
        return self.buffer

    def store(self, experience):
        if self.validator(experience):
            if not self.full and len(self) >= self.maxlen:
                Logger.debug('Memory bank is full ({})'.format(self.maxlen))
                self.full = True
            self.buffer.append(experience)
            return True
        else:
            raise ValueError('Invalid experience: {}'.format(experience))

    def get_batch(self, batch_size=None):
        batch_size = batch_size or self.batch_size

        if batch_size > len(self):
            raise ValueError('Memory only has {} experiences! Cannot fulfill batch size {}.'.format(len(self), batch_size))
        if len(self) < self.minlen:
            raise ValueError('Memory does not have enough experiences!')

        return random.choice(self.buffer, size=batch_size)
