# 🎥 Advanced Surveillance System

[![Django Version](https://img.shields.io/badge/Django-4.1.13-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-orange.svg)](https://opencv.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Djongo-green.svg)](https://www.mongodb.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-FF6F00.svg)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-grade **AI-powered anomaly detection platform** for intelligent video surveillance. Built with Django, MongoDB, TensorFlow, and OpenCV, this system detects anomalous activities in real-time or uploaded video streams with high accuracy.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [AI & Detection Workflow](#ai--detection-workflow)
- [Supported Anomaly Classes](#supported-anomaly-classes)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**Advanced Surveillance System** combines enterprise-grade backend architecture with cutting-edge computer vision to deliver intelligent video analysis. The platform processes surveillance footage through a trained deep learning model to identify anomalous activities in real-time or on-demand.

### Use Cases
- 🏪 Retail security and theft prevention
- 🏭 Industrial incident detection
- 🚔 Public safety monitoring
- 🏢 Corporate facility surveillance
- 🚗 Traffic and transportation analysis

---

## ✨ Key Features

- 🤖 **AI-Powered Detection**: Trained deep learning model for accurate anomaly classification
- 📹 **Multi-Source Support**: Process uploaded videos or live webcam streams
- ⚡ **Real-Time Processing**: Frame-by-frame analysis with instant feedback
- 🔐 **Secure Authentication**: User login, registration, and session management
- 💾 **Flexible Storage**: MongoDB for scalable document-oriented data persistence
- 📊 **Professional Dashboard**: Responsive UI with video playback and result visualization
- 🎯 **Annotated Output**: Predicted classes and confidence scores overlaid on video frames
- 📱 **Mobile-Responsive**: Clean, modern interface accessible on all devices
- 🐳 **Docker-Ready**: Containerized deployment for seamless scaling
- 📈 **High Performance**: Optimized inference pipeline with batch processing

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Django 4.1.13, Django REST Framework |
| **Database** | MongoDB 3.12 with Djongo ORM |
| **AI/ML** | TensorFlow 2.15.0, Keras 2.15.0, scikit-learn 1.3.2 |
| **Computer Vision** | OpenCV 4.9.0 |
| **Web Server** | Gunicorn 22.0.0, ASGI/WSGI |
| **Frontend** | HTML5, CSS3, JavaScript, Django Templates |
| **Data Processing** | NumPy, SciPy, pandas |
| **Containerization** | Docker |
| **Python Version** | 3.9+

---

## 📁 Project Structure

```
anomaly_detection/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── README.md                    # This file
│
├── anomaly_detection/           # Django project settings
│   ├── settings.py             # Main configuration
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI entry point
│   ├── asgi.py                 # ASGI entry point
│   └── __init__.py
│
├── app/                         # Main application
│   ├── models.py               # Database models
│   ├── views.py                # View logic & endpoints
│   ├── urls.py                 # App URL routing
│   ├── forms.py                # Django forms
│   ├── Deeplearning.py         # ML inference engine
│   ├── manger.py               # Manager utilities
│   ├── admin.py                # Django admin config
│   └── migrations/             # Database migrations
│
├── templates/                   # HTML templates
│   ├── index.html              # Home page
│   ├── video.html              # Video upload
│   ├── live_video.html         # Live streaming
│   ├── video_get.html          # Video results
│   ├── Login.html              # Authentication
│   ├── register.html
│   ├── about.html
│   ├── contact.html
│   ├── service.html
│   └── video_get.html
│
├── static/                      # Static files
│   ├── css/
│   │   └── styles.css          # Main stylesheet
│   ├── js/
│   │   └── main.js             # Client-side logic
│   ├── images/
│   └── models/
│
├── media/                       # User uploads & outputs
│   ├── videos/                 # Uploaded videos
│   └── ML_output/              # Processed results
│
└── staticfiles/                # Collected static files
```

---

## 📋 Prerequisites

Before you begin, ensure you have installed:

- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **MongoDB Community** ([Download](https://docs.mongodb.com/manual/installation/))
- **pip** (comes with Python)
- **Git** (for cloning the repository)
- **Docker** (optional, for containerized deployment)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Advanced-Surveillance-System.git
cd Advanced-Surveillance-System/anomaly_detection
```

### Step 2: Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Install System Dependencies (if needed)

For Linux/Ubuntu users, you may need to install additional libraries for OpenCV:

```bash
sudo apt-get install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev
```

### Step 5: Configure MongoDB

Ensure MongoDB is running on your system:

```bash
# Check MongoDB status
mongod --version

# Start MongoDB (if not running)
# Windows: mongod
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod
```

---

## ⚙️ Configuration

### Step 1: Update Django Settings

Edit `anomaly_detection/settings.py` with your environment-specific settings:

```python
# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_database_name',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        }
    }
}

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Step 2: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 3: Run Migrations

```bash
python manage.py migrate
```

### Step 4: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## 🎬 Quick Start

### 1. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

### 2. Access the Application

- **Home Page**: http://localhost:8000/
- **Django Admin**: http://localhost:8000/admin/ (use your superuser credentials)
- **Video Upload**: http://localhost:8000/upload/ or similar video processing page

### 3. Register an Account

1. Navigate to the registration page
2. Create a new account with email and password
3. Log in with your credentials

### 4. Upload a Video

1. Go to the video upload section
2. Select a video file from your computer
3. Wait for processing to complete
4. View results with anomaly predictions and confidence scores

### 5. Live Streaming (if enabled)

1. Navigate to the live video page
2. Allow webcam access
3. The system will display real-time anomaly predictions

---

## 💻 Usage

### Video Upload Workflow

```
Upload Video → Frame Extraction → Sequence Grouping → 
Model Inference → Frame Annotation → Result Display
```

### API Endpoints (Example)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/register/` | User registration |
| POST | `/register/` | Submit registration |
| GET | `/login/` | User login |
| POST | `/login/` | Submit login |
| POST | `/video/upload/` | Upload video for analysis |
| GET | `/video/results/<id>/` | View analysis results |
| GET | `/live/` | Live streaming page |

---

## 🤖 AI & Detection Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    VIDEO INPUT SOURCE                        │
│              (Upload or Live Stream)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │    FRAME EXTRACTION           │
        │  Extract frames from video   │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   PREPROCESSING              │
        │ • Resize frames              │
        │ • Normalize pixel values     │
        │ • Group into sequences       │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   MODEL INFERENCE            │
        │  TensorFlow/Keras Model      │
        │  Predict anomaly class       │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   POST-PROCESSING            │
        │ • Assign confidence scores   │
        │ • Map to class labels        │
        │ • Annotate frames            │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   OUTPUT GENERATION          │
        │ • Write annotated video      │
        │ • Generate results JSON      │
        │ • Store in database          │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │    RESULTS DISPLAY           │
        │  Show to user in UI          │
        └──────────────────────────────┘
```

### Detection Pipeline Details

1. **Input**: Video file (MP4, AVI, etc.) or live camera feed
2. **Frame Extraction**: Extract frames at configured FPS
3. **Normalization**: Resize to model input dimensions, normalize pixel values
4. **Sequence Grouping**: Group frames into fixed-length temporal sequences
5. **Inference**: Run through trained TensorFlow/Keras model
6. **Prediction**: Get anomaly class and confidence score
7. **Annotation**: Write predictions onto output video frames
8. **Storage**: Save results and annotated video to MongoDB + Media folder
9. **Display**: Show annotated video and results in web UI

---

## 🎯 Supported Anomaly Classes

The model is trained to detect the following anomalous activities:

| Class | Description |
|-------|-------------|
| 🔥 **Arson** | Fire/burning incidents |
| ✅ **Normal_Videos** | No anomalies detected |
| 👮 **Arrest** | Law enforcement activity |
| 🏪 **Burglary** | Breaking and entering |
| 😠 **Abuse** | Abusive behavior |
| 👊 **Assault** | Violent confrontation |

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t advanced-surveillance-system:latest .
```

### Run Container

```bash
docker run -d \
  --name surveillance-app \
  -p 8000:8000 \
  -v $(pwd)/media:/app/media \
  -e DATABASE_URL="mongodb://mongo:27017/anomaly_db" \
  advanced-surveillance-system:latest
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mongodb://mongo:27017/anomaly_db
    volumes:
      - ./media:/app/media
    depends_on:
      - mongo

  mongo:
    image: mongo:5
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

Start services:

```bash
docker-compose up -d
```

---

## 🧪 Testing

### Run Unit Tests

```bash
python manage.py test app
```

### Test Video Upload

1. Use the admin panel or web UI to upload a test video
2. Monitor logs for processing status
3. Verify results in the database and UI

---

## 🔧 Troubleshooting

### MongoDB Connection Issues

```bash
# Check MongoDB status
mongod --version

# Verify connection
mongo
```

### Model Loading Errors

- Ensure the pre-trained model file is in the correct path
- Check `Deeplearning.py` for model loading configuration
- Verify TensorFlow/Keras versions match model requirements

### Video Processing Errors

- Check video format compatibility (MP4, AVI recommended)
- Verify sufficient disk space in media folder
- Check OpenCV installation: `pip install opencv-python --upgrade`

---

## 📝 Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=anomaly_detection_db
MONGODB_HOST=localhost
MONGODB_PORT=27017
```

Load in `settings.py`:

```python
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY')
```

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

### Development Guidelines

- Follow PEP 8 style guide
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Support & Contact

- **Issues**: Please use GitHub Issues for bug reports and feature requests
- **Email**: contact@example.com
- **Documentation**: See `/docs` folder for detailed guides

---

## 🙏 Acknowledgments

- Django and DRF communities
- OpenCV for computer vision capabilities
- TensorFlow/Keras for deep learning framework
- MongoDB for flexible data storage

---

**Last Updated**: May 2026 | **Version**: 1.0.0
- Explosion
- Fighting

## Architecture Highlights

- Django handles routing, authentication, forms, views, and template rendering.
- MongoDB stores application data with a flexible schema approach.
- OpenCV manages video decoding, camera access, and output generation.
- The AI model performs sequence-based anomaly classification.
- The UI presents upload, live preview, and results screens in a structured flow.

## Project Structure

```text
anomaly_detection/
  manage.py
  anomaly_detection/
    settings.py
    urls.py
    asgi.py
    wsgi.py
  app/
    views.py
    forms.py
    models.py
    Deeplearning.py
    urls.py
    templates/
    static/
  media/
  static/
  staticfiles/
```

## Requirements

- Python 3.10 or newer
- Django 4.2
- MongoDB Atlas or local MongoDB access
- OpenCV
- NumPy
- Djongo
- MoviePy

## Setup

1. Create and activate a virtual environment.
2. Install the project dependencies:

```bash
pip install -r requirements.txt
```

3. Create a local `.env` file from `.env.example` and set your values for `DJANGO_SECRET_KEY`, `MONGODB_URI`, `MONGODB_NAME`, `MONGODB_USERNAME`, and `MONGODB_PASSWORD`.
4. Ensure the trained model file is available in the static models directory.
5. Run database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## Usage

- Register or log in to access the application.
- Upload a surveillance video for analysis.
- Start a live camera session for real-time detection.
- Review the predicted label, confidence score, and generated output video.

## UI Focus

The interface is intended to feel modern, clear, and operational rather than experimental. The layout supports surveillance workflows with a clean visual hierarchy, readable content blocks, and practical navigation for upload, live monitoring, and results review.

## Notes

- The repository includes AI inference logic and media processing code, so runtime dependencies must be installed correctly.
- Large uploaded videos and generated outputs should be managed with appropriate storage policies in production.
- Sensitive credentials should be moved to environment variables before deployment.

## Future Enhancements

- Add containerized deployment support.
- Replace local model loading with a managed model service.
- Introduce richer analytics dashboards and alerting.
- Add API endpoints for external integrations.
- Improve camera stream controls and monitoring metadata.

## License

Add your preferred license here before publishing the repository publicly.