course_list = ["django", "scrapy", "tornado"]
course_size = len(course_list)
if course_size >=3:
  print("課程多，數量：{}".format(course_size))


# := 為 3.8 後的海象運算符
if (course_size2 := len(course_list)) >= 3:
  print("課程多，數量：{}".format(course_size2))

powers = [course_size3:=len(course_list), course_size3**2, course_size3**3]
print(powers)

import re
desc = "frank:18"
m = re.match("frank:(.*)", desc)
if m:
  age = m.group(1)
  print(age)

desc2 = "frank:18"
if m2 := re.match("frank:(.*)", desc2):
  age = m2.group(1)
  print(age)
