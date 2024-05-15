# pip install streamlit
import streamlit as st
import pickle
import numpy as np
import math
# pip install sklearn
#
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')

company = st.selectbox('Brand',df['Company'].unique())
type = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])
weight = st.number_input('Weight of the laptop')
touchscreen = st.selectbox('Touchscreen',['No','Yes'])
ips = st.selectbox('IPS',['No','Yes'])
screen_size = st.number_input('Screen Size')
resolution = st.selectbox('Screen Resolution',['1920*1080','1366*768','1600*900','3840*2160','3200*1800',
                                               '2880*1880','2560*1680','2560*1440','2304*1440'])
cpu = st.selectbox('CPU',df['Cpu brand'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2084])
sdd = st.selectbox('SDD(in GB)',[0,8,128,256,512,1024,2084])
gpu = st.selectbox('GPU',df['Gpu brand'].unique())
os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,sdd,gpu,os])
    query = query.reshape(1,12)
    st.title('the price is: '+ str(int(np.exp(pipe.predict(query)[0]))))