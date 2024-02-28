"""Contact book."""


class Person:
    """Person class."""

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        """Person constructor."""
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def get_full_name(self) -> str:
        """
        Get full name of the person.

        Return firstname and lastname separated by space.
        If the lastname is empty, then return only the firstname.
        """
        if self.lastname == "":
            return self.firstname
        else:
            return f"{self.firstname} {self.lastname}"


class ContactBook:
    """Contact book class."""

    def __init__(self):
        """Contact book constructor."""
        self.contacts = []

    def add_person_to_contacts(self, person: Person) -> None:
        """Add person to contact book if phone number and firstname are not empty strings."""
        if person.firstname != "" and person.phone_number != "":
            self.contacts.append(person)

    def find_contact_by_number(self, number) -> Person:
        """
        Return person who has the given number.

        If there are several people with the given number, return the first.
        If there is no person with the given number, return None.
        """
        for n in self.contacts:
            if n.phone_number == number:
                return n

    def get_sorted_contacts(self) -> list:
        """Sort contacts alphabetically by full name."""
        conlist = []
        for n in self.contacts:
            conlist.append(n)
        conlist_sorted = sorted(conlist, key=lambda n: n.get_full_name(), reverse=False)
        return conlist_sorted