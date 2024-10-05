import cv2 as cv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.geometry('250x150')
root.configure(bg='lavender')
img = None

haar_cascade = cv.CascadeClassifier(r'C:\Users\DELL\OneDrive\Desktop\My Folder\internship\internship_project\Face_Recognition\haar_face.xml')

people = ['ShahrukhKhan', 'Vicky Kaushal', 'Ben Affleck']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

def open_file_dialog():
    global img,shared_name, shared_img
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("jpg", "*.jpg"), ("All files", "*.*")])
    if file_path:
        print("Selected file:", file_path)
        img = cv.imread(file_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Person', gray)
        #print("image is: ",img)
        shared_name, shared_img = detect_and_display_faces(gray)
        #print("shared is: ",shared_name, shared_img)
        return shared_name, shared_img
    else:
        print("No file selected.")

def detect_and_display_faces(gray):
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y + h, x:x + w]
        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')
        cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('Detected Face', img)
    response=messagebox.showinfo('Notification','Image is detected and uploaded on cloud...')
    return people[label], img

button = tk.Button(root, text="Select Image", command=open_file_dialog,width=10,height=2)
button.pack(pady=50)
root.mainloop()
cv.waitKey(2000)