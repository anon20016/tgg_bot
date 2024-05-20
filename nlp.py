def lemmatize(message: str, nlp):
    message = replace_active(message)
    words = []
    for token in nlp(message):
        if (token.is_stop != True) and (token.is_punct != True) and \
                (token.is_space != True) and (token.is_digit != True):
            words.append(token.lemma_)
    return ' '.join(words)


def replace_active(message: str):
    if "найти" not in message:
        message = message.replace("где", "найти")
    return message
