def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input("Enter score: "))
print(score, "->", letter_grade(score))


#(b) Why must the test for A+ come before the test for A?

#The test for A+ must come before A because Python checks the conditions from top to bottom. 
# If the test for A comes first, a score of 97 or higher will match A immediately, and Python will never reach the A+ test.

#(c) What happens if you swap them?

#If I swap the tests, scores that should receive A+ will receive A instead.
#  For example, a score of 99 would be graded as A rather than A+.