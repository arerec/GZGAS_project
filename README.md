# GZGAS_project
GZGAS_project

文件说明：model.h5模型文件
        interface.py判断接口文件

使用方法：
使用命令：python interface.py 运行接口，然后访问接口

接口地址：
http://127.0.0.1:5678/predict
方法：POST
参数：6个气量数据，每一个数据代表两个月的气量和
data1 浮点型
data2 浮点型
data3 浮点型
data4 浮点型
data5 浮点型
data6 浮点型
返回：一个[0-1]的分数，小于0.5预测为民用，大于0.5预测为工商