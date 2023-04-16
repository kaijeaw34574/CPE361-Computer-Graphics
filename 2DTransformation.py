# 2D transformation
#
# Created by Pornthep Sangthongkhamsuk ID: 63070503431

import numpy as np
import math
from decimal import *

def matt(a,b):
  A = np.array([[0,0,a], [0,0,b], [0,0,1]])
  return A
def translation(A,b,c):
  B = np.array([[1,0,b], [0,1,c], [0,0,1]])
  C = B.dot(A)
  return C
def scaling(A,b,c):
  B = np.array([[b,0,0], [0,c,0], [0,0,1]])
  C = B.dot(A)
  return C
def rotation(A,b):
  B = np.array([[np.cos(math.radians(b)),-np.sin(math.radians(b)),0], [np.sin(math.radians(b)),np.cos(math.radians(b)),0], [0,0,1]])
  C = B.dot(A)
  return C
def mirrorX(A):
  B = np.array([[1,0,0], [0,-1,0], [0,0,1]])
  C = B.dot(A)
  return C
def mirrorY(A):
  B = np.array([[-1,0,0], [0,1,0], [0,0,1]])
  C = B.dot(A)
  return C
def output(A):
  X = '%.3f'% A[0][2]
  Y = '%.3f'% A[1][2]
  print("("+ X +", "+ Y +")")

points = [matt(1,1), matt(2,1), matt(3,1), matt(4,1), matt(5,1), matt(6,1), matt(7,1), matt(8,1), matt(9,1), matt(10,1), matt(10,2), matt(10,3), matt(10,4), matt(10,5), matt(10,6), matt(10,7), matt(10,8), matt(10,9), matt(10,10), matt(9,9), matt(8,8), matt(7,7), matt(6,6), matt(5,5), matt(4,4), matt(3,3), matt(2,2)]
a = float(input())
if a == 1:
# translation
  b = float(input())
  c = float(input())
  for A in points:
    A = translation(A,b,c)
    output(A)

elif a == 2:
# scaling
  b = float(input())
  c = float(input())
  d = float(input())
  e = float(input())
  for A in points:
    A = translation(A,-d,-e)
    A = scaling(A,b,c)
    A = translation(A,d,e)
    output(A)
  
elif a == 3:
# rotation
  b = float(input())
  c = float(input())
  d = float(input())
  for A in points:
    A = translation(A,-c,-d)
    A = rotation(A,b)
    A = translation(A,c,d)
    output(A)

elif a == 4:
# mirror
  b = float(input())
  if b == 1:
# mirror x
    c = float(input())
    for A in points:
      A = translation(A,0,-c)
      A = mirrorX(A)
      A = translation(A,0,c)
      output(A)
  elif b == 2:
# mirror y
    c = float(input())  
    for A in points:
      A = translation(A,-c,0)
      A = mirrorY(A)
      A = translation(A,c,0)
      output(A)
  elif b == 3:
# mirror rotate
    c = float(input())
    for A in points:
      A = rotation(A,-c)
      A = mirrorX(A)
      A = rotation(A,c)
      output(A)