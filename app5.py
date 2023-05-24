import streamlit as st

def main() : 
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법
    
    img = st.image('data/image_03.jpg')
    
    st.image('data/image_03.jpg', use_column_width = True)
    print(img)

    st.image('https://i.namu.wiki/i/NHL1KKhGXJnZDskH6mvLhIbD-9V4iVVJBinBKnJZzZb3Ty0uAlISGuKcNVZ_-azmwg-JiWyxiy23IdYXGL6_Q0SMzTXSV0PNE8fVOFSXiKPSgkaSjk6Gb2WdR06-vp-h4OQfgnPgiFSnyCzEdRaayw.webp')
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)

if __name__  == '__main__' :
    main()

