# -= Homework #2 by Mykola Honchar =-
#
# Дан словарь такого типа:
sample_dict = {
   "class_a": {
      "student1": {
         "name": "Misha",
         "marks": {
            "math": 90,
            "history": 85
         }
      }
   }
}

# sample_dict = {"class_a": {"student1": {"name": "Misha", "marks": {
#                                             "math": 90, "history": 85}}}}
# 1. Вывести значение ключа "name";
print("# 1 output 'name' value- ", sample_dict["class_a"]["student1"]["name"])

# 2. Вывести значение ключа "history";
print("# 2 output 'history' value- ",
      sample_dict["class_a"]["student1"]["marks"]["history"])

# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
sample_dict["class_a"].update({"student2": {"name": "Victor", "marks": {
                                            "math": 110, "history": 75}}})
print("# 3 sample_dict after add new student", sample_dict)

# 4. Добавить новый класс со студентами (в sample_dict нужно добавить class_b,
# в котором будет 2 студента);
sample_dict.update({"class_b": {
    "student1": {"name": "lusy", "marks": {
        "math": 85, "history": 90}},
    "student2": {"name": "lidya", "marks": {
        "math": 95, "history": 90}}}})
print("# 4 sample_dict after add new class", sample_dict)

# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
sample_dict["class_a"]["student1"]["marks"]["physics"] = 90
sample_dict["class_a"]["student2"]["marks"]["physics"] = 85
sample_dict["class_b"]["student1"]["marks"]["physics"] = 95
sample_dict["class_b"]["student2"]["marks"]["physics"] = 90
print("# 5 sample_dict after add physics", sample_dict)

# 6. Подсчитать средний бал по каждому студенту (результат округлить до
# 2 знаков после запятой);
average_marks_student1_cl_a =\
    round(sum(sample_dict["class_a"]["student1"]["marks"].values())
          / len(sample_dict["class_a"]["student1"]["marks"]), 2)
average_marks_student2_cl_a =\
    round(sum(sample_dict["class_a"]["student2"]["marks"].values())
          / len(sample_dict["class_a"]["student1"]["marks"]), 2)
average_marks_student1_cl_b =\
    round(sum(sample_dict["class_b"]["student1"]["marks"].values())
          / len(sample_dict["class_b"]["student1"]["marks"]), 2)
average_marks_student2_cl_b =\
    round(sum(sample_dict["class_b"]["student2"]["marks"].values())
          / len(sample_dict["class_b"]["student1"]["marks"]), 2)

print("# 6 average_marks_student1_cl_a= ", average_marks_student1_cl_a,
      "average_marks_student2_cl_a= ", average_marks_student2_cl_a,
      "average_marks_student1_cl_b= ", average_marks_student1_cl_b,
      "average_marks_student2_cl_b= ", average_marks_student2_cl_b)

# 7. Создать словарь со средним баллом за каждого студента;
average_marks_students_dict = {"student1_cl_a": average_marks_student1_cl_a,
                       "student2_cl_a": average_marks_student2_cl_a,
                       "student1_cl_b": average_marks_student1_cl_b,
                       "student2_cl_b": average_marks_student2_cl_b}
print("# 7 average_marks_students_dict: ", average_marks_students_dict)

# 8. Определить лучшего студента по успеваемости;
# print(marks_students_dict.(max(marks_students_dict.values())))
better_stud =\
    list(average_marks_students_dict.keys())[list(average_marks_students_dict
    .values()).index(max(list(average_marks_students_dict.values())))]
print(f"# 8 Best student - {better_stud}, his average mark is"
      f" {max(average_marks_students_dict.values())}!!!")


# 9. Подсчитать средний бал по каждому классу (результат округлить до 2
# знаков после запятой);
average_marks_students_cl_a =\
    round((sum(sample_dict["class_a"]["student1"]["marks"].values()) +
           sum(sample_dict["class_a"]["student2"]["marks"].values()))/
          (len(sample_dict["class_a"]["student1"]["marks"]) +
           len(sample_dict["class_a"]["student2"]["marks"])), 2)
average_marks_students_cl_b =\
    round((sum(sample_dict["class_b"]["student1"]["marks"].values()) +
           sum(sample_dict["class_b"]["student2"]["marks"].values()))/
          (len(sample_dict["class_b"]["student1"]["marks"]) +
           len(sample_dict["class_b"]["student2"]["marks"])), 2)

print(f"# 9 average_marks_students_cl_a= {average_marks_students_cl_a},"
      f" average_marks_students_cl_b= {average_marks_students_cl_b}")

# 10. Создать словарь со средним баллом за классы;
average_marks_students = {"class_a": average_marks_students_cl_a,
                          "class_b": average_marks_students_cl_b}
print("# 10", average_marks_students)

# 11. Определить лучший класс по успеваемости.
better_class =\
    list(average_marks_students.keys())[list(average_marks_students
    .values()).index(max(list(average_marks_students.values())))]
print(f"# 11 Best class - {better_class}, it average mark is"
      f" {max(average_marks_students.values())}!!!")