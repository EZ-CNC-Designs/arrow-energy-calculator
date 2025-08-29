from archery_physics import ArcheryPhysics

if __name__ == "__main__":
    arrow_1 = ArcheryPhysics()
    total_energy = arrow_1.receive_user_input()
    arrow_1.check_lethality(total_energy, view_chart=True)
    