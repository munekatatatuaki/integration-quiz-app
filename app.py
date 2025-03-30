import random
import sympy as sp
import streamlit as st

# 定積分問題の生成
def generate_problem():
    x = sp.symbols('x')
    terms = random.randint(1, 5)
    expression = sum(random.randint(1, 10) * x**random.randint(0, 3) for _ in range(terms))
    a = random.randint(-5, 5)
    b = random.randint(a + 1, 10)
    definite_integral = sp.integrate(expression, (x, a, b))
    return expression, a, b, definite_integral

# 数式を文字列に変換
def format_expression(expr):
    return str(expr).replace("**", "^")

st.title("定積分クイズ")

if "expr" not in st.session_state:
    st.session_state.expr, st.session_state.a, st.session_state.b, st.session_state.answer = generate_problem()

st.write(f"∫({format_expression(st.session_state.expr)})dx, 範囲: {st.session_state.a} から {st.session_state.b} まで")

user_input = st.text_input("解答を入力してください:")

if st.button("答え合わせ"):
    try:
        user_answer = sp.sympify(user_input)
        if user_answer == st.session_state.answer:
            st.success("正解！")
        else:
            st.error("不正解")
    except Exception as ex:
        st.error(f"入力が無効です: {ex}")

if st.button("次の問題"):
    st.session_state.expr, st.session_state.a, st.session_state.b, st.session_state.answer = generate_problem()
    st.experimental_rerun()
