#Tools lib
import numpy as np
import cv2
import re
import random
import time
import os
#Metrics lib
from metrics import calc_psnr, calc_ssim
#TF lib
import os.path as ops
import argparse
import sys
sys.path.append('../attentive-gan-derainnet')
sys.path.append('EvaluateMetric/video-quality')
from test_model import test_model_TF


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str)
    parser.add_argument("--input_dir", type=str)
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--gt_dir", type=str)
    args = parser.parse_args()
    return args

def align_to_four(img):
    #print ('before alignment, row = %d, col = %d'%(img.shape[0], img.shape[1]))
    #align to four
    a_row = int(img.shape[0]/4)*4
    a_col = int(img.shape[1]/4)*4
    img = img[0:a_row, 0:a_col]
    #print ('after alignment, row = %d, col = %d'%(img.shape[0], img.shape[1]))
    return img

if __name__ == '__main__':
    '''
    input_dir
    gt_dir
    weights_path
    '''
    #input_dir = "TF_test/"
    input_dir = "/data/RainDrop/ICIP19_rainy/test_a/data/"
    #gt_dir = "TF_gt/"
    gt_dir = "/data/RainDrop/ICIP19_rainy/test_a/gt/"
    #save_dir = "TF_res/test_a/"
    save_dir = "TF_res/test_a_15conn/"
    weights_path = "model/derain_gan/derain_gan_2019-06-03-18-25-12.ckpt-65000"

    input_list = os.listdir(input_dir)
    input_list.sort(key = lambda strs:int(re.search(r'^[0-9]+',strs)[0]))
    gt_list = os.listdir(gt_dir)
    gt_list.sort(key = lambda strs:int(re.search(r'^[0-9]+',strs)[0]))
    num = len(input_list)
    cumulative_psnr = 0
    cumulative_ssim = 0
    cumulative_niqe = 0
    for i in range(num):
        print ('Processing image: %s'%(input_list[i]))
        gt = cv2.imread(gt_dir + gt_list[i])
        cur_ssim,cur_psnr = test_model_TF(input_dir + input_list[i], weights_path, save_dir, gt_dir+gt_list[i])
        print(save_dir + input_list[i][:-4])
        result = cv2.imread(save_dir + input_list[i][:-4]+"_Done.png")
        gt = cv2.resize(gt, (result.shape[1], result.shape[0]), interpolation=cv2.INTER_LINEAR)
        if gt_dir is None:
            cur_psnr = calc_psnr(result, gt)
            cur_ssim = calc_ssim(result, gt)
        cumulative_psnr += cur_psnr
        cumulative_ssim += cur_ssim
        #cumulative_niqe += niqe(cv2.cvtColor(result,cv2.COLOR_BGR2GRAY))
    print('In testing dataset, PSNR is %.4f, SSIM is %.4f, and NIQE is %.4f'
        %(cumulative_psnr/num, cumulative_ssim/num,cumulative_niqe/num))

