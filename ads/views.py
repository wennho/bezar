from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render

from ads.models import Ad

class IndexView(generic.ListView):
    template_name = 'ads/index.html'
    context_object_name = 'latest_ad_list'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)        
        if 'q' in self.request.GET:
            context['search'] = self.request.GET['q']
        return context
    
        
    def get_queryset(self):
        
        queryset = Ad.objects
        
        if 'q' in self.request.GET:
            search_words = self.request.GET['q'].strip().split()
            for word in search_words:
                queryset = queryset.filter(title__icontains=word)
        return queryset.order_by('-create_datetime')[:20]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'ads/detail.html'

class CreateView(generic.CreateView):
    model = Ad        
    template_name = 'ads/create.html'    
    def get_success_url(self):
        return reverse('ads:detail', kwargs={'pk':self.object.id})

class UpdateView(generic.UpdateView):
    model = Ad        
    template_name = 'ads/update.html'    
    def get_success_url(self):
        return reverse('ads:detail', kwargs={'pk':self.object.id})

class DeleteView(generic.DeleteView):
    model = Ad
    template_name = 'ads/delete.html'  
    def get_success_url(self):
        return reverse('ads:index')
