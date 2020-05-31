import torch

#不初始化
print(torch.empty(5,3))

#随机初始化5x3矩阵
print(torch.rand(5,3))

#全为0，long类型
print(torch.zeros(5,3,dtype=torch.long))

x = torch.tensor([5,2])
print(x)

#从一个tensor，构造另一个tensor
x = x.new_ones(5,3,dtype=torch.double)
print(x)

x = torch.rand_like(x,dtype=torch.float)
print(x) #维度一致
print(x.size()) #是一个元组