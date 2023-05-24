import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() : 
    st.title('내 앱 대시보드')

    df = pd.read_csv('data/iris.csv')

    st.dataframe(df)

    # sepal_length, sepal_width의 관계를 차트로

    fig = plt.figure()
    plt.scatter(data = df, x = 'sepal_length', y = 'sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')

    st.pyplot(fig) # Matplotlib으로 그려진 그래프(fig)를 스트림릿(stremlit) 앱에 표시합니다.

    fig2 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length', y = 'sepal_width')
    # 데이터프레임(df)의 'sepal_length'를 x축으로, 'sepal_width'를 y축으로 해서 산점도와 회귀선을 그립니다. 
    # 이때 seaborn 라이브러리의 regplot 함수를 사용합니다.
    st.pyplot(fig2)

    correlation = df[['sepal_length','sepal_width']].corr()
    st.dataframe(correlation)

    # sepal_length로 히스토그램을 그리자.
    # bin의 갯수는 20개로

    fig3 =  plt.figure(figsize= (10, 4)) # 가로는 10, 세로는 4
    plt.subplot(1, 2, 1)
    plt.hist(data = df, x = 'sepal_length', rwidth= 0.8, bins = 20)
    
    plt.subplot(1, 2, 2)
    plt.hist(data = df, x = 'sepal_length', rwidth= 0.8, bins = 10)
    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종별로 몇 개씩의 데이터가 있는지
    # 차트로 나타내시오.
    
    st.dataframe(df['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data= df, x='species')
    st.pyplot(fig4)

    ## 데이터 프레임의 차트 그리는 코드도 실행 가능
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='barh') # bar : 수직, barh : 수평
    st.pyplot(fig5)

    # 데이터프레임의 자체 plot 함수는 스트림릿에서 안된다.
    fig6 = plt.figure()
    df.plot()
    st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)


if __name__  == '__main__' :
    main()