import numpy as np
def knn(person):
  #1 F(female = 0) , M(Male = 1)
  #2 อายุ, 
  #3 น้ำหนัก , 
  #4 ส่วนสูง
  #ผลการทำนาย ผอม = thin , สมส่วน = slim , อ้วน = fat


  x = np.array( [[1,27,60,170],
                 [1,18,70,180],
                 [0,19,64,174],
                 [0,25,80,167],
                 [1,40,56,172],
                 [0,32,45,156],
                 [1,24,52,170],
                 [1,28,70,180],
                 [0,19,45,165],
                 [1,20,120,165] ] )

  y = np.array( ['สมส่วน',
                 'อ้วน',
                 'สมส่วน',
                 'อ้วน',
                 'สมส่วน',
                 'ผอม',
                 'ผอม',
                 'สมส่วน',
                 'ผอม',
                 'อ้วน'] ) #ผลการทำนาย

  P = np.array(person)  #person
  B = np.zeros(len(y))  #body
#สูตรใช้คำนวณ
  for i,dataX in enumerate(x):
    B[i] = np.sqrt(np.sum((P-dataX)**2))  #ผลรวม
  
  minB = np.min(B) #ค่าต่ำสุด = ไกล้เคียงที่สุด
  indexMin = np.argmin(B)
  predict = y[indexMin] #ผลการทำนาย

  #return minC,indexMin,predict
  return predict 
