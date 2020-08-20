import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_nod(perc_fatl_speed,perc_fatl_alcohol,perc_fatl_1st_time):
    input=np.array([[perc_fatl_speed,perc_fatl_alcohol,perc_fatl_1st_time]]).astype(np.float64)
    prediction=model.predict(input)
    pred=round(prediction[0], 2)
    return float(pred)

def main():
    st.title("Finding Fatal Collisions")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Reducing Traffic Mortality </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    perc_fatl_speed= st.text_input("Percentage of drivers involved in fatal collisions who were speeding","Type Here")
    perc_fatl_alcohol = st.text_input("Percentage of drivers involved in fatal collisions who were alcohol-impaired","Type Here")
    perc_fatl_1st_time = st.text_input("Percentage of drivers involved in fatal collisions who had not been involved in previous accidents","Type Here")
   

    if st.button("Predict"):
        output=predict_nod(perc_fatl_speed,perc_fatl_alcohol,perc_fatl_1st_time)
        st.success('Number of drivers involved in fatal collisions per billion miles {}'.format(output))

        

if __name__=='__main__':
    main()




