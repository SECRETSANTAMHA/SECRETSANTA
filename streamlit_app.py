import streamlit as st
import base64
from pathlib import Path

# ------------------ BACKGROUND ---------------------

st.markdown(
    """
    <style>
    .stApp {
        background: url("background.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* ALL normal text */
    .stMarkdown, 
    .stMarkdown p,
    .stText,
    .stCaption,
    .stAlert,
    .stInfo,
    .stSuccess,
    .stWarning,
    .stError,
    span, p, div {
        color: white !important;
    }

    /* Input labels */
    label {
        color: white !important;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Expander title */
    div[data-testid="stExpander"] > div:first-child {
        color: white !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Primary button */
    button[kind="primary"] {
        color: white !important;
    }

    /* Secondary button (transparent look) */
    button[kind="secondary"] {
        background-color: transparent !important;
        color: white !important;
        border: 1px solid white !important;
    }

    /* Tertiary button */
    button[kind="tertiary"] {
        background-color: transparent !important;
        color: white !important;
    }

    /* Button hover */
    button:hover {
        filter: brightness(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)








def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local("background.png")

st.markdown(
    """
    <style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.65);  /* dark glass effect */
        backdrop-filter: blur(6px);
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Sidebar headers */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Top header bar (contains sidebar toggle icon) */
    header[data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0.65);
        backdrop-filter: blur(6px);
    }

    /* Sidebar collapse / expand icon */
    button[kind="header"] {
        color: white !important;
    }

    /* Icon hover effect */
    button[kind="header"]:hover {
        background-color: rgba(255, 255, 255, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True
)










# ------------------ RULES --------------------------
with st.sidebar:
    st.header("HOW TO PLAY")
    st.write("-> A tile can only be moved to an empty spot.")
    st.write("-> A tile can be moved only if it is adjacent to the empty spot")
    st.write("-> To move a tile, you must tap on it.")
    st.header("OBJECTIVE")
    st.write("You must rearrange the tiles such that it is arranged as follows:")
    st.write(" 1  2  3  4")
    st.write(" 5  6  7  8")
    st.write(" 9  10  11  12")
    st.write(" 13  14  15  _")
    st.write("'_' represents an empty spot")




    
# ---------------------- game play -----------------------------
st.title("🎄 PUZZLE 🧩")

if "board" not in st.session_state:
    st.session_state["board"] = [
        [2, 5, 7, 4],
        [9, 12, 13, 8],
        [14, 6, 11, 3],
        [1, 10, 15, 0]
    ]




# ------------------- initial board(shuffled) -----------------

def shuffled_board():
    board=[[2, 5, 7, 4],
           [9, 12, 13, 8],
           [14, 6, 11, 3],
           [1, 10, 15, 0]]
    
    return board

# ---------------- find empty tile ------------------------

def find_empty_tile(board):
    for row in range(4):
        for col in range(4):
            if board[row][col]==0:
                return row,col


# ------------ check if two tiles are adjacent -------------

def adjacent_check(tile_row,tile_col,empty_row,empty_col):
    row_distance=abs(tile_row-empty_row)
    col_distance=abs(tile_col-empty_col)

    if row_distance+col_distance==1:
        return True
    else:
        return False

# -------------- check if puzzle is solved --------------------

def solved_check(board):
    if board == [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 0]]:
        return True

# --------------- initializing session state --------------------


if "board" not in st.session_state:
    st.session_state.board = shuffled_board()

# ---------------- draw the board -------------------------------

board = st.session_state.board
empty_row, empty_col = find_empty_tile(board)

for row in range(4):
    cols = st.columns(4)
    for col in range(4):
        value = board[row][col]

        if value == 0:
            cols[col].button(" ", disabled=True, key=f"{row}-{col}")
        else:
            clicked = cols[col].button(str(value), key=f"{row}-{col}")

            if clicked:
                if adjacent_check(row, col, empty_row, empty_col):
                    board[empty_row][empty_col] = value
                    board[row][col] = 0
                    st.rerun()


# ------------------- check win condition --------------------------------

if solved_check(board):
    st.success("KUDOS! you cracked it!")
    st.write("The password is: 000")



if st.button("RESET", type="secondary"):
    st.session_state.board = [
        [2, 5, 7, 4],
        [9, 12, 13, 8],
        [14, 6, 11, 3],
        [1, 10, 15, 0]
    ]



    st.rerun()
