import streamlit as st
from modules import doc_functions

if False:
    with st.expander("Very Important Info (Click here to open)!", icon=":material/info:", expanded=False):

        TERMS_AND_CONDITIONS_TAB, PRIVACY_POLICY_TAB = st.tabs(["Terms & Conditions", "Privacy Policy"], width="stretch")

        with TERMS_AND_CONDITIONS_TAB:
            doc_functions.terms_and_conditions()

        with PRIVACY_POLICY_TAB:
            doc_functions.privacy_policy()

family_ticket_orders_form_embed_link = '<iframe class="airtable-embed" src="https://airtable.com/embed/app1FPAjv4OEUJ5T4/pagtrSD4inJU17gHc/form" frameborder="0" onmousewheel="" width="100%" height="800" style="background: transparent; border: 1px solid #ccc;"></iframe>'

st.markdown(family_ticket_orders_form_embed_link, unsafe_allow_html=True)
