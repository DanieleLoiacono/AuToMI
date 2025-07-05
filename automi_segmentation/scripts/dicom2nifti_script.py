import dicom2nifti

if __name__ == '__main__':

    dicom2nifti.convert_directory(
        "/home/aiart/AUTOMI/AUTOMI_new_patients/dicom/c2791efd2/",
        "/home/aiart/AUTOMI/AUTOMI_new_patients/nifti/c2791efd2",
        compression=True,
        reorient=True
    )
