import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

def main() : 
    st.title('내 앱 대시보드')    

    df1 = pd.read_csv('data/lang_data.csv')

    st.dataframe(df1)

    st.text(df1.shape) # 행과 열을 보여줌

    print(df1.columns[1:])

    lang_list = df1.columns[1:]

    choice_list = st.multiselect('언어를 선택하세요.', lang_list)

    # 유저가 아무것도 선택 안 했을 때 처리

    print(choice_list)

    if len(choice_list) > 0 :


        choice_df = df1[ choice_list ] # 원래 있던 df1에서 내가 선택한 df만 가져오는 것

        

        st.dataframe(choice_df) # 내가 선택한 컬럼으로 데이터 프레임을 가지고 온다.

        #streamlit이 제공하는 라인 차트
        st.line_chart(choice_df) 

        #streamlit이 제공하는 영역 차트
        st.area_chart(choice_df) 


    df2 = pd.read_csv('data/iris.csv')

    #스트림릿이 제공하는 바차트

    df3 = df2[ ['sepal_length','sepal_width']]

    st.bar_chart(df3)

    # Altair 이용
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'sepal_length',y = 'sepal_width', color = 'species')
    st.altair_chart(chart)

    # 스트림릿의 map 차트
    df4 = pd.read_csv('data/location.csv', index_col=0)

    print(df4)

    st.map(df4)

    df5 = pd.read_csv('data/prog_languages_data.csv')
    st.dataframe(df5)

    # plotly의 pie 차트 (파이차트는 비율을 보고 싶을 때)
    fig1 = px.pie(df5, 'lang', 'Sum', title = '각 언어별 비율')
    st.plotly_chart(fig1)

    # plotly의 bar 차트
    df5.sort_values('Sum', ascending=False)
    fig2 = px.bar(df5 , x = 'lang', y = 'Sum')
    st.plotly_chart(fig2)


if __name__  == '__main__' :
    main()