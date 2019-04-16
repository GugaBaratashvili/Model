from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import PostForm
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt, mpld3
#import seaborn as sns
#import matplotlib.animation as animation
from mpl_toolkits.axisartist.axislines import Subplot
import os
from decimal import Decimal



class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ResultPage(TemplateView):
    template_name = 'result.html'


class SimulationPage(TemplateView):
    template_name = 'new_simulation.html'
    NumOfCusts = "1"


    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            Sum_of_Var1_and_Var2 = form.cleaned_data['Min_serving_time_of_the_receptionits']+form.cleaned_data['Max_serving_time_of_the_receptionits']
            NumOfCusts = form.cleaned_data['Number_of_Costomers']
            NumOfRecs = form.cleaned_data['Number_of_Receptionists']
            MinServTime = form.cleaned_data['Min_serving_time_of_the_receptionits']
            MaxServTime = form.cleaned_data['Max_serving_time_of_the_receptionits']
            MinArvTime = form.cleaned_data['MinCustonArrivalTime']
            MaxArvTime = form.cleaned_data['MaxCustonArrivalTime']
            CustSwitchT = form.cleaned_data['CustomerSwitchTime']

        intNumOfCusts = int(NumOfCusts)
        a=np.random.rand(intNumOfCusts)

        b=np.array(range(intNumOfCusts), int)
        L=np.array(range(intNumOfCusts), int)
        q=np.array(range(intNumOfCusts), int)

        def fu(self, request):
            for i in b:
                b[i]=np.random.randint(MinServTime,MaxServTime)
        fu(self, request)

        c=(a+b)/NumOfRecs
        a2=np.random.rand(intNumOfCusts)
        b2=np.array(range(intNumOfCusts), int)

        def fu2(self, request):
            for i in b2:
                b2[i]=np.random.randint(MinArvTime,MaxArvTime)
        fu2(self, request)
        e=a2+b2

        f=np.array(range(intNumOfCusts), float)

        def fu3(self, request):
            f[0]=e[0]
            i=1
            while 0<i<intNumOfCusts:
                f[i]=e[i]+f[i-1]
                i+=1
        fu3(self, request)

        T=CustSwitchT
        g=np.array(range(intNumOfCusts), float)

        def fu4(self, request):
            g[0]=c[0]+e[0]
            i=1
            while 0<i<intNumOfCusts:
                if g[i-1]>e[i]+e[i-1]:
                    g[i]=T+g[i-1]+c[i]

                else:
                    T+e[i]+e[i-1]+c[i]

                i+=1


        fu4(self,request)

        h=np.array(range(intNumOfCusts), float)

        def fu5(self, request):
            h[0]=0
            i=1
            while 0<i<intNumOfCusts:
                h[i]=g[i-1]-f[i]-T
                i+=1
        fu5(self, request)

        z=np.array(range(intNumOfCusts), float)

        def fu6(self, request):
            z[0]=0
            i=1
            while 0<i<intNumOfCusts:
                if h[i]>0:
                    z[i]=h[i]
                else:
                    z[i]=0
                i+=1
        fu6(self, request)


        Label=intNumOfCusts+1
        DAT=range(1,Label,1)
        q=h.tolist()
        TEST = pd.Series(q, DAT)
        #TEST.plot.bar()
        fig, ax = plt.subplots()
        ax.plot(DAT, q)
        ax.set(xlabel='Customer numaration sorted by arrival time', ylabel='Waiting time of a customer (Minutes)',
       title='Your Result')
        RES=mpld3.fig_to_html(fig)
        ax.grid()
        fig.savefig('D:\Model\MyWeb\static\Main\images\myplot.png')



        df=pd.DataFrame(data=q,index=DAT,columns=['The waiting line of each customer'])




        xyz=np.array(range(intNumOfCusts), float)
        def fu7(self, request):
            xyz[0]=0
            i=1
            while 0<i<intNumOfCusts:
                if z[i]>0:
                    xyz[i]=round(Decimal(z[i]), 2)
                else:
                    xyz[i]=0
                i+=1
        fu7(self, request)


        args = {'form':form, 'Sum_of_Var1_and_Var2':Sum_of_Var1_and_Var2,
        'intNumOfCusts':intNumOfCusts, 'a':a, 'b':b, 'a2':a2, 'b2':b2, 'g':g, 'c':c,
        'NumOfCusts':NumOfCusts, 'MinServTime':MinServTime, 'MaxServTime':MaxServTime,
        'h':h, 'e':e, 'f':f, 'z':z, 'L':L, 'xyz':xyz,
        'TEST':TEST, 'DAT':DAT, 'Label':Label, 'q':q, 'df':df, 'fig':fig, 'RES':RES,}
        return render(request, self.template_name, args)



class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

#class SimulationPage(TemplateView):
    #template_name = 'new_simulation.html'
