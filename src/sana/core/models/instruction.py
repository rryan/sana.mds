"""
The subject model for the Sana data engine.

:Authors: Sana dev team
:Version: 2.0
"""

from django.db import models
_app="core"
## ?Procedure step. First iteration
class Instruction(models.Model):
    
    class Meta:
        app_label = _app
    concept = models.ForeignKey('Concept')
    ''' Contextual information about the instruction '''
    
    predicate = models.CharField(max_length=64)
    ''' The predicate logic used for this instruction within a decision tree.'''
    
    algorithm = models.CharField(max_length=64)
    ''' The name of an algorithm used to calculate a score for the instruction.'''
    
    compound = models.BooleanField(default=False)
    ''' True if this Instruction has child instructions. '''

    boolean_operator = models.CharField(max_length=64, blank=True)
    ''' The logical operator to apply when evaluating children if compound.'''

    
    
    