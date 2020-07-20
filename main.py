import os
import pandas as pd
#import matplotlib.pyplot as plt
DATASET_DIR = "./"
IMAGE_DIR = "./Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/"
TRAIN_DIR = IMAGE_DIR + 'train/'
TEST_DIR = IMAGE_DIR + 'test/'
df = pd.read_csv(DATASET_DIR + 'Chest_xray_Corona_Metadata.csv')


# In[160]:


df_normal = df.loc[(df['Dataset_type'] == 'TRAIN')]
df_normal_train = df.loc[(df['Dataset_type'] == 'TRAIN') & (df['Label'] == 'Normal')]
df_covid_train = df.loc[(df['Dataset_type'] == 'TRAIN') & (df['Label'] != 'Normal')]
df_normal_test = df.loc[(df['Dataset_type'] == 'TEST') & (df['Label'] == 'Normal')]
df_covid_test = df.loc[(df['Dataset_type'] == 'TEST') & (df['Label'] != 'Normal')]
df_normal_copy = df_normal.copy()


# In[161]:


df_normal_copy['X_ray_image_name'].str.rsplit('.',n=1, expand = True)


# In[162]:


df_normal_copy[['img_name','extension']] = df_normal_copy['X_ray_image_name'].str.rsplit('.',n=1, expand = True)
df_normal_copy['img_name'] = df_normal_copy['img_name'].apply(lambda x: x + '_1.jpeg')
df_normal_copy['X_ray_image_name'] = df_normal_copy['img_name']
df_normal_copy = df_normal_copy.drop(['img_name','extension'], axis = 1)
df_normal_copy


# In[163]:


df_normal = pd.concat([df_normal, df_normal_copy], ignore_index=True)


# In[164]:


df_normal


# In[165]:


df_normal_copy2 = df_normal.copy()


# In[166]:


df_normal_copy2[['img_name','extension']] = df_normal_copy2['X_ray_image_name'].str.rsplit('.',n=1, expand = True)
df_normal_copy2['img_name'] = df_normal_copy2['img_name'].apply(lambda x: x + '_2.jpeg')
df_normal_copy2['X_ray_image_name'] = df_normal_copy2['img_name']
df_normal_copy2 = df_normal_copy2.drop(['img_name','extension'], axis = 1)
df_normal_copy2


# In[167]:


df_normal = pd.concat([df_normal, df_normal_copy2], ignore_index=True)


# In[29]:

df_normal_copy3 = df_normal.copy()
df_normal_copy3[['img_name','extension']] = df_normal_copy3['X_ray_image_name'].str.rsplit('.',n=1, expand = True)
df_normal_copy3['img_name'] = df_normal_copy3['img_name'].apply(lambda x: x + '_3.jpeg')
df_normal_copy3['X_ray_image_name'] = df_normal_copy3['img_name']
df_normal_copy3 = df_normal_copy3.drop(['img_name','extension'], axis = 1)
df_normal = pd.concat([df_normal, df_normal_copy3], ignore_index=True)


# In[168]:


from multiprocessing import Pool, Lock
import matplotlib.image as mpimg
import time


def images_to_arrays(file_list):
    
    normal_images = []
    normal_images.append(mpimg.imread(TRAIN_DIR + file_list))
    return normal_images

start = time.time()
p = Pool()
normal_images2 = p.map(images_to_arrays, df_normal['X_ray_image_name'])
p.close()
end = time.time()
time_delta = end - start
print("Loaded images: ", len(normal_images2))
print("{} images/s".format(len(normal_images2)/time_delta))

