# License Plate Recognition System

This is a license plate recognition application based on PySide6 and deep learning models. The application can recognize license plates through images, videos, or real-time camera input and display the recognition results.

## Key Features

- **Image Recognition**: Users can upload an image containing a license plate, and the system will display the recognized license plate number.
- **Video Recognition**: Users can upload a video file, and the system will analyze and recognize the license plates frame by frame.
- **Real-time Recognition**: Users can turn on the camera, and the system will recognize and display license plate numbers in real-time.
- **Data Logging**: Recognition results can be logged and saved to a CSV file.
- **User Management**: Supports user registration, login, and auto-login functionality.

## Technology Stack

- **Python**: Primary programming language.
- **PySide6**: Used for building the graphical user interface.
- **OpenCV**: Handles video and image files.
- **YOLOv5**: License plate detection.
- **LPRNet**: License plate character recognition.

## Installation Steps

1. Clone the repository
'''git clone https://github.com/Luchanaaaaa/PlateDetect-QT-YOLOv5-LPRNe.git'''
2. Install dependencies:
''' pip install -r requirements.txt '''
3. Run the application:
''' python main.py '''

## Usage

- Upon starting the application, users need to register or log in first.
- After logging in, choose the recognition mode (Image, Video, Real-time).
- For images and videos, upload the files using the file dialog.
- Real-time recognition will automatically enable the camera.
- Recognition results will be displayed on the main interface, with an option to save the results.

## File Structure

- `main.py`: Entry point file for the application.
- `LogInPage_UI.py`, `SignUpPage_UI.py`, `SelectPage_UI.py`, `RecognitionWindow_UI.py`: Layout files for each interface.
- `OperationDB.py`: Handles database operations for user data.
- `myYOLODetector.py`, `myLPRNeDetector.py`: Implementation of license plate detection and recognition.
- `utils/`: Contains auxiliary functions such as plotting.

Thank you for using this application! Looking forward to your feedback and suggestions!
