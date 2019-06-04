1. This pj owes greatly to [MaybeShewill-CV](https://github.com/MaybeShewill-CV).So please refer to [Readme.md](https://github.com/MaybeShewill-CV/attentive-gan-derainnet/blob/master/README.md) to learn about the way to operate on this pj.

2. My tiny work on attentive GAN(Tensorflow version)
Your can find my report [here](https://github.com/luochonghai/RaindropRemoval/blob/master/ReadmeMaterial/Report_HuixiangLuo_15307130012.pdf).

3. Simply set `weights_path`, `gt_path` ,`data_path` and `save_path` in predict.py, then run the command:
```
python tools/predict.py
```
You will get PSNR and SSIM metrics. When running niqe.m, you'd get NIQE metric.

### Result list 
|Model        	   					|Dataset      |PSNR    |SSIM   |NIQE   |
| -----------  	 					| ----------- | ------ | ----- | ----- |
|Torch ver        					|test_a       |31.5160 |0.9213 |3.6448 | 
|             						|test_b       |24.9249 |0.8091 |4.1802 |
|TF ver(trained by MaybeShewill-CV) |test_a       |25.7948 |0.9043 |3.7938 | 
|             						|test_b       |24.3363 |0.8409 |4.5349 |
|TF ver(smoothed mask)        		|test_a       |26.1360 |0.9109 |3.6528 | 
|             						|test_b       |24.5049 |0.8435 |4.2612 |
|TF ver(ssim-loss)        			|test_a       |26.3702 |0.9151 |3.5834 | 
|             						|test_b       |24.5303 |0.8451 |4.0724 |
