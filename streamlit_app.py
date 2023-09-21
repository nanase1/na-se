import streamlit as st
import random

# タイトルを設定
st.title("おみくじアプリ")

if st.button("おみくじを引く"):
    results=["大吉","中吉","小吉","吉","凶","大凶",]
    result=random.choice(results)
    st.write(f"結果:{result}")

    
# タイトルを設定
st.title("今日する教科")

if st.button("さあ、選べ、、、"):
    results=["古文","論国","数Ⅱ","物理","公共","地理","化学","数Ｂ"]
    result=random.choice(results)
    st.write(f"結果:{result}")

 