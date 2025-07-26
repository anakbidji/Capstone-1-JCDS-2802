# List of admin accounts and their passwords
admin_accounts = [{'username': 'admin1', 'password': '1234'}, {'username': 'admin2', 'password': '1234'}]

# FitClub member data, each contains unique ID, name, age, membership months, and PT sessions
member_data = [
    {'member_id': 1, 'first_name': 'uriel', 'last_name': 'siboro', 'age': 26, 'remaining_membership_months': 12, 'remaining_pt_sessions': 0},
    {'member_id': 2, 'first_name': 'hugo', 'last_name': 'pratama', 'age': 26, 'remaining_membership_months': 8, 'remaining_pt_sessions': 0},
    {'member_id': 3, 'first_name': 'kevin', 'last_name': 'putra', 'age': 26, 'remaining_membership_months': 6, 'remaining_pt_sessions': 0}
]

# Available membership packages
membership_packages = [
    {'Package Name': 'pro', 'Membership Price': 1_000_000, 'membership_months': 12},
    {'Package Name': 'athlete', 'Membership Price': 600_000, 'membership_months': 6},
    {'Package Name': 'beginner', 'Membership Price': 400_000, 'membership_months': 3}
]

# Available Personal Trainer packages
pt_packages = [
    {'Package Name': 'bodybuilder', 'PT Price': 1_000_000, 'pt_sessions': 12},
    {'Package Name': 'athlete', 'PT Price': 600_000, 'pt_sessions': 6},
    {'Package Name': 'beginner', 'PT Price': 400_000, 'pt_sessions': 3}
]


def admin_login():
    """Allows FitClub admin to log in."""
    while True:
        confirm = input('Are you sure you want to log in with admin credentials? (y or n): ').lower().strip()
        if confirm == 'n':
            return
        elif confirm == 'y':
            for attempt in range(3):
                print('\n=== Welcome FitClub Admin ===\n')
                username = input('Enter your username: ')
                password = input('Enter your password: ')

                # Check if username and password match
                for admin in admin_accounts:
                    if username == admin['username'] and password == admin['password']:
                        print(f'\nLogin successful! Welcome {username}!\n')
                        return admin
                else:
                    print('\nIncorrect username or password!\n')
                    while True:
                        back = input('Return to main menu? (y or n): ').lower().strip()
                        if back == 'y':
                            return main_menu()
                        elif back == 'n':
                            break
                        else:
                            print('Input must be y or n!')
            else:
                print('Failed to login 3 times, please wait 5 minutes before trying again!')
                return
        else:
            print('Input must be y or n!')


def admin_menu(admin):
    """Menu displayed for admin after successful login."""
    while True:
        print('\n=== Admin Menu ===')
        print('1. View Member Information')
        print('2. Delete Member')
        print('3. Add Member')
        print('4. Main Menu')
        choice = input('Enter choice (1-4): ')
        if choice == '1':
            show_members()
        elif choice == '2':
            delete_member()
        elif choice == '3':
            add_member()
        elif choice == '4':
            return
        else:
            print('Invalid choice.')


def member_login():
    """Allows FitClub members to log in."""
    while True:
        confirm = input('Are you sure you want to log in as a member? (y or n): ').lower().strip()
        if confirm == 'n':
            return
        elif confirm == 'y':
            for attempt in range(3):
                print('\n=== Welcome FitClub Member! ===\n')
                while True:
                    try:
                        member_id_input = int(input('Enter your member ID: '))
                        break
                    except ValueError:
                        print('ID must be a number!')

                first_name_input = input('Enter your first name: ').lower().strip()

                # Find matching member
                for member in member_data:
                    if member['member_id'] == member_id_input and member['first_name'] == first_name_input:
                        return member
                else:
                    print('Incorrect ID or first name!\n')
                    while True:
                        back = input('Return to main menu? (y or n): ').lower().strip()
                        if back == 'y':
                            return main_menu()
                        elif back == 'n':
                            break
                        else:
                            print('Input must be y or n!')
            else:
                print('Failed to login 3 times, please wait 5 minutes.')
                return
        else:
            print('Input must be y or n!')


def member_menu(member):
    """Menu displayed for logged-in members."""
    while True:
        print('\n=== Member Menu ===')
        print('1. Extend Membership')
        print('2. Buy More Personal Trainer Sessions')
        print('3. Check Remaining Membership & PT Sessions')
        print('4. Main Menu')
        choice = input('Enter choice (1-4): ')
        if choice == '1':
            extend_membership(member)
        elif choice == '2':
            extend_pt_sessions(member)
        elif choice == '3':
            print(f"\nRemaining membership: {member['remaining_membership_months']} months")
            print(f"Remaining PT sessions: {member['remaining_pt_sessions']} sessions")
        elif choice == '4':
            return
        else:
            print('Invalid choice.')


def non_member_menu():
    """Menu for users who are not yet members."""
    while True:
        print('\n=== Non-Member Menu ===')
        print('1. View Membership Prices')
        print('2. Register as Member')
        print('3. Main Menu')
        choice = input('Enter choice (1-3): ')
        if choice == '1':
            show_membership_prices()
        elif choice == '2':
            register_new_member()
        elif choice == '3':
            return


def add_member():
    """Admin adds a new member."""
    new_id = unique_member_id()
    first_name = input('Enter first name: ').lower().strip()
    last_name = input('Enter last name: ').lower().strip()
    while True:
        try:
            age = int(input('Enter age: '))
            if age < 12:
                print('Age must be at least 12!')
                continue
            break
        except ValueError:
            print('Age must be a number!')
    while True:
        try:
            months = int(input('Enter membership months: '))
            break
        except ValueError:
            print('Input must be a number!')
    while True:
        try:
            sessions = int(input('Enter PT sessions: '))
            break
        except ValueError:
            print('Input must be a number!')

    member_data.append({
        'member_id': new_id,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'remaining_membership_months': months,
        'remaining_pt_sessions': sessions
    })
    print('New member successfully added!')


def delete_member():
    """Admin deletes a member by member ID."""
    while True:
        show_members()
        try:
            member_id = int(input('Enter member ID to delete: '))
        except ValueError:
            print('ID must be a number!')
            continue

        for member in member_data:
            if member['member_id'] == member_id:
                confirm = input(f"Are you sure you want to delete {member['first_name']} {member['last_name']}? (y/n): ").lower().strip()
                if confirm == 'y':
                    member_data.remove(member)
                    print('Member deleted.')
                else:
                    print('Deletion cancelled.')
                return
        print('ID not found. Try again.')


def show_members():
    """Display all registered members."""
    print('\n=== FitClub Members ===')
    for m in member_data:
        print(f"ID: {m['member_id']} | Name: {m['first_name']} {m['last_name']} | Age: {m['age']} | Membership: {m['remaining_membership_months']} months | PT Sessions: {m['remaining_pt_sessions']}")


def show_membership_prices():
    """Show all available membership packages."""
    print('\n=== Membership Prices ===')
    for p in membership_packages:
        print(f"Package {p['Package Name']}: {p['membership_months']} months, Rp {p['Membership Price']}")


def show_pt_prices():
    """Show all available Personal Trainer packages."""
    print('\n=== Personal Trainer Prices ===')
    for pt in pt_packages:
        print(f"Package {pt['Package Name']}: {pt['pt_sessions']} sessions, Rp {pt['PT Price']}")


def process_payment(amount):
    """Simulate payment process."""
    print(f"Total to pay: Rp {amount}")
    while True:
        try:
            payment = int(input('Enter payment amount: Rp '))
            change = payment - amount
            if payment < amount:
                print(f'Insufficient funds. Missing Rp {amount - payment}')
                continue
            if change > 0:
                print(f"\nPayment successful. Change: Rp {change}")
            else:
                print("\nExact payment received.")
            return 'success'
        except ValueError:
            print('Input must be a number!')


def register_new_member():
    """Register a new member from non-member menu."""
    show_membership_prices()
    while True:
        package_name = input('Choose package name: ').lower().strip()
        for pkg in membership_packages:
            if package_name == pkg['Package Name']:
                price = pkg['Membership Price']
                months = pkg['membership_months']
                confirm = input(f'Are you sure you want to choose package {package_name}? (y or n): ').lower().strip()
                if confirm == 'n':
                    print('Registration cancelled.')
                    return
                elif confirm == 'y':
                    if process_payment(price) == 'success':
                        new_id = unique_member_id()
                        first_name = input('Enter your first name: ').lower().strip()
                        last_name = input('Enter your last name: ').lower().strip()
                        while True:
                            try:
                                age = int(input('Enter your age: '))
                                if age < 12:
                                    print('Age must be at least 12!')
                                    continue
                                break
                            except ValueError:
                                print('Age must be a number!')
                        member_data.append({
                            'member_id': new_id,
                            'first_name': first_name,
                            'last_name': last_name,
                            'age': age,
                            'remaining_membership_months': months,
                            'remaining_pt_sessions': 0
                        })
                        print('Registration successful!')
                        show_members()
                        return
                    else:
                        print('Payment failed.')
                else:
                    print('Input must be y or n!')
        else:
            print('Package not found.')


def extend_membership(member):
    """Member extends their membership."""
    show_membership_prices()
    while True:
        package_name = input('Choose package: ').lower().strip()
        for pkg in membership_packages:
            if package_name == pkg['Package Name']:
                months = pkg['membership_months']
                price = pkg['Membership Price']
                confirm = input(f'Are you sure you want to choose package {package_name}? (y or n): ').lower()
                if confirm == 'n':
                    return
                if process_payment(price) == 'success':
                    member['remaining_membership_months'] += months
                    print(f"\nYour membership is now {member['remaining_membership_months']} months")
                    return
                else:
                    continue
        print('Package not found.')


def extend_pt_sessions(member):
    """Member buys more PT sessions."""
    show_pt_prices()
    while True:
        package_name = input('Choose PT package: ').lower().strip()
        for pkg in pt_packages:
            if package_name == pkg['Package Name']:
                sessions = pkg['pt_sessions']
                price = pkg['PT Price']
                confirm = input(f'Are you sure you want to choose package {package_name}? (y or n): ').lower().strip()
                if confirm == 'n':
                    return
                if process_payment(price) == 'success':
                    member['remaining_pt_sessions'] += sessions
                    print(f'\nYour PT sessions are now {member["remaining_pt_sessions"]} sessions')
                    return
                else:
                    continue
        print('Package not found.')


def unique_member_id():
    """Ensures entered member ID is unique."""
    while True:
        try:
            new_id = int(input('Enter new member ID: '))
        except ValueError:
            print('ID must be a number!')
            continue
        if any(m['member_id'] == new_id for m in member_data):
            print(f'ID {new_id} is already taken!')
            print('Used IDs:')
            for m in member_data:
                print(f"{m['member_id']}")
        else:
            return new_id


def main_menu():
    """Main program menu."""
    while True:
        print('\n=== Welcome to FitClub ===')
        print('1. Admin')
        print('2. Member')
        print('3. Non-Member')
        print('4. Exit Program')
        choice = input('Choose (1-4): ')
        if choice == '1':
            admin = admin_login()
            if admin:
                admin_menu(admin)
        elif choice == '2':
            member = member_login()
            if member:
                member_menu(member)
        elif choice == '3':
            non_member_menu()
        elif choice == '4':
            print('Thank you! Program ended.')
            return
        else:
            print('Invalid choice.')


main_menu()
