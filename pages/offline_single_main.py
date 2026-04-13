import streamlit as st
from modules import doc_functions

st.title("Voice of Grace")

st.divider()

if False:
    with st.expander("Very Important Info (Click here to open)!", icon=":material/info:", expanded=False):

        TERMS_AND_CONDITIONS_TAB, PRIVACY_POLICY_TAB = st.tabs(["Terms & Conditions", "Privacy Policy"], width="stretch")

        with TERMS_AND_CONDITIONS_TAB:
            doc_functions.terms_and_conditions()

        with PRIVACY_POLICY_TAB:
            doc_functions.privacy_policy()

single_ticket_orders_form_embed_link = '<iframe class="airtable-embed" src="https://airtable.com/embed/app1FPAjv4OEUJ5T4/paggDj87JU5V1VSHD/form" frameborder="0" onmousewheel="" width="100%" height="800" style="background: transparent; border: 1px solid #ccc;"></iframe>'

st.markdown(single_ticket_orders_form_embed_link, unsafe_allow_html=True)
