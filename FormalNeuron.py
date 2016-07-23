#FormalNeuron.py

#Variables

x0 = 0
x1 = 0
x2 = 0

w0 = 0
w1 = 0
w2 = 0

y = (x0*w0)-(x1*w1)-(x2*w2)

#Fonction Seuil
if y < 0:
	y = 0
else:
	y = 1

print(y)

