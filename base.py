""" 
Active Learning 18

@author: Albert França Josuá Costa
@email: albertfrancajosuacosta@gmail.com
"""

import abc

__all__ = ["ActiveLearningBase"]

class ActiveLearningBase():
    
    """ Base classe for Active Learning Library """
    
    @abc.abstractmethod()
    def describe(self, describe):
        ...
