import streamlit as st
import time
from PIL import Image   

st.title('Streamlit 超入門')


st.write('プログレスバー')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration + {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示するよ')
if button:
    right_column.write('ここは右だよ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')


# option = st.text_input('あなたの趣味は？')

# 'あなたの趣味は', option

# condition = st.slider('あなたの調子は？',0,100,50)
# 'コンディション', condition 

# if st.checkbox('show image'):
#     img = Image.open('image.png')
#     st.image(img, caption='genshin', use_column_width=True)



# """
# # タイトル

# ## サブタイトル

# ### カテゴリタイトル

# ``` python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```



# """