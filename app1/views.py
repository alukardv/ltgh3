from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView
from django.views import View


from app1.forms import QuestionForm, UsersTGForm
from app1.models import Question, UserTG, Region, TypeOfUser, VeteransAssistant


def main(request):
    data = {
        'title': 'Main',
    }
    return render(request, 'app1/index.html', data)




class UsersView(View):
    template_name = 'app1/users.html'

    def get(self, request, *args, **kwargs):
        form = UsersTGForm(request.GET)
        return self.render_users_tg(request, form)

    def post(self, request, *args, **kwargs):
        form = UsersTGForm(request.POST)
        if form.is_valid():
            queryset = UserTG.objects.all()
            if form.cleaned_data['full_name']:
                queryset = queryset.filter(full_name__icontains=form.cleaned_data['full_name'])
            if form.cleaned_data['phone_number']:
                queryset = queryset.filter(phone_number__icontains=form.cleaned_data['phone_number'])
            if form.cleaned_data['date_of_birth']:
                queryset = queryset.filter(date_of_birth=form.cleaned_data['date_of_birth'])
            if form.cleaned_data['region']:
                queryset = queryset.filter(region=form.cleaned_data['region'])
            if form.cleaned_data['type_of_user']:
                queryset = queryset.filter(type_of_user=form.cleaned_data['type_of_user'])
            if form.cleaned_data['time_create']:
                queryset = queryset.filter(time_create__gte=form.cleaned_data['time_create'])
            users_tg = queryset
        else:
            users_tg = UserTG.objects.all()

        return self.render_users_tg(request, form, users_tg)

    def render_users_tg(self, request, form, users_tg=None):
        if users_tg is None:
            users_tg = UserTG.objects.all()
        return render(request, self.template_name, {'title': 'Users', 'users_tg': users_tg, 'form': form})


class QuestionListView(View):
    template_name = 'app1/question.html'

    def get(self, request, *args, **kwargs):
        form = QuestionForm(request.GET)
        return self.render_questions(request, form)

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            queryset = Question.objects.all()
            if form.cleaned_data['veterans_assistant']:
                queryset = queryset.filter(veterans_assistant=form.cleaned_data['veterans_assistant'])
            if form.cleaned_data['user_gt']:
                queryset = queryset.filter(user_gt=form.cleaned_data['user_gt'])
            if form.cleaned_data['text_question']:
                queryset = queryset.filter(text_question__icontains=form.cleaned_data['text_question'])
            if form.cleaned_data['time_create']:
                queryset = queryset.filter(time_create__gte=form.cleaned_data['time_create'])
            questions = queryset
        else:
            questions = Question.objects.all()

        return self.render_questions(request, form, questions)

    def render_questions(self, request, form, questions=None):
        if questions is None:
            questions = Question.objects.all()
        return render(request, self.template_name, {'title': 'Question', 'questions': questions, 'form': form})


def about(request):
    data = {
        'title': 'About',
    }
    return render(request, 'app1/about.html', data)


def page_not_found(request, exception):
    msg = """<title>404</title>
             <style>* { font-family: consolas, monospace; }</style>
             <h1><b>404 PAGE NOT FOUND</b><h1>"""
    return HttpResponseNotFound(msg)
