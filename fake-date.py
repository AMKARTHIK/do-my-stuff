#/usr/bin python

from faker import Factory

Fake = Factory.create('en_US')

fake_data = """
Name:\t{0}\n
Email:\t{1}\n
Company Name:\t{2}\n
Company Email:\t{3}\n
Address:\t{4}\n
Tin:\t{5}\n
Tel:\t{6}\n
""".format(Fake.name(),Fake.email(),Fake.company(),Fake.company_email(),Fake.address(),Fake.random_number(9),Fake.random_number(10))

print fake_data
