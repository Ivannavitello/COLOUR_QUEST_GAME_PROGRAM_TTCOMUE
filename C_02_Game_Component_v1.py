from tkinter import *
from functools import partial # To prevent unwanted windows

class StartGame:

    """
    Initial Game interface (asks users how many rounds they
    would like to play)
    """
    def __init__(self):
        """
        Gets number of rounds from user
        """
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Create play button ...
        self.play_button = Button(self.start_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#005708", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)


    def check_rounds(self):
        """
        Checks users have entered 1 0r more rounds
        """

        Play(5)
        # Hide root window (ie: hide rounds choice window)
        root.withdraw()


# Reminder that when we're wanting to invoke
# a new class there's three steps, it's button function and class

class Play:

    """
    Interface for playing the Colour Quest game
    """
    # (previous mistake of making this "int" and not "init"
    def __init__(self,how_many):

        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        # body font for most labels ...
        body_font = ("Arial", "12")

        # List for label details (text | font | background | row)
        play_labels_list = [
            ["Round # of #", ("Arial", "16", "bold"), None, 0],
            ["Score to beat: #", body_font, "#FFF2CC", 1],
            ["Choose a colour below. Good luck. #", body_font, "#DSE804", 2],
            ["You chose, result", body_font, "#D5E8D4", 4]

        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.game_frame, text=item[0], font=item[1],
                                    bg=item[2], wraplength=300, justify="left")
            self.make_label.grid(row=item[3], pady=10, padx=10)

            play_labels_ref.append(item)

        # Retrieve Labels so they can be configured later
        self.heading_label = play_labels_ref[0]
        self.target_label = play_labels_ref[1]
        self.results_label = play_labels_ref[3]




    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        # This will get rid of  our dialog
        self.play_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk ()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()

