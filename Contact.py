class Contact:
    def __init__(self, name, phone_nums, email):
        """
      The constructor creates a Contact object
      :param name: The contact's name, a string
      :param phone_nums: The contact's phone numbers, a list
      :param email: The contact's email address, a string
      """
        if not type(phone_nums) is list:
            # 'phone_nums' should be a list
            raise ValueError('phone_nums should be a list!')

        self._name = name
        self._phone_nums = phone_nums
        self._email = email

    @property
    def phone_nums(self):
        return self._phone_nums

    def add_number(self, phone_number):
        if phone_number in self._phone_nums:
            print("That number is already in the list!")
        else:
            self._phone_nums.append(phone_number)

    def remove_number(self, phone_number):
        if phone_number in self._phone_nums:
            self._phone_nums.remove(phone_number)

    def __str__(self):
        return_string = "Name: " + self._name + "\n"
        return_string += "Phone Numbers: "
        for num in self._phone_nums:
            return_string += num + " "
        return_string += '\n'
        return_string += "Email: " + self._email

        return return_string
