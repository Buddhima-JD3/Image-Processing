# Image Processing & Video Streaming Application

A Django-based web application that provides real-time video streaming with various image processing features including grayscale conversion, binary thresholding, and distance measurement capabilities.

## Features

### 1. **Real-Time Video Streaming**
- Live webcam video feed streaming through a web browser
- Smooth video capture at 900x600 resolution
- Motion JPEG encoding for efficient video transmission

### 2. **Image Processing Filters**
- **Normal View**: Standard webcam feed with interactive measurement tools
- **Grayscale Mode**: Convert live video to grayscale
- **Binary Mode**: Apply binary thresholding (black and white) to the video stream

### 3. **Interactive Distance Measurement**
- Click on the video canvas to mark two points
- Automatic distance calculation between marked points
- Visual representation with dotted lines connecting points
- Real-time coordinate tracking with mouse movement
- Record and manage multiple measurements in a table
- Delete or select previous measurements

### 4. **Face Detection Ready**
- Pre-configured with Haar Cascade classifiers for face detection
- Deep learning models for face mask detection
- Caffe model files for advanced face recognition

## Technology Stack

- **Backend**: Django 3.0.5
- **Computer Vision**: OpenCV (opencv-python 4.2.0.34)
- **Machine Learning**: TensorFlow 2.3.0
- **Image Processing**: 
  - NumPy 1.18.2
  - Pillow 7.1.1
  - imutils 0.5.3
- **Frontend**: 
  - Bootstrap 3.4.1
  - jQuery 3.5.1
  - HTML5 Canvas API
- **Database**: SQLite3

## Prerequisites

- Python 3.x
- Webcam/Camera device
- pip package manager

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Buddhima-JD3/Image-Processing.git
   cd Image-Processing
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your web browser and navigate to: `http://127.0.0.1:8000/`
   - Allow camera permissions when prompted

## Usage

### Main Interface
1. Launch the application and grant camera access
2. The main page displays your live webcam feed

### Distance Measurement
1. Click on the video canvas to mark the first point (a blue circle appears)
2. Click again to mark the second point
3. A dotted line connects the two points with the calculated distance
4. The measurement is automatically saved in the records table
5. Click a third time to clear and start a new measurement

### Switching Modes
- Click **"Gray Scale"** button to switch to grayscale view
- Click **"Binary"** button to switch to binary threshold view
- Each mode has its own dedicated page with the respective video filter

### Managing Measurements
- **Delete**: Click the red (×) button to remove a measurement from the table
- **Select**: Click the green (✓) button to visualize a previous measurement on the canvas

## Project Structure

```
Image-Processing/
│
├── face_detector/                    # Face detection models and data
│   ├── deploy.prototxt              # Caffe model configuration
│   ├── mask_detector.model          # Face mask detection model
│   └── res10_300x300_ssd_iter_140000.caffemodel
│
├── opencv_haarcascade_data/         # Haar Cascade classifiers
│   └── haarcascade_frontalface_default.xml
│
├── streamapp/                        # Main application
│   ├── camera.py                    # Video capture and processing classes
│   ├── views.py                     # Django views for handling requests
│   ├── urls.py                      # URL routing
│   ├── templates/streamapp/         # HTML templates
│   │   ├── home.html               # Main interface
│   │   ├── grey.html               # Grayscale mode
│   │   └── binary.html             # Binary mode
│   └── ...
│
├── video_stream/                     # Django project settings
│   ├── settings.py                  # Project configuration
│   ├── urls.py                      # Root URL configuration
│   └── wsgi.py                      # WSGI application
│
├── manage.py                         # Django management script
├── requirement.txt                   # Python dependencies
└── db.sqlite3                        # SQLite database
```

## Key Components

### Camera Classes (`streamapp/camera.py`)

- **VideoCamera**: Captures and streams normal video feed
- **GreyVideoCamera**: Converts video to grayscale using `cv2.cvtColor()`
- **BinaryVideoCamera**: Applies binary threshold to create black and white images

### Views (`streamapp/views.py`)

- `index`: Main page with normal video and measurement tools
- `grey_scale_page`: Grayscale video page
- `binary_scale_page`: Binary threshold video page
- `video_feed`: Streaming endpoint for normal video
- `grey_scale`: Streaming endpoint for grayscale video
- `binary_scale`: Streaming endpoint for binary video

## API Endpoints

- `/` - Main application page
- `/video_feed` - Normal video stream
- `/grey_scale_page` - Grayscale mode page
- `/grey_scale` - Grayscale video stream
- `/binary_scale_page` - Binary mode page
- `/binary_scale` - Binary video stream

## Dependencies Highlights

Key packages from `requirement.txt`:
- **Django 3.0.5** - Web framework
- **opencv-python 4.2.0.34** - Computer vision library
- **TensorFlow 2.3.0** - Machine learning framework
- **NumPy 1.18.2** - Numerical computing
- **Pillow 7.1.1** - Image processing
- **imutils 0.5.3** - OpenCV convenience functions

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari (with camera permissions)

## Notes

- Make sure your camera is not being used by another application
- The application requires camera permissions to function
- For production deployment, update `SECRET_KEY` in `settings.py` and set `DEBUG=False`
- Configure `ALLOWED_HOSTS` for production environments

## Future Enhancements

The codebase includes pre-configured models for:
- Face mask detection
- Face recognition using deep learning
- Advanced image processing pipelines

## License

This project is available for educational and development purposes.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## Troubleshooting

**Camera not working?**
- Ensure camera permissions are granted in your browser
- Check if another application is using the camera
- Verify the camera device is properly connected

**Dependencies installation failing?**
- Make sure you're using Python 3.x
- Try upgrading pip: `pip install --upgrade pip`
- Install system dependencies for OpenCV if on Linux

**Server not starting?**
- Check if port 8000 is available
- Ensure all migrations are applied: `python manage.py migrate`
- Verify virtual environment is activated
