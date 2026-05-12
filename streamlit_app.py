import streamlit as st

st.markdown("*Knowledge* is **Very** ***Important***.")
st.markdown('''
    :red[we] :orange[can] :green[change] :blue[the] :violet[world]
    :gray[Go] :rainbow[to] and :blue-background[Emas] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
