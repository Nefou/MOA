emails = [
    "student1@yandex.ru",
    "student2@gmail.com",
    "student3@yandex.ru"
]

email_dict = {}

for email in emails:
    user, domain = email.split('@')
  
    domain = domain.lower()

    if domain not in email_dict:
        email_dict[domain] = []
    email_dict[domain].append(email)

    print(email_dict)
