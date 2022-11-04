def text_writing(pol, name):
    text_to_file = open(f"{name}", "w")
    text_to_file.write(pol)
    text_to_file.close()