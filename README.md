# Capstone Project 1, Drexel University
## Data Collection
There are two ways that we could obtain the training data. Manual - where we scrape the internet for the images or a dataset route, where we download the images as part of the dataset.

1. we go the scraping route we have two options:
  - Fatkun - extension would allow us with the least amount of preparation to download the images that are present on the screen. So we could use google search to narrow down the list of images that we would like to download. 
  - We could also go down the manual path of writing a Python scraper, but this would most likely be overkill. We would only go this route if we find data in the dynamically loaded pages. 
2. If we do decide to follow the dataset path we could use one of the datasets listed in this public repository:
  - https://github.com/tobiagru/ObjectDetectionGroceryProducts
Our final decision will strongly depend on the requirements of this class, since using a ready dataset could yield the best result, but may not satisfy the amount of effort this class requires to be placed on the data exploration step. 

Dataset that we currently use
- https://drive.google.com/drive/folders/1OofnsREqF1QNfUqZPZgcXu2VkWr2JUMA

## Data Transformation
- For the Data transformation part we are going to use LabelImg, it is a graphical image annotation tool.
- It is written in Python and uses Qt for its graphical interface, we would be using this for creating the bounding boxes in the images from our datasets.
- After the bounding boxes are created we would label the image such that the images that we predict get classified by the bounding boxes.
- Annotations are saved as XML files in PASCAL VOC format, and also, it also supports YOLO format, which we would be using in this project.
- Data exploration
  - We can visualize some images and their masks.
  - We can plot the distribution of image sizes.
  - We can try smoothing the images.
  - Derivative with Respect to X of the images.
  - We can find the gradient magnitude of the images.
  - Second Derivatives with Respect to X of the images.
  - We can find the magnitude of the curl of the gradient.

>> Reference

>> https://github.com/tzutalin/labelImg

>> https://www.kaggle.com/muonneutrino/exploration-transforming-images-in-python

## Modeling(Transfer Learning)
- For the modeling part we’re going to use a technique called Transfer Learning
- Transfer Learning will help in reducing the time to create our own object detection setup instead we’ll use a pre-trained object detection API like Tensorflow Object Detection - API or YoloV3
- These two models will help us in identifying the objects/person in a video feed
  - [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
  - [YoloV3](https://pjreddie.com/darknet/yolo/)

- These models are trained to identify 100 different classes in a frame like dog, cat, person, glass etc. We will retrain these models to identify 8 custom items that we’re putting in our shop demo
- Apart from this we will also use OpenCV library so that we can manipulate the results coming in from the video feed to establish a certain relationship between different items, different persons and relationship of the person with the item.

## Post Processing
- After we have successfully trained our model to identify items from pictures, the item will be linked with its information i.e. price, weight or any information that benefits to manage a grocery store.
- The item information may be stored in a hash table like a Python dictionary.
- The model will be also trained to detect a person as an object. In this case, we will start with one person in a frame.
- The next task is to identify when a person grabs an item from the shelf. A script will trigger the model to identify what item a person has picked along with the coordinate of the bounding box created by the model.
- For more frames of the video that are fed into the model, the object will be tracked with the person until he/she puts it back to the shelf.
- One problem that we expected to occur is that the model will give a fault detection due to the environment of the picture such as distance of the object to the camera. We have planned to solve the problem by calculating the ratio of object size with respect to distance of an object to the camera. However, we may encounter unexpected problems that cause the performance of the model after we deploy it to the real environment. Therefore, we will try our best to pinpoint problems and improve the model. For the worst case scenario which the problem cannot be fixed in time, we will pinpoint all the problems and possible solutions then include them as future work for our project. 

