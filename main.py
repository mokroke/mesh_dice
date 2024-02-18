import streamlit as st

def main():
    st.title('Simple Square Calculator')

    # ユーザーに数値を入力してもらう
    number = st.number_input('Enter a number:')

    # 入力された数値を二乗して表示する
    squared_number = number ** 2
    st.write(f'The square of {number} is {squared_number}')

if __name__ == "__main__":
    main()
