import os
import cv2
import numpy as np
import pickle
from collections import deque
from django.conf import settings
# import datetime as dt



STATIC_DIR = settings.STATIC_DIR
pickled_model = pickle.load(open(os.path.join(STATIC_DIR,'./models/Anamoly-detection-model.pkl'), mode='rb'))


# In[ ]:

CLASSES_LIST = ["Arson", "Normal_Videos", "Arrest", "Burglary", "Abuse", "Assault", "Explosion", "Fighting"]
def predict_on_video(video_file_path, output_file_path, SEQUENCE_LENGTH=20):
    '''
    This function will perform action recognition on a video using the LRCN model.
    Args:
    video_file_path:  The path of the video stored in the disk on which the action recognition is to be performed.
    output_file_path: The path where the ouput video with the predicted action being performed overlayed will be stored.
    SEQUENCE_LENGTH:  The fixed number of frames of a video that can be passed to the model as one sequence.
    '''
    
    # Initialize the VideoCapture object to read from the video file.
    video_reader = cv2.VideoCapture(video_file_path)

    # Code for geting the video Length.
    fps = video_reader.get(cv2.CAP_PROP_FPS)
  
    # Get the width and height of the video.
    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Initialize the VideoWriter Object to store the output video in the disk.
    video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc(*'VP80'), 
                                   video_reader.get(cv2.CAP_PROP_FPS), (original_video_width, original_video_height))

    # Declare a queue to store video frames.
    frames_queue = deque(maxlen = SEQUENCE_LENGTH)

    # Initialize a variable to store the predicted action being performed in the video.
    predicted_class_name = ''

    # Storing the prediction score and name of label.
    pred_results = dict(label=[],
                        probability=[],
                        predicted=[],
                        video_duration=[])
    
    processed_frames = 0
    # predicted_labels_probabilities = [0]
    # Iterate until the video is accessed successfully.
    while video_reader.isOpened():

        # Read the frame.
        ok, frame = video_reader.read() 
        
        # Check if frame is not read properly then break the loop.
        if not ok:
            break

        processed_frames += 1

        # Resize the Frame to fixed Dimensions.
        resized_frame = cv2.resize(frame, (64, 64))
        
        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
        normalized_frame = resized_frame / 255

        # Appending the pre-processed frame into the frames list.
        frames_queue.append(normalized_frame)
        
        # Check if the number of frames in the queue are equal to the fixed sequence length.
        if len(frames_queue) == SEQUENCE_LENGTH:

            # Pass the normalized frames to the model and get the predicted probabilities.
            predicted_labels_probabilities = pickled_model.predict(np.expand_dims(frames_queue, axis = 0))[0]

            # Get the index of class with highest probability.
            predicted_label = np.argmax(predicted_labels_probabilities)

            # Get the class name using the retrieved index.
            predicted_class_name = (CLASSES_LIST[predicted_label])

        # Write predicted class name on top of the frame.
        cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print(predicted_class_name)
        # Write The frame into the disk using the VideoWriter Object.
        video_writer.write(frame)
      
        # Displaying the output video while predicting for realtime prediction.
        cv2.imshow("preview",frame)
        
        
    # Wait key to stop the preview window.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if processed_frames != 0:
        duration = processed_frames // fps
    else:
        duration = 0

    pred_results['label'].append(predicted_class_name)    
    pred_results['probability'].append(round(max(predicted_labels_probabilities)*100,2))
    pred_results['predicted'].append(True) 
    pred_results['video_duration'].append(duration)
    # Release the VideoCapture and VideoWriter objects.
    video_reader.release()
    video_writer.release()
    cv2.destroyAllWindows()

    return pred_results



# Construct the output video path.
# test_videos_directory = './test_videos'
# SEQUENCE_LENGTH  = 20
# output_video_file_path = f'{test_videos_directory}/{"output-vid"}-Output-SeqLen{SEQUENCE_LENGTH}.mp4'

# # Perform Action Recognition on the Test Video.
# predict_on_video("./test_videos/Arrest_1.mp4", output_video_file_path, SEQUENCE_LENGTH)

# # Display the output video.
# VideoFileClip(output_video_file_path, audio=False, target_resolution=(300,300)).ipython_display()


# # In[ ]:


# # For live detection.
# predict_on_video(0, output_video_file_path, SEQUENCE_LENGTH)



# # Displaying the output after the reading process
# import cv2
# # importing libraries 
# import cv2 
# import numpy as np 

# def video_test(file_path):
# # Create a VideoCapture object and read from input file 
#     cap = cv2.VideoCapture(file_path) 

#     # Check if camera opened successfully 
#     if (cap.isOpened()== False): 
#         print("Error opening video file") 

#     # Read until video is completed 
#     while(cap.isOpened()): 
        
#     # Capture frame-by-frame 
#         ret, frame = cap.read() 
#         if ret == True: 
#         # Display the resulting frame 
#             cv2.imshow('Frame', frame) 
            
#         # Press Q on keyboard to exit 
#             if cv2.waitKey(25) & 0xFF == ord('q'): 
#                 break

#     # Break the loop 
#         else: 
#             break

#     # When everything done, release 
#     # the video capture object 
#     cap.release() 

#     # Closes all the frames 
#     cv2.destroyAllWindows() 
    

