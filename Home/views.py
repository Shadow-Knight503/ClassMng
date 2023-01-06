from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from .models import UserProf, CodeProb, Code, Status
from .forms import CreateUser, UserProfPage, CodeSubForm, LoginUser
from django.contrib import messages


# Create your views here.
def data(request):
    us_id = request.user.id
    users = UserProf.objects.get(User_id=us_id)
    url = users.Profile_pic.url
    name = users.Name
    roll = users.RollNo
    return url, name, roll


def home(request):
    if request.user.is_authenticated:
        func = data(request)
        code_probs =[]
        code_problems = CodeProb.objects.all()
        for cd_prb in code_problems:
            code = Code.objects.filter(Problem=cd_prb, Author=UserProf.objects.get(User=request.user))
            print(code)
            if not code:
                code_probs.append(cd_prb)
        ctx = {
            "AllProblems": code_problems,
            "CodeProblems": code_probs,
            "Url": func[0],
            "Name": func[1],
            "User": request.user,
        }
        return render(request, "Home.html", ctx)
    else:
        return HttpResponse("Create or Login")


def codes(request, code_id):
    func = data(request)
    code_problem = CodeProb.objects.get(id=code_id)
    code_form = CodeSubForm()
    user_list = {}
    for user in UserProf.objects.all().order_by('RollNo'):
        status = Status.objects.filter(UserAsg=user, Prblm=code_problem)
        if not status:
            status = None
        else:
            status = 1
        user_list[user] = status
    if request.method == "POST":
        code_form = CodeSubForm(request.POST, request.FILES)
        if code_form.is_valid():
            code_sub = code_form.save(commit=False)
            code_sub.Author = UserProf.objects.get(User=request.user)
            code_sub.Problem = code_problem
            code_sub.save()
            status = Status()
            status.UserAsg = UserProf.objects.get(User=request.user)
            status.Prblm = code_problem
            status.save()
            messages.error(request, code_form.errors)
            return redirect('Home Page')
    print(user_list)
    ctx = {
        "CodeProblem": code_problem,
        "CodeForm": code_form,
        "User": request.user,
        "User_List": user_list,
        "Url": func[0],
        "Name": func[1],
        "Roll": func[2],
    }
    return render(request, "CodeProb.html", ctx)


def register(request):
    profiles = UserProfPage()
    forms = CreateUser()
    if request.method == 'POST':
        profiles = UserProfPage(request.POST, request.FILES)
        forms = CreateUser(request.POST)
        if forms.is_valid() and profiles.is_valid():
            forms.password2 = None
            user = forms.save(commit=False)
            # username = forms.cleaned_data.get('username')
            # user.username = username
            user.save()
            profile = profiles.save(commit=False)
            profile.User = user
            profile.save()
            messages.success(request, "Account was successfully created")
            messages.error(request, forms.errors, profiles.errors)
            return redirect('Login Page')
        else:
            print(forms.errors)
            print(profiles.errors)
    ctx = {
        'forms': forms,
        'profiles': profiles,
        'user': request.user,
    }
    return render(request, "Register.html", ctx)


def login_user(request):
    forms = LoginUser()
    ctx = {'forms': forms}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home Page')
        else:
            messages.info(request, "Username or Password is Incorrect")
    return render(request, "Login.html", ctx)


def logout_user(request):
    logout(request)
    return redirect('Home Page')
