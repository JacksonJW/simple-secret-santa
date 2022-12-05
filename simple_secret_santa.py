""" Simple Secret Santa"""
from typing import List
import random


def simple_secret_santa(
    participants: List[str], unpaired_participants: List[List[str]]
) -> List[tuple[str]]:
    """Takes in a list of participants and a list of unpaired_participants and returns a list of
    tuples representing the gifters and recipients"""

    unpaired_participants_table = {}
    sets_of_unpaired_participants = [set(group) for group in unpaired_participants]
    for unpaired_participants_list, unpaired_participants_set in zip(
        unpaired_participants, sets_of_unpaired_participants
    ):
        for participant in unpaired_participants_list:
            unpaired_participants_table[participant] = unpaired_participants_set

    result = []
    recipients = set(participants.copy())
    for gifter in participants:
        possible_recipients = {
            index: recipient
            for (index, recipient) in zip(range(len(recipients)), recipients)
        }
        recipient_index, recipient = random.choice(list(possible_recipients.items()))
        while recipient == gifter or (
            gifter in unpaired_participants_table
            and recipient in unpaired_participants_table[gifter]
        ):
            possible_recipients.pop(recipient_index)
            recipient_index, recipient = random.choice(
                list(possible_recipients.items())
            )
        result.append((gifter, recipient))
        recipients.remove(recipient)

    return result


if __name__ == "__main__":

    participants_user_input = input("Enter in participants separated by spaces: \n")
    unpaired_participants_user_input = input(
        "Enter in participant groups that cannot be paired w/ eachother separated by commas: \n"
    )

    participants_input = participants_user_input.split(" ")
    unpaired_participants_input = [
        x.split(" ") for x in unpaired_participants_user_input.split(", ")
    ]

    print(simple_secret_santa(participants_input, unpaired_participants_input))
