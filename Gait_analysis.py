# import libary
import numpy as np
import pandas as pd
from gaitpy.gait import *
import datetime as dt

# Preprocess acceleration data & convert it to accelerometer data that gaitpy can process
raw_data = pd.read_csv("Accelerometer.csv",names=['unix_timestamps','timestamps','elapsed', 'x', 'y', 'z'], usecols=[0, 1, 2, 3,4,5])
raw_data.drop(['timestamps','elapsed'], axis=1, inplace=True)

raw_data = raw_data.iloc[1: , :]
raw_data.to_csv("acc_data.csv", header=False, index=False)


# Load preprocessed accelerometer data and extract gait metrics 
raw_data = pd.read_csv('acc_data.csv', names=['unix_timestamps','x', 'y', 'z'], usecols=[0, 1, 2, 3])
sample_rate = 100 # hertz
subject_height = 166 # centimeters


### Create an instance of GaitPy ###
gaitpy = Gaitpy(raw_data,
                    sample_rate,
                    v_acc_col_name='y',
                    ts_col_name='unix_timestamps',
                    v_acc_units='g',
                    ts_units='ms',
                    flip=False)


#### Classify bouts of gait ####
gait_bouts = gaitpy.classify_bouts(result_file='classify_bouts.h5')

 #### Extract gait characteristics ####
gait_features = gaitpy.extract_features(subject_height,
                                            subject_height_units='centimeters',
                                            result_file='gait_features.csv',
                                            classified_gait=gait_bouts)

#### Plot results of gait feature extraction ####
gaitpy.plot_contacts(gait_features, result_file='plot_contacts.html', show_plot=False)


# Add step start time and milliseconds
gait_df = pd.read_csv('gait_features.csv')

gait_df['Step_Start(IC)_Time']= pd.to_datetime(gait_df['IC'], unit='ms').apply(lambda x: x.to_datetime64())
gait_df['Time_lapse'] = gait_df['IC']-gait_df.loc[0,'IC']

gait_df = gait_df[['bout_number', 'bout_length_sec', 'bout_start_time','Step_Start(IC)_Time','Time_lapse','IC', 'FC',
       'gait_cycles', 'steps', 'stride_duration', 'stride_duration_asymmetry',
       'step_duration', 'step_duration_asymmetry', 'cadence',
       'initial_double_support', 'initial_double_support_asymmetry',
       'terminal_double_support', 'terminal_double_support_asymmetry',
       'double_support', 'double_support_asymmetry', 'single_limb_support',
       'single_limb_support_asymmetry', 'stance', 'stance_asymmetry', 'swing',
       'swing_asymmetry', 'step_length', 'step_length_asymmetry',
       'stride_length', 'stride_length_asymmetry', 'gait_speed']]


gait_df.to_csv('gait_features.csv')






