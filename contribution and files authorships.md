# Project Contributions and Authorsinp of Files
### The project we've made is a combination of several components:

1. Data Acquisition
2. Labeling Images
3. Data Transformation
4. Exploratory Data Analysis
5. Data Modeling and making predictions

I'll briefly describe the authorship of the work done for the following components using python scripts/different tools:

#### 1. Data Acquisition: Harshit, Chingiz
We've acquired two types of datasets, we downloaded one dataset from internet and for another we gather images from google search using a tool called: Fatkun Batch Image Downloader. The link to both the datasets is present in our readme.md file.

After acquiring the first set of dataset which is prelabeled by labelimg tool, we investigated the xml files to pick 8 objects which will be used in the model. The following notebook shows it has been done.
- `ExploringDataPickItems.ipynb`



#### 2. Labeling Images: Himanshu, Harshit
We've used a tool called LabelImg(https://github.com/tzutalin/labelImg). Using this tool we've created the bounding boxes and the xml files that contains the information of the bounding boxes


#### 3. Data Transformation: Chingiz, Smith
After we have all the images and xml files accordingly, we have to make sure that the label of prelabeled dataset and self-label data are the same. We have changed the label in the prelabeled dataset to match with our labeb because the label will be used as a target class name. Since the prelabeled data consist of information about objects that we won't use in this project (not our 8 objects), the information needs to be removed from the xml record. The following notebook shows the process of the described procedure.
- `Prepare Dataset.ipynb`
- `change_name_combine.ipynb`
The model does accepts the data in .tfrecord file format so we had to convert the xml files created in setp-3 to .csv first then generate the .tfrecord files from the .csv files.
For this part we've used help from several online resources to create and modify 2 python files:
- `generate_tf_record.py`
- `xml_to_csv.py`

#### 4. Exploratory Data Analysis: Smith, Himanshu
After we have all the images and xml files accordingly, we have done some EDA to understand the characteristics of  the dataset. Firstly, objects that we focus on are cropped from original images for the purpose of analysis. Seconely, metadata of both original images and cropped images are created which include file name, width, height, size, mean, standard deviation, median, range and number of objects of the images (for original image). Then several techniques of EDA are performed such as, basic statistical analysis, principal component analysis and edge detection. The following notebooks demonstrate the steps we have described.

`cropPics.ipynb`
`EDA.ipynb`

#### 5. Data Modeling and making predictionsL: Himanshu, Harshit, Smith, Chingiz
This is the final and the biggest component of our project in which we've created 2 jupyter notebooks using online resources and Tensorflow object detection API documentation. We have trained 4 models by utilizing cloud computing resources including 3 virtual machines and 1 colab notebook. The spec of virtual machine are 2vCPU 4gb memory 50 storage and 2 VMs of 8vCPU 32gb memory. The specification for the colab notebook is Tesla K80 gpu 2 gigs ram. We have run into some problems for some VMs due to the training requ high computational cost. As a result, we only choose the best working model from a VM to illustrate the project.

In this part we've used the the official Tensorflow object detection API repository(https://github.com/tensorflow/models/tree/master/research/object_detection) and modified some files as per our use case.
The two notebooks we created are:
- `model_train_test.ipynb` Installing dependencies, downloading TF object detection API repo, downloading the dataset, training the model, exporting the frozen model
- `making_predictions_using_tf_model.ipynb` : installing dependencies, downloading TF object detection API repo, using the frozen model to make predictions


The complete code for training and testing is present in github and google drive. Since github has uploading restrictions so the TF model along
