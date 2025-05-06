import os


labels = []
for i in os.listdir('dataset_merge'):
    labels.append(i)
    
print(labels)



for i in labels:
    label_folder = f'dataset_merge/{i}/labels'
    image_folder = f'dataset_merge/{i}/images'
    
    for l in os.listdir(label_folder):
        ind = labels.index(i)
        with open(label_folder + '/' + l, 'r') as f_r:
            line = f_r.readline()  
            words = line.strip().split()

        updated_line=''
        if words:
            words[0] = str(ind)
            updated_line = ' '.join(words)
        print(updated_line)
        
        test = open(label_folder + '/' + l,'w')
        test.write(updated_line)
        

            
        # print(updated_line)
        
        
        # label_path = label_folder+'/'+l
        # print(label_path)
        # imagepath = image_folder+'/'+l[:-4]+'.jpg'
        # os.remove(label_path)
        # os.remove(imagepath)
        
    
    # test = open('test.txt','w')
    # test.write(updated_line)
    # # print(updated_line)