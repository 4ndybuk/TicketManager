import re
text = f"This is the ticket\n\n•Ticket created by me at 18:00:24•\n\n•Ticket created by me at 18:00:24•\n\n•Ticket created by me at 18:00:24•"

split = re.split(r"(•.*?•)", text, flags=re.DOTALL)
print(split)