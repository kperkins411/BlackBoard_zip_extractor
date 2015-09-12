Uses: python 3.4

IDE:  pyCharm community

Automates extracting, arranging and cleaning ridiculously formatted blackboard zip files

BB zips are so long that when extracted the path\name often overruns the limit allowed for max-path (thanks blackboard)
so this module will:
  truncate the name of the orig zip (truncname.zip)
  create a directory with the name of that zip (\truncname)
  unzip truncname.zip into \truncname
  go into \truncname
  unzip all .zip and .rar into seperate directories
  delete all .zip, .rar and mostly useless .txt files
