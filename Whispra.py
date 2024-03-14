import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time, random
from tinydb import TinyDB, Query




db = TinyDB("messages.json")
data = Query()

st.markdown("""
# Whispra
developer email: rynstheoverlord@gmail.com
""")

if st.button("why isn't my message sending?"):
  st.toast("well you haven't entered your username yet, that's why.")
auto_refresh = st.toggle("Enable Auto refresh")

st.divider()


def add_message(username, message):
  db.insert({'username': username, 'message': message, 'timesent': time.ctime()})
  

def render_messages():
  for block in db.all():
    format = [block['username'], block['message'], block['timesent']]
    
    with st.chat_message("user"):
      st.write(f"**{format[0]}**")
      st.write(format[1])
      st.caption(f"Sent at {format[2]}")
  if len(db.all()) > 20:
    db.truncate()





st.title("Converse")
st.write("Anonymous chatting...")




username = st.text_input("Enter your username (don't use your real name)")

user_message = st.chat_input("Enter your message here")

if user_message:
  if len(username) > 0:     
    add_message(username, user_message)
  else:
    st.error(":red[please enter a username above to continue]")
  render_messages()




if auto_refresh:
  refresh_count = st_autorefresh(interval=1000, key="chatmessagecounter")
  st.button("Refresh", disabled=True)

else:
  if st.button("Refresh"):
    render_messages()
    st.toast("Refreshed!")
