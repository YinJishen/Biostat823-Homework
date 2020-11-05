import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

@st.cache
def load_data_1():
    df = pd.read_csv("data1_total.csv")
    return df

@st.cache
def load_data_2():
    df = pd.read_csv("data1_col.csv")
    return df

@st.cache
def load_data_3():
    df = pd.read_csv("data2_all.csv")
    return df



def main():
    df1 = load_data_1()
    df2 = load_data_2()
    df3 = load_data_3()
    page = st.sidebar.selectbox("Choose a page", ["Table 4", "Table 6"])

    if page == "Table 4":
        st.header("Top 20 doctorate-granting institutions ranked by number of doctorate recipients, by broad field of study: 2017")
        mode = st.selectbox("Total or By Field", ['Total', 'By Field'])
        if mode == 'Total':
            x = 'field'
            y = 'total'
            graph = alt.Chart(df1).mark_bar().encode(
                x = alt.X(x, sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20)), 
                y = alt.Y(y, sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20)),
                color = x,
                tooltip = ["field", "total"]).interactive()
            st.altair_chart(graph, use_container_width=True)
            #st.write(graph)
        elif mode == 'By Field':
            field = st.selectbox("Choose a field", list(np.unique(df2['field'])))
            x = "Field and institution"
            y = "Doctorate recipients"
            tmp = df2.loc[df2['field'] == field,]
            graph = alt.Chart(tmp).mark_bar().encode(
                x = alt.X(x, sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20)), 
                y = alt.Y(y, sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20, title="Number")),
                tooltip = [x, y]).interactive()
            st.altair_chart(graph, use_container_width=True)
    elif page == "Table 6":
        st.header("Doctorates awarded, by state or location, broad field of study, and sex of doctorate recipients: 2017")
        field = st.selectbox("Choose a field", list(np.unique(df3['field'])))
        tmp = df3.loc[df3['field']==field,]
        state = st.selectbox("Choose a state/location", list(np.unique(tmp['State or location'])))
        graph = alt.Chart(tmp.loc[tmp["State or location"] == state,]).mark_bar().encode(
            x = alt.X("sex", sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20)), 
            y = alt.Y("value", sort=None, axis=alt.Axis(labelFontSize=15, titleFontSize=20)),
            tooltip = ["field", "sex", "value"]).interactive()
        st.altair_chart(graph, use_container_width=True)
        st.write("Note: For State Not Available in the options, it's either 0 or confidential.")
        
if __name__ == "__main__":
    main()