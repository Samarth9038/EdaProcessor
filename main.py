import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder

st.set_page_config(page_title="Preprocessor", layout="wide")

st.title("Data Preprocessor and EDA tool")

dataset = st.file_uploader("Choose a file")
loaded = False
if dataset is not None:
    if "df" not in st.session_state or st.session_state.get("file_name") != dataset.name:
        st.session_state.df = pd.read_csv(dataset)
        st.session_state.file_name = dataset.name
    loaded = True
else:
    st.write("No file uploaded")

if "viz_column" not in st.session_state:
    st.session_state.viz_column = None

if loaded:
    df = st.session_state.df
    
    if len(df) >= 10:
        display = df.head(10)
        st.subheader("First few rows:")
        st.write(display)
    else:
        st.write(df)

    infodf = pd.DataFrame(
    {
        "Column":df.columns,
        "Type":df.dtypes.values,
    })

    st.header("Detected Columns:")
    for i in infodf['Column']:
        st.markdown(f"{i}, type: **{df[i].dtype}**")
        croot1, croot2, croot3, croot4, _ = st.columns([1,1, 1,4, 1])
        typecol = str(df[i].dtype)
        isnumeric = "int" in typecol or "float" in typecol
        iscategorical = "object" in typecol or "category" in typecol
        with croot1:
            drop = st.button("Drop", i)
            if drop:
                st.session_state.df = df.drop(columns=i)
                df = st.session_state.df
                st.caption(f"Dropped {i} column.")
                st.rerun()
        with croot2:
            with st.popover("Preprocess"):
                if isnumeric:
                    st.markdown("**Numeric Scaling:**")
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Standardize", "standardize"+i):
                            sc = StandardScaler()
                            st.session_state.df[i] = sc.fit_transform(df[[i]])
                            st.rerun()
                    with col2:
                        if st.button("Normalize", "normalize"+i):
                            nm = MinMaxScaler()
                            st.session_state.df[i] = nm.fit_transform(df[[i]])
                            st.rerun()
                    if st.button("Convert to Categorical", "catconv"+i):
                        st.session_state.df[i] = st.session_state.df[i].astype(str)
                        st.rerun()
                if iscategorical or isnumeric:
                    st.markdown("**Encoding:**")
                    col3, col4 = st.columns(2)
                    
                    with col3:
                        if st.button("Label Encode", "le"+i):
                            le = LabelEncoder()
                            st.session_state.df[i] = le.fit_transform(df[i].astype(str))
                            st.rerun()
                    with col4:
                        if st.button("One Hot Encode", "ohe"+i):
                            ohe = OneHotEncoder(sparse_output=False)
                            encoded = ohe.fit_transform(df[[i]])
                            colnew = ohe.get_feature_names_out([i])
                            encodedDf = pd.DataFrame(
                                encoded,
                                columns=colnew,
                                index=df.index
                            )
                            st.session_state.df = pd.concat([st.session_state.df.drop(columns=[i]), encodedDf], axis = 1)
                            st.rerun()


                st.markdown("**Missing Values:**")
                col5, col6 = st.columns(2)
                with col5:
                    with st.popover("Fill Nulls"):
                        c1, c2, c3 = st.columns(3)
                        with c1:
                            if st.button("Mean", "mean"+i):
                                st.session_state.df[i] = st.session_state.df[i].fillna(df[i].mean())
                                st.rerun()
                        with c2:
                            if st.button("Median", "median"+i):
                                st.session_state.df[i] = st.session_state.df[i].fillna(df[i].median())
                                st.rerun()
                        with c3:
                            if st.button("Mode", "mode"+i):
                                mval = df[i].mode()[0]
                                st.session_state.df[i] = st.session_state.df[i].fillna(mval)
                                st.rerun()
                with col6:
                    if st.button("Drop Nulls", "dropnull"+i):
                        st.session_state.df = st.session_state.df.dropna(subset=[i])
                        st.rerun()
        with croot3:
            if st.button("Show Distribution", "showdistri" + i):
                st.session_state.viz_column = i
                pass
        if st.session_state.get('viz_column') == i:
            with croot4:
                st.write(f"### Insights: {i}")
            if isnumeric:
                counts, _ = np.histogram(df[i].dropna(), bins=20)
                st.line_chart(counts)
            else:
                topcats = df[i].value_counts().head(20)
                st.bar_chart(topcats)
            
            if st.button("Close Chart", "close" + i):
                st.session_state.viz_column = None
                st.rerun()
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Processed Data", csv, "processed.csv", "text/csv")