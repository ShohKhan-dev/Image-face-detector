import face_recognition
from PIL import Image, ImageDraw

mark_image = face_recognition.load_image_file('./single/mark.jpg')
mark_encoding = face_recognition.face_encodings(mark_image)[0]

#second_image = face_recognition.load_image_file('./single/second.jpg')
#second_encoding = face_recognition.face_encodings(dad_image)[0]

### You can add as many single person imgages as you want

people_face_encodings = [
    mark_encoding
    #second_encoding
]

# add this encoding list


# add other person's names as you opened above
known_names = [
    "MARK"
]


    
test_image = face_recognition.load_image_file('./group/mark_and_milk.jpg')

face_location = face_recognition.face_locations(test_image)

number_of_people = len(face_location)

print("There are ", number_of_people, " people in the picture")

face_encoding = face_recognition.face_encodings(test_image, face_location)



pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_enc in zip(face_location, face_encoding):
    matches = face_recognition.compare_faces(people_face_encodings, face_enc)

    name = "UNDEFINED"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    text_width, text_height = draw.textsize(name)

    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))

    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

pil_image.show()









