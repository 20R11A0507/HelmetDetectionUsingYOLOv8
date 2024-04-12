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

Install ***Thonny*** version ***4.1.4*** as it has easier access to change the python versions in that IDE. Once the installation is done
execute the **_img.py_** program where **_N_** images will be saved in the folder location mentioned in the program. After the execution, under the ***run*** tab
select ***Configure Interpreter***. Choose the python version as ***Python 3.8***.

After the change in version is done, under the ***Tools*** tab select ***Open system shell***. Once the shell is opened perform
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
