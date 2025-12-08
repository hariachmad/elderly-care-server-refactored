

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
    "visit except doctor schedule specific day",

    "fall",
    "help",
    "i am ok",

    "greeting",
    "call assistant",

    "other topics"
]

node_configs = {
    "help" : {
        "node": "help",
        "final_answer": "i will call you assistant"
    },
    "i_am_ok" : {
        "node": "i am ok",
        "final_answer": "Glad to know you are safe"
    },
    "fall" : {
        "node": "fall",
        "final_answer": "Hi, Do you need any help"
    },          
    "medicine_today": {
        "node": "medicine schedule for today",
        "final_answer": "here is your medicine schedule for today"
    },
    "medicine_weekly": {
        "node": "medicine schedule for this week",
        "final_answer": "here is your weekly medicine schedule"
    },
    "medicine_monthly": {
        "node": "medicine schedule for this month",
        "final_answer": "here is your monthly medicine schedule"
    },
    "medicine_schedule_specific_day": {
        "node": "medicine schedule for specific day",
        "final_answer": "here is your medicine schedule for that specific day"
    },

    # Doctor appointment nodes
    "doctor_appointment_today": {
        "node": "doctor appointment schedule for today",
        "final_answer": "here is your doctor appointment schedule for today"
    },
    "doctor_appointment_weekly": {
        "node": "doctor appointment schedule for this week",
        "final_answer": "here is your weekly doctor appointment schedule"
    }
,
    "doctor_appointment_monthly": {
        "node": "doctor appointment schedule for this month",
        "final_answer": "here is your monthly doctor appointment schedule"
    },
    "doctor_appointment_specific_day": {
        "node": "doctor appointment schedule for specific day",
        "final_answer": "here is your doctor appointment schedule for that specific day"
    },

    # Social activity nodes
    "social_activity_today": {
        "node": "social activity schedule for today",
        "final_answer": "here are your social activities for today"
    },
    "social_activity_weekly": {
        "node": "social activity schedule for this week",
        "final_answer": "here are your weekly social activities"
    },
    "social_activity_monthly": {
        "node": "social activity schedule for this month",
        "final_answer": "here are your monthly social activities"
    },
    "social_activity_specific_day": {
        "node": "social activity schedule for specific day",
        "final_answer": "here are your social activities for that specific day"
    },

    # Visit except doctor nodes
    "visit_except_doctor_today": {
        "node": "visit schedule for today",
        "final_answer": "here is your visit schedule for today"
    },
    "visit_except_doctor_weekly": {
        "node": "visit schedule for this week",
        "final_answer": "here is your weekly visit schedule"
    },
    "visit_except_doctor_monthly": {
        "node": "visit schedule for this month",
        "final_answer": "here is your monthly visit schedule"
    },
    "visit_except_doctor_specific_day": {
        "node": "visit schedule specific day",
        "final_answer": "here is your visit schedule for that specific day"
    },


    "greeting" : {
        "node": "greeting",
        "final_answer": "asking again"
    },

    "call_assistant" : {
        "node": "call assistant",
        "final_answer": "Ok, wait i will call you assistant"
    },

    # Final fallback
    "final": {
        "node": "no matching node",
        "final_answer": "i don't have an answer for you this time"
    }}

INTENT_TO_NODE = {
    # Medicine
    "medicine schedule today": "medicine_today",
    "medicine schedule weekly": "medicine_weekly",
    "medicine schedule monthly": "medicine_monthly",
    "medicine schedule specific day": "medicine_schedule_specific_day",

    # Doctor Appointment
    "doctor appointment schedule today": "doctor_appointment_today",
    "doctor appointment schedule weekly": "doctor_appointment_weekly",
    "doctor appointment schedule monthly": "doctor_appointment_monthly",
    "doctor appointment schedule specific day": "doctor_appointment_specific_day",

    # Social Activity
    "social activity schedule today": "social_activity_today",
    "social activity schedule weekly": "social_activity_weekly",
    "social activity schedule monthly": "social_activity_monthly",
    "social activity schedule specific day": "social_activity_specific_day",

    # Visit Except Doctor
    "visit except doctor schedule today": "visit_except_doctor_today",
    "visit except doctor schedule weekly": "visit_except_doctor_weekly",
    "visit except doctor schedule monthly": "visit_except_doctor_monthly",
    "visit except doctor schedule specific day": "visit_except_doctor_specific_day",

    # Fall Detection
    "fall": "fall",
    "help": "help",
    "i am ok": "i_am_ok",

    "greeting": "greeting",
    "call assistant" : "call_assistant"
}

UNNAVIGATOR_INTENT = [
    "other topics","other","greeting"
]