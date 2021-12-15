from django.shortcuts import render, redirect, reverse
from .models import Lead , Agent
from .form import LeadModelForm
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView



#LIST OF LEADS

class LeadListView(ListView):
    template_name = "Lead/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "Lead/lead_detail.html/"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "Lead/lead_create.html/"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:home")

class LeadUpdateView(UpdateView):
    template_name = "Lead/update_lead.html/"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:home")


class LeadDeleteView(DeleteView):
    template_name = "Lead/delete_lead.html/"
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:home")





# #CREATE LEAD
# def lead_create (request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")

#     context = {
#         "form" : form
#     }
#     return render(request, "Lead/lead_create.html", context)


# #LEAD DETAILS
# # def lead_detail (request, id):
# #     lead = Lead.objects.get(id=id)
# #     context = {
# #         "lead" : lead
# #     }
# #     return render(request, "Lead/lead_detail.html", context)



# #UPDATE LEAD
# def update_lead (request, id):
#     lead = Lead.objects.get(id=id)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form" : form,
#         "lead" : lead
#     }
#     return render(request, "Lead/update_lead.html", context)



# # DELETE LEAD
# def delete_lead (request, id):
#     lead = Lead.objects.get(id=id)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             lead.delete()
#             return redirect("/leads")
#     context = {
#         "form" : form,
#         "lead" : lead
#     }
#     return render(request, "Lead/delete_lead.html", context)