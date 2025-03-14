from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCollegeInfo(Action):
    def name(self) -> Text:
        return "action_college_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Retrieve intent and slot values
        intent = tracker.latest_message['intent'].get('name')
        
        # Define response based on the intent
        if intent == "college_name":
            dispatcher.utter_message(text="The name of the college is Shri Vishnu Engineering College for Women.")
        
        elif intent == "college_branches":
            dispatcher.utter_message(text="The college offers branches including Computer Science, Electronics, Mechanical, and Civil Engineering.")
        
        elif intent == "college_placements":
            dispatcher.utter_message(text="The college has a strong placement record with many students getting placed in top companies. Recent placement details: 1474 students in 2023, 1892 students in 2022, 933 students in 2021, and 789 students in 2020.")
        
        elif intent == "college_facilities":
            dispatcher.utter_message(text="The college provides facilities such as a library, hostel, sports complex, and modern laboratories.")
        
        elif intent == "fee_structure":
            dispatcher.utter_message(text="The fee structure is Rs.77,000/- per year. Branch-wise details are as follows: CSE [AI & DS] :: 120, CSE [AI & ML] :: 120, CSE [Cyber Security] :: 60, CSE :: 180, IT :: 180, ECE :: 120, EEE :: 60, CE :: 60, ME :: 60.")
        
        elif intent == "admission_procedure":
            dispatcher.utter_message(text="Admission is based on EAPCET marks and counseling. Lateral Entry Admissions are through ECET counseling. Candidates should have passed 10+2 with Physics & Mathematics and a minimum of 50% marks.")
        
        elif intent == "principal":
            dispatcher.utter_message(text="The principal of Shri Vishnu Engineering College for Women is G. Srinivasarao.")
        
        elif intent == "chairman":
            dispatcher.utter_message(text="The chairman of Shri Vishnu Engineering College for Women is Sri. K.V. Vishnu Raju.")
        
        elif intent == "contact_details":
            dispatcher.utter_message(text="Contact us at: Phone: 08816 – 250864, Fax: 08816 – 250099, Email: info@svecw.edu.in, principal@svecw.edu.in. Address: Vishnupur, BHIMAVARAM – 534202, West Godavari District, Andhra Pradesh, India.")
        
        return []
