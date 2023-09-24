import base64
import streamlit as st
import sim

@st.cache_data
def get_img_as_base64(file):
    with open(file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def page_1_1():
    
    # 시작 페이지
    # st.title("오뚜기 왕국의 귀공자들과 두근두근 소개팅")

    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p1_text.png")
    st.image(f"data:image/png;base64,{img}")
    
    # col1, col2 = st.columns([1, 1])

    # with col1:
    #     st.header("a cat")
    # with col2:
    if st.button("START"):
        st.session_state.page = 1
        st.experimental_rerun()
            
# 세계관 줄거리 소개
def page_1_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("나는 오뚜기 왕국의 공주다.")
    # st.text("")
    # st.text("결혼적령기가 넘어 오뚜기 왕국의 귀공자들과 소개팅을 하기로 했다.")
    
    img = get_img_as_base64("p2_text.png")
    st.image(f"data:image/png;base64,{img}")
    if st.button("Next"):
        st.session_state.page = 2
        st.experimental_rerun()
    
# 소개팅 상대 고르기 페이지
def page_1_3():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p3_text.png")
    st.image(f"data:image/png;base64,{img}")
    img = get_img_as_base64("p3_bt1.png")
    st.image(f"data:image/png;base64,{img}")
    # st.button("3분 카레 공작")
    if st.button("3분 카레 공작"):
        st.session_state.page = 3
        st.session_state['man'] = 0
        st.experimental_rerun()
    
    img = get_img_as_base64("p3_bt2.png")
    st.image(f"data:image/png;base64,{img}")
    if st.button("진라면 순한맛 백작"):
        st.session_state.page = 3
        st.session_state['man'] = 1
        st.experimental_rerun()
    
    img = get_img_as_base64("p3_bt3.png")
    st.image(f"data:image/png;base64,{img}")
    if st.button("토마토 케찹 자작"):
        st.session_state.page = 3
        st.session_state['man'] = 2
        st.experimental_rerun()
    
    img = get_img_as_base64("p3_bt4.png")
    st.image(f"data:image/png;base64,{img}")
    if st.button("오뚜기 흰쌀밥 후작"):
        st.session_state.page = 3
        st.session_state['man'] = 3
        st.experimental_rerun()
    # st.experimental_rerun()
    
# 선택 후 다음 화면 (1)
def page_2_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("아하하~ 그렇구나ㅎㅎ")
    
    img = get_img_as_base64("p4_text1.png")
    st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
        
    img = get_img_as_base64("p4_text2.png")
    st.image(f"data:image/png;base64,{img}")
    # st.text("나: 응, 웃기지")
    if st.button("Next"):
        st.session_state.page = 4
        st.experimental_rerun()
    
# 선택 후 다음 화면 (2)
def page_2_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("화기애애한 분위기")
    # st.text("대화주제는 자연스레")
    # st.text("음식 얘기로 넘어갔다.")
    # st.text("")
    # st.text("역시, 오뚜기 왕국")
    # st.text("사람들의 대화엔")
    # st.text("음식 얘기가 빠질 수")
    # st.text("없다.")
    
    img = get_img_as_base64("p5_text.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.button("NEXT"):
        st.session_state.page = 5
        st.experimental_rerun()
    
# 질문 page 1
def page_3_1_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # 1. 공주님은 집에서 음식 만들어 드실 때, 간단하게 조리하는 음식을 즐기는 편이세요? 아니면 레시피를 찾아보고 처음부터 끝까지 직접 조리해서 드시나요?
    
    img = get_img_as_base64("p6_text.png")
    st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
    
    if st.button("Next"):
        st.session_state.page = 6
        st.experimental_rerun()
        

# 질문 page 1
def page_3_1_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    # 간단하게 조리하는 음식을 먹어서 시간을 단축하는 게 좋아요. (→ 즉석식품)
    if st.button("A1. 간단하게 조리하는 음식을 먹어서 시간을 단축하는 게 좋아요."):
        st.session_state.result_list[0:2]=[1, 0]
        st.session_state.page = 7
        st.experimental_rerun()
    # 레시피를 찾아보며 음식을 요리할 때 뿌듯하고 즐거워요. (→ 요리재료)
    if st.button("A2. 레시피를 찾아보며 음식을 요리할 때 뿌듯하고 즐거워요."):
        st.session_state.result_list[0:2]=[0, 1]
        st.session_state.page = 7
        st.experimental_rerun()
    
# 질문 page 2
def page_3_2_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    # 오.. 그러시구나. 그러면 음식종류 중에서는 무엇을 제일 좋아하세요?
    img = get_img_as_base64("8p_text.png")
    st.image(f"data:image/png;base64,{img}")

    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
    
    if st.button("Next"):
        st.session_state.page = 8
        st.experimental_rerun()
        
def page_3_2_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)        
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    # 밥이요! 오뚜기 왕국 사람은 역시 밥심이죠~ (→ 밥)
    if st.button("A1. 밥이요! 오뚜기 왕국 사람은 역시 밥심이죠~"):
        st.session_state.result_list[2:7]=[1,0,0,0,0]
        st.session_state.page = 9
        st.experimental_rerun()
    # 빵이요! 빵은 간단하고 맛있어서 너무 좋아요 ㅎㅎ (→ 빵)
    if st.button("A2. 빵이요! 빵은 간단하고 맛있어서 너무 좋아요 ㅎㅎ"):
        st.session_state.result_list[2:7]=[0,1,0,0,0]
        st.session_state.page = 9
        st.experimental_rerun()
    # 면이요! 후루룩후루룩 잘 들어가는 게 제 취향이에요~ (→ 면)
    if st.button("A3. 면이요! 후루룩후루룩 잘 들어가는 게 제 취향이에요~"):
        st.session_state.result_list[2:7]=[0,0,1,0,0]
        st.session_state.page = 9
        st.experimental_rerun()
        
    # 떡이요! 쫄깃쫄깃한 식감이 제 스타일이에요! (→ 떡)
    if st.button("A4. 떡이요! 쫄깃쫄깃한 식감이 제 스타일이에요!"):
        st.session_state.result_list[2:7]=[0,0,0,1,0]
        st.session_state.page = 9
        st.experimental_rerun()
        
    # 튀김이요! 튀김음식은 신발을 튀겨도 맛있을걸요? (→ 튀김)
    if st.button("A5. 튀김이요! 튀김음식은 신발을 튀겨도 맛있을걸요?"):
        st.session_state.result_list[2:7]=[0,0,0,0,1]
        st.session_state.page = 9
        st.experimental_rerun()
    
# 질문 page 3
def page_3_3_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("Q1. 공주님은 단 음식 좋아해?")
    
    # 저도 그래요! 역시 저랑 잘 맞으시네요. 혹시 한식, 일식, 중식, 양식 중에서는 어때요? 저는 중식이요!
    img = get_img_as_base64("10p_text.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
        
    if st.button("Next"):
        st.session_state.page = 10
        st.experimental_rerun()

def page_3_3_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
            
    # 저는 한식이 제일 좋아요! 깔끔하잖아요! (→ 한식)
    if st.button("A1. 저는 한식이 제일 좋아요! 깔끔하잖아요!"):
        st.session_state.result_list[7:11]=[1,0,0,0]
        st.session_state.page = 11
        st.experimental_rerun()
        
    # 앗, 저는 일식파예요 헤헤 (→ 일식)
    if st.button("A2. 앗, 저는 일식파예요 헤헤"):
        st.session_state.result_list[7:11]=[0,1,0,0]
        st.session_state.page = 11
        st.experimental_rerun()
        
    # 우와 저도 중식이 가장 좋아요! 대박~ (→ 중식)
    if st.button("A3. 우와 저도 중식이 가장 좋아요! 대박~"):
        st.session_state.result_list[7:11]=[0,0,1,0]
        st.session_state.page = 11
        st.experimental_rerun()
        
    # 저는 양식을 즐겨먹어요~ (→ 양식)
    if st.button("A4. 저는 양식을 즐겨먹어요~"):
        st.session_state.result_list[7:11]=[0,0,0,1]
        st.session_state.page = 11
        st.experimental_rerun()
    
# 질문 page 4
def page_3_4_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("Q1. 공주님은 단 음식 좋아해?")
    
    # 오호 공주님을 더 많이 알아가는 것 같아요. 그러면 매운거 좋아하세요? 저는 매운걸 먹으면 스트레스가 풀리더라고요
    img = get_img_as_base64("12p_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
        
    if st.button("Next"):
        st.session_state.page = 12
        st.experimental_rerun()

def page_3_4_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
            
    # 우와 저도 매운걸 즐겨 먹어요. 스트레스가 좍 풀려요 (→ 매운맛 O)
    if st.button("A1. 우와 저도 매운걸 즐겨 먹어요. 스트레스가 좍 풀려요"):
        st.session_state.result_list[11:13]=[1, 0]
        st.session_state.page = 13
        st.experimental_rerun()
    
    # 앗 저는 좀 맵찔이라...ㅠㅠ 즐겨 먹진 않아요 (→ 매운맛 X)
    if st.button("A2. 앗 저는 좀 맵찔이라...ㅠㅠ 즐겨 먹진 않아요"):
        st.session_state.result_list[11:13]=[0, 1]
        st.session_state.page = 13
        st.experimental_rerun()
    
# 질문 page 5
def page_3_5_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("Q1. 공주님은 단 음식 좋아해?")
    
    # 다음 데이트 때 참고해야겠어요! 그러면 밥 먹은 후에 꼭 디저트를 먹는편? 군것질은 피하는편?
    img = get_img_as_base64("14p_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
    
    if st.button("Next"):
        st.session_state.page = 14
        st.experimental_rerun()
        
def page_3_5_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    # 아 디저트배는 따로 있죠~ 디저트는 꼭 먹습니다! (→ 단맛 O)
    if st.button("A1. 아 디저트배는 따로 있죠~ 디저트는 꼭 먹습니다!"):
        st.session_state.result_list[13:15]=[1, 0]
        st.session_state.page = 15
        st.experimental_rerun()
        
    # 요즘 건강관리 하느라, 당은 좀 피하고 있어요 ㅎㅎ. 군것질을 잘 안 합니다! (→ 단맛X)
    if st.button("A2. 요즘 건강관리 하느라, 당은 좀 피하고 있어요 ㅎㅎ. 군것질을 잘 안 합니다!"):
        st.session_state.result_list[13:15]=[0, 1]
        st.session_state.page = 15
        st.experimental_rerun()
    
# 질문 page 6
def page_3_6_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("Q1. 공주님은 단 음식 좋아해?")
    
    # 아아 이걸 까먹을 뻔 했다! 혹시 고기 드실 수 있으세요?
    img = get_img_as_base64("16p_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
        
    if st.button("Next"):
        st.session_state.page = 16
        st.experimental_rerun()
        
        
def page_3_6_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)

    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    # 고기 좋아해요 완전!!! 고기 들어간 음식이면 다 잘 먹어요! (→ 육식)
    if st.button("A1. 고기 좋아해요 완전!!! 고기 들어간 음식이면 다 잘 먹어요!"):
        st.session_state.result_list[15:17]=[1, 0]
        st.session_state.page = 17
        st.experimental_rerun()
        
    # 고기는 안 먹어요! 채식이나 과일은 먹을 수 있습니다! (→ 채식)
    if st.button("A2. 고기는 안 먹어요! 채식이나 과일은 먹을 수 있습니다!"):
        st.session_state.result_list[15:17]=[0, 1]
        st.session_state.page = 17
        st.experimental_rerun()
    
# 질문 page 7
def page_3_7_1():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    # st.text("Q1. 공주님은 단 음식 좋아해?")
    
    # 마지막으로, 새콤한 음식도 좋아하세요?
    img = get_img_as_base64("18p_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
        
    if st.button("Next"):
        st.session_state.page = 18
        st.experimental_rerun()
        
        
def page_3_7_2():
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("answer_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    img = get_img_as_base64("p7_text1.png")
    st.image(f"data:image/png;base64,{img}")
    
    # 그럼요~! 입안이 시원해져서 좋아해요! (→ 신맛O)
    if st.button("A1. 그럼요~! 입안이 시원해져서 좋아해요!"):
        st.session_state.result_list[17:19]=[1, 0]
        st.session_state.page = 19
        st.experimental_rerun()
    
    # 아니요ㅠ 신 음식은 좀... (→ 신맛X)
    if st.button("A2. 아니요ㅠ 신 음식은 좀..."):
        st.session_state.result_list[17:19]=[0, 1]
        st.session_state.page = 19
        st.experimental_rerun()
    
# 결과 페이지
def page_result():
    
    # 배경화면 이미지 CSS 스타일
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    # 설문조사 벡터
    print(st.session_state.result_list)
    
    # sim.recommend(df, st.session_state.result_list)
    
    
    img = get_img_as_base64("org_bg.png")
    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top center;
    background-repeat: repeat-y;
    background-attachment: local;
    margin: 0 auto;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    # 배경화면 이미지 스타일을 적용
    st.markdown(background_style, unsafe_allow_html=True)
    
    product, review_product_list = sim.get_sim_data(st.session_state.result_list)
    product_name = product['title']
    product_url =product['image']
    product_text = product['body']
    
    
    st.subheader("공주님.. 저와 함께")
    if st.session_state.man == 0:
        img = get_img_as_base64("chr1.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 1:
        img = get_img_as_base64("chr2.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 2:
        img = get_img_as_base64("chr3.png")
        st.image(f"data:image/png;base64,{img}")
    if st.session_state.man == 3:
        img = get_img_as_base64("chr4.png")
        st.image(f"data:image/png;base64,{img}")
    st.header(f"{product_name}")
    st.subheader("어때요?")
    st.image(f"{product_url}")
    st.header("제품 특징")
    st.subheader(product_text)
    st.subheader("듣기만 해도 침이 고이네요ㅎㅎ 당장 먹으러 가요!")
    st.subheader(f"아래 음식들을 좋아하신다면, {product_name}도 더욱 좋아하실 거에요")
    
    st.header(f"{review_product_list.iloc[0]['title']}")
    st.image(f"{review_product_list.iloc[0]['image']}")
    st.header(f"{review_product_list.iloc[1]['title']}")
    st.image(f"{review_product_list.iloc[1]['image']}")
    st.header(f"{review_product_list.iloc[2]['title']}")
    st.image(f"{review_product_list.iloc[2]['image']}")
    st.header(f"{review_product_list.iloc[3]['title']}")
    st.image(f"{review_product_list.iloc[3]['image']}")
    st.header(f"{review_product_list.iloc[4]['title']}")
    st.image(f"{review_product_list.iloc[4]['image']}")
    if st.button("THE END"):    
        st.session_state.page = 0
        st.experimental_rerun()


def app():
    if "page" not in st.session_state:
        st.session_state.page = 0
        
    if "result_list" not in st.session_state:
        st.session_state.result_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # 선택한 페이지에 따라 내용을 표시
    if st.session_state.page == 0:
        page_1_1()
    elif st.session_state.page == 1:
        page_1_2()
    elif st.session_state.page == 2:
        page_1_3()
    elif st.session_state.page == 3:
        page_2_1()
    elif st.session_state.page == 4:
        page_2_2()
    elif st.session_state.page == 5:
        page_3_1_1()
    elif st.session_state.page == 6:
        page_3_1_2()
    elif st.session_state.page == 7:
        page_3_2_1()
    elif st.session_state.page == 8:
        page_3_2_2()
    elif st.session_state.page == 9:
        page_3_3_1()
    elif st.session_state.page == 10:
        page_3_3_2()
    elif st.session_state.page == 11:
        page_3_4_1()
    elif st.session_state.page == 12:
        page_3_4_2()
    elif st.session_state.page == 13:
        page_3_5_1()
    elif st.session_state.page == 14:
        page_3_5_2()
    elif st.session_state.page == 15:
        page_3_6_1()
    elif st.session_state.page == 16:
        page_3_6_2()
    elif st.session_state.page == 17:
        page_3_7_1()
    elif st.session_state.page == 18:
        page_3_7_2()
    elif st.session_state.page == 19:
        page_result()
        

if __name__ == "__main__":
    app()
