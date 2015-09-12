<b>Uses: python 3.4 <br>
IDE:  pyCharm community<br>
Automates extracting, arranging and cleaning ridiculously formatted blackboard zip files</b><br>
BB zips are so long that when extracted the path\name often overruns the limit allowed for max-path (thanks blackboard)
so this module will:<br>
  <ul>truncate the name of the orig zip (truncname.zip)<br>
  create a directory with the name of that zip (\truncname)<br>
  unzip truncname.zip into \truncname<br>
  go into \truncname<br>
  unzip all .zip and .rar into seperate directories<br>
  delete all .zip, .rar and mostly useless .txt files </ul><br>
