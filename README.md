# Capstone Project 1, Drexel University
## Data Collection
There were two primary ways we had obtained our data. First being a pre-made dataset that we had tailored for our needs and the second being the manualy scraped images of the web that we then label.

1. Manualy scraped images:
    - We download the images containing the objects we are interested in.
    - Open the files in `labelImg` and draw bounding boxes around the target objects. 
2. Premade dataset:
    - https://github.com/tobiagru/ObjectDetectionGroceryProducts#holoselecta

Our complete data corpus contains a combination of images from the first and second approach. This way we obtain a decently sized dataset as well demonstrate the expertise in obtainig and preparing datasets. 

Link to a final cleaned dataset with the xml metadata files as well as tensorflow representation of the data. 
- [Google Drive](https://drive.google.com/drive/folders/17BqR0APW45aGXbQR9VqAN1oVrTyK7uWe?usp=sharing)

## Data Transformation
- For the Data transformation part we are going to use LabelImg, it is a graphical image annotation tool.
- It is written in Python and uses Qt for its graphical interface, we would be using this for creating the bounding boxes in the images from our datasets.
- After the bounding boxes are created we would label the image such that the images that we predict get classified by the bounding boxes.
- Annotations are saved as XML files in PASCAL VOC format.
 

## Data exploration
  - We can visualize some images and their masks.
  - We can plot the distribution of image sizes.
  - We can try smoothing the images.
  - Derivative with Respect to X of the images.
  - We can find the gradient magnitude of the images.
  - Second Derivatives with Respect to X of the images.
  - We can find the magnitude of the curl of the gradient.



## Modeling(Transfer Learning)
- For the modeling part we are using a technique called Transfer Learning
- Transfer Learning will help in reducing the time to create our own object detection setup instead we’ll use a pre-trained object detection API like Tensorflow Object Detection - API.
- These two models will help us in identifying the objects/person in a video feed
  - [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)

- These models are trained to identify 100 different classes in a frame like dog, cat, person, glass etc. We will retrain these models to identify 8 custom items that we’re putting in our shop demo.
- Apart from this we will also use OpenCV library in the future so that we can manipulate the results coming in from the video feed to establish a certain relationship between different items, different persons and relationship of the person with the item.

## Future Capstone 2 work: Post Processing
- After we have successfully trained our model to identify items from pictures, the item will be linked with its information i.e. price, weight or any information that benefits to manage a grocery store.
- The item information may be stored in a hash table like a Python dictionary.
- The model will be also trained to detect a person as an object. In this case, we will start with one person in a frame.
- The next task is to identify when a person grabs an item from the shelf. A script will trigger the model to identify what item a person has picked along with the coordinate of the bounding box created by the model.
- For more frames of the video that are fed into the model, the object will be tracked with the person until he/she puts it back to the shelf.
- One problem that we expected to occur is that the model will give a fault detection due to the environment of the picture such as distance of the object to the camera. We have planned to solve the problem by calculating the ratio of object size with respect to distance of an object to the camera. However, we may encounter unexpected problems that cause the performance of the model after we deploy it to the real environment. Therefore, we will try our best to pinpoint problems and improve the model. For the worst case scenario which the problem cannot be fixed in time, we will pinpoint all the problems and possible solutions then include them as future work for our project. 

## Reference

> https://github.com/tzutalin/labelImg

> https://www.kaggle.com/muonneutrino/exploration-transforming-images-in-python
