import os 

# ['Angry', 'Disgust', 'Fear', 'Happy', 'Natural', 'Sad', 'Surprised']

folder_list = ['angry', 'disgust', 'fear', 'happy', 'natural', 'sad', 'surprised']
image_folder = 'Human Face Expression.v20i.yolov8/train/images'
label_folder = 'Human Face Expression.v20i.yolov8/train/labels'

for folder in folder_list:  
    os.makedirs(f'dataset_merge/{folder.lower()}', exist_ok=True)
    os.makedirs(f'dataset_merge/{folder.lower()}/images', exist_ok=True)
    os.makedirs(f'dataset_merge/{folder.lower()}/labels', exist_ok=True)
    
    
for file_name in os.listdir(image_folder):
    

    f = file_name[:-4]
    print(f)
    f_txt = f + '.txt'
    
    if f_txt in os.listdir(label_folder):
        with open(os.path.join(label_folder, f_txt), 'r') as f:
            lines = f.readlines()
            try:
                    
                x = lines[0].split(' ')[0]
                print(x)
                f.close()
                
                new_image_folder = f'dataset_merge/{folder_list[int(x)]}/images/{file_name}'
                image_path = image_folder + '/' + file_name
                os.replace(image_path, new_image_folder)
                
                new_label_folder = f'dataset_merge/{folder_list[int(x)]}/labels/{f_txt}'
                label_path = label_folder + '/' + f_txt
                
                print(label_path)
                print(new_label_folder)
                os.replace(label_path, new_label_folder)
            except:
                print('error')
                

        
        
        
            
           
    
    
    
    
    
    