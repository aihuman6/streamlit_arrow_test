import pandas as pd
import streamlit as st


arrow = ('up','down', 'up')
direction = (1, 0, 1)

df = pd.DataFrame({'arrow_type': arrow,'direction':direction})

df.direction.replace([1, 0],["&#8593;", "&#8595;"], inplace=True)    #replace the values using html codes for up and down arrow.

html_df= df.to_html(escape=False, index=False)    #convert the df to html for better formatting view

html_df = html_df.replace("<td>&amp;#8595;</td>","<td><font color = red>&#8595;</font></td>")    # Remove extra tags and added red colour to down arrow
html_df = html_df.replace("<td>&amp;#8593;</td>","<td><font color = green>&#8593;</font></td>")    # Remove extra tags and added green colour to up arrow

st.write(html_df, unsafe_allow_html=True)
