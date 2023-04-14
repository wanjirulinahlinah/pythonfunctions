def my_country(country="Rwanda"):
    print(f"Hello from {country}")

    def great(*names):
    for name in names:
        print(f"Hello {name}")
def sum(*numbers):
    output=0
    for number in numbers:
        output+=number
    return output
def multiplication(*nambari):
    answer=1
    for namb in nambari:
        answer*=namb
    return answer
def student_att(**kwags):
    for key,value in kwags.items():
        print(f"{key}:{value}")
def concatenate_args(*argss):
    strs=""
    for arg in argss:
        strs+=arg
    return strs
def concatenate_kwargs(**kwargs):
    answer = ""
    for key,value in kwargs.items():
        answer+=value
    return answer




















