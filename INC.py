import pandas as pd
import streamlit as st

st.set_page_config(page_title="INC Data analysis",
                   page_icon=":bar_chart:",
                   layout="wide")
# noinspection PyTypeChecker
df = pd.read_excel(
    io="Financials.xlsx",
    engine="openpyxl",
    sheet_name='Financials',
    skiprows=0,
    usecols='A:L',
    nrows=100)

st.sidebar.header("Please select the Domain filter here")
Domain = st.sidebar.multiselect(
    "Select the Domain:",
    options=df["Domain"].unique(),
    default=df["Domain"].unique()
)

st.sidebar.header("Please select the Country filter here")
Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

st.sidebar.header("Please select the Channel filter here")
Channel = st.sidebar.multiselect(
    "Select the Channel:",
    options=df["Channel"].unique(),
    default=df["Channel"].unique()
)

df_selection = df.query(
    "Domain == @Domain & Country == @Country & Channel == @Channel")

st.title(":bar_chart: INC Data Analysis & Prediction")
st.markdown("##")

total_INC = int(df_selection["INC"].count())

print(total_INC)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader(f"total_INC :white_check_mark: {total_INC}")
with middle_column:
    st.subheader(f"total_INC :100:{total_INC}")
with right_column:
    st.subheader(f"total_INC {total_INC}:star:")

Txt_Search = st.text_input("Enter the Search text ")

df_search = df.query(
    " Domain == @Txt_Search | Severity == @Txt_Search | INC_category == @Txt_Search | INC_subcategory == @Txt_Search")
# df['Domain']=df['Domain'].str.lower()
df_s = df.query(
    '(INC.str.lower()).str.contains(@Txt_Search) | (Domain.str.lower()).str.contains(@Txt_Search) | ('
    'Severity.str.lower()).str.contains(@Txt_Search)| (INC_category.str.lower()).str.contains(@Txt_Search) | ('
    'Country.str.lower()).str.contains(@Txt_Search)')
# if (df_s is not None):


# st.dataframe(df_search)
st.dataframe(df_s)
st.subheader(f"Overall Details:white_check_mark:")
# st.dataframe(df_selection)
