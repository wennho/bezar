from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from ads.models import Ad

class IndexView(generic.ListView):
    template_name = 'ads/index.html'
    context_object_name = 'latest_ad_list'

    def get_queryset(self):
        """Return the last 20 published ads."""
        return Ad.objects.order_by('-create_datetime')[:20]


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