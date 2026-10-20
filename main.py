from pyscript import document, display

club_members = ["Alessia Moreau", "Alexander Whitmore", "Isabella Laurent", "Sebastian Klein", "Valentina Rossi"]

def check_member(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    full_name = first_name + " " + last_name
    
    is_member = full_name.lower() in [name.lower() for name in club_members]

    messages = {
        True: "Congratulations " + full_name + "!" + " " + "You are eligible for this event.",
        False: "Sorry " + full_name + ", kindly reach out in-office to confirm your application status."

    }

    document.getElementById("result").innerHTML = messages[is_member]

def clear_fields(e):
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
    document.getElementById("result").value = ""