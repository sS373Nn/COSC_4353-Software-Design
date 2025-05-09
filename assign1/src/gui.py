import tkinter as tk
from tkinter import messagebox

from src.color import Color
from src.result import Result
from src.match import Match
from src.master_mind import play, select_colors

color_picked = [None, None]
attempt_number = 1
puzzle_colors = select_colors()
game_state = Result.LOST
MAX_ATTEMPTS = 20
NUMBER_OF_COLORS_PER_GUESS = 6

def build_gui():
    master = tk.Tk()
    master.title("Master Mind Game")
    master.geometry("800x1025")

    submit_button = tk.Button(master, text="SUBMIT GUESS", command=lambda: on_submit_button_click(color_boxes, feedback_frames, master))
    submit_button.pack(side="top", pady=10, padx=20)

    create_color_buttons(master, on_color_click)

    color_boxes = []
    feedback_frames = []

    color_boxes, feedback_frames = create_color_rows(master, create_color_box, create_feedback_box, bind_buttons)

    end_game_button = tk.Button(master, text="END GAME", command=lambda: destroy_gui(master))
    end_game_button.pack(side="bottom", pady=10)

    return master

def destroy_gui(window):
    window.destroy()

def create_color_buttons(gui_window, click_function):
    color_frame = tk.Frame(gui_window)
    color_frame.pack(side="top", pady=10)

    colors = [Color.BLUE, Color.BROWN, Color.CYAN, Color.GREEN, Color.ORANGE, Color.PINK, Color.PURPLE, Color.RED, Color.WHITE, Color.YELLOW]
    for color in colors:
        button = tk.Button(color_frame, name=color.name.lower(), bg=color.name.lower(), width=5, height=1, command=lambda c=color: click_function(c))
        button.color = color
        button.pack(side="left", padx=5)

    return color_frame

def create_color_box(input_frame):
    color_box = tk.Label(input_frame, text="", bg="#D3D3D3", width=5, height=2, borderwidth=1, relief="solid")
    return color_box

def create_feedback_box(feedback_frame):
    feedback_box = tk.Label(feedback_frame, text="", bg="gray", width=2, height=2, borderwidth=1, relief="solid")
    return feedback_box

def create_color_rows(gui_window, create_selection_box_function, create_feedback_box_function, bind_buttons_function):
    color_boxes = []
    feedback_frames = []

    for row in range(MAX_ATTEMPTS):
        row_frame = tk.Frame(gui_window)
        row_frame.pack(pady=5)

        row_color_boxes = []
        for col in range(NUMBER_OF_COLORS_PER_GUESS):
            color_box = create_selection_box_function(row_frame)
            row_color_boxes.append(color_box)
            color_box.pack(side="left", padx=5)

        if row == 0:
            bind_buttons_function(row_color_boxes)

        row_feedback_boxes = []
        feedback_frame = tk.Frame(row_frame)
        feedback_frame.pack(side="right", padx=20)
        for fb_col in range(NUMBER_OF_COLORS_PER_GUESS):
            feedback_box = create_feedback_box_function(feedback_frame)
            row_feedback_boxes.append(feedback_box)
            feedback_box.pack(side="left", padx=3)

        color_boxes.append(row_color_boxes)
        feedback_frames.append(row_feedback_boxes)

    return color_boxes, feedback_frames

def fill_selected_color_array(colors_picked):
    color_array = []

    for box in colors_picked:
        if box.cget('bg') == "#D3D3D3":
            return color_array

        color_array.append(box.color)

    return color_array

def update_feedback_boxes(feedback_box_array, result_of_guess):
    exact = result_of_guess[Match.EXACT]
    present = result_of_guess[Match.PRESENT]

    for box in feedback_box_array[: exact]:
        box.config(bg="black")
    
    for box in feedback_box_array[exact: exact + present]:
        box.config(bg="silver")

def bind_buttons(array_of_boxes):
    for box in array_of_boxes:
        box.bind("<Button-1>", lambda e, b=box: on_color_box_click(b))

def unbind_buttons(array_of_boxes):
    for box in array_of_boxes:
        box.unbind("<Button-1>")

def on_color_click(color):
    global color_picked
    color_picked[0] = color.name.lower()
    color_picked[1] = color

def on_color_box_click(box):
    if color_picked:
        box.config(bg=color_picked[0])
        box.color = color_picked[1]

def show_game_over(game_status, gui_window):
    if game_status == Result.WON:
        messagebox.showinfo("CONGRATULATIONS!", "You've won!")
        destroy_gui(gui_window)
    
    elif game_status == Result.GAME_OVER:
        messagebox.showinfo("GAME OVER", "Sorry, better luck next time!")
        destroy_gui(gui_window)
    
def handle_game_over(selected_colors, user_colors, attempts, gui_window):
    try:
        result, attempts, response = play(selected_colors, user_colors, attempts)

        if result == Result.WON:
            show_game_over(Result.WON)

        elif attempts == MAX_ATTEMPTS + 1:
            show_game_over(Result.GAME_OVER, gui_window)

        else:
            return result, attempts, response

    except Exception as e:
        if str(e) == str(Result.GAME_OVER):
            print("GAME OVER")
            show_game_over(Result.GAME_OVER, gui_window)
            return

def on_submit_button_click(all_selection_boxes, all_feedback_boxes, gui_window):
    global attempt_number
    global game_state
    selected_colors = []

    if attempt_number <= len(all_selection_boxes):

        unbind_buttons(all_selection_boxes[attempt_number - 1])

        selected_colors = fill_selected_color_array(all_selection_boxes[attempt_number - 1])
        if len(selected_colors) < NUMBER_OF_COLORS_PER_GUESS:
            bind_buttons(all_selection_boxes[attempt_number - 1])
            return None

        game_state, attempt_number, silver_and_black_boxes = handle_game_over(puzzle_colors, selected_colors, attempt_number, gui_window)

        update_feedback_boxes(all_feedback_boxes[attempt_number - 2], silver_and_black_boxes)

        if attempt_number <= len(all_selection_boxes):
            bind_buttons(all_selection_boxes[attempt_number - 1])

if __name__ == "__main__":
    game_window = build_gui()
    game_window.mainloop()
