class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        if owner:
            owner.add_pet(self)  # Automatically link pet to owner
        Pet.all.append(self)  # Keep track of all pets

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Store pets privately

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only pets can be added")
        
        self._pets.append(pet)
        pet.owner = self  # Set the owner of the pet

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)