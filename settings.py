import pickle
import logging

class Settings:
    '''
    A crappy class for saving a single string
    Overwrites file every time
    should use pickle instead
    '''

    def __init__(self,fileName):
        self.filename=fileName
        self.logger = logging.getLogger(__name__)

    def stateSave(self,strdata):
        try:
            fileObject = open(self.filename,'w')
            fileObject.write(strdata)
            fileObject.close()
        except:
            self.logger.debug("Cannot save state:", exc_info=True)

    def stateRestore(self):
        retval = ''

        try:
            fileObject = open(self.filename,'r')
            retval = fileObject.readline()
            fileObject.close()
        except:
            self.logger.debug("Cannot open UIState file, initilizing state to defaults:",exc_info=True)

        return retval