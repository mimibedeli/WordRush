import sys

def dog_years(age):
    return (
        0 if age == 0 else 
        15 if age == 1 else
        24 if age == 2 else
        24 + 5 * (age - 2)
    )
    
def main(age):
    human_years = dog_years(age)
    print(f"A {age}-year old dog is equivalent to a {human_years}-year-old"
          f" person")
    
if __name__ == "__main__":
    age = int(sys.argv[1])
    main(age)