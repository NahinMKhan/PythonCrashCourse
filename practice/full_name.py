first_name = "ada"
last_name = "lovelace"
full_name= f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
message_space = f"Hello, {full_name.title()}! "

while message != message_space:
    print("Not same")
    message_space = message_space.strip()

print("Same now")

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

