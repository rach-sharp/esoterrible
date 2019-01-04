import datetime
import re
import sys
import os
import pytz
import pkg_resources


UK_WORDS = pkg_resources.resource_string('esoterrible.resources', 'uk_words.txt').decode("utf-8").split()
US_WORDS = pkg_resources.resource_string('esoterrible.resources', 'us_words.txt').decode("utf-8").split()

datetime_datetime = datetime.datetime


class InconsistentSpellingError(Exception):
    pass


class VeryBritishDatetime(datetime.datetime):
    london = pytz.timezone('Europe/London')

    def __new__(cls, *args, **kwargs):
        result = super().__new__(cls, *args, **kwargs)
        return cls.london.localize(result)


class VeryAmericanDatetime(datetime.datetime):
    # I'm not dedicated enough to fine-tune timezone based on regional dialects
    new_york = pytz.timezone('America/New_York')

    def __new__(cls, *args, **kwargs):
        result = super().__new__(cls, *args, **kwargs)
        return cls.new_york.localize(result)


def set_datetime_to_dialect_timezone(source_file_path):
    with open(source_file_path, 'r') as source_code_file:
        source_uk_words = []
        source_us_words = []
        source_code = source_code_file.read()

        # stripping punctuation from file
        source_code = re.sub(r'[^\w\s]', '', source_code)

        for word in source_code.split():
            if word in UK_WORDS:
                source_uk_words.append(word)
            if word in US_WORDS:
                source_us_words.append(word)

        if source_uk_words and source_us_words:

            if len(source_uk_words) > len(source_us_words):
                minority_of_words = source_uk_words
            else:
                minority_of_words = source_us_words

            raise InconsistentSpellingError(
                "American and British English? Make your mind up! You probably want to change the "
                f"spelling of these words: {', '.join(minority_of_words)}")
        elif source_uk_words:
            datetime.datetime = VeryBritishDatetime
        elif source_us_words:
            datetime.datetime = VeryAmericanDatetime
        else:
            print("Nothing very American or British about your code")


try:
    main_file_path = os.path.abspath(sys.modules['__main__'].__file__)
    set_datetime_to_dialect_timezone(main_file_path)
except AttributeError:
    print("Skipping code language detection as Python is running in interactive mode")
