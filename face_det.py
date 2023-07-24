from tkinter import*
from PIL import ImageTk, Image
import face_recognition
from tkinter import messagebox
import cv2
import numpy as np
import os
from datetime import datetime
import csv
#import mysql.connector

a=Tk()
a.title("collage")
a.geometry("500x500")
a.config(bg="pink")
#text
t=Text(a,height=2,width=15,bg="white",fg="black")
t.place(x=350,y=250)
t1=Text(a,height=2,width=15,bg="white",fg="black")
t1.place(x=350,y=300)

#lable
l=Label(a,text="BUDDY'S COMPANY",font=("Timesnewroman",20),bg="white",fg="black",height=3,width=50)
l.place(x=100,y=100)
l1=Label(a,text="USER NAME",font=("Timesnewroman",20),bg="white",fg="black",height=1,width=10)
l1.place(x=150,y=250)
l2=Label(a,text="PASSWARD",font=("Timesnewroman",20),bg="White",fg="black",height=1,width=10)
l2.place(x=150,y=300)



def face_detect():
    y=t.get("1.0",'end-1c')
    y1=t1.get("1.0",'end-1c')
    
    username="sharan"
    pasward="1234"
    
    if username==y and pasward==y1:
        messagebox.showinfo("START","IF YOU WANT QUITE USE Q KEY")
        
    
        '''db=mysql.connector.connect(host="localhost",user="root",passwd="Sharanmilky",database="login")
        b=db.cursor()'''
    
        video_capture=cv2.VideoCapture(0)
        employee_1=face_recognition.load_image_file('C:\\Users\\karth\\OneDrive\\Pictures\\facce_rg\\ajith.jpg')
        employee_1_encoding=face_recognition.face_encodings(employee_1)[0]
        employee_2=face_recognition.load_image_file('C:\\Users\\karth\\OneDrive\\Pictures\\facce_rg\\dq.jpeg')
        employee_2_encoding=face_recognition.face_encodings(employee_2)[0]
        employee_3=face_recognition.load_image_file('C:\\Users\\karth\\OneDrive\\Pictures\\facce_rg\\pike.jpg')
        employee_3_encoding=face_recognition.face_encodings(employee_3)[0]
        employee_4=face_recognition.load_image_file('C:\\Users\\karth\\OneDrive\\Pictures\\facce_rg\\str.jpg')
        employee_4_encoding=face_recognition.face_encodings(employee_4)[0]

        employee_faces_encoding=[employee_1_encoding,employee_2_encoding,employee_3_encoding,employee_4_encoding]
        employee_faces_names=["ajith","dq","pike","str"]

        employee=employee_faces_names.copy()

        face_locations=[]
        face_encodings=[]
        face_names=[]
        s=True

        now=datetime.now()
        current_date=now.strftime("%Y-%m-%d")
        employee_data = []
        #f=open(current_date+'.csv','w+',newline='')
        #lnwriter=csv.writer(f)
        
        while True:
            _,frame=video_capture.read()
            small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            #rgb_small_frame=small_frame[:,:,::-1]
            if s:
                face_locations=face_recognition.face_locations(rgb_small_frame)
                face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
                face_names=[]
                for face_encoding in face_encodings:
                    matches=face_recognition.compare_faces(employee_faces_encoding,face_encoding)
                    name=""
                    face_distance=face_recognition.face_distance(employee_faces_encoding,face_encoding)
                    best_match_index=np.argmin(face_distance)
                    if matches[best_match_index]:
                        name=employee_faces_names[best_match_index]

                    face_names.append(name)
                    if name in employee_faces_names:
                        if name in employee:
                            employee.remove(name)
                            print(employee)
                            current_time=now.strftime("%H-%M-%S")
                            '''lnwriter.writerow([name,current_time])
                            employee_data.append([name,current_time])
                            with open(filename, 'w+', newline='') as f:
                                lnwriter = csv.writer(f)
                                lnwriter.writerows(employee_data)'''
                            
            cv2.imshow("attendence system",frame)
            if cv2.waitKey(1)& 0xFF ==ord('q'):
                break
            '''key=cv2.waitKey(1)
            if key==81 or key==113:
                break'''

        '''a="INSERT INTO present(name,time,date1)VALUES (%s,%s,%s)"
        f=[(name,current_time,current_date)]
        b.executemany(a,f)
        db.commit()'''
        video_capture.release()
        cv2.destroyAllWindows()
        f.close()
    else:
        messagebox.showerror("wrong","USERNAME OR PASSWARD INCORRECT")

b=Button(text="DETECTED THE FACE",activebackground="RED",activeforeground="blue",height=2,width=20,bg="white",command=face_detect)
b.place(x=400,y=400)
