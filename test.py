from script import BB_ZipFix
filenamezip ='/home/keith/Desktop/475 575/gradebook_CPSC575_9043_Spring_Semester_2017_Project1_Slots_2017-02-13-22-37-02.zip'
filename2   ='/home/keith/Desktop/475 575/9043\\Project1_Slots_00886464_attempt_2017-02-09-23-33-16_SlotMachineTurnIn.zip'
filename    ='/home/keith/Desktop/475 575/gradebook_CPSC575_9043\\Project1_Slots_00886464_attempt_2017-02-09-23-33-16_SlotMachineTurnIn.zip'
chartosearch ='_'

a= BB_ZipFix("toast")
short_Name_Only, short_Name_plus_ext = a._BB_ZipFix__strip_path_and_shortName(filenamezip,chartosearch)
short_Name_Only, short_Name_plus_ext = a._BB_ZipFix__strip_path_and_shortName(filename2,chartosearch)
short_Name_Only, short_Name_plus_ext = a._BB_ZipFix__strip_path_and_shortName(filename,chartosearch)
pass

