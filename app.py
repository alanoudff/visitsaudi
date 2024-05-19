import streamlit as st
import pickle
from PIL import Image
  
knn=pickle.load(open('svm_model.pkl','rb'))



def classify(num):
    if num==0:
        return ' not ideal'
    else :
        return 'ideal'
    

def main():
    st.title("visit saudi")
    
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;"> visit Classification</h2>
    </div>
    """
    

    
    st.header('about the web')
    st.write('Welcome to your one-stop guide for selecting the ideal month to visit any city in Saudi Arabia! Our website understands that navigating a  country with diverse climates can be tricky. Were here to shed light on the weather conditions across Saudi Arabia, ensuring a smooth and enjoyable travel experience for every visitor.')
    st.write('Whether you crave the warmth of the Red Sea coast or the cooler embrace  of the mountains, well recommend the perfect month for your specific destination and desired activities. So, pack your bags and get ready to explore the wonders of Saudi Arabia  well steer you towards the season that best suits your travel dreams! ')
    city =st.text_input('Enter the name of city you plan to visit:')
    st.write('The city that you entered :' , city)


    st.subheader('Type of city you want to visit')
    city_type= st.selectbox('1 - coastal  2 - inner   3 - mountain',
                    (1,2,3))                      
    st.write(' you selected :' , city_type)
  
    st.subheader('Enter the month that you plan to visit the city:')
    month =st.number_input(' Enter the month that you plan to visit in it  (number):')
    st.write(' The month that you entered :' , month)



    st.subheader('Enter the average day temperature:')
    day_temp =st.number_input(' Enter the average day temperature:')
    st.write(' The number you entered :' , day_temp)


    st.subheader('Enter the average night temperature:')
    night_temp =st.number_input(' Enter the average night temperature:')
    st.write('The number you entered :' , night_temp)


    st.subheader('Enter the average rain day:')
    rain_day =st.number_input (' Enter the average rain day:')
    st.write('The number you entered :', rain_day)


 
    

    inputs= [[ day_temp, night_temp,  night_temp, month, city_type]]
    if st.button('classify'):
     st.success(classify(knn.predict(inputs)))


if __name__=='__main__':
    main()
