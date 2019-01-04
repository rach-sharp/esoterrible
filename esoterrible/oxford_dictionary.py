import builtins
import random
import warnings
import PyDictionary

dict_builtin = dict


class OxfordDict(dict):

    def __init__(self, *args, **kwargs):

        self.dictionary = PyDictionary.PyDictionary()
        super().__init__(*args, **kwargs)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError as ex:

            # stop overriding while using PyDictionary.meaning
            builtins.dict = dict_builtin

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                meanings = self.dictionary.meaning(str(item))
                if meanings is None:
                    raise
                result = random.choice(list(meanings.values())[0])

            builtins.dict = OxfordDict
            return result


builtins.dict = OxfordDict
