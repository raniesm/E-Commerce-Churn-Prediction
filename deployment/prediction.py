import streamlit as st
import pandas as pd
import numpy as np
import pickle

#Load model

with open('model_dt.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

def run():
    st.title('E-Commerce Customer Churn Prediction')

    with st.form('form_e-commerce_customer_churn'):
        st.write('Enter data for churn prediction')
        Product_Category = st.selectbox('Product Category', ['Electronics', 'Clothing', 'Home Appliances', 'Books'], index=0, help='Select your product category')
        Product_Price = st.number_input('Product Price', value=50, step=1)
        Quantity = st.number_input('Quantity', value=1, step=1, min_value=1)
        Total_Purchase_Amount = st.number_input('Total Purchase Amount', value=100, step=1)
        Payment_Method = st.selectbox('Payment Method', ['Credit Card', 'Cash', 'PayPal', 'Crypto'], index=0, help='Select your payment method')
        Customer_Age = st.number_input('Customer Age', value=21, max_value=100,step=1)
        Returns = st.number_input('Returns', value=0, step=1, min_value=0, max_value=1, help='0 for no return, 1 for return')
        Gender = st.selectbox('Gender', ['Male', 'Female'], index=0)
        Year_of_Purchase = st.number_input('Year of Purchase', value=2022, max_value=2024,step=1)
        Month_of_Purchase = st.number_input('Month of Purchase', value=6, min_value=1,max_value=12,step=1)
        Day_of_Purchase = st.number_input('Day of Purchase', value=24, min_value=1,max_value=30,step=1)
        Weekday_of_Purchase = st.number_input('Weekday of Purchase', value=6, min_value=0,max_value=6,step=1, help='0=Monday until 6=Sunday')
        Age_Category = st.selectbox('Age Category', ['0-20', '21-40', '41-60', '61-80'], index=0)
        
        #submit button form
        submitted = st.form_submit_button('Predict Churn')
    
    if submitted:
        data_inf = {
            'Product Category' : Product_Category, 
            'Product Price' : Product_Price , 
            'Quantity' : Quantity,
            'Total Purchase Amount' :  Total_Purchase_Amount, 
            'Payment Method' : Payment_Method, 
            'Customer Age' : Customer_Age, 
            'Returns' : Returns,
            'Gender' : Gender, 
            'Year of Purchase': Year_of_Purchase, 
            'Month of Purchase' : Month_of_Purchase, 
            'Day of Purchase' : Day_of_Purchase,
            'Weekday of Purchase': Weekday_of_Purchase, 
            'Age Category' : Age_Category
        }
        data_inf_df = pd.DataFrame([data_inf])
        prediction = loaded_model.predict(data_inf_df)
        result = "Churn" if prediction[0] == 1 else "Not Churn"
        st.write(f'## Prediction: {result}')

if __name__ == '__main__':
   run()