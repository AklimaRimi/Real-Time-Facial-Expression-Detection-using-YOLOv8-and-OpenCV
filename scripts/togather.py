import os


label_folder_ = f'dataset_merge/labels'
image_folder_= f'dataset_merge/images'

os.makedirs(label_folder_, exist_ok=True)
os.makedirs(image_folder_, exist_ok=True)

labels = []
for i in os.listdir('dataset_merge/Face Emotion'):
    labels.append(i)
    print(i)
    
    label_folder = f'dataset_merge/Face Emotion/{i}/labels'
    image_folder = f'dataset_merge/Face Emotion/{i}/images'
    for l in os.listdir(label_folder):
        label_path = label_folder+'/'+l
        imagepath = image_folder+'/'+l[:-4]+'.jpg'
        os.replace(label_path, label_folder_+'/'+l)
        os.replace(imagepath, image_folder_+'/'+l[:-4]+'.jpg')
        
        
        
print(labels)