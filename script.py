#!python
__author__ = 'Perkins'
import zipfile,os
import sys
#import patoolib     #to unextract .rar files
import logging

'''
orig_zipfile        name of the zip downloaded from bb
delete_text_files   delete text files that come in
show_results        show stats
'''
class BB_ZipFix:
    def __init__(self,orig_zipfile,char_to_search = "_"):
        self.logger = logging.getLogger(__name__)
        self.orig_zipfile   = orig_zipfile
        self.char_to_search = char_to_search

        #the ones to be deleted (add .txt if needed
        self.black_list = ['.sdf']
        self.white_list = ['.zip','.rar']
        self.logger.info("Will delete Blackboard .txt files")
        self.logger.info("Will unzip .rar and .zip files")

    def __shortenName_then_unzip_to_dir_then_delete_zip(self,path_plus_origName_Plus_Ext,char_to_search):
        #strip out relative parts
        path_plus_short_Name_No_Ext, path_plus_short_Name_Plus_Ext = self.__strip_path_and_shortName(path_plus_origName_Plus_Ext,char_to_search)

        #shorten giant scholar name
        self.__renamefile(path_plus_origName_Plus_Ext,path_plus_short_Name_Plus_Ext)

        #unzip into directory(make it if necessary)
        if self.__unzip_to_dir(path_plus_short_Name_Plus_Ext,path_plus_short_Name_No_Ext):
            self.__DeleteFile(path_plus_short_Name_Plus_Ext)

        #where it was unzipped to
        return path_plus_short_Name_No_Ext

    def setupProjects(self):
        """
        Shrinks name of orig zip
        unzips to a dir of same name (call it parentdir)
        extracts all zip, rar files in that dir to new dirs
        deletes .txt and .zip,.rar files in parentdir
        :return: nothing
        """
        try:
            path_plus_short_Name_No_Ext = self.__shortenName_then_unzip_to_dir_then_delete_zip(self.orig_zipfile,self.char_to_search)

            #change into newly created dir and delete files with  self.black_list extensions
            #unzip those with white list extensions
            self.__extract_and_clean_allfiles(path_plus_short_Name_No_Ext)
        except:
            self.logger.info("Error in setupProjects",exc_info=True)

    def __extract_and_clean_allfiles(self,path):
        #better than nothing check
        if(path==None or path=="c:\\"):
            return False

        dirs= os.listdir(path)
        for file in dirs:
            filename, file_extension = os.path.splitext(file)
            try:
                if   file_extension in self.black_list:
                    self.__DeleteFile(path+ "\\" + file)
                elif file_extension in self.white_list:
                    #first extract all from zip or rar
                    pathandfile=os.path.join(path, file)
                    self.__shortenName_then_unzip_to_dir_then_delete_zip(pathandfile,self.char_to_search)
                else:
                    self.logger.debug("<B>found file that is in neithe white or blacklist:" + file +"</b>")
            except:
                self.logger.info("Error in __extract_and_clean_allfiles",exc_info=True)

        return True

    def __DeleteFile(self,path_Plus_file):
           try:
                os.remove(path_Plus_file)
                self.logger.info("Deleted file:"+path_Plus_file)
           except:
                self.logger.debug("Error in __DeleteFile:", exc_info=True)

    def __unzip_to_dir(self,zippedfile,dest_directory):
        ret = True
        try:
             #unzip into directory(make it if necessary)
            tmpZip = zipfile.ZipFile(zippedfile)
            tmpZip.extractall(dest_directory)
            self.logger.info("Extracting files to:"+dest_directory)
        except:
            self.logger.debug("Error Unzipping zip:" + zippedfile + "\ntrying rar:", exc_info=True)
            filenameonly,file_ext = os.path.splitext(zippedfile)
            if file_ext == '.rar':
                try:
                    #OK lets try .rar extractor
                    #first create directory
                    if not os.path.exists(dest_directory):
                        os.makedirs(dest_directory)
                        self.logger.info("   Unzip failed trying .rar file to:"+dest_directory)
                    #then extract
                    # patoolib.extract_archive(zippedfile,verbosity=1, outdir=dest_directory)
                except:
                    self.logger.debug("Error cannot extract rar file", exc_info=True)
                    ret= False
        return ret


    #strips the rubbish that scholar appends while preserving the extension
    #returns the path,
    def __strip_path_and_shortName(self,filename, char_to_search):
        #find second  occurrence of '_'
        sep = os.path.sep
        if len(filename)>0:
            try:
                path,filename_plus_ext =  os.path.split(filename)
                if path:
                    path +=sep
                filenameonly,file_ext = os.path.splitext(filename_plus_ext)
                tmp = filenameonly.split(char_to_search,3)

                short_Name_Only = path
                for val in tmp:
                    r= val.find("00")
                    if r != -1:
                        short_Name_Only = path+ val[r:r+8]
                        break


                short_Name_plus_ext = short_Name_Only+ file_ext

                self.logger.debug("Original giant zip:"+ filename)
                self.logger.debug("Short zip:"+ short_Name_plus_ext)

                return[short_Name_Only, short_Name_plus_ext ]

            except ValueError:
                self.logger.debug("ERROR: " + self.orig_zipfile +" did not contain " + char_to_search)


    #just renames a file, prints exeption info if thrown
    def __renamefile(self,origname,newname):
        try:
            os.rename(origname,newname)
            self.logger.debug("Renamed:"+ origname + " to " +newname)
        except:
            self.logger.debug("Error renaming file:", exc_info=True)
            raise  #jig is up if you cannot even rename a file


    #extract zip, expects path, will create a folder called filename without the ext
    def __extractZip(self,path,filename):
        pass

def main():
    # Configure only in your main program clause
    logging.basicConfig(level=logging.DEBUG,
                        filename='bbzipfix.log', filemode='w',
                        format='%(name)s %(levelname)s %(message)s')
    #if user passed a filename
    filename = int(sys.argv[1])
    bb = BB_ZipFix("filename")
    bb.unzip_to_dir()

if __name__ == "__main__":
    main()
