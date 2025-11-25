medical_keywords = [
    "ECG", "EKG", "EEG", "MRI", "CT Scan", "Ultrasound", "X-ray",
    "Blood pressure monitor", "Glucometer", "Pulse oximeter", "Thermometer",
    "Spirometer", "Infusion pump", "Insulin pump", "Dialysis machine",
    "Ventilator", "Nebulizer", "Defibrillator", "Pacemaker", "Hearing aid",
    "Orthopedic implant", "Prosthetic limb", "Hematology analyzer",
    "Biochemistry analyzer", "PCR machine", "Microscope", "Centrifuge",
    "ELISA reader", "Blood analyzer", "Surgical robot", "Endoscope",
    "Laparoscope", "Stethoscope", "Syringe pump", "Catheter",
    "Surgical laser", "Dental drill", "Ophthalmic lens", "Medical device",
    "Diagnostic tool", "Implant", "Prosthesis", "Medical scanner",
    "Monitoring device", "Rehabilitation device", "Wearable health tracker", "diagnosis", "medications","medication"
]

predefined_intents = [
    # Medicine
    "medicine schedule today",
    "medicine schedule weekly",
    "medicine schedule monthly",
    "medicine schedule specific day",

    # Doctor Appointment
    "doctor appointment schedule today",
    "doctor appointment schedule weekly",
    "doctor appointment schedule monthly",
    "doctor appointment schedule specific day",

    # Social Activity
    "social activity schedule today",
    "social activity schedule weekly",
    "social activity schedule monthly",
    "social activity schedule specific day",

    # Visit Except Doctor
    "visit except doctor schedule today",
    "visit except doctor schedule weekly",
    "visit except doctor schedule monthly",
    "visit except doctor schedule specific day"
]

node_configs = {
    # Medicine nodes
    "medicine_today": "medicine schedule for today",
    "medicine_weekly": "medicine schedule for this week", 
    "medicine_monthly": "medicine schedule for this month",
    
    # Doctor appointment nodes
    "doctor_appointment_today": "doctor appointment schedule for today",
    "doctor_appointment_weekly": "doctor appointment schedule for this week",
    "doctor_appointment_monthly": "doctor appointment schedule for this month",
    
    # Social activity nodes  
    "social_activity_today": "social activity schedule for today",
    "social_activity_weekly": "social activity schedule for this week",
    "social_activity_monthly": "social activity schedule for this month",
    
    # Visit except doctor nodes
    "visit_except_doctor_today": "visit schedule (except doctor) for today", 
    "visit_except_doctor_weekly": "visit schedule (except doctor) for this week",
    "visit_except_doctor_monthly": "visit schedule (except doctor) for this month",
    
    "final": "answer, i dont have answer to you this time"
}