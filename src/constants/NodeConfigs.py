node_configs = {
    "SHOW_INVOICE_WEEK": {
        "node": "invoice schedule for this week",
        "message_key": "here_are_your_invoices_for_",
        "need_additional_final_answer": True
    },
    "SHOW_INVOICE_MONTH": {
        "node": "invoice schedule for this month",
        "message_key": "here_are_your_invoices_for_",
        "need_additional_final_answer": True
    },
    "SHOW_INVOICE_SPECIFIC_DAY": {
        "node": "invoice schedule for this specific day",
        "message_key": "here_are_your_invoices_for_",
        "need_additional_final_answer": True
    },
    "ALL_ACTIVITIES_SPECIFIC_DAY" : {
        "node": "all activities for this specific day",
        "message_key": "here_are_your_activities_for_",
        "need_additional_final_answer": True
    },
    "ALL_SCHEDULE_SPECIFIC_DAY" : {
        "node": "all schedule for this specific day",
        "message_key": "here_are_your_schedule_for_",
        "need_additional_final_answer": True,
    },
    "INCIDENT_HELP_EVENT_DETECTED" : {
        "node": "help",
        "message_key": "i_will_call_you_assistant",
        "need_additional_final_answer": False,
    },
    "i_am_ok" : {
        "node": "i am ok",
        "message_key": "glad_to_know_you_are_safe",
        "need_additional_final_answer": False,
    },
    "i_have_problem" : {
        "node": "i have problem",
        "message_key": "glad_to_know_you_are_safe",
        "need_additional_final_answer": False,
    },
    "SHOW_MEDICINE_SCHEDULE_WEEK": {
        "node": "medicine schedule for this week",
        "message_key": "here_is_your_medicine_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_MEDICINE_SCHEDULE_MONTH": {
        "node": "medicine schedule for this month",
        "message_key": "here_is_your_medicine_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_MEDICINE_SCHEDULE_SPECIFIC_DAY": {
        "node": "medicine schedule for specific day",
        "message_key": "here_is_your_medicine_schedule_for_",
        "need_additional_final_answer": True,
    },

    # Doctor appointment nodes
    "SHOW_APPOINTMENT_SCHEDULE_WEEK": {
        "node": "doctor appointment schedule for this week",
        "message_key": "here_is_your_doctor_appointment_schedule_for_",
        "need_additional_final_answer": True,
    }
,
    "SHOW_APPOINTMENT_SCHEDULE_MONTH": {
        "node": "doctor appointment schedule for this month",
        "message_key": "here_is_your_doctor_appointment_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_APPOINTMENT_SCHEDULE_SPECIFIC_DAY": {
        "node": "doctor appointment schedule for specific day",
        "message_key": "here_is_your_doctor_appointment_schedule_for_",
        "need_additional_final_answer": True,
    },

    # Health activity nodes
    "SHOW_HEALTH_ACTIVITY_WEEK": {
        "node": "health activity schedule for this week",
        "message_key": "here_is_your_health_activity_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_HEALTH_ACTIVITY_MONTH": {
        "node": "health activity schedule for this month",
        "message_key": "here_is_your_health_activity_schedule_for__",
        "need_additional_final_answer": True,
    },
    "SHOW_HEALTH_ACTIVITY_SPECIFIC_DAY": {
        "node": "health activity schedule for specific day",
        "message_key": "here_is_your_health_activity_schedule_for_",
        "need_additional_final_answer": True,
    },


    # Social activity nodes
    "SHOW_SOCIAL_ACTIVITY_WEEK": {
        "node": "social activity schedule for this week",
        "message_key": "here_are_your_social_activities_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_SOCIAL_ACTIVITY_MONTH": {
        "node": "social activity schedule for this month",
        "message_key": "here_are_your_social_activities_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_SOCIAL_ACTIVITY_SPECIFIC_DAY": {
        "node": "social activity schedule for specific day",
        "message_key": "here_are_your_social_activities_for_",
        "need_additional_final_answer": True,
    },

    # Visit except doctor nodes
    "SHOW_VISITS_WEEK": {
        "node": "visit schedule for this week",
        "message_key": "here_is_your_visit_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_VISITS_MONTH": {
        "node": "visit schedule for this month",
        "message_key": "here_is_your_visit_schedule_for_",
        "need_additional_final_answer": True,
    },
    "SHOW_VISITS_SPECIFIC_DAY": {
        "node": "visit schedule specific day",
        "message_key": "here_is_your_visit_schedule_for_",
        "need_additional_final_answer": True,
    },

    #Hardware Functionalities
    "INCREASE_BRIGHTNESS" : {
        "node" : "increase_screen_brightness",
        "message_key": "screen_brightness_increased",
        "need_additional_final_answer": False,
    },
    "DECREASE_BRIGHTNESS" : {
        "node" : "reduce_screen_brightness",
        "message_key": "screen_brightness_reduced",
        "need_additional_final_answer": False,
    },
    "INCREASE_VOLUME" : {
        "node" : "increase_volume",
        "message_key": "volume_increased",
        "need_additional_final_answer": False,
    },
    "DECREASE_VOLUME" : {
        "node" : "reduce volume",
        "message_key": "volume_reduced",
        "need_additional_final_answer": False,
    },
    "greeting" : {
        "node": "greeting",
        "message_key": "hi_can_i_help_you?",
        "need_additional_final_answer": False,
    },

    "call_assistant" : {
        "node": "call_assistant",
        "message_key": "ok_wait_i_will_call_you_assistant",
        "need_additional_final_answer": False,
    },

    # Final fallback
    "final": {
        "node": "no matching node",
        "message_key": "i_dont_have_an_answer_for_you_this_time",
        "need_additional_final_answer": False,
    },

    "other": {
        "node": "no matching node",
        "message_key": "i_dont_have_an_answer_for_you_this_time",
        "need_additional_final_answer": False,
    },

    "other_topics": {
        "node": "no matching node",
        "message_key": "i_dont_have_an_answer_for_you_this_time",
        "need_additional_final_answer": False,
    },
    
    #New
    "DEVICE_OFF" : {
        "node": "turn off device",
        "message_key": "turning_off_device",
        "need_additional_final_answer": False,
    },
    "DEVICE_RESET" : {
        "node": "reset device",
        "message_key": "resetting_device",
        "need_additional_final_answer": False,
    },
    "DEVICE_RESTART" : {
        "node": "restart device",
        "message_key": "restarting_device",
        "need_additional_final_answer": False,
    },

    "ALARM_STOP" : {
        "node": "stop alarm",
        "message_key": "stopping_alarm",
        "need_additional_final_answer": False,
    },

    "ALARM_SNOOZE" : {
        "node": "snooze alarm",
        "message_key": "snoozing_alarm",
        "need_additional_final_answer": False,
    },

    }



