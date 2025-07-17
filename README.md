# AuToMI
This repository contains the models developed for the AuToMI project.

# automi_segmentation
 A project called AUTOMI that involves the segmentation of organs in CT images using deep learning.

 One of the goals of the project was to automatically segment lymph nodes and the spleen in full-body CT scans. This segmentation is needed for radiotherapy treatment planning, but doing it manually is very time consuming. The specific treatment is Total Marrow Irradiation (TMI) or Total Marrow and Lymph-node Irradiation (TMLI).

 We share in this repository:
 
 - A U-Net training pipeline used in one of our articles on segmentation of the Planning Target Volume (PTV) for TMI/TMLI.
 - A nnU-Netv2 model that segments the Clinical Target Volume (CTV) for TMI/TMLI: https://zenodo.org/records/15812720
 - Scripts that add the prediction to an RTSTRUCT file.

To use the nnU-Netv2 model to predict the CTV for your TMI/TMLI patients, you will need to follow the instructions for inference described in the nnU-Netv2 repository: https://github.com/MIC-DKFZ/nnUNet

I will briefly summarize the steps needed for inference. If you have any technical problems, please look for details on the provided nnU-Net link.

To use the model, you will need to create, for example, an Anaconda environment and install the nnunetv2 python package.
Having this set up, you will need to activate this new environment and set up environment variables. These variables are the fixed paths, where you would have your raw training data, the pre-processed data, and the model-related data. In this case, we only have the model's data, and that is all you need, but nevertheless, you need to set up the other environment variables:

Set environment variables
export nnUNet_raw="/home/aiart/nnUnetAUTOMI/dataset/nnUnet_raw"
export nnUNet_preprocessed="/home/aiart/nnUnetAUTOMI/dataset/nnUNet_preprocessed"
export nnUNet_results="/home/aiart/nnUnetAUTOMI/dataset/nnUNet_results"

If you are starting with a DICOM volume, use the script in this repository called "scripts/dicom2nifti_script.py" and change the path of DICOM folder to match your DICOM's folder path.

Using the NIFTI file, you must check that its location and its name are in the correct format. If your file is named "patient", the nifti file must be in a folder named "patient" and the file needs to have '_0000' after its name, like the following example: '.../patient/patient_0000.nii.gz'
Now, you can start by running the prediction command of the nnU-Netv2:
nnUNetv2_predict -i PATH_TO_NEW_PATIENT_FOLDER -o PATH_TO_FOLDER_PREDICTIONS -d 03 -c 3d_fullres

Finally, using the NIFTI prediction of the CTV can be added to an RTSTRUCT file using the script "scripts/nifti2rtstruct_script.py".

To verify the prediction and its spatial orientation and alignment with the DICOM volume, you can use 3DSlicer to visualize the volume and the RTSTRUCT.

 

