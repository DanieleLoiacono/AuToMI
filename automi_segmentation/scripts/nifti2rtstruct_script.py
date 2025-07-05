'''
Turns a nifti segmentation into a newly created DICOM RTSTRUCT file.
'''

from rt_utils import RTStructBuilder
import nibabel as nib
import numpy as np

#rtstruct = RTStructBuilder.create_from(dicom_series_path="/home/aiart/AUTOMI/AUTOMI_new_patients/dicom/0c0bbe81/", rt_struct_path="/home/aiart/AUTOMI/AUTOMI_new_patients/dicom/0c0bbe81/RS1.2.752.243.1.1.20250617160256223.2680.44462.dcm")
rtstruct = RTStructBuilder.create_new(dicom_series_path='/home/aiart/AUTOMI/AUTOMI_new_patients/dicom/c2791efd2/')

# Read nifti segmentation prediction file
nifti_pred = nib.load('/home/aiart/AUTOMI/AUTOMI_new_patients/pred/c2791efd2.nii.gz')
nifti_pred = nifti_pred.get_fdata()
nifti_pred = nifti_pred.transpose(1, 0, 2)
# flip the nifti_pred to match the DICOM coordinate system
nifti_pred = np.flip(nifti_pred, axis=0)
nifti_pred = np.round(nifti_pred / np.max(nifti_pred)).astype("int8")
nifti_pred = nifti_pred > 0

rtstruct.add_roi(mask=nifti_pred, name='CTV_pred', roi_number=1)

rtstruct.save('/home/aiart/AUTOMI/AUTOMI_new_patients/rtstruct/c2791efd2/c2791efd2.dcm')