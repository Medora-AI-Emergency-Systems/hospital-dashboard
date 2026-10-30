import random

def confirm_emergency(patient_data):
    """
    Simulates an ML model that confirms if a situation is a real emergency.
    In a real scenario, this would use a trained model (e.g., Random Forest, CNN).
    """
    # Placeholder logic: 80% chance it's a confirmed emergency
    is_confirmed = random.random() < 0.8
    confidence_score = random.uniform(0.7, 0.99) if is_confirmed else random.uniform(0.1, 0.5)
    
    return {
        "is_confirmed": is_confirmed,
        "confidence_score": confidence_score,
        "priority": "High" if confidence_score > 0.9 else "Medium"
    }

def check_hospital_availability(hospital_data):
    """
    Logic to check if the hospital can handle the emergency.
    """
    beds = hospital_data.get('available_beds', 0)
    doctors = hospital_data.get('available_doctors', 0)
    
    if beds > 0 and doctors > 0:
        return True
    return False

if __name__ == "__main__":
    # Example usage
    sample_patient = {"id": "P001", "condition": "Chest Pain"}
    result = confirm_emergency(sample_patient)
    print(f"Emergency Confirmation Result: {result}")
