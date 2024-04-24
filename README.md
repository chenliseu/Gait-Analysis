# Convert accelerometer data for gait analysis

## We will use Gaitpy API in Python to read accelerometer data into gait metric. Accelerometer data can be obtained by wearing sensors that track your movement. 

### Gaitpy API is an open source python API that public available and can be installed on your local laptop, here are using links: 

[API installation link](https://pypi.org/project/gaitpy/)

[Paper that explains how API work](https://joss.theoj.org/papers/10.21105/joss.01778.pdf)




### GaitPy utilizes vertical acceleration data (y) from a wearable device located on the lower back (lumbar region) and returns following data metric:
* stride duration
* step duration
* cadence
* initial double support
* terminal double support
* double support
* single limb support
* stance
* swing
* step length
* stride length
* gait speed
* Step asymmetry 


### In this project, we use a wearable sensor to read accelerometer data, and use API to populate gait metrics via Python. 

![Plot of Gait Analysis Outcome](https://github.com/chenliseu/Gait-Analysis/blob/main/gait_plot.png)

