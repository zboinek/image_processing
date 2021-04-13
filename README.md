# Outdated - 13.04.2021
Managed to use Tensorflow pre-fetch mechanism to lazy load files in batches. 

# Multi CPU image processing
I want to write high performance image loader. For now I'm stack at 250 images/s

# DataSet images download
Data set can be downloaded by
`kaggle datasets download -d praveengovi/coronahack-chest-xraydataset`  

# Run
Tu run you can use image_processing notebook or `main.py`

# Current stats

## Disk usage
![Disk usage screenshot](images/disk.png)

## Images per second stats
![Images per second](images/ips.png)

# Questions
I defenitely don't know how to go further. Is there a way to read images straight to GPU? Use of another library to read image? Another way of multiprocessing files?
