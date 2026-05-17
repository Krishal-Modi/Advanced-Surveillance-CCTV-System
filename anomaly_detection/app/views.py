# # from django.shortcuts import redirect
# from django.shortcuts import render
# from django.http import HttpResponse
# # To connect the `machinelearning.py` to this views 
# # To connect the media_root with the pipline_model
# from django.conf import settings
# from app.models import FaceRecognition
# *************************** NEW ***********************************#
import os
# import boto3
from app.forms import AnomalyDetectForm
from app.Deeplearning import predict_on_video
from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
import threading
import cv2
import base64
from django.core.files.base import ContentFile
from django.views.decorators import gzip
# from django.http import JsonResponse

User = get_user_model()


# Create your views here.


def home(request):
    return render(request, "index.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(username=username, email=email, phone=phone, message=message)
        return redirect("/index/")

    return render(request, "contact.html")


# def video(request):
#     if request.method == 'POST':
#         video_file = request.FILES.get('video')
#         if video_file:
#             new_video = Video(video_file=video_file)
#             new_video.save()
#             return JsonResponse({'success': True, 'message': 'Video uploaded successfully.'})
#         else:
#             return JsonResponse({'success': False, 'message': 'No video file provided.'})
#     elif request.method == 'GET':
#         return render(request, 'video.html')
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def about(request):
    return render(request, "about.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return render(request, 'Login.html')

        login(request, user)
        return redirect('home')

    return render(request, 'Login.html')


def delete_user(request, user_id):
    user_instance = get_object_or_404(User, id=user_id)

    # Save the username before deleting for the success message
    username = user_instance.username

    user_instance.delete()

    # Add a success message
    messages.success(request, f"User '{username}' deleted successfully!")

    return redirect('Login')


def user_logout(request):
    logout(request)
    return redirect('Login')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        organization_Name = request.POST.get('organization_Name')

        try:
            # Check if the username already exists
            user = User.objects.get(username=username)
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'register.html')
        except User.DoesNotExist:
            try:
                # Check if the phone number already exists
                user = User.objects.get(phone=phone)
                messages.error(request, 'Phone number already registered. Please use a different one.')
                return render(request, 'register.html')

            except User.DoesNotExist:
                try:
                    # Check if the email already exists
                    user = User.objects.get(email=email)
                    messages.error(request, 'Email address already registered. Please use a different one.')
                    return render(request, 'register.html')

                except User.DoesNotExist:

                    user = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password,
                        organization_Name=organization_Name
                    )
                    messages.success(request, 'Account created successfully')
                    return redirect('Login')

    return render(request, 'register.html')


def video_get(request):
    form = AnomalyDetectForm()

    if request.method == 'POST':
        form = AnomalyDetectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)

            # extract hte image object from databse
            primary_key = save.pk
            # videos = FaceRecognition.objects.all()
            vidobj = AnomalyDetection.objects.get(pk=primary_key)
            fileroot = str(
                vidobj.video)  # It will the image from the database(aka model FaceRcoginition.image field)  .
            filepath = os.path.join(settings.MEDIA_ROOT, fileroot)
            results = predict_on_video(filepath, "./media/ML_output/process.webm")
            print(results)

            return render(request, 'video_get.html', {'form': form, 'upload': True, 'results': results})

    return render(request, 'video_get.html', {'form': form, 'upload': False})



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad!
        pass

def index(request, *args, **kwargs):
    return render(request, 'live_video_2.html')


from django.core.files.base import ContentFile
import base64
from moviepy.editor import VideoFileClip

def live_video(request):
    # if request.method == 'POST':
        # video_data = request.POST.get('video_data', None)
        # if video_data is not None:
        #     # The video data is base64-encoded, so decode it
        #     format, video_str = video_data.split(';base64,')  
        #     ext = format.split('/')[-1] 

        #     # Create a Django ContentFile object with the decoded video data
        #     video_file = ContentFile(base64.b64decode(video_str), name='temp.' + ext)

        #     # Save the video file to a temporary file
        #     temp_filename = '/tmp/temp.' + ext
        #     with open(temp_filename, 'wb') as f:
        #         for chunk in video_file.chunks():
        #             f.write(chunk)

        #     # Convert the video file to mp4
        #     clip = VideoFileClip(temp_filename)
        #     clip.write_videofile('/tmp/output.mp4')

            # Now you can use this file as input to your predict_on_video function
    results=predict_on_video(0, "./media/ML_output/process_live.webm")
            # print(results)

    return render(request, 'live_video.html',{'results':results})

    # return render(request, 'live_video.html')


# # A view for Live Streaming.
# def live_video(request):
#     return render(request, 'live_video.html')


# # To capture Video class
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()


#     def __del__(self):
#         pass


#     def get_frame(self):
#         pass


#     def update(self):
#         pass





# from django.conf import settings
# import os

# def video_get(request):
#     form = AnomalyDetectForm()

#     if request.method == 'POST':
#         form = AnomalyDetectForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             save = form.save(commit=True)

#             # extract the video object from database
#             primary_key = save.pk
#             vidobj = AnomalyDetection.objects.get(pk=primary_key)
#             fileroot = str(vidobj.video)
#             filepath = os.path.join(settings.MEDIA_ROOT, fileroot)

#             # Create the output directory if it doesn't exist
#             output_dir = os.path.join(settings.MEDIA_ROOT, "ML_output")
#             os.makedirs(output_dir, exist_ok=True)

#             # Generate the output file path
#             output_file_name = "process.webm"
#             output_file_path = os.path.join(output_dir, output_file_name)

#             results = predict_on_video(filepath, output_file_path)
#             print(results)

#             return render(request, 'video_get.html', {'form': form, 'upload':True, 'results':results})

#     return render(request, 'video_get.html', {'form': form, 'upload': False})


# def upload_file_to_s3(local_file_path, bucket, s3_file_path):
#     s3 = boto3.client('s3')
#     s3.upload_file(local_file_path, bucket, s3_file_path)


# def video_get(request):
#     form = AnomalyDetectForm()

#     if request.method == 'POST':
#         form = AnomalyDetectForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             save = form.save(commit=True)

#             # extract the video object from database
#             primary_key = save.pk
#             vidobj = AnomalyDetection.objects.get(pk=primary_key)
#             fileroot = str(vidobj.video)
#             filepath = os.path.join(settings.MEDIA_ROOT, fileroot)

#             # Create the output directory if it doesn't exist
#             output_dir = os.path.join(settings.MEDIA_ROOT, "ML_output")
#             os.makedirs(output_dir, exist_ok=True)

#             # Generate the output file path
#             output_file_name = "process.webm"
#             output_file_path = os.path.join(output_dir, output_file_name)

#             results = predict_on_video(filepath, output_file_path)
#             print(results)

#             # Upload the output file to S3
#             bucket = 'anomaly-detection'  # replace with your bucket name
#             s3_file_path = 's3://anomaly-videos/ML_output/' + output_file_name  # replace with your desired S3 file path
#             upload_file_to_s3(output_file_path, bucket, s3_file_path)

#             return render(request, 'video_get.html', {'form': form, 'upload':True, 'results':results})
    # return render(request, 'video_get.html', {'form': form, 'upload': False})