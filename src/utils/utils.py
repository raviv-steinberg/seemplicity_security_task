import random
import string


class Utils:
    """
    Utility class for various helper methods.
    """

    @staticmethod
    def generate_random_string(length: int) -> str:
        """
        Generates a random string of the specified length containing only letters.
        Example:
            Calling generate_random_string(10) might return 'aZbCdEfGhI'

        :param length: The length of the random string to generate
        :return: A random string of the specified length containing only letters
        """
        characters = string.ascii_letters
        random_string = ''.join(random.choices(characters, k=length))
        return random_string
