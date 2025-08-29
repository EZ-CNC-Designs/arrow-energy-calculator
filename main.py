from arrow_energy_calculator import ArrowEnergyCalculator

if __name__ == "__main__":
    arrow_1 = ArrowEnergyCalculator()
    total_energy = arrow_1.receive_user_input()
    arrow_1.check_lethality(total_energy, view_chart=True)
    
    