#!/bin/bash

#Ping and then intrerupt
for i in google.com yahoo.com
do 
  ping -c 2 $i
  if [$? = 0] ; then
  echo "Success"
  else
  echo "Error"
  fi
done