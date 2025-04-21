from faker import Faker
import pandas as pd
import random
import uuid

fake = Faker()
Faker.seed(42)

def generate_members(num_members=5000):
    data = []
    for _ in range(num_members):
        member_id = str(uuid.uuid4())
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        gender = random.choice(['M', 'F'])
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=65)
        start_date = fake.date_between(start_date='-2y', end_date='today')  # FIXED LINE
        membership_type = random.choice(['Basic', 'Premium', 'VIP'])
        status = random.choice(['Active', 'Inactive'])
        data.append([member_id, first_name, last_name, email, phone, gender, birthdate, start_date,
                     membership_type, status])

    print("Data generation complete")
    df = pd.DataFrame(data, columns=['member_id', 'first_name', 'last_name', 'email', 'phone_number',
                                     'gender', 'birthdate', 'start_date', 'membership_type', 'status'])
    df.to_csv('members.csv', index=False)
    print("members.csv created!")
    print("Script finished")
    return df

def generate_checkins(members_df,num_checkins=500):
    data = []
    for _ in range(num_checkins):
        checkin_id = str(uuid.uuid4())
        member_id = random.choice(members_df['member_id'].values)
        checkin_time = fake.date_time_between(start_date= '-1y', end_date= 'now')
        location = random.choice(['Downtown Gym', 'Uptown Gym', 'Suburb Gym'])

        data.append([checkin_id, member_id, checkin_time, location])

    df = pd.DataFrame(data, columns=['checkin_id','member_id','checkin_time', 'location'])
    df.to_csv('checkins.csv', index = False)
    print("checkins.csv created!")
    return df


def generate_payments(members_df, months=12):
    data = []
    for member_id in members_df['member_id'].values:
        for month in range(months):
            payment_id = str(uuid.uuid4())
            amount = random.choice([29.99, 49.99, 69.99])
            payment_date = fake.date_between(start_date=f'-{month + 1}m', end_date=f'-{month}m')
            status = random.choices(['Paid', 'Failed'], weights=[0.9, 0.1])[0]

            data.append([payment_id, member_id, amount, payment_date, status])

    df = pd.DataFrame(data, columns=['payment_id', 'member_id', 'amount', 'payment_date', 'status'])
    df.to_csv('payments.csv', index=False)
    print("✅ payments.csv created!")
    return df

if __name__ == "__main__":
    members_df = generate_members()
    generate_checkins(members_df)
    generate_payments(members_df)
    print("🎉 All data files created successfully!")