import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kuqo5gvy.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Jessica :wave:")
    st.title("An English teacher From Australia")
    st.write(
        """
        Hello there! My name is Jessica, a vibrant English teacher hailing from the sun-kissed coasts of Australia. I've been teaching for more than five years, and let me tell you, it's been a journey filled with endless learning and countless smiles. I absolutely adore children; their energy, their curiosity, their potential. Each day in the classroom is a new adventure and I wouldn't trade it for anything else.

But teaching isn't my only passion. I'm a bona fide food lover, always eager to whip up new recipes and share my culinary creations with family and friends. And then there are my plants. Nothing brings me more joy than getting my hands in the soil and nurturing my green babies. It's a kind of therapy, really. The great outdoors is my sanctuary, where I find inspiration and rejuvenation.

Bringing my love for food, plants, and nature into the classroom has been such a delight. I find that it adds a spark to my English lessons and fosters a sense of wonder and exploration in my students. And in the end, that's what teaching is all about for me - inspiring young minds to discover, learn, and grow. So here's to the joy of teaching and the passion for life!
        """
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Here is how I can help you")
        st.write("##")
        st.write(
            """
            As your English teacher, I can help you with:
            - Streamlining your English learning journey if you're currently studying the language and often find yourself thinking - "there has to be a better way."
            - Enhancing your professional communication skills through Business English, enabling you to navigate corporate communications, negotiations, and presentations with confidence.
            - Improving your conversational English, allowing you to communicate effectively and naturally in diverse social settings.
            - Overcoming challenges in English grammar, vocabulary, pronunciation, or comprehension with personalized and effective solutions.
            - Delving into the world of English literature, where you can explore renowned works while honing your analytical and critical thinking skills.

            If this sounds interesting to you, and you're ready to take your English skills to the next level, don't hesitate to get in touch. You can submit your inquiry through the contact form at the bottom of my page. I'm looking forward to embarking on this linguistic journey with you!
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# # ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/leonardogiroldo@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()