# Footballl_Players_Training
 This project uses YOLO (You Only Look Once) V8 object detection model for Training Players, GoalKeepers, Referees and Ball.

## Demo
This is how the Image looks after the model is Trained and detection is done:<br>
![To_Git](https://github.com/user-attachments/assets/259056e0-4986-4491-8d77-0383bec230fc)

## Run Locally or on Google Colab
I have run the files both on my Local PC and Google Colab.<br>
Both files can be found in the Repo.<br>

<br>Please refer the folder 'Google_Colab_Training_and_Results' for training on Google Colab:<br>

Google Colab:Players_Ball_Referee_Detection.ipynb<br>
Local Machine: Football_Players_Ball_Referee_Training.py


## Installation
Creating a new environment variable is recommended.

If Conda is available, use the following commands to create one:

```bash
conda create -n Football python==3.8

conda activate Football
```
    

Install all the Dependencies Required using the requirements file.

```bash
pip install -r requirements.txt
```

## Challenges
While Training on a Local Machine and when a Limited GPU is available, training can take a lot of time, and we might face an issue with memory allocation. <br>
![To_Git_1](https://github.com/user-attachments/assets/7fdd0deb-982b-443a-8302-5fec1d40a080)
In that case, try reducing the Batch Size to 4 or 2. 

While Training on a Local Machine and when a Limited GPU is available, you can also try reducing the Image Size to 640 or 320 if less accurate results are also acceptable.

## Results<br>
Please refer the following path for Trained Model(Trained for 50 Epochs on 372 Images):<br> [**[Trained Model
](https://drive.google.com/file/d/1-hivwD8eBcCPVU-FyDKNODZ464apmJz1/view?usp=sharing)**]

## Sources<br>
All the **source Images** are taken from:  <br>
**https://app.roboflow.com/carton-box/football_project-qi0r6/1**
