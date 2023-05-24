import streamlit as st
from app_image import run_app_image
from app_csv import run_app_csv
from app_about import run_app_about

def main() : 
    st.title('내 앱 대시보드')
    
    menu = ['Image','csv업로드','About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == menu[0] :
        run_app_image()

    elif choice == menu[1] :
        run_app_csv()

    else :
        run_app_about()
    

if __name__  == '__main__' :
    main()