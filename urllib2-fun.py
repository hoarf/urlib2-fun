import urllib2
import urllib
from bs4 import BeautifulSoup
import re

""" 
  02-2014

  This script downloads and parse shit from EPTC bus lines 
  Although they are partners with google it might be better idea to use their api 

"""

with open('linhas.txt','r') as arquivo:
  for l in arquivo:
    chomp
    print l

# data we need to pass to url form
query_args = { 
          'Tipo':'TH',
          'Linha':'620-11',
          'Veiculo':'1',
          'Sentido':'0',
          'Logradouro':'1'
}

linhas = []

linhas["267-7"] 

linhas["267-7"]["consorcio"] = "consorcio"
linhas["267-7"]["consorcio"] = "consorcio"
 

# our target url
url = 'http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp'

# we need to encode this hash into a more accepted format by the webserver
encoded_args = urllib.urlencode(query_args)

# gets the page file from url 
page_file = urllib2.urlopen(url, encoded_args)

# reads the file into a string representation 
content = page_file.read()

# devs of yore didn't know about encoding it seems...
sane_content = unicode(content, errors='ignore')

# this will help us dig through html more easily
soup = BeautifulSoup(sane_content)

# lets write this down to see how we doing so far
with open('result.txt','w') as f:
  # lets do it as fabulous as we can tho..
  f.write(soup.prettify()) 

# alright _now_ the fun begins

# a function to get us the consortium name
def get_consortium_name(soup):
  for tag in soup.find_all("B", text=re.compile("Cons")):
    return tag

# a function to get us the name of the line
def get_line_name(soup):
  for tag in soup.find_all("div", text=re.compile(".+\-.+")):
    return tag.text

def get_horarios(soup):
  pass

# cria uma expressao regular que traz uma lista das tabelas do site
reg_tabelas = re.compile(r"<table.*?>.*?</table>", re.S)
reg_horarios = re.compile(r"\d{2}:\d{2}")

# aplica a expressao regular para o conteudo do site
match_tabelas = reg_tabelas.findall(sane_content)

# para cada tabela cria um array dos horarios
def pega_horarios_tabela(tabela):
  return reg_horarios.findall(tabela)

print "horarios tabela dias :\n" + str(pega_horarios_tabela(match_tabelas[1])) +"\n"

print "horarios tabela sabado:\n" + str(pega_horarios_tabela(match_tabelas[1])) + "\n"
  
line_name       = get_line_name(soup)
consortium_name = get_consortium_name(soup) 
horarios        = get_horarios(soup)

print consortium_name
print line_name