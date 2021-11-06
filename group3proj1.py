def student_status(class_avg, student_score):
    pass_mark = 60
    if student_score >= pass_mark:
        if student_score >= class_avg:
            print(student_name + 'passed with fying colours.')
        elif student_score >= class_avg-5:
            print(student_name+' passed but almost didn;t make it, they got close to the class average of' + class_avg)
        elif student_score < class_avg:
            print(student_name + ' beat pass mark of' + pass_mark + 'but failed to beat class average of' + class_avg)
    elif student_score < pass_mark and student_score >= class_avg:
        print(student_name + 'beat class avg of' +class_avg +'but not pass mark of ' + pass_mark)
    else:
        print(student_name + 'failed')

student_name = input('insert student name: ')
student_score = int(input('insert student mark: '))
class_avg = float(input('input avg: '))
student_status(class_avg,student_score)