from PIL import Image      #pillow=used to images from our webapp #to run write streamlit run app.py
import requests 
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit as st
from streamlit_option_menu import option_menu

# import plotly.graph_objects as go  #pip install plotly
#for emoji icons :- https:https://web.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="vend here ",page_icon = ": tada :", layout ="wide")
#used to hide other streamlit default icons etc.
hide_st_style="""  
            <style>
            #MainMenu {visibility   :  hidden;}
            footer {visibility  : hidden;}
            header {visibility : hidden;}
            </style>"""
st.markdown(hide_st_style,unsafe_allow_html=True)    

# 2.as horizontal menu
selected = option_menu(
         menu_title=None,#this only shows text wriitten above navigation-bar Top.
        options=["Home","Food Items","contact Us","Payment"], #required
        icons=["house-gear","basket-fill","bug-fill","cash-coin"],  #only write name of icons from bootstrap https://icons.getbootstrap.com/. 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={"container":{ "container": {"padding": "0!important", "background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }
        }
    )

if selected=="Home":
    # from streamlit import Style

    def load_lottieurl(url):  #thu function access the json data of lotttie animation.
            r= requests.get(url)  #if request is successfull for lottie file (vending machine) it will return 200.
            if r.status_code !=200 :
                return None    #eor we will return nothing if not accessed.
            return r.json()  #otherwise we will return the json data

        # Use local CSS 
    def local_css(file_name):    #from here to
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) # to here this code should remain as it is in any streamlit app for importing css file.

    local_css("style/style.css")  #calling our css file here from the folder style.
        #animation through lottiefiles
    lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_d16uoqsh.json")  #this is your actual vending machine lottie file inside variable lottie_coding
    lottie_codinganother=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_YnsM0o.json")
    # img_contact_form =Image.open("images/yt_contact_form.png")   # add relative path and name a variable for images.
    # img_lottie_animation =Image.open("images/yt_lottie_animation.png")
    # img_minisamosas_animation=Image.open("images\mini_samosa_animation.png")

        #header section---
    st.subheader(" Vending Machine at MIT-ADT")
    st.title("A new way to catch up with snacks ")
    st.write("this page contains all your queries related to vending machine! ")

    st.write("if you are new NO WORRIES ")
    st.write("[click here to learn through visual use ->](https://youtu.be/NNh2Y6sbA6k)")

    with st.container():
        st.write("---")
        image_column,text_column=st.columns((1,2))  #image_column(left)should be twice as big as text_column(right)
        with image_column:
           st.write("$$$$$")
           st.write(''' we are introducing a new way for Mitians to get their snacks and foods from the vending machine....
                We have seen our fellows running from tuck shop to their destinations (classes)
                between the breaks for 15 min which take them to travel from SOE building to get the lift on time.
                and many more problems faced by them.   \n\n
                thus, what if we get our snacks in our places 
                like in IT building and many more parts of MIT
                -adt university from without going through a
                   lengthy process of getting out of the building 
                ,taking tokens and then getting desired food.  
                    ''')
        with text_column:
            st_lottie(lottie_coding,height =450,key = "vending machine ")


if selected=="Food Items":  
    st.title(f"You have selected {selected}")
    img_contact_form =Image.open("images/yt_contact_form.png")   # add relative path and name a variable for images.
    img_lottie_animation =Image.open("images/yt_lottie_animation.png")
    img_minisamosas_animation=Image.open("images\mini_samosa_animation.png")

                        #--contact about item --
    with st.container():
        st.write("---")
        st.header(" Items available at Store ")
        st.write("##")
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(img_lottie_animation)   #insert image
            
        with text_column:
            st.subheader(" Beverage ")
            st.write(
                """    
                    
                    |Queries                     |Answers |                              
                    |--------------------------:|-------------------------------------:|
                    |Prperties                  |RAW Fountain 3 Day Green Juice Cleanse|
                    |100% Natural Raw           |Organic                    |
                    |Cold Pressed Fruit         |& Vegetable Juices       |
                    | Herbal                    |Detox Cleanse Weight Loss|                                       
                    """
            )
            st.markdown("[watch video to paste quiries.....](https://www.quackit.com/html/codes/add_comments_to_website.cfm)")
    with st.container():

        st.write("-------")  #hlps to create a line between items
    image_column,text_column=st.columns((1,2))
    with image_column:
            st.image(img_minisamosas_animation) 
            
    with text_column:
            st.subheader("Mini Samosa ")
            st.write(
                """
                        |Querys           |Answers|
                        |-----------------:|------------------------:|
                        |Brand	        |BIKANO|
                        |Flavour	        |Spicy|
                        |Diet Type	    |Vegetarian| 
                        |Specialty	    |Suitable for vegetarians|                   
                        |Number of Items	|3|                    
                        |Units	        |1200 gram|         
                        |Package Weight	|500 Grams|
                        |Package Type	|Box|
                    """
            )
            st.markdown("[watch video to paste quiries.....](https://www.quackit.com/html/codes/add_comments_to_website.cfm)")

  
    with st.container():
        st.write("-------")
    image_column,text_column= st.columns((2,3))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Snickers Chocolate bar ")
        st.write("""
                                        
                        |Brand	    |Snickers|
                        |----------:|-------:|
                        |Form	    |Bar|
                        |Occasion	|Holiday, Birthday, Thank You, Thanksgiving|
                        |Flavour	|"Peanut", value:"Peanut;"Chocolate", value:"Chocolate|
                        |Units	    |45.0 gram|
                        |Specialty	|Vegetarian|
                        |Size	    |45 g (Pack of 1)|
                        """)
        st.markdown("[check the price for V&V here --->](https://fetchnbuy.in/products/snickers-chocolate-bar-14g?currency=INR&variant=41390612283560&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping)")
        
if selected=="contact Us":
        st.title(f"You have selected {selected}")
        def load_lottieurl(url):  #thu function access the json data of lotttie animation.
            r= requests.get(url)  #if request is successfull for lottie file (vending machine) it will return 200.
            if r.status_code !=200 :
                return None    #eor we will return nothing if not accessed.
            return r.json()  #otherwise we will return the json data

        # Use local CSS 
        def local_css(file_name):    #from here to
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) # to here this code should remain as it is in any streamlit app for importing css file.

        local_css("style/style.css")  #calling our css file here from the folder style.
                    #animation through lottiefiles
        lottie_codinganother=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_YnsM0o.json")
    
    ## using a free service for form called formsumbit.co  ,documentation : https://formsubmit.co/ change email address!!!
            #no captcha message will be shown as value is false.
        with st.container():
            st.write("-----")
            st.header(":mailbox: Get in touch with Us !")
            st.header("##")
            contact_form ="""
                    <form action="/add your email" method="POST"> 
                    <input type ="hidden" name "_captcha " value="false" > 
                        <input type="text" name="name" placeholder= "Enter name" required>
                        <input type="email" name="email" placeholder = "Enter Your email" required>
                        <textarea name ="message" placeholder= "Your comment/Queries " required></textarea>
                        <button type="submit">Send</button>
                </form>"""
        image_column,text_column=st.columns(2)
        with image_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with text_column:
            st_lottie(lottie_codinganother,height=350,key='combo burger')
            # st.empty()  #our column keeping  it blank
if selected=="Payment":
        st.title(f"You have selected {selected}")
         # Use local CSS 
        def local_css(file_name):    #from here to
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) # to here this code should remain as it is in any streamlit app for importing css file.

        local_css("style/style.css")  #calling our css file here from the folder style.
               
        # load Animation ->to open the snow emoji hold (win_key+.) or (win_key+;)
        animation_symbol="❄️"
        st.markdown(
             f"""
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             <div class="snowflakes">{animation_symbol}</div>
             """,unsafe_allow_html=True)  

