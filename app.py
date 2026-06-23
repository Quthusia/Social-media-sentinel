import streamlit as st
import pandas as pd
import os

# Smart Local Rule-Based Data Transformation Function (100% Stable Offline Mode)
def transform_text_offline(text_content):
    text_lower = str(text_content).lower()
    
    # 1. Look for highly critical or negative words to assign Sentiment & Severity
    critical_negative_words = ['freeze', 'crash', 'broke', 'bug', 'broken', 'expensive', 'slow', 'fail', 'robbery', 'greed', 'bad', 'ruined', 'frustrating', 'error', 'locked', 'rude', 'cold', 'unappetizing', 'torn']
    positive_words = ['love', 'good', 'great', 'awesome', 'amazing', 'perfect', 'shoutout', 'excellent', 'fast', 'value', 'delicious', 'premium', 'friendly', 'clean', 'hygiene']

    if any(word in text_lower for word in critical_negative_words):
        sentiment = "Negative"
        # Calculate a high severity level if multiple urgent words are found
        if any(word in text_lower for word in ['freeze', 'crash', 'bug', 'fail', 'error', 'locked', 'charged']):
            severity = 5 if 'immediately' in text_lower or 'broke' in text_lower else 4
        else:
            severity = 3
    elif any(word in text_lower for word in positive_words):
        sentiment = "Positive"
        severity = 1
    else:
        sentiment = "Neutral"
        severity = 2
        
    # 2. Assign the operational department column based on keyword matching
    if any(w in text_lower for w in ['app', 'bug', 'freeze', 'crash', 'button', 'screen', 'tech', 'website', 'page', 'error', 'checkout']):
        category = "Technical"
    elif any(w in text_lower for w in ['price', 'expensive', 'cost', 'money', 'billing', 'charged', 'rupees', 'fee', 'subscription']):
        category = "Pricing"
    elif any(w in text_lower for w in ['delivery', 'driver', 'package', 'shipping', 'arrive', 'slow', 'wait', 'rain', 'torn']):
        category = "Shipping"
    else:
        category = "Support"

    return {"Sentiment": sentiment, "Category": category, "Severity": severity}

# --- Streamlit Dashboard Interface Layout ---
st.set_page_config(page_title="Social Media Sentinel", layout="wide")
st.title("🛡️ Social Media Sentinel: Enterprise Analytics Engine")
st.markdown("### Powered by Rule-Based NLP Data Pipelines (Production Stable)")

st.markdown("## 🕹️ Live Model Sandbox (For Interviewers)")
user_input = st.text_input("Type any customer comment here to test the data transformation layer:")

if user_input:
    result = transform_text_offline(user_input)
    col_res1, col_res2, col_res3 = st.columns(3)
    col_res1.metric("Predicted Sentiment", result.get("Sentiment"))
    col_res2.metric("Target Department", result.get("Category"))
    col_res3.metric("Calculated Severity Level", f"{result.get('Severity')} / 5")

st.markdown("---")
st.markdown("## 📊 Bulk Pipeline Operations")

if os.path.exists("dataset.csv"):
    raw_df = pd.read_csv("dataset.csv")
    st.write(f"📁 **Data Source Detected**: `dataset.csv` contains **{len(raw_df)} total records** loaded.")
    
    # UNLOCKED TO 1000 RECORDS MAX VALUE BELOW
    sample_size = st.slider("Select batch size to process through the pipeline:", min_value=10, max_value=1000, value=1000)
    
    if st.button("🚀 Execute Batch Analysis Pipeline"):
        with st.spinner(f"Processing {sample_size} records through local NLP transform layer..."):
            batch_df = raw_df.head(sample_size)
            structured_results = []
            
            for index, row in batch_df.iterrows():
                analysis = transform_text_offline(row['Review_Text'])
                processed_row = {
                    "Review_ID": row['Review_ID'],
                    "Review_Text": row['Review_Text'],
                    "Sentiment": analysis.get("Sentiment"),
                    "Category": analysis.get("Category"),
                    "Severity": analysis.get("Severity")
                }
                structured_results.append(processed_row)
            
            st.session_state['processed_data'] = pd.DataFrame(structured_results)
            st.success("Batch pipeline processing completed successfully.")

    if 'processed_data' in st.session_state:
        df = st.session_state['processed_data']
        
        st.markdown("### Pipeline Analytics Dashboard")
        c1, c2, c3 = st.columns(3)
        c1.metric("Batch Records", len(df))
        c2.metric("Mean Severity Index", round(df['Severity'].mean(), 2))
        c3.metric("Escalation Flags", len(df[df['Severity'] >= 4]))
        
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.markdown("#### Sentiment Overview")
            st.bar_chart(df['Sentiment'].value_counts())
        with chart_col2:
            st.markdown("#### Category Allocation")
            st.bar_chart(df['Category'].value_counts())
            
        st.subheader("📋 Clean Structured Dataset")
        st.dataframe(df, use_container_width=True)
else:
    st.error("Error: `dataset.csv` not detected in workspace.")
