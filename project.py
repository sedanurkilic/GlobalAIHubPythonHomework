Courses=[]
username="SEDA KILIÇ"
check=False
def courseCount():
    if len(Courses)<3:
        count=len(Courses)
        print(f"You take {count} courses")
        Courses.clear()
        return "You failed in class"
def grades():
    g={"midterm":0,"final":0,"project":0}
    midterm=int(input("Midterm grade: "))
    final=int(input("Final grade: "))
    project=int(input("Project grade: "))
    g[midterm]=midterm
    g[final]=final
    g[project]=project
    grade= midterm*0.3 + final*0.5 + project*0.2
    return grade
entry=3
while range(3):   
    name=input("Please enter your name and surname with capital letters: ")
    if name=="seda" or name=="Seda" or name=="SEDA":
        break
    if name.upper()==username:
        print(f"WELCOME {username}!!")
        for i in range(5):
            i+=1
            print("Select courses to stop selecting, press q")
            course=input(f"Select the course {i}: ")
            if course=="q":
                print(courseCount())
                break              
            Courses.append(course)
            print("Your courses: ", Courses)
        check=True
        break
    else:
        entry-=1
        if entry==0:
            print("Please try again later")
            break
            
if check==True:
    while True:
        selectCourse=int(input("Please enter the number of the lesson you want to calculate: "))
        if selectCourse>len(Courses) or selectCourse<1:
            print("Invalid course.Please try again!")
        else:
            x=Courses[selectCourse-1]
            print(f"Your selected course: {x}")
            grade=grades()
            if grade>=90:
                print(f"Your average is {grade}")
                print("AA")
            elif 90>grade>=70:
                print(f"Your average is {grade}")
                print("BB")
            elif 70>grade>=50:
                print(f"Your average is {grade}")
                print("CC")
            elif 50>grade>=30:
                print(f"Your average is {grade}")
                print("DD")
            else:
                print(f"Your average is {grade}")
                print("FF")
                print("YOU FAILED!!")
       
        break