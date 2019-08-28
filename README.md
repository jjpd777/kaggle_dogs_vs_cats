# kaggle_dogs_vs_cats
For this project I decided to build a deep learning solution for the [Kaggle competition of Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats). The dataset consists of a total of 25,000 images, accounting for approximately 40GB of information.

In order to speed up the training and development process, I used [this tutorial](https://www.pyimagesearch.com/2017/09/20/pre-configured-amazon-aws-deep-learning-ami-with-python/) from PyImageSearch on setting up an Amazon Machine Image (AMI) for deep learning. I used an p2.xlarge, 61 GiB Memory EC2 instance, with access to a Nvidia K80 GPU.
I downloaded the dataset directly to my AMI via the Kaggle API, and added an additional 100GB of EBS volume to work properly with the data. 
## Data Pipeline:

### 1) Feature extraction using _ResNet50_:
- After downloading the dataset, I used the _ResNet50_ model from _Keras.applications_ with _ImageNet_ weights and without the fully connected layers. 
- The extracted feature vectors had shape (1,100352) and were saved in an HDF5 file.
---

This project comes from [Adrian Rosebrock](https://www.linkedin.com/in/adrian-rosebrock-59b8732a/) book _Deep Learning for Computer Vision_. For more information on the book, [take a look at this link.](https://www.pyimagesearch.com/deep-learning-computer-vision-python-book/)

