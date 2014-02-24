import re

text  = r"""
<td bgcolor="#D6F2FF" width="75">
 <font color="#5F5B5B" face="verdana" size="1">
  <div align="center">
   <b>
    12:42
    <img alt="Em veculo adaptado para portador de deficincia" border="0" src="imagens/APD.gif"/>
   </b>
  </div>
 </font>
</td>
<td bgcolor="#D6F2FF" width="75">
 <font color="#5F5B5B" face="verdana" size="1">
  <div align="center">
   <b>
    12:42
    <img alt="Em veculo adaptado para portador de deficincia" border="0" src="imagens/APD.gif"/>
   </b>
  </div>
 </font>
</td>
"""

reg = re.compile(r"""(?P<NOME>\d{2}:\d{2}).*<img.*/>""", re.S)

"""(?P<NOME>\d{2}:\d{2}).*<img.*/>"""

match = reg.findall(text)



print match
