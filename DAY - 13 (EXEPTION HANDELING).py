#Exception Handling
#TRY,EXCEPT
try:
    print(10  + "5")
except:
    print("something went wrong")


try:
    name = input("name here:  ")
    year_born = input("year of birth:  ")
    age = 2026 - year_born
except:
     print('Something went wrong')

#FINALLY

def test_flow():
    try:
        return "From Try"
    finally:
        return "From Finally"
print(test_flow()

try:
    num = int("abc")
    except Exception:
        print("Generic catch")
    expect ValueError:
         print("Specific catch"





