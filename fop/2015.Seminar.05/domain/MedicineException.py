class MedicineException(Exception):
    def __init__(self, message):
        self._msg = message
    
    def __repr__(self, *args, **kwargs):
        return self._msg
