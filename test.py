import numpy as np

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

load_npy("sequence/sliced_data/002_S_0295.npy")