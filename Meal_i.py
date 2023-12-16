import streamlit as st
import numpy as numpy
import requests
import json
from streamlit_lottie import st_lottie
import datetime
col1, col2, col3 =st.columns(3)

##Removal logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
##
st.title("TGYYMP Meal Planner")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Pot_Url = "https://lottie.host/728462af-3e70-44b9-ac15-26da4edb9d78/zB5U2gBCXU.json"
lottie_Pot = load_lottieurl(Pot_Url)
st_lottie(lottie_Pot,speed=1.5, reverse=False, loop=True, quality="medium", height=200, width=250,
    key=None )
with col1:
    Board_Url = "https://lottie.host/05bf6149-b7d7-4432-b93f-10e990d85dd6/G6b5l6kPGd.json"
    lottie_Board = load_lottieurl(Board_Url)
    st_lottie(lottie_Board,speed=2, reverse=False, loop=True, quality="medium", height=200, width=250,
    key=None )


#Food List
with st.expander("**FOOD LIST**"):
    st.write("**|Fruit|**", "/Apples","/Bananas", "/Oranges", "/Strawberries", "/Blueberries","/Raspberries", "/Avocado","/Grapefruit","/Mango","/Pears", "/Grapes", "/Lemons", "/Limes", "/Peaches", "/Watermelon","/Pomegrantes", "/Plums", "/Plantain", "/Pineapple","/Payapa", "/Coconut", "/Guava", "/Dates", "/Dewberry", "/Cherries",
    "**|Nuts & Seeds|**", "/Almonds","/Walnuts","/Chia seeds","/Flax seeds","/Hemp seeds", "/Sunflower seeds","/Pumpkin seeds", "/Cashews", "/Benne seeds", "/Brazil nuts", "/Pecans", "/Hazelnuts",
    "**|Meat & Fish|**", "/Chicken", "/Turkey", "/Tuna", "/Salmon", "/Mackerel", "/Haddock", "/Catfish","/Pork","/Crayfish", "/Sardines", "/Shrimp","/Mussels","/oysters", "/perch", "/beef", "/lamb","**|Oils|**", "/Coconut oil", "/Olive oil", "/Sesame oil", "/Palm oil","/Peanut oil","/Shea butter", "/Ghee", "/Flaxseed oil", "/Rapseed oil","**|Vegetables|**", "/Spinach", "/Brocolli", "/Potato", "/Sweet Potato", "/Cauliflower", "/Carrots", "/Bell peppers", "/Tomatoes", "/Zucchini", "/Cucumbers","/Kale","/Lettuce","/Mushrooms","/Onions", "/Spinach", "/Radish","/Lettuce", "/Green Beans", "/jicama", "/Okra", "/Eggplant","/Cabbage","/Brussels sprouts","**|Condiments|**", "/Hummus","/Tahini", "/Balsamic vinegar", "/Honey", "**|Drinks|**", "/Herbal tea", "/Water", "/Wine", "/Coffee", "/Squash", "**|Dairy|**", "/Eggs", "/Cheese", "/Yogurt","/Butter milk", "/Almond milk", "/Rice milk", "/Soy milk","**|Beans|**", "/Black eyed peas", "/Broad beans", "/Butter beans", "/Chick peas", "/Cow peas", "/Kidney beans", "/Lentils","/Lima Beans", "/Pigeon peas", "**|Starches, Wholegrains & Tubers|**", "/Amaranth", "/Bread" ,"/Barley", "/Couscous", "/Corn", "/Millet", "/Rice","/Sorghum", "/Teff", "/Cassava", "/Yams", "/Yucca", "/Whole grain bread", "/Pasta", "**|Herbs & Spices|**", "/Bay leaf", "/Cinnamon", "/Cilantro", "/Cloves", "/Coriander", "/Parsley", "/Mint", "/Curry leaf", "/Dill", "/Ginger", "/Mustard", "/Oregano", "/Paprika", "/Sage" , "/Chilli pepper", "/Tumeric","/Garlic", "/Nutmeg", "/Cacao", "/Cayenne pepper")

tab1, tab2, tab3, tab4 = st.tabs(["Week 1", "Week 2", "Week 3", "Week 4"])
col1,col2 =st.columns(2)
#eth_nic = st.multiselect("Ethnic Meal Options:" , ["Mexican", "Italian", "Indian", "African","Carribean", "Greek","Mediterranean","French", "Vegan", "Vegetarian","Paleo", "Oriental","Arabian" ])
with col2:
    with tab1:
       pass
    with tab2:
       pass
    with tab3:
       pass
    with tab4:
       pass



#Gallery code
#Place a check box "click for Galley optimization" , if gallery optimaization
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button
    
#st.button('Click to view schedule', on_click=click_button)
Gallery_code = st.button('*Click to view schedule*', on_click=click_button)
if st.session_state.button:
    eth_nic = st.multiselect("Ethnic Meal Options:" , ["Mexican", "Italian", "Indian", "African","Carribean", "Greek","Mediterranean","French", "Vegan", "Vegetarian","Paleo", "Oriental","Arabian" ])
    # The message and nested widget will remain on the page. Including Gallery
    TGYYMP_date = st.date_input("Today's Date ", datetime.date(2023, 11, 29))
    txt = st.text_area("Monday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_2 = st.text_area("Tuesday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_3 = st.text_area("Wednesday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_4 = st.text_area("Thursday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_5 = st.text_area("Friday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_6 = st.text_area("Saturday","Breakfast.... Lunch.... Dinner...Snacks")
    txt_7 = st.text_area("Sunday","Breakfast.... Lunch.... Dinner...Snacks")

    Overview_1 = st.expander("Overview")
    with st.expander("Overview"):
        TGYYMP_date
        "Monday" 
        txt 
        "Tuesday"
        txt_2
        "Wednesday"
        txt_3
        "Thursday"
        txt_4
        "Friday"
        txt_5
        "Saturday"
        txt_6
        "Sunday"
        txt_7
        text_contents = f" Monday..<{txt}>.,Tuesday...<{txt_2}>,Wednesday.... <{txt_3}>,Thursday.....<{txt_4}>,Friday......<{txt_5}>,Saturday.......<{txt_6}>,Sunday.......<{txt_7}> "

        st.download_button('File', text_contents)
#Login



