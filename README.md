# Unlocking the Power of Real-Time Face Recognition with Python
Ever wondered how machines recognize faces in real-time? Let’s build one from scratch! This project showcases a real-time face recognition system using Python, OpenCV, and the face_recognition library. From unlocking smartphones to enhancing security systems, face recognition technology is everywhere, and now you can create your own version!

## Features

- **Real-Time Detection**: Capture and recognize faces live through your webcam.
- **User-Friendly Interface**: Simple prompts for capturing images and displaying results.
- **Customizable Code**: Modify the code to meet your needs and improve functionality.

## Prerequisites

Before diving in, make sure you have the following installed:

- Python 3.x
- OpenCV
- face_recognition
- numpy
- Visual Studio C++ (for compiling dlib)

## Installation

1. Install the required libraries:
   ```bash
   pip install opencv-python opencv_contrib-python face_recognition numpy
   ```

2. Ensure Visual Studio C++ is set up with the "Desktop development with C++" package.

## Getting Started

### Step 1: Capture Training Images

Run the script to capture images of your face:

```bash
python capture_training_images.py
```

You’ll be prompted to enter your name, and once you press 'c', it will save your image.

### Step 2: Start Face Recognition

Launch the recognition script:

```bash
python face_recognition_system.py
```

Press 'q' to exit the program.

## How It Works

1. **Capture Images**: The system captures images from your webcam and saves them for training.
2. **Face Encoding**: It encodes facial features into numerical arrays for recognition.
3. **Real-Time Detection**: The program processes video frames, detects faces, and matches them against saved encodings.

## Challenges Faced

Setting up the face_recognition library was tricky due to its dependencies on Visual Studio tools. Optimizing performance for real-time detection required downscaling video frames without losing accuracy.

## Conclusion

Building this real-time face recognition system was an exciting journey that highlighted the power of computer vision technology. With just a few tweaks and modifications, you can customize this project to fit your needs!

## Learn More

For a detailed walkthrough of my journey, check out my article https://medium.com/@suditi/building-real-time-face-recognition-with-python-b0584900d631. You can also watch my Youtube video https://youtu.be/6UUCxWAH4zQ for a complete breakdown of the code and model.

Feel free to contribute or raise issues on this project!
