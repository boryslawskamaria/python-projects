import emoji
import re
import num2words

text_file='text.txt'
no_special_characters = []


def remove_special_characters(text_file):
    with open(text_file) as f:
        for line in f.readlines():
            newline = re.sub(r'[?|$|!|¡|,]', r'', line)
            no_special_characters.append(newline.strip())
    return no_special_characters


def find_email(text_file):
    emails = re.findall('[a-zA-Z0-9]+[\.\_\-]?[a-zA-Z0-9]+@\w+.\w+', text_file)
    if emails:
        def multiple_replace(dict, text):
            regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
            return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

        if __name__ != "__main__":
            pass

        else:
            dict = {
                "@": " arroba ",
                ".": " punto ",
            }

            text_file = (multiple_replace(dict, text_file))
    return text_file


def remove_emoji(text_file):
    text_file = emoji.demojize(text_file)
    text_file = re.sub(r'(:[!_\-\w]+:)', '', text_file)
    return text_file


def remove_digits(text_file):
    text_no_numbers = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0)), lang='es'), str(text_file))
    return text_no_numbers


text_file = remove_special_characters(text_file)
text_no_emails = (find_email(str(text_file)))
text_no_emoji = (remove_emoji(str(text_file)))
print(remove_digits(text_file))
