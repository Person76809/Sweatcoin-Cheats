import random

def generate_fake_steps():
    # Generate a random number of steps between 1,000 and 10,000
    fake_steps = random.randint(1000, 10000)
    return fake_steps

fake_step_count = generate_fake_steps()
print("Fake Step Count:", fake_step_count)
