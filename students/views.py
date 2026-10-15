from django.shortcuts import render, redirect
from .models import Student, Company, Placement
from .forms import StudentForm, CompanyForm, PlacementForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    total_students = Student.objects.count()
    total_companies = Company.objects.count()

    total_placements = Placement.objects.count()
    applied_count = Placement.objects.filter(status="Applied").count()
    shortlisted_count = Placement.objects.filter(status="Shortlisted").count()
    selected_count = Placement.objects.filter(status="Selected").count()
    rejected_count = Placement.objects.filter(status="Rejected").count()

    return render(request, "students/home.html", {
        "total_students": total_students,
        "total_companies": total_companies,
        "total_placements": total_placements,
        "applied_count": applied_count,
        "shortlisted_count": shortlisted_count,
        "selected_count": selected_count,
        "rejected_count": rejected_count,
    })

@login_required
def student_list(request):
    query = request.GET.get("q")
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
    })

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/add_student.html", {
        "form": form
    })

@login_required
def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.course = request.POST["course"]

        student.save()

        return redirect("student_list")

    return render(request, "edit_student.html", {"student": student})


@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

@login_required

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, "students/student_detail.html", {"student": student})

@login_required
def company_list(request):
    query = request.GET.get("q")
    if query:
        companies = Company.objects.filter(name__icontains=query)
    else:
        companies = Company.objects.all()
    return render(request, "students/company_list.html", {
        "companies": companies,
        "query": query,})

@login_required
def add_company(request):

    if request.method == "POST":

        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("company_list")

    else:
        form = CompanyForm()

    return render(request, "students/add_company.html", {
        "form": form
    })

@login_required
def edit_company(request, id):
    company = Company.objects.get(id=id)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = CompanyForm(instance=company)

    return render(request, "students/edit_company.html", {
        "form": form
    })

@login_required
def delete_company(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('company_list')


@login_required
def placement_list(request):

    query = request.GET.get("q")
    status = request.GET.get("status")

    placements = Placement.objects.all()

    if query:
        placements = placements.filter(
            student__name__icontains=query
        ) | placements.filter(
            company__name__icontains=query
        )

    if status:
        placements = placements.filter(status=status)

    return render(request, "students/placement_list.html", {
        "placements": placements,
        "query": query,
        "status": status,
    })

@login_required
def add_placement(request):

    if request.method == "POST":
        form = PlacementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("placement_list")

    else:
        form = PlacementForm()

    return render(request, "students/add_placement.html", {
        "form": form
    })

@login_required
def edit_placement(request, id):

    placement = Placement.objects.get(id=id)

    if request.method == "POST":
        form = PlacementForm(request.POST, instance=placement)

        if form.is_valid():
            form.save()
            return redirect("placement_list")

    else:
        form = PlacementForm(instance=placement)

    return render(request, "students/add_placement.html", {
        "form": form
    })



@login_required
def delete_placement(request, id):

    placement = Placement.objects.get(id=id)

    if request.method == "POST":
        placement.delete()
        return redirect("placement_list")

    return render(request, "students/delete_placement.html", {
        "placement": placement
    })

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(request, "students/login.html", {
                "error": "Invalid username or password."
            })

    return render(request, "students/login.html")



def logout_view(request):
    logout(request)
    return redirect("login")