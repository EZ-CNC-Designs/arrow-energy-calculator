import pyinputplus as pyip

class ArrowEnergyCalculator():
    """Calculates the foot-pounds of energy based on an arrows weight and speed.
    
    Methods:
        receive_user_input
        calculate_energy_total_weight
        calculate_energy_component_weight
        check_lethality

    Examples:
        arrow_1 = ArrowEnergyCalculator()
        energy = arrow_1.receive_user_input()
        arrow1.check_lethality(energy)
    """

    def __init__(self):
        pass

        
    def receive_user_input(self):
        """Prompt the user on information about their arrows.
        
        Returns:
            float: Energy of the users arrow in ft.-lbs.
        """
        know_weight = pyip.inputYesNo("Do you know the total weight of the arrow (yes/no)? "
                                        "If not, you will be asked to provide component weights: ")
        if know_weight == "yes":
            # Ask the user for total arrow weight & arrow speed
            self.arrow_weight = pyip.inputNum("Enter the arrow weight (grains): ")
            self.arrow_speed = pyip.inputNum("Enter the arrow speed (feet per second): ")
            arrow_energy = self.calculate_energy_total_weight(arrow_weight=self.arrow_weight,
                                                                arrow_speed=self.arrow_speed)
            
            return arrow_energy
            
        elif know_weight == "no":
            # Ask the user for component weights & arrow speed
            self.broadhead_weight = pyip.inputNum("Enter the broadhead weight (grains): ")
            self.insert_weight = pyip.inputNum("Enter the insert weight (grains): ")
            self.shaft_grains_per_inch = pyip.inputNum("Enter the broadhead shaft weight (grains): ")
            self.shaft_length = pyip.inputNum("Enter the broadhead shaft length (inches): ")
            self.fletching_weight = pyip.inputNum("Enter the weight of 1 fletching: ", )
            self.number_fletchings = pyip.inputInt("Enter the number of fletchings: ", min=3, max=4)
            self.arrow_wrap_weight = pyip.inputNum("Enter the weight of your arrow wrap, or leave blank if none: ",
                                                    blank=True) # Blank returns nothing
            self.arrow_wrap_weight = 0 if self.arrow_wrap_weight == "" else self.arrow_wrap_weight
            self.nock_weight = pyip.inputNum("Enter the nock weight (grains): ")
            self.arrow_speed = pyip.inputNum("Enter the arrow speed (feet per second): ")
            arrow_energy = self.calculate_energy_component_weight(broadhead_weight=self.broadhead_weight,
                                                                  insert_weight=self.insert_weight,
                                                                  shaft_grains_per_inch=self.shaft_grains_per_inch,
                                                                  shaft_length=self.shaft_length,
                                                                  fletching_weight=self.fletching_weight,
                                                                  number_fletchings=self.number_fletchings,
                                                                  nock_weight=self.nock_weight,
                                                                  arrow_speed=self.arrow_speed,
                                                                  arrow_wrap_weight=self.arrow_wrap_weight)
            
            return arrow_energy
            

    def calculate_energy_total_weight(self, arrow_weight:float, arrow_speed:float,
                                    round_digits:int=2) -> float:
        """Calculate the foot pounds of energy from an arrow using the full arrow
        weight and arrow speed.
        
        Returns:
            float: Energy of the arrow in ft.-lbs.
        """

        self.arrow_weight = arrow_weight
        self.arrow_speed = arrow_speed
        self.total_energy = round(self.arrow_weight * self.arrow_speed ** 2 / 450_800, round_digits)
        print(f"\nArrow weight: {self.arrow_weight} grains\n"
              f"Arrow speed: {self.arrow_speed} feet per second\n"
              f"Energy: {self.total_energy} foot-pounds\n")
        return self.total_energy


    def calculate_energy_component_weight(self, broadhead_weight:float, insert_weight:float,
                                           shaft_grains_per_inch:float, shaft_length:float,
                                           fletching_weight:float, number_fletchings:int,
                                           nock_weight:float, arrow_speed:int,
                                           arrow_wrap_weight:float=0, round_digits:int=2) -> float:
        """Calculate the foot pounds of energy from an arrow using the weight &
        quantity of all the components and arrow speed.
        
        Returns:
            float: Energy of the arrow in ft.-lbs.
        """
        self.broadhead_weight = broadhead_weight
        self.insert_weight = insert_weight
        self.shaft_grains_per_inch = shaft_grains_per_inch
        self.shaft_length = shaft_length
        self.fletching_weight = fletching_weight
        self.number_fletchings = number_fletchings
        self.nock_weight = nock_weight
        self.arrow_wrap_weight = arrow_wrap_weight
        self.arrow_speed = arrow_speed


        self.arrow_weight = (self.broadhead_weight + self.insert_weight +
                            (self.shaft_grains_per_inch * self.shaft_length) +
                            (self.fletching_weight * self.number_fletchings) +
                            self.nock_weight + self.arrow_wrap_weight)
        
        self.total_energy = round(self.arrow_weight * self.arrow_speed ** 2 / 450_800, round_digits)

        print(f"\nArrow weight: {self.arrow_weight} grains\n"
              f"Arrow speed: {self.arrow_speed} feet per second\n"
              f"Energy: {self.total_energy} foot-pounds\n")
        return self.total_energy


    def check_lethality(self, kinetic_energy:float, view_chart=False) -> None:
        """Verify what species of animals can be lethally hunted based on an arrows kinetic energy."""
        if kinetic_energy >= 65.0:
                print("Your arrow has enough kinetic energy for Moose, bison, musk ox, or large grizzly.")
        elif kinetic_energy >= 45.0:
            print("Your arrow has enough kinetic energy for elk, mule deer, large black bear, or caribou.")
        elif kinetic_energy >= 35.0:
            print("Your arrow has enough kinetic energy for whitetail deer, antalope, black bear, or wild hogs.")
        elif kinetic_energy >= 25.0:
            print("Your arrow has enough kinetic energy for turkeys, coyotes, or javelinas.")
        elif kinetic_energy >= 20.0:
            print("Your arrow has enough kinetic energy for rabbits, squirrels, or birds.")
        else:
            print("Your arrow does not have enough kinetic energy for any game animals.")

        if view_chart == True:
            print()
            print("Small game (rabbits, squirrels, birds): ~20–25 ft-lbs")
            print("Medium game (turkeys, coyotes, javelina): ~25–35 ft-lbs")
            print("Whitetail deer, antelope, black bear, wild hogs: ~35–45 ft-lbs")
            print("Elk, mule deer, large black bear, caribou: ~45–65 ft-lbs")
            print("Moose, bison, musk ox, large grizzly: 65+ ft-lbs")
            print()

            