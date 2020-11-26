The project we've made is a combination of several components:

1. Data Acquisition
2. Exploratory Data Analysis
3. Labeling Images
4. Data Transformation
5. Data Modeling and making predictions

I'll briefly describe the authorship of the work done for the following components using python scripts/different tools:

1. Data Acquisition: Harshit, Chingiz
We've acquired two types of datasets, we downloaded one dataset from internet and for another we gather images from google search using a tool called: Fatkun Batch Image Downloader
The link to both the datasets is present in our readme.md file.


2. Exploratory Data Analysis: Smith, Himanshu


3. Labeling Images: Himanshu, Harshit
We've used a tool called LabelImg(https://github.com/tzutalin/labelImg). Using this tool we've created the bounding boxes and the xml files that contains the information of the bounding boxes

4. Data Transformation: Chingiz, Smith
The model does accepts the data in .tfrecord file format so we had to convert the xml files created in setp-3 to .csv first then generate the .tfrecord files from the .csv files.
For this part we've used help from several online resources to create and modify 2 python files:
-> generate_tf_record.py
-> xml_to_csv.py

5. Data Modeling and making predictionsL: Himanshu, Harshit, Smith, Chingiz
This is the final and the biggest component of our project in which we've created 2 jupyter notebooks using online resources and Tensorflow object detection API documentation. ,
In this part we've used the the official Tensorflow object detection API repository(https://github.com/tensorflow/models/tree/master/research/object_detection) and modified some files as per our use case.
The two notebooks we created are:

1. model_train_test.ipynbInstalling dependencies, downloading TF object detection API repo, downloading the dataset, training the model, exporting the frozen model
2. making_predictions_using_tf_model.ipynb: installing dependencies, downloading TF object detection API repo, using the frozen model to make predictions


The complete code for training and testing is present in github and google drive. Since github has uploading restrictions so the TF model along with official repository is sitting on google drive(https://drive.google.com/drive/folders/1_yaNEU4rQFk6Abj0GnmaOBxImpVt2g71?usp=sharing)
