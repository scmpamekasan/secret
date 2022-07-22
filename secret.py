import streamlit as st
import os



# Everything in this section will be available as an environment variable
db_username = "Pamekasan"
db_password = "12345"

# You can also add other sections if you like.
# The contents of sections as shown below will not become environment variables,
# but they'll be easily accessible from within Streamlit anyway as we show
# later in this doc.
[my_cool_secrets]
things_i_like = ["Streamlit", "Python"]

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:


st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
