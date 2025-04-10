Ball Bouncing Counter

Overview:
This project is a ball bouncing counter implemented using computer vision techniques with the help of OpenCV and NumPy. 
The goal is to accurately count the number of bounces of a ball in a pre-recorded video, providing insights into the ball's motion dynamics.

Modules Used:
OpenCV: Utilized for image processing and computer vision tasks. The project uses OpenCV to convert video frames to grayscale, apply Gaussian Blur, and employ the Hough Circle Transform for ball detection.

NumPy: Used for numerical operations and array manipulations. NumPy is employed to handle the array representations of image frames and circle coordinates.

Time: The time module is used to measure the duration of each bounce, facilitating the calculation of the total bounce time.

CSV: The project utilizes the csv module to log bounce count and time data into a CSV file for further analysis.

How it Works:
Ball Detection: The project starts by converting each video frame to grayscale. Subsequently, a Gaussian Blur is applied to enhance the detection process. The Hough Circle Transform is then employed to identify circles in the frame, representing the ball.

Bounce Counting: The program keeps track of the ball's motion by monitoring its vertical position in successive frames. When the ball transitions from moving upwards to downwards, a bounce is detected, and the count is incremented. The total bounce time is accumulated throughout the video.

Data Logging: The project logs the bounce count and corresponding time into a CSV file ('bounce_data.csv'). This file serves as a record for further analysis or visualization.
