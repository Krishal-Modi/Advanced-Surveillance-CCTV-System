# Advanced Surveillance System

An AI-powered anomaly detection platform built with Django, MongoDB, and OpenCV for intelligent video surveillance. This project is designed to process uploaded videos or live camera streams, analyze frames with a trained deep learning model, and surface abnormal activity with a clean, responsive web interface.

## Overview

Advanced Surveillance System combines a secure Django backend with computer vision and machine learning workflows to support modern video intelligence use cases. The application can ingest surveillance footage, run frame-by-frame inference using a pre-trained anomaly detection model, and generate annotated output for review.

The platform is built to support real-world monitoring scenarios where fast detection, structured storage, and a polished user experience matter.

## Key Features

- AI-based video anomaly detection using a trained deep learning model.
- OpenCV-powered video preprocessing, frame extraction, and annotated output generation.
- Live webcam streaming for real-time monitoring use cases.
- Video upload workflow with server-side prediction and result rendering.
- Django authentication flow for login, registration, and session-based access.
- MongoDB persistence through Djongo for flexible document-oriented storage.
- Responsive templates and clean UI components for a professional dashboard-like experience.
- Media handling for uploaded videos and machine learning output files.

## Technology Stack

- Backend: Django 4.2
- Database: MongoDB with Djongo
- Computer Vision: OpenCV
- AI / ML: Pickled anomaly detection model, sequence-based video inference, NumPy-based preprocessing
- Media Processing: VideoCapture, VideoWriter, webcam streaming, frame annotation
- Frontend: Django templates, HTML, CSS, JavaScript
- Deployment Ready Components: Static files, media storage, ASGI/WSGI configuration

## AI and Detection Workflow

1. A video is uploaded or captured from a live camera feed.
2. Frames are resized, normalized, and grouped into fixed-length sequences.
3. The trained deep learning model performs inference on the frame sequence.
4. The predicted class and confidence score are generated.
5. The output video is written with prediction labels overlaid on each frame.
6. Results are returned to the UI for review and traceability.

## Supported Detection Classes

The current model is configured to recognize classes such as:

- Arson
- Normal_Videos
- Arrest
- Burglary
- Abuse
- Assault
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