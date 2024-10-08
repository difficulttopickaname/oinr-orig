import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
import os

def load_npy(file_path):
    try:
        data = np.load(file_path)
        print(f"data {file_path} is of shape {data.shape}")
        return data
    except Exception as e:
        print(f"error: {e}")
        return None

def show_slices(mri_data):  # center slices
    x_center = mri_data.shape[0] // 2
    y_center = mri_data.shape[1] // 2
    z_center = mri_data.shape[2] // 2

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(mri_data[x_center, :, :], cmap='gray')
    axes[0].set_title(f'Sagittal Slice (X={x_center})')

    axes[1].imshow(mri_data[:, y_center, :], cmap='gray')
    axes[1].set_title(f'Coronal Slice (Y={y_center})')

    axes[2].imshow(mri_data[:, :, z_center], cmap='gray')
    axes[2].set_title(f'Axial Slice (Z={z_center})')

    plt.show()

def resample_z_axis(mri_data, target_slices=20, method='subset'):
    z_slices = mri_data.shape[2]

    if method == 'subset':
        step = z_slices // target_slices
        resampled_data = mri_data[:, :, ::step]
    elif method == 'interpolation':
        zoom_factor = target_slices / z_slices
        resampled_data = zoom(mri_data, (1, 1, zoom_factor))
    else:
        raise ValueError("Method must be 'subset' or 'interpolation'")
    
    return resampled_data

if __name__ == "__main__":
    """
    fp = "/home/minhan/mr_machine_updated/data/"  # 91, 109, 91 036_S_5271.npy
    sp = "/home/minhan/oinr/original/sequence/sliced_data/"

    for filename in os.listdir(fp):
        mri_data = load_npy(fp + filename)
        resampled_mri_data = resample_z_axis(mri_data, target_slices=20, method='subset')
        # show_slices(resampled_mri_data)

        np.save(sp + filename, resampled_mri_data)
    """
    d = load_npy("sequence/result/adni/Results/13/final_output/final_prediction.npy")
    show_slices(d)