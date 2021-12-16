from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from .models import Lead , Agent
from .form import LeadModelForm, CustomUserCreationForm
from django.views import generic

class SignupView(generic.CreateView):
    template_name = "registration/signup.html/"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")
class DashbordView(generic.TemplateView):
    template_name = "dashbord.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "Lead/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "Lead/lead_detail.html/"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "Lead/lead_create.html/"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:home")
    
    def form_valid (self, form):
        send_mail(
            subject=" A Lead has been created",
            message=" Go to site to see new lead ",
            from_email=" test@test.com ",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "Lead/update_lead.html/"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:home")

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
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