# -*- coding:utf-8 -*-
from gensim import models
import numpy as np
from sklearn.decomposition import PCA
import jieba
import gensim
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import jieba.analyse
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import word2vec, KeyedVectors,Word2Vec
import jieba.posseg as pseg #加载各库
import pkuseg
import csv
import itertools
import matplotlib.pyplot as plt
import nltk
# -*- coding:utf-8 -*-




jycfyc=[['制备','研究'],['无机','轨道'],['有机','电子'],['化学','力学'],['染料','强化'],['显微镜','减少'],['半导体','水解'],['腐蚀','电阻'],['导电','吸水性'],['疏水性','离子'],['元素','结果'],['粒子','问题'],['氧化','曲线'],['旋转','光束'],['左手','反射率'],['夹层','粉末'],['纤维','凝胶'],['天然','熔融'],['水解','碳'],['金属','平衡'],['新型','扫描'],['条件','数值'],['原理','梯度'],['TEM','激光'],['红外','氧化铝'],['破坏','硅'],['机械','矿物'],['复合材料','滚动'],['抗氧化','磁导率'],['DNA','钢'],['波动','薄膜'],['表面波','负压'],['简化','幅度'],['压力','全面'],['系数','丙烯'],['特殊','混合'],['颗粒','苯'],['石墨','镧系'],['凝聚','脱硫'],['电压','纳米'],['电流','热导率'],['铝粉','学科'],['浪费','流体'],['钛合金','组织'],['丙烯','晶体'],['相变','涂层'],['氧化','辐照'],['界面','传感器'],['电容器','局部'],['正极','工艺'],['电子','流体'],['电池','铝粉'],['钛合金','储能'],['塑料','玻璃'],['黄铜','原子'],['正电','硬度'],['表面','简化'],['薄膜','流体'],['电子','粒径'],['电容','强度'],['纳米','电流'],['机械','脱硫'],['电镜','无机'],['样品','苯'],['碳','金属'],['石墨','金属'],['电化学','高分子'],['直径','热'],['纤维','计算'],['组织','分析'],['电负性','腐蚀'],['离子键','发展'],['前景','金属'],['氢键','Cu'],['晶格','Fe'],['恒温','C'],['能级','水解'],['价带','工艺'],['强度','电压'],['退火','电流'],['紫铜','电阻'],['聚合物','热导率'],['加聚','铁'],['导电性','粉末'],['载流子','旋转'],['超导性','体积'],['极化率','红外'],['吸收','相变'],['折射','搅拌'],['折射','氧化'],['荧光','溶液'],['反射','溶液'],['磁化','阳离子'],['抗磁性','阴离子'],['化学','正极'],['化学','减少'],['物理','铝粉'],['热加工','丙烯'],['加工','镧系'],['光伏','DNA']]

matrix = [[0 for i in range(2)] for i in range(500)]
for i in range(0,100):
 matrix[i][0] = jycfyc[i][0]
 matrix[i+100][0] = jycfyc[i][0]
 matrix[i + 200][0] = jycfyc[i][0]
 matrix[i + 300][0] = jycfyc[i][0]
 matrix[i + 400][0] = jycfyc[i][0]
 matrix[i][1] = jycfyc[i][1]
 j = i+1
 if j > 99:
  j = j-100
 jj = i+2
 if jj > 99:
  jj = jj-100
 jjj = i+3
 if jjj > 99:
  jjj = jjj-100
 jjjj = i + 4
 if jjjj > 99:
  jjjj = jjjj - 100
 matrix[i + 100][1] = jycfyc[j][1]
 matrix[i + 200][1] = jycfyc[jj][1]
 matrix[i + 300][1] = jycfyc[jjj][1]
 matrix[i + 400][1] = jycfyc[jjjj][1]
model = gensim.models.Word2Vec.load('word2vec0824.model')
print(len(matrix))
taiy = ['太阳能电池','光电','受体','光伏电池','吸光层','DSCs','器件','能源','铅卤化物','转换','半导体','n-型','光伏','发光','染料','敏化','光热','杂化','光催化','电致','空穴','钙钛矿太阳能电池','太阳能电池材料']
dian = ['电池','锂离子','负极','正极','电流','电池硅','锂电池','LiCoO2','电压','LIBs','锂','脱嵌','电容','LiNi1-x-y','非锂离子','CoxMnyO2','储能','热电池','锰酸','电压','硅碳','Sn基','石墨']

matriy = [[0 for i in range(2)] for i in range(500)]
cc = list(itertools.combinations(taiy, 2))
matriy[:250]=cc[:250]
dd = list(itertools.combinations(dian, 2))
matriy[250:]=dd[:250]
print(len(matriy))
print(matriy)

res=[]
for i in range(0,500):
 try:
  cosin = model.wv.similarity(matriy[i][0],matriy[i][1]) #计算任意两个词向量之间的余弦相似度
  res.append(cosin)
 except:
  cosin = 0  # 计算任意两个词向量之间的余弦相似度
  res.append(cosin)
y_pred = res
print(y_pred)

for i in range(0,500):
 try:
  cosin = model.wv.similarity(matrix[i][0],matrix[i][1]) #计算任意两个词向量之间的余弦相似度
  res.append(cosin)
 except:
  cosin = 1  # 计算任意两个词向量之间的余弦相似度
  res.append(cosin)
y_pred = res


for i in range(0,1000):
    if y_pred[i]>0.4:
        y_pred[i]=1
    else:
        y_pred[i]=0
print(len(y_pred))
print(y_pred)

def storFile(data, fileName):
    with open(fileName, 'w', newline='') as f:
        mywrite = csv.writer(f)

        for i in data:
            mywrite.writerow([i])

data = y_pred
print(data)
storFile(data, "ha.csv")


sns.set()
f,ax=plt.subplots()
C2 = [[473,27],[404,96]] #【473不相关判定为不相关TN，27不相关判定为相关FN】【404相关判定为不相关FP，96相关判定为相关TP】[Based on
# TN, FN, FP and TP, calculate Accuracy, Precision, F-score, Recall from website)# [00,01],[10,11]
print(C2)
h=sns.heatmap(C2,annot=False,ax=ax,cbar=False,linewidths=1,annot_kws={'size':28, 'fontproperties':'Times New Roman', 'weight':'bold'})
plt.rcParams['font.family']="Times New Roman"
plt.tick_params(labelsize=28)
cb = h.figure.colorbar(h.collections[0])
cb.ax.tick_params(labelsize=28)

ax.set_title('confusion matrix',fontsize=28,fontproperties = 'Times New Roman') #标题
ax.set_xlabel('prediction',fontsize=28,fontproperties = 'Times New Roman') #x轴
ax.set_ylabel('true',fontsize=28,fontproperties = 'Times New Roman') #y轴
plt.show()

