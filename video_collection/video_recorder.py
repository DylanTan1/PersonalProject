import cv2
import time
import imageio

def record_video(duration=2, output_file="record.gif",fps=30):
    # Turn the camera on
    cap = cv2.VideoCapture(0)
    
    # Camera error
    if not cap.isOpened():
        print("Error with opening cam")
        return
    
    # Frames list keeps all the frames of the video
    frames=[]
    start_time = time.time()
    
    # Check whether current time - start time is over the duration
    while int(time.time() - start_time) < duration:
        # Capture the frame
        # ret = whether frame capture is successful
        ret, frame = cap.read()
        
        # If successful, convert the colour and add frame to list
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)
            cv2.imshow('<<<<<<RECORDING>>>>>>', frame)
            
            # Stop early by pressing q
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Cleanup; Close camera and remove all windows
    cap.release()
    cv2.destroyAllWindows()
    
    # Save as gif
    imageio.mimsave(output_file, frames, fps=fps)