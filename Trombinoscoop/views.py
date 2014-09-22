# -*- coding: utf-8 -*-

from django.http import HttpResponse

def welcome(request): 
    return HttpResponse('<?xml version="1.0" encoding="UTF-8" ?> \
<!DOCTYPE html> \
<html xmlns="http://www.w3.org/1999/xhtml"> \
  <head> \
    <title>Trombinoscoop</title> \
  </head> \
  <body> \
    <p>Bienvenue sur Trombinoscoop !</p> \
  </body> \
</html>') 
