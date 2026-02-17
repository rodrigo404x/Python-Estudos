medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('A medida de {}m vai dar {}cm e {}mm'.format(medida,cm,mm ))
print('A medida de {}m vai dar {}hm e {}dam, e {}dm'.format(medida, hm, dam, dm))
