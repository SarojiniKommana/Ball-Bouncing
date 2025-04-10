import cv2
import numpy as np
import time
import csv
def  detect_ball(frame):
     # Converting  the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian Blur to the grayscale frame using GuassianBlur 
    gray_blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # Use the Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=10,
                               maxRadius=100)

    # If circles are detected, draw a rectangle around the first one
    if circles is not None:
        circles = np.uint16(np.around(circles))
        circle = circles[0, 0]  # selecting the first detected circle
        x, y, radius = circle # storing x y cordinates and radius of first detected circle
        x, y, radius = int(x), int(y), int(radius)  # Convert to integers
        cv2.circle(frame, (x, y), radius, (0,0,255), 2)
        return (x,y)
    return None

# Input video file
cap = cv2.VideoCapture(r"bounce.mp4")

bounce_count = 0
prev_center = None
upward = False
start_time = time.time()
total_bounce_time = 0  # Initialize total bounce time

# Create and open a CSV file to write data
csv_file = open('bounce_data.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['BOUNCE COUNT', 'TIME'])


while True:
    ret, frame = cap.read()
    if not ret:
        break
    (x,y)=detect_ball(frame)
    if (x,y) is not None:
        if prev_center is not None:
            if y > prev_center:
                upward = False
            elif y < prev_center and not upward:
                bounce_count += 1
                upward = True
                # Accumulate the total time of bounces
                current_time = time.time()
                total_bounce_time += current_time - start_time
                start_time = current_time

                # Print data in terminal and write to CSV
                csv_writer.writerow([bounce_count, total_bounce_time])

        # Display the total bounce time on the top-right corner
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, f'Bounce Count: {bounce_count}', (10, 30), font, 1, (255, 255, 255), 4, cv2.LINE_AA)
        cv2.putText(frame, f'Time: {total_bounce_time:.2f} s', (frame.shape[1] - 250, 30), font, 1,
                    (255, 255, 255), 2, cv2.LINE_AA)

    prev_center = y

    cv2.imshow('BALL_BOUNCINGCOUNT', frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()

# Close the CSV file
csv_file.close()