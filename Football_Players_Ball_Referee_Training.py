# Importing os and YOLO
import os
from ultralytics import YOLO
import ultralytics

# Ensure the script entry point is guarded
if __name__ == '__main__':

    # Get the current working directory
    HOME = os.getcwd()
    print(HOME)

    # Check system environment
    ultralytics.checks()  

    # Check if GPU is available
    device = 'cuda' 
    print(f"Using device: {device}")

    # Load the pre-trained YOLOv8 model
    model = YOLO("yolov8x.pt")

    # Train the model with output folder specified
    model.train(
        # Path to your data.yaml file
        data= r'M:\Uni_Siegen\Sem-5\Projects\Football_Project\Training\Python\data.yaml',

        # Number of training epochs
        epochs=50,

        # Batch size
        batch=2,
        
        # Image size
        imgsz=1280,

        # Enable plot generation during training            
        plots=True,
    )