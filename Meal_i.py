from dotenv import load_dotenv
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
OPENAI_API_KEY = "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"

load_dotenv()

API_KEY = os.environ["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=API_KEY, temperature=0.5)
##Removal of logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
#haiku = llm("write a haiku about the Python programming Language")
#print(haiku)

prompt_template = PromptTemplate(
    template="Give me an example of a meal could be made using the following ingredients: {ingredients}",
    input_variables =['ingredients']
)

Meal_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    verbose=True
)
st.title("TGYYMP Meal Planner")
Pre_gym_workout = st.expander("Pre-workout Meals")
Post_gym_workout = st.expander("Post-workout Meals")
col1, col2 =st.columns(2)

#Food List
with st.expander("Food list"):
    st.write("**|Fruit|**", "/Apples","/Bananas", "/Oranges", "/Strawberries", "/Blueberries","/Raspberries", "/Avocado","/Grapefruit","/Mango","/Pears", "/Grapes", "/Lemons", "/Limes", "/Peaches", "/Watermelon","/Pomegrantes", "/Plums", "/Plantain", "/Pineapple","/Payapa", "/Coconut", "/Guava", "/Dates", "/Dewberry", "/Cherries",
    "**|Nuts & Seeds|**", "/Almonds","/Walnuts","/Chia seeds","/Flax seeds","/Hemp seeds", "/Sunflower seeds","/Pumpkin seeds", "/Cashews", "/Benne seeds", "/Brazil nuts", "/Pecans", "/Hazelnuts",
    "**|Meat & Fish|**", "/Chicken", "/Turkey", "/Tuna", "/Salmon", "/Mackerel", "/Haddock", "/Catfish","/Pork","/Crayfish", "/Sardines", "/Shrimp","/Mussels","/oysters", "/perch", "/beef", "/lamb","**|Oils|**", "/Coconut oil", "/Olive oil", "/Sesame oil", "/Palm oil","/Peanut oil","/Shea butter", "/Ghee", "/Flaxseed oil", "/Rapseed oil","**|Vegetables|**", "/Spinach", "/Brocolli", "/Potato", "/Sweet Potato", "/Cauliflower", "/Carrots", "/Bell peppers", "/Tomatoes", "/Zucchini", "/Cucumbers","/Kale","/Lettuce","/Mushrooms","/Onions", "/Spinach", "/Radish","/Lettuce", "/Green Beans", "/jicama", "/Okra", "/Eggplant","/Cabbage","/Brussels sprouts","**|Condiments|**", "/Hummus","/Tahini", "/Balsamic vinegar", "/Honey", "**|Drinks|**", "/Herbal tea", "/Water", "/Wine", "/Coffee", "/Squash", "**|Dairy|**", "/Eggs", "/Cheese", "/Yogurt","/Butter milk", "/Almond milk", "/Rice milk", "/Soy milk","**|Beans|**", "/Black eyed peas", "/Broad beans", "/Butter beans", "/Chick peas", "/Cow peas", "/Kidney beans", "/Lentils","/Lima Beans", "/Pigeon peas", "**|Starches, Wholegrains & Tubers|**", "/Amaranth", "/Bread" ,"/Barley", "/Couscous", "/Corn", "/Millet", "/Rice","/Sorghum", "/Teff", "/Cassava", "/Yams", "/Yucca", "/Whole grain bread", "/Pasta", "**|Herbs & Spices|**", "/Bay leaf", "/Cinnamon", "/Cilantro", "/Cloves", "/Coriander", "/Parsley", "/Mint", "/Curry leaf", "/Dill", "/Ginger", "/Mustard", "/Oregano", "/Paprika", "/Sage" , "/Chilli pepper", "/Tumeric","/Garlic", "/Nutmeg", "/Cacao", "/Cayenne pepper")



with col1:
    st.text_input("Pre-workout Meal")
with col2:
    st.text_input("Post-workout Meal")

