from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'base/calculator.html')

def calculate(request):
    if request.method == 'POST':
        number_one = request.POST.get("number_one")
        number_two = request.POST.get("number_two")
        operation = request.POST.get("operation")

        if number_one and number_two:
            number_one, number_two = float(number_one), float(number_two)

            if operation == "add":
                result = number_one + number_two
            elif operation == "subtract":
                result = number_one - number_two
            elif operation == "multiply":
                result = number_one * number_two
            elif operation == "divide":
                result = number_one / number_two if number_two != 0 else "Error (Division by Zero)"
            else:
                result = "Invalid Operation"
        else:
            result = "Error"

        return render(request, "base/calculator.html", {'result': result})
    else:
        return HttpResponse("Invalid Request")







# from django.shortcuts import render
# from django.http import HttpResponse

# def main(request):
#     return render(request, 'base/calculator.html')

# def calculate(request):
#     if request.method == 'POST':
#         number_one = request.POST.get("number_one")
#         number_two = request.POST.get("number_two")
#         operation = request.POST.get("operation")

#         try:
#             num1 = float(number_one)
#             num2 = float(number_two)
#         except ValueError:
#             return render(request, "base/calculator.html", {"result": "Invalid Input!"})

#         # Perform calculation
#         result = None
#         if operation == "add":
#             result = num1 + num2
#         elif operation == "subtract":
#             result = num1 - num2
#         elif operation == "multiply":  
#             result = num1 * num2
#         elif operation == "divide":
#             result = "Cannot divide by zero!" if num2 == 0 else num1 / num2
#         else:
#             result = "Invalid Operation!"

#         return render(request, "base/calculator.html", {"result": result})

#     return render(request, "base/calculator.html")  
