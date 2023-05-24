import streamlit as st
import pandas as pd
def main() : 
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')
    # print(df)

    st.dataframe(df)

    species = df['species'].unique()
    '아이리스 꽃은' + species + '으로 되어있다.'

    st.write(df.head())
if __name__  == '__main__' :
    main()

