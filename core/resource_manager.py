class ResourceManager:
    def __init__(self, beds=10, ventilators=5, doctors=8):
        self.resources = {"Beds": beds, "Ventilators": ventilators, "Doctors": doctors}
        self.patients = []

    def allocate(self, patient):
        # Simple allocation: allocate 1 bed, 1 ventilator, 1 doctor if available
        if all(self.resources[r] > 0 for r in self.resources):
            for r in self.resources:
                self.resources[r] -= 1
            self.patients.append(patient)
            return True, "Resources allocated."
        else:
            return False, "Not enough resources."

    def emergency(self, patient):
        # Step 1: Try normal allocation
        allocated = False
        for r in self.resources:
            if self.resources[r] > 0:
                self.resources[r] -= 1
                allocated = True

        if allocated:
            self.patients.insert(0, patient)
            return True, "Emergency resources allocated."

        # Step 2: No resources available — try preempting a low-risk patient
        for i, existing_patient in enumerate(self.patients):
            if existing_patient.get("risk") == "low":
                # Remove this low-risk patient and reassign their resources
                self.patients.pop(i)
                for r in self.resources:
                    self.resources[r] += 1  # Reclaim resources
                for r in self.resources:
                    self.resources[r] -= 1  # Reassign to emergency patient
                self.patients.insert(0, patient)
                return True, f"Emergency patient allocated by preempting low-risk patient {existing_patient.get('name')}."

            # Step 3: No low-risk patients to preempt
        return False, "Resources can't be assigned due to non-availability, SORRY"


    # def emergency(self, patient):
    #     # Emergency: prioritize patient, allocate if any resource is available
    #     allocated = False
    #     for r in self.resources:
    #         if self.resources[r] > 0:
    #             self.resources[r] -= 1
    #             allocated = True
    #     if allocated:
    #         self.patients.insert(0, patient)  # Emergency patients at top
    #         return True, "Emergency resources allocated."
    #     else:
    #         return False, "No resources available for emergency."

    def status(self):
        # For dashboard: return patients and available resources as list
        return {
            "patients": self.patients,
            "available": [self.resources["Beds"], self.resources["Ventilators"], self.resources["Doctors"]]
        }



