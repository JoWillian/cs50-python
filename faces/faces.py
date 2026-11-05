def convert(face):
    face = face.replace(":(","🙁")
    face = face.replace(":)","🙂")
    return face
def main():
    emoticon = convert(str(input()))
    print(emoticon)

main()


