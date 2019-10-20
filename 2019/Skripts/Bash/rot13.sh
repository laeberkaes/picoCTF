#!/bin/bash

echo ROT13:
read v

echo $v | tr 'A-Za-z' 'N-ZA-Mn-za-n'
