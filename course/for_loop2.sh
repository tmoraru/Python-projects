#!/bin/bash

#Ping and then intrerupt and clear the screen if is success and only print success or in other case, error
for i in google.com yahoo.com
do 
  clear
  ping -c 2 $i > /dev/null  2>&1
  if [ $? = 0 ] ; then
  echo "Success"
  else
  echo "Error"
  fi
done