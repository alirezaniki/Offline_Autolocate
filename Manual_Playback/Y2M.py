import obspy as obs

st = obs.read ("/home/alireza/Desktop/Offline_Autolocate-master/Manual_Playback/YFile/Test/Y*")
st.write ("/home/alireza/Desktop/Offline_Autolocate-master/Manual_Playback/YFile/Test/Test.mseed", format="mseed")
