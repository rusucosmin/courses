__author__ = 'cosmin'

def representsInt(s):
    '''
    Function to return True if the :param s can be converted to int

    :param s: the string that the user has given
    :rtype : boolean
    :return: True if string s is an integer
             False is string s is not an integer
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False
