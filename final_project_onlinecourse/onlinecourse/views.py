from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course, Enrollment, Lesson, Question, Choice, Submission
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-total_enrollment')[:10]


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail_bootstrap.html'


def check_if_enrolled(user, course):
    is_enrolled = False
    if user.is_authenticated:
        if Enrollment.objects.filter(user=user, course=course).exists():
            is_enrolled = True
    return is_enrolled


def registration_request(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse(viewname='onlinecourse:index'))
        else:
            context['registration_form'] = form
            return render(request, 'onlinecourse/user_registration_bootstrap.html', context)
    else:
        form = UserCreationForm()
        context['registration_form'] = form
        return render(request, 'onlinecourse/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(viewname='onlinecourse:index'))
        else:
            context['message'] = "Invalid user name or password."
            return render(request, 'onlinecourse/user_login_bootstrap.html', context)
    else:
        return render(request, 'onlinecourse/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse(viewname='onlinecourse:index'))


def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    is_enrolled = check_if_enrolled(user, course)
    if not is_enrolled and user.is_authenticated:
        Enrollment.objects.create(user=user, course=course, mode='honor')
        course.total_enrollment += 1
        course.save()

    return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))


def extract_answers(request):
    submitted_answers = []
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse(viewname='onlinecourse:login'))

    enrollment = Enrollment.objects.filter(user=user, course=course).first()
    if not enrollment:
        enrollment = Enrollment.objects.create(user=user, course=course, mode='honor')

    if request.method == 'POST':
        submission = Submission.objects.create(enrollment=enrollment)
        selected_choices = extract_answers(request)
        for choice_id in selected_choices:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)

        return HttpResponseRedirect(
            reverse(viewname='onlinecourse:show_exam_result', args=(course.id, submission.id))
        )

    return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_choices = submission.choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    total_score = 0
    questions = course.question_set.all()
    max_score = sum([question.grade for question in questions])

    for question in questions:
        if question.is_get_score(selected_ids):
            total_score += question.grade

    grade = int((total_score / max_score * 100)) if max_score > 0 else 0

    context = {
        'course': course,
        'grade': grade,
        'total_score': total_score,
        'max_score': max_score,
        'questions': questions,
        'selected_ids': selected_ids
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
