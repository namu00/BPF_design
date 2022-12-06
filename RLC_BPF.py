#201921280 김남훈
# 2022년도 2학년 2학기
# 전기회로 및 실습2
# RLC직렬회로의 공진특성 그래프

import os
import platform
import numpy as np
import math
from matplotlib import pyplot as plt

#단위변수 정의
pi = math.pi   #pi
k = 10 ** (3)  #kilo
m = 10 ** (-3) #millies
u = 10 ** (-6) #micro

#교류 주파수, 첨두치 정의
Hz = np.linspace(1000,20000,1000)   #1000 Hz ~ 10000Hz를 1000등분하여 저장
kHz = np.linspace(1,20,1000)        #1kHz ~ 10kHz를 1000등분하여 저장
Vpp = np.ones(1000) * 2             #Vpp 행렬 1x1000 선언

#커패시턴스(C), 리엑턴스(L), 저항(R) 정의
C = 0.1 * u #0.1 uF
L = 10 * m  #10 mH
R = 470     #470 Ohm

#유도성/용량성 리엑턴스 정의
f = Hz
Xl = 2*pi*f*L       #Xl = 2(pi)FL
Xc = 1 / (2*pi*f*C) #Xc = 1 / (2(pi)FC)
Xt = Xl - Xc        #전체 리엑턴스 정의

#임피던스 Z정의
Z = R**2 + Xt**2
Z = np.sqrt(Z)

#공진주파수 정의
Fr = np.sqrt(L*C)
Fr = 2*pi*Fr
Fr = 1/Fr

#주파수에 따른 전류 정의
I = Vpp/Z                   #Ohm's Law에 의한 공식
I_fr = I[np.argmax(I)]*k    #공진주파수 전류
I_Band = I_fr * 0.7
#print(I_Band)


#Cut-Off 주파수 정의
# for value in I:
#    if(value == I_Band): print(value)
#    #print(value)

#print(I_Band)


#계산된 Parameter 출력
#if platform.system() == "Windows": os.system("cls") #터미널창 정리를 위한 명령어
#else: os.system("clear")                            #터미널창 정리를 위한 명령어

print("Resonant Frequency(kHz)  : %.2f kHz" % (Fr/k))
print("Resonant Impedence(Z)    : %.2f Ohm" % (Z[np.argmin(Z)]))
print("Resonant Current(mA)     : %.2f mA" % (I[np.argmax(I)]*k))

#주파수 변화에 따른 전류(I)의 변화 그래프 Plot
plt.title("RLC Series Curcuit\nF-I Curve")
plt.xlabel("Frequency (kHz)")
plt.ylabel("Current (mA)")
plt.axhline(I_Band,linestyle='--')
plt.scatter(Fr/k,I[np.argmax(I)]*k,c='r')
plt.annotate("Resonant",(Fr/k,I[np.argmax(I)]*k))
plt.plot(kHz, I*k)
plt.show()