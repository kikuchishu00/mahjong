from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import SignUpForm
from .forms import DataAddForm
from django.urls import reverse_lazy
from . import models
from . import graph
from rest_framework import viewsets
from django.http import HttpResponse
from .serializer import StatsSerializer
# Create your views here.



class IndexView(TemplateView):
    template_name="index.html"

class DataAddView(CreateView):
    template_name='add.html'
    form_class=DataAddForm
    success_url=reverse_lazy('show')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user1 = models.User.objects.get(pk=self.request.user.id)
        form.fields["user"].initial=user1
        return form

class DataShowView(ListView):
    template_name="show.html"
    model = models.Stats
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["stats_list"] = models.Stats.objects.filter(user=self.request.user.id).order_by('date')
        return ctx

class DataTopView(ListView):
    template_name="top.html"
    model = models.Stats
    def get_context_data(self, **kwargs) :
        ctx=super().get_context_data(**kwargs)
        usedata = models.Stats.objects.filter(user=self.request.user.id).order_by('date')
        GameNumber=0
        AvarageRank=0
        RankPoints=0
        BasePoints=0
        TotalPoints=0
        SumFirst=0
        SumSecond=0
        SumThird=0
        SumFourth=0
        GraphX = []
        GraphY = []
        for data in usedata:
            GameNumber+=data.counts
            AvarageRank+=data.first+data.second*2+data.third*3+data.fourth*4
            RankPoint=(data.first*45+data.second*5+data.third*(-15)+data.fourth*(-35))
            RankPoints+=RankPoint
            BasePoints+=data.points-RankPoint
            TotalPoints+=data.points
            SumFirst+=data.first
            SumSecond+=data.second
            SumThird+=data.third
            SumFourth+=data.fourth
            GraphX.append(data.date)
            if len(GraphY)==0:
                GraphY.append(data.points)
            else:
                GraphY.append(GraphY[-1]+data.points)
        chart=graph.Plot_Graph(GraphX,GraphY)
        if GameNumber!=0:
            AvarageRank/=GameNumber
        ctx["chart"]=chart
        ctx["GameNumber"]=GameNumber
        ctx["TotalPoints"]=round(TotalPoints,2)
        ctx["AvarageRank"]=round(AvarageRank,3)
        ctx["RankPoints"]=round(RankPoints,3)
        ctx["BasePoints"]=round(BasePoints,2)
        ctx["SumFirst"]=SumFirst
        ctx["SumSecond"]=SumSecond
        ctx["SumThird"]=SumThird
        ctx["SumFourth"]=SumFourth
        return ctx

class DataUpdateView(UpdateView):
    template_name='update.html'
    model=models.Stats
    form_class=DataAddForm
    success_url=reverse_lazy('show')
    # fields=["date","counts","points","first","second","third","fourth"]

class DataDeleteView(DeleteView):
    template_name='delete.html'
    model=models.Stats
    success_url=reverse_lazy('show')

class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class= SignUpForm
    success_url=reverse_lazy('login')

class StatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer
    def get_queryset(self):
        queryset = models.Stats.objects.filter(user=self.request.user.id).order_by('date')
        return queryset