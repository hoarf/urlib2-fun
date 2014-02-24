#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup
import re

""" 
 Changelog:

  - Corrected the encoding problems
  - Created the debug option that uses the downloaded file instead of repeatedly hitting the website for no reason

  02-2014

  This script downloads and parse shit from EPTC bus lines 
  Although now they are partners with google so it might be a better idea to use their api instead 

"""

debug = True

# data we need to pass to url form
query_args = { 
          'Tipo':'TH',
          'Linha':'620-11',
          'Veiculo':'1',
          'Sentido':'0',
          'Logradouro':'1'
}

# our target url
url = 'http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp'

# we need to encode this hash into a more accepted format by the webserver
encoded_args = urllib.urlencode(query_args)

page_file = None

if debug:
  # gets the page file from url 
  print "reading from fs..."
  page_file = open('result.txt','r')
else:
  print "reading from web..."
  page_file = urllib2.urlopen(url, encoded_args)

# reads the file into a string representation 
content = page_file.read()

# clean up mess
if debug:
  print "closing file.."
  page_file.close()

# this will help us dig through html more easily
soup = BeautifulSoup(content, from_encoding='windows_1252')

if not debug:
  # lets write this down to see how we doing so far
  with open('result.txt','w') as f:
    # lets do it as fabulous as we can tho..
    f.write(soup.prettify('windows_1252')) 

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
match_tabelas = reg_tabelas.findall(content)

# para cada tabela cria um array dos horarios
def pega_horarios_tabela(tabela):
  return reg_horarios.findall(tabela)

print "Dias Úteis:\n" + str(pega_horarios_tabela(match_tabelas[1])) +"\n"

print "Sábados:\n" + str(pega_horarios_tabela(match_tabelas[2])) + "\n"
  
line_name       = get_line_name(soup)
consortium_name = get_consortium_name(soup) 
horarios        = get_horarios(soup)

print consortium_name
print line_name
