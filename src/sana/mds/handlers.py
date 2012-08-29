'''
Created on Feb 29, 2012

:Authors: Sana Dev Team
:Version: 2.0
'''
import logging

#must import the local module models for the handlers
from sana.mds.models import *
from sana.core import handlers
from sana.api.decorators import logged
from sana.mds.signals import *

__all__ = ['ConceptHandler', 'RelationshipHandler','RelationshipCategoryHandler',
           'DeviceHandler', 
           'EncounterHandler', 
           'NotificationHandler', 
           'ObservationHandler', 
           'ObserverHandler',
           'ProcedureHandler',
           'RequestLogHandler',
           'SubjectHandler',]

# Get an instance of a logger

@logged
class ConceptHandler(handlers.ConceptHandler):
    """ Handles concept requests. """
    allowed_methods = ('GET', 'POST')
    model = Concept
    logger = (signal_logger, done_logging)

@logged
class RelationshipHandler(handlers.RelationshipHandler):
    """ Handles concept relationship requests. """
    allowed_methods = ('GET', 'POST')
    model = Relationship
    
@logged
class RelationshipCategoryHandler(handlers.RelationshipCategoryHandler):
    """ Handles concept relationship category requests. """
    allowed_methods = ('GET', 'POST')
    model = RelationshipCategory


@logged
class DeviceHandler(handlers.DeviceHandler):
    """ Handles device requests. """
    allowed_methods = ('GET', 'POST')
    model = Device

@logged
class EncounterHandler(handlers.EncounterHandler):
    """ Handles encounter requests. """
    model = Encounter
    
    def create(self,request,*args,**kwargs):
        pass

@logged
class NotificationHandler(handlers.NotificationHandler):
    """ Handles notification requests. """
    allowed_methods = ('GET', 'POST')
    model = Notification

@logged
class ObservationHandler(handlers.ObservationHandler):
    allowed_methods = ('GET', 'POST')
    model = Observation

@logged 
class ObserverHandler(handlers.ObserverHandler):
    """ Handles observer requests. """
    allowed_methods = ('GET', 'POST')
    model = Observer
    
@logged
class ProcedureHandler(handlers.ProcedureHandler):
    allowed_methods = ('GET', 'POST')
    model = Procedure

class RequestLogHandler(handlers.RequestLogHandler):
    """ Handles network request log requests. """
    allowed_methods = ('GET', 'POST')
    model = RequestLog


@logged
class SubjectHandler(handlers.SubjectHandler):
    """ Handles subject requests. """
    model = Subject

    
    