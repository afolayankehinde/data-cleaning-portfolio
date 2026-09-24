# Data Cleaning Portfolio for AI Training

Python QA workflow for annotation tasks (Micro1 / Scale AI style)

### What it does
- Cleans raw emails/phones: strip(), lower()
- Validates with testable criteria:
    - Good Email = contains "@" and len > 5
    - Good Phone = len == 11 after cleaning
- Splits into Good / Bad lists
- Counts: Total | Good | Bad
- Exports: good_emails.csv (client-ready)

### Sample Output
Total: 5 | Good: 2 | Bad: 3

### Tech
Python, CSV, Data QA, Audit Trail
