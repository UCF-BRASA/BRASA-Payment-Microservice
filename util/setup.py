
from venmo_api import Client

# 3. Get .env file setup

# get's Venmo logging in information (for obvious reasons, do not share any of this info with anyone. I will have a team-wide account setup in a few days)
your_username = input(
    'Enter your Venmo associated email: (this information will NOT be stored)\n')
your_password = input(
    'Enter your Venmo account password: (this information will NOT be stored)\n')
new_access_token = Client.get_access_token(
    username=your_username, password=your_password)
your_user_id = Client(new_access_token).user.get_my_profile().id

# # writes all the info into the .env file (MAKE SURE THIS FILE NEVER GETS PUSHED TO THE REPOSITORY!!!!)
with open(".env", "w") as f:
    f.write('ACCESS_TOKEN=' + new_access_token + '\n')
    f.write('ID=' + your_user_id + '\n')
    f.write("DB_URI=\"GET THIS INFO WITH FACHETTI OR DUDA (it won't run without it)\"")

# log out, if needed
# Client(access_token=new_access_token).log_out(access_token=new_access_token)
