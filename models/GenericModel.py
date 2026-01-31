'''
GenericModel for all models data flow
- Elemental Design
- handles operations for all element
- managing flow of information
'''
from DB.Dobject import *


class GenericModel:
    def __init__(self, information, db_handle):
        '''
        Initiates element with only Existence and makes information dictionary
        + Initiate via Dobject request
        + Edit request syncs information level
        '''
        
