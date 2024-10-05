import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import cv2
from tkinter import messagebox
from recognition import shared_name,shared_img

cred = credentials.Certificate('C:\\Users\\DELL\\OneDrive\\Desktop\\My Folder\\imagecollect-8443a-firebase-adminsdk-vbtun-9dde5f7eaf.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://imagecollect-8443a-default-rtdb.asia-southeast1.firebasedatabase.app/','storageBucket': 'imagecollect-8443a.appspot.com'})

def generate_random_filename():
    random_uuid = uuid.uuid4()
    random_filename = str(random_uuid).replace('-', '')
    return random_filename

def upload_image_to_storage(person_name, image_path):
    random_filename = f"{person_name}_{generate_random_filename()}.jpg"
    image_bytes = cv2.imencode('.jpg', image_path)[1].tobytes()
    bucket = storage.bucket()
    blob = bucket.blob(f'images/{random_filename}')
    blob.upload_from_string(image_bytes, content_type='image/jpeg')

#person_image_path = r'C:\Users\DELL\OneDrive\Desktop\internship\internship_project\people\Vicky Kaushal\gettyimages-1257870759-612x612.jpg'
upload_image_to_storage(shared_name,shared_img)
print("Image is detected and uploaded on cloud...")
response=messagebox.showinfo('Notification','Image is detected and uploaded on cloud...')
#print("shared in upload is: ",shared_name, shared_img)