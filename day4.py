emails = ["  KEHINDE@GMAIL.COM  ", "  Bola@Yahoo.com ", "bademail.com", "  Tolu@GMAIL.com  ", "  no-at-sign  "]

good_emails = []
bad_emails = []

for email in emails:
    clean = email.strip().lower()
    
    if "@" in clean:
        good_emails.append(clean)
    else:
        bad_emails.append(clean)

print("Good emails:", good_emails)
print("Bad emails:", bad_emails)
print(f"Total: {len(emails)} | Good: {len(good_emails)} | Bad: {len(bad_emails)}")

# Save good ones to a file
with open("good_emails.csv", "w") as file:
    for email in good_emails:
        file.write(email + "\n")

print("Saved good_emails.csv — ready to send to client!")