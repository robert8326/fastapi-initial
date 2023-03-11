def get_description():
    try:
        with open('description.md') as f:
            description = f.read()
    except:
        description = ''

    return description
