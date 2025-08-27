import tkinter as tk
from tkinter import ttk

class ArrowEnergyCalculator():
    """Calculates the foot-pounds of energy based on an arrows weight and speed."""
    def __init__(self, root):
        """Initiate."""
        self.root = root
        self.root.title("Arrow Energy Calculator")
        self.root.geometry("300x300")

        self.display()


    def display(self):
        """Main page display."""
        # "Arrow Weight" label.
        self.arrow_weight_label = ttk.Label(root, text="Arrow Weight (Grains)")
        self.arrow_weight_label.pack(pady=10)

        # "Arrow Weight" entry.
        self.arrow_weight_entry = ttk.Entry(root)
        self.arrow_weight_entry.pack(pady=10)

        # "Arrow Speed" label.
        self.arrow_speed_label = ttk.Label(root, text="Arrow Speed (Feet Per Second)")
        self.arrow_speed_label.pack(pady=10)

        # "Arrow Speed" entry.
        self.arrow_speed_entry = ttk.Entry(root)
        self.arrow_speed_entry.pack(pady=10)

        # "Calculate Foot-Pounds" button.
        self.calculate_foot_pounds_button = tk.Button(root, text="Calculate Foot-Pounds", command=self.foot_pounds_formula)
        self.calculate_foot_pounds_button.pack(pady=10)

        # "Foot-Pounds" label.
        self.foot_pounds_label = ttk.Label(root, text="Foot-Pounds")
        self.foot_pounds_label.pack(pady=10)


    def foot_pounds_formula(self):
        """Calculate the foot-pounds of energy."""
        #foot-pounds=(grams*fps^2)/450240
        try:
            weight = float(self.arrow_weight_entry.get())
            speed = float(self.arrow_speed_entry.get())
            energy = (weight * (speed**2)) / 450240
            self.foot_pounds_label.config(text=f"Foot-Pounds: {energy:.2f}")

        except ValueError:
            self.foot_pounds_label.config(text="Error: Enter a valid number")


if __name__ == "__main__":
    root = tk.Tk()
    app = ArrowEnergyCalculator(root)
    root.mainloop()