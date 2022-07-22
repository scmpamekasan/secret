import streamlit as st
import os



# Everything in this section will be available as an environment variable

# You can also add other sections if you like.
# The contents of sections as shown below will not become environment variables,
# but they'll be easily accessible from within Streamlit anyway as we show
# later in this doc.

# Everything is accessible via the st.secrets dict:


# Verbose version

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
