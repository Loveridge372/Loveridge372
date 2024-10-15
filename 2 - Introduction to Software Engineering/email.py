
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Default value for email status

    def mark_as_read(self):
        self.has_been_read = True  # Marks the email as read


# Create an empty list to store email objects
inbox = []


# Function to add emails to the inbox
def populate_inbox(email_address, subject_line, email_content):
    new_email = Email(email_address, subject_line, email_content)
    inbox.append(new_email)


# Function to list all emails with their status (read/unread)
def list_emails():
    if len(inbox) == 0:
        print("\nYour inbox is empty.\n")
    else:
        print("\nYour inbox:")
        for index, email in enumerate(inbox, start=1):
            status = "Read" if email.has_been_read else "Unread"
            print(f"{index}. {email.subject_line} ({status})")
        print()


# Function to display a specific email and mark it as read
def read_email(index):
    try:
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    except IndexError:
        print("\nInvalid email number. Please try again.\n")


# Function to display unread emails only
def view_unread_emails():
    unread_emails = [email for email in inbox if not email.has_been_read]
    if len(unread_emails) == 0:
        print("\nNo unread emails.\n")
    else:
        print("\nUnread Emails:")
        for index, email in enumerate(unread_emails, start=1):
            print(f"{index}. {email.subject_line}")
        print()


# Main application function
def email_simulator():
    while True:
        print("Email Simulator Menu:")
        print("1. View all emails")
        print("2. Read an email")
        print("3. View unread emails")
        print("4. Quit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            list_emails()
        elif choice == "2":
            if len(inbox) == 0:
                print("\nNo emails to read.\n")
            else:
                try:
                    email_num = int(input("Enter the email number to read: ")) - 1
                    read_email(email_num)
                except ValueError:
                    print("\nPlease enter a valid number.\n")
        elif choice == "3":
            view_unread_emails()
        elif choice == "4":
            print("\nExiting the Email Simulator. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")


# Populate the inbox with sample emails
populate_inbox("loveridgezvidzai7@gmail.com", "Meeting Tomorrow", "Hey, just a reminder about the meeting tomorrow.")
populate_inbox("loveridgezvidzai96@gmail.com", "New Project", "Check out the details for the new project.")
populate_inbox("loveridgezinyama@gmail.com", "Holiday Plans", "Do you have any plans for the holidays?")

# Start the email simulator
email_simulator() 