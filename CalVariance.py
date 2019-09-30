# -*- coding: utf-8 -*-
import numpy as np
import scipy.io as scio
def CalVariance(nums):
    """
    计算方差
    :param nums:传入的数组
    :return:
    """
    # 求均值
    arr_mean = np.mean(nums)
    # 求方差
    arr_var = np.var(nums)
    # 求标准差
    arr_std = np.std(nums, axis=0)
    print(arr_std)
def Variance(versicolor_petal_length):
    # Array of differences to mean: differences
    differences = versicolor_petal_length - np.mean(versicolor_petal_length)
    # Square the differences: diff_sq
    diff_sq = np.square(differences)
    # Compute the mean square difference: variance_explicit
    variance_explicit = np.mean(diff_sq)
    # Compute the variance using NumPy: variance_np
    variance_np = np.var(versicolor_petal_length)
    # Print the results
    print(variance_explicit, variance_np)

if __name__=='__main__':
    lizhenghao = "mos.txt"
    content = [line.rstrip('\n') for line in open(lizhenghao, 'r',encoding='utf-8')]
    scores=[]
    for i in content:
        scores.append(float(i))
    # CalVariance(scores)
    Variance(scores)
    # data = scio.loadmat('dmos.mat')
    # sss=data.get('dmos')
    # CalVariance(sss)