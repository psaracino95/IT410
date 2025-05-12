Wal_colcla= [
    "accounting",
    "business management",
    "it-210",
    "cloud security",
    "it-463",
    "it-410"
]
#lower case
Wal_colcla = [Wal_colcla.lower() for Wal_colcla in Wal_colcla]

# Sort the list
Wal_colcla.sort()

for Wal_colcla in Wal_colcla:
    print(f"I have taken {Wal_colcla.upper()} at Walsh College.")

#These are the courses you took
taken_course= ["business management",
    "it-210",
    "cloud security",
    "it-463",
    "it-410"
]

#Next courses
next_course=["accounting"
]
taken_course = [course.lower() for course in taken_course]
next_course = [course.lower() for course in next_course]

#Courses you didn't take
print("I plan to take",next_course)

#Add to the list, re-sort, print
taken_course.extend(next_course)
taken_course.sort()
print(taken_course)



#6 The %means remainder in this case, we dont include 0 for the count, hell we can start it at 6
Divisible=[num for num in range(1, 1001) if num % 6 == 0]
#print(Divisible)

#We want the first 20 in the list
print("The 20 numbers divisible by 6")
for num in Divisible[:20]:
    print(num)

#The maximum value in that list
max_val=max(Divisible[:20])
print("MaxValue:",max_val)

#Calculate the sums from 10th to 50th
ten_fifty=sum(Divisible[9:50])
print(ten_fifty)

#The overwrite
taken_course=Divisible