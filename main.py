import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def generate_master_list(master_list_str, adventure_type):
    sublist_categories = ["preparation", "essentials", "equipment", "nutrition", "clothing", "dog", "entertainment", "treats", "optional"]
    for category in sublist_categories:
        master_list_str = append_sub_list(master_list_str, adventure_type, category)
    return master_list_str

def append_sub_list(master_list_str, adventure_type, sub_list_name):
    filename = "lists/" + sub_list_name + ".json"
    with open(filename) as json_file:
        full_dict = json.load(json_file)
    sub_list = full_dict[adventure_type]
    # Add to the master list only if the sub_list has items in it.
    if len(sub_list) > 0:
        # Append sub-list to final_list.
        master_list_str = master_list_str + "\n" + sub_list_name
        for item in sub_list:
            master_list_str = master_list_str + "\n" + "- " + item
        master_list_str += "\n"
    return master_list_str

def email_list(master_list_str, target_email):
    email_user = "sphowley8@gmail.com"
    email_password = ""
    email_send = target_email

    subject = "Test email from python"

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject

    body = "Howdy, here is your packing list for your upcoming trip!\n\n" + master_list_str
    msg.attach(MIMEText(body,"plain"))

    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

if __name__ == "__main__":
    # Generate master list.
    
    master_list_str = generate_master_list("", "camping")
    print(master_list_str)
    # Email master list
    #email_list(master_list_str, "sphowley8@gmail.com")