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



import streamlit as st
import random

# 元素のリスト
elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

# ガチャガチャの関数
def gacha():
    return random.choice(elements)


# Streamlitアプリケーション
def main():
    st.title("原子周期表のガチャガチャ")
    st.write("ランダムに元素を選択します。")
    if st.button("ガチャを回す"):
        result = gacha()
        st.write(f"選ばれた元素は {result} です！")

if __name__ == "__main__":
    main()