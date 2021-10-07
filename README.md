## ✔ REAL TIME HUMAN DETECTION & COUNTING
- An application which allows to detect human or people's in any image, video or even through Camera.
- Also along with detecting, it also counts the maximum no. of people appeared.
- It also visualize the data of no. of human detected and the avg. accuracy with which humans got detected w.r.t. time, using graph plot.

****

### REQUIREMENTS :
- python 3
- tkinter
- filedialog from tkinter
- messagebox
- from PIL import Image, ImageTk
- cv2
- argparse
- matplotlib.pyplot
- numpy
- time
- os
- tensorflow

****

### How this Script works :
- User just need to download the file and run the main.py on their local system.
- On th starting window of the application, user will be able to see START and EXIT option, using which user can start the application or exit from the application.
- When user starts the application using START button, a new window will open, which allows user with options like, DETECT FROM IMAGE, DETECT FROM VIDEO or DETECT FROM CAMERA.
- When user selects any of the first two option, he/she needs to select the respective files using SELECT button.
- User can preview the selected file using PREVIEW button, and detect and count the humans using DETECT button.
- And when user selects, the last option of detecting through camera, user need to open the Camera, using OPEN CAMERA button, As soon as camera opens, detection process will start.
- After detection process gets completed or user manually completes it, two graph get plotted, 1.) Enumeration Plot(Human Count Vs. time) and 2.) Avg. Accuracy Plot(Avg. Accuracy Vs. time).
- Along with this two plots, an option to generate crowd report also appears, On clicking on it, a crowd report in form of PDF is generated ans saved autmatically at the project file location.
- In the crowd report genrated, there will be information like, What is Max Human Count, Max Accuracy, Max Avg. Accuracy, and also a two line status about crowd.

### Purrpose :
- This scripts helps user to easily get the count of human through real time image, video or camera, and thereafter also analysis of crowd through crowd report.

### Compilation Steps :
- Install all the required libraries.
- After that download the code file, and run main.py on local system.
- Then the script will start running and user can explore it by detecting the human and also getting the count of it.

****

### SCREENSHOTS :

<p align="center">
  <img width = 1000 src="Images/1.jpg" /><br>
  <img width = 1000 src="Images/2.jpg" /><br>
  <img width = 1000 src="Images/3.jpg" /><br>
  <img width = 1000 src="Images/4.jpg" /><br>
  <img width = 1000 src="Images/5.jpg" /><br>
  <img width = 1000 src="Images/6.jpg" /><br>
  <img width = 1000 src="Images/7.jpg" /><br>
  <img width = 1000 src="Images/8.jpg" /><br>
</p>


