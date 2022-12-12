Trained DnCNN Models
====================

This directory contains the parameters of flax CNN models trained as denoisers (DnCNN) following the method described in:

Kai Zhang, Wangmeng Zuo, Yunjin Chen, Deyu Meng, and Lei Zhang. Beyond a Gaussian denoiser: residual learning of deep CNN for image denoising. *IEEE Transactions on Image Processing*, 26(7):3142–3155, July 2017.

Trained models are contained in files of the format ``dncnn<n><L|M|H>.npz``, where ``n`` is the number of layers in the model (currently 6 or 17), and ``L|M|H`` denotes the noise level at which the model was trained:

* ``L``: model trained for Gaussian noise with standard deviation of 0.06 for data in the range [0,1]
* ``M``: model trained for Gaussian noise with standard deviation of 0.10 for data in the range [0,1]
* ``H``: model trained for Gaussian noise with standard deviation of 0.20 for data in the range [0,1]


Additional trained models for a DnCNN variant with a noise standard deviation input are contained in files of the format ``dncnn<n>N.npz``, where ``n`` is the number of layers in the model (currently 6 or 17).
