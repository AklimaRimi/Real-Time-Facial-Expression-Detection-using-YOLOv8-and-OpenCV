import os
import random


images_path = 'train/images'
labels_path = 'train/labels'

os.makedirs('valid/images', exist_ok=True)
os.makedirs('valid/labels', exist_ok=True)

list_of_files = os.listdir(images_path)
random.shuffle(list_of_files)

for filename in list_of_files[:700]: 
        print(filename)    
        label_filename = filename.replace('.jpg', '.txt')
        

        if os.path.exists(os.path.join(labels_path, label_filename)):
            os.replace(images_path+'/'+filename, 'valid/images/'+ filename)
            os.replace(labels_path+'/'+label_filename,'valid/labels/'+ label_filename)