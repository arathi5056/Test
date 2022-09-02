from django.shortcuts import render
from django.template import loader
# Create your views here.
from .corelate import get_corelation ,plot_correlation
from django.http import HttpResponse
from .forms import InputForm , MyForm
from .genrategraph import return_graph_Totalcases,return_graph_Totaldeaths,return_grid_IND
from .regression import linearregessionc19
import logging

def index(request):
  return HttpResponse("Hello Geeks")


 
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render

@csrf_exempt 
def loaddata(request):
  form= InputForm(request.POST)
    #if 'submit' in request.POST:
      #form= InputForm(request.POST)
  if form.is_valid():
    datar = form.cleaned_data['geeks_field']
    print(datar)
    if 'submit' in request.POST :
       print('THis is regression')
       datar= linearregessionc19()
       context={
         'datasetname':datar
       }
       template = loader.get_template('home.html')
       return HttpResponse(template.render(context,request))

      #return HttpResponse(template.render(context,request))
    #context={
        # 'dataseturl':datar,
       #  'form':form
      # }
    #template = loader.get_template('responseform.html')
    #return HttpResponse(template.render(context,request))
    #return redirect('/responseform.html')
  return render(request,"loaddata.html",{'form':form})

@csrf_exempt 
def home_view(request):
  form= InputForm(request.POST)
    #if 'submit' in request.POST:
      #form= InputForm(request.POST)
  if form.is_valid():
    datar = form.cleaned_data['geeks_field']
    print(datar)
      #return HttpResponse(template.render(context,request))
    #context={
        # 'dataseturl':datar,
       #  'form':form
      # }
    #template = loader.get_template('responseform.html')
    #return HttpResponse(template.render(context,request))
    #return redirect('/responseform.html')
  return render(request,"home.html",{'form':form})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def responseform(request):
 #if form is submitted
     form = MyForm()
     #if 'do-something-else' in request.POST:
      # return render(request,'home.html')regressionres
     if 'regressionres' in request.POST :
       print('THis is regression')
       datar= linearregessionc19()
       context={
         'linearresult':datar
       }
       template = loader.get_template('regressionresult.html')
       return HttpResponse(template.render(context,request))

     if  'eda' in request.POST:
       
        print('eda is clicked')
        gragh_totaldeaths = return_graph_Totaldeaths()
        gragh_totalcases = return_graph_Totalcases()
        grid_IND =return_grid_IND()
        context = {
          'gragh_totalcases': gragh_totalcases,
            'gragh_totaldeaths':gragh_totaldeaths,
            'grid_IND' :grid_IND
        }
        template = loader.get_template('eda.html')
        return HttpResponse(template.render(context,request))

        

     if  'corelate' in request.POST:
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            #feild_val=myForm.cleaned_data['geeks_field']
            xcsv = myForm.cleaned_data['xcsv']
            ycsv = myForm.cleaned_data['ycsv']
            corr=get_corelation(xcsv,ycsv)
            p_data =plot_correlation(xcsv,ycsv)
            #radio=myForm.cleaned_data['radio']
            #feedback = myForm.cleaned_data['feedback']
            #corr=get_corelation('Total_number_of_students','Positive_cases')
            

            context = {
            'name': xcsv,
            'email': corr,
           'p_data':p_data
            #'feedback': feedback
            }

            template = loader.get_template('thankyou.html')
            

              #returing the template
            return HttpResponse(template.render(context,request))

     
     else:
         form = MyForm()
     #returning form

     return render(request, 'responseform.html', {'form':form});


def delete_product(request):
    template = loader.get_template('thankyou.html')
    if request.method == "Post":
        print('Inside delete')
        
        
    return HttpResponse(template.render(request))

   