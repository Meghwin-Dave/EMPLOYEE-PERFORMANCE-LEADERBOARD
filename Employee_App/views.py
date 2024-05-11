from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"index.html")

def number(request):
	num = request.POST["num"]
	return render(request,"data.html",{"data":range(int(num))})

def final_data(request):
	username=request.POST.getlist("username")
	rating=request.POST.getlist("rating")
	employees = []
	for name, rating in zip(username, rating):
		employees.append({"name": name, "performance_rating": float(rating)})
	
	def merge_sort(employees):
		if len(employees) > 1:
			mid = len(employees) // 2
			left_half = employees[:mid]
			right_half = employees[mid:]

			merge_sort(left_half)
			merge_sort(right_half)
			
			i = j = k = 0

			while i < len(left_half) and j < len(right_half):
				if left_half[i]['performance_rating'] > right_half[j]['performance_rating']:
					employees[k] = left_half[i]
					i += 1
				elif left_half[i]['performance_rating'] == right_half[j]['performance_rating']:
					employees[k] = left_half[i]
					i += 1
				else:
					employees[k] = right_half[j]
					j += 1
				k += 1

			while i < len(left_half):
				employees[k] = left_half[i]
				i += 1
				k += 1

			while j < len(right_half):
				employees[k] = right_half[j]
				j += 1
				k += 1

	merge_sort(employees)
	return render(request,"final_data.html",{"data":employees})