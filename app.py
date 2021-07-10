import streamlit as st
import pickle
import config
import requests

#loading pickle file
model=pickle.load(open('model.pkl','rb'))
@st.cache()


#recommend crop
def recommend(Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall):
    # Making predictions 
    prediction = model.predict( 
        [[Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall]])
    return prediction





#main function for the webpage
def app():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Crop Prediction ML App</h1> 
    </div> 
    """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

     # following lines create boxes in which user can enter data required to make prediction
    Nitrogen=st.number_input("Nitrogen value")
    Phosphorous=st.number_input("Phosphorous value")
    Potassium=st.number_input("Potassium value")
    ph=st.slider("Choose ph value",0.0,14.0)
    rainfall=st.slider("Choose rainfall",0.0,100.0)
    temperature=st.slider("Choose temperature",0.0,100.0)
    humidity=st.slider("Choose temperature",0.0,100.0)
    result =""

    # when 'Recommend Crop' is clicked, make the prediction and store it 
    if st.button("Recommend Crop"):
        result=recommend(Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall)
        st.success("Your crop is {}".format(result))




    
    


         

if __name__ == '__main__':
    app()