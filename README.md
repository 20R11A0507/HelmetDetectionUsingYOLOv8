# HelmetDetectionUsingYOLOv8
This project is a naive implementation of the object detection which is done using YOLOv8 under the Ultralytics Platform.

# Methods of Execution
## To train the Model
Training a model is a very simple task in the Ultralytics package but creating a custom dataset is a time demanding process.<br>
To create the dataset we take the ***2wheelerTrafficWOHelmet.webm*** and extract the first **_N_** frames. **_N_** can be specifed in the **_img.py_** as the ***maxFrames*** variable.<br>

>[!NOTE]
>Make sure to install ***python version 3.8 and version 3.12*** as we'll use both versions

>[!TIP]
>Installing python from the Microsoft Store is easier

Install ***Thonny*** version ***4.1.4*** as it has easier access to change the python versions in that IDE. Once the installation is done under the ***tools*** tab click on ***Manage Packages***. In the pop-up, search for these 3 packages and install them.
1. opencv-python
2. Ultralytics
3. cvzone

After the installation of these packages are done execute the **_img.py_** program where **_N_** images will be saved in the folder location mentioned in the program. After the execution, under the ***run*** tab select ***Configure Interpreter*** and choose the python version as ***Python 3.8***.

After the change in version is done, under the ***Tools*** tab select ***Open system shell***. Once the shell is opened, perform
```
pip install labelimg
```
After the installation is complete, re-open the system shell and open LabelImg using the command.
```
labelimg
```
Once LabelImg is open, choose ***Open Dir*** and select the folder containing the images. Then choose ***Change Save Dir*** and select the same folder.
>[!IMPORTANT]
>Make sure that the save version is YOLO.

Click on ***Create RectBox*** and using the cursor select around the area containing the helmet or noHelmet. Keep in mind to label the ***RectBoxes*** respectively.

**Here is an example:**
![LabelImg ScreenShot](/ScreenShot1.jpg)

Make sure to save the progress and move further to the next image.

After the completion of all the ***N*** images, close ***LabelImg***. You can notice that in the folder where your images were saved ***N*** text files and a ***Classes.txt*** file is created. The ***Classes.txt*** file contains the names of the classes (i.e helmet and noHelmet). In those other text files the coordinates of each ***RectBox*** are saved respective of the Index Number of the Classes (0 and 1). In our case 0 represents ***helmet*** and 1 represents ***noHelmet***.

Create a new folder naming it accordingly, lets assume that the name is "***MainDataset***". Create new folder within the folder such that this hierarchy is followed:

- MainDataset
  - images
    - training
    - validation
  - labels
    - training
    - validation
  - data.yaml

The training and validation in both images and labels should contain all the contents of the folder containing the images that we labeled (these include ***Classes.txt***, ***helmet images*** and ***helmet labels***). Paste the ***data.yaml*** file in the ***MainDataset*** folder and make sure that the path mentioned for training and validation in the ***data.yaml*** file contains the correct path.

``` python
train: ../MainDataset/images/training
val: ../MainDataset/labels/validation

#no of classes
nc: 2

#names of the classes
names: ['helmet', 'noHelmet']
```
Zip the ***MainDataset*** folder and proceed to upload the ***MainDataset.zip*** to your ***Google Drive***.

Open ***Google Colab*** in your browser and proceed to login to the same account where you uploaded the zip file to. Upload and open the ***yolov8_helmet_noHelmet.ipyny*** in ***Google Colab***. Connect to the GPU provided by ***Google Colab*** and execute all the cells in that sequence itself.

```
%cd {HOME}
!yolo task=detect mode=predict model=yolov8n.pt conf=0.25 source='https://media.roboflow.com/notebooks/examples/dog.jpeg' show=True
```
This cell of code is just to test the Pre-Trained ***yolov8n.pt*** model that is provided by Ultralytics.

The last cell is where we train our own model with the dataset that we prepared.

```
%cd {HOME}
!yolo task=detect mode=train model=yolov8s.pt data='/content/datasets/MajorProjectNew/data.yaml' epochs=100 imgsz=800 plots=True
```
Once the training is complete a ***best.pt*** file is generated and saved in the temporary environment that is provided by ***Google Colab***. Download the ***best.pt*** file to your computer and save it to your main folder of the project.

### Your Custom Trained Model is READY!
## To predict from our Custom Trained Model
Executing the ***driver.py*** program, given that the folder that it is contained in also contains the test video and our custom trained ***best.pt*** model, you can predict ***helmet and noHelmet*** for any given video.

