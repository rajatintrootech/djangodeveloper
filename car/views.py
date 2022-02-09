from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import CarModel
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from accounts.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class CreateCarView(CreateView):
    model = CarModel
    fields = "__all__"
    success_url = "/"

    def get_form(self):
        """add date picker in forms"""
        from django.forms.widgets import SelectDateWidget

        form = super(CreateCarView, self).get_form()
        form.fields["year"].widget = SelectDateWidget()
        return form


class ListCarView(ListView):
    model = CarModel
    paginate_by = 10

    def get_queryset(self):
        make = self.request.GET.get("make", "")
        object_list = self.model.objects.all()
        if make:
            object_list = object_list.filter(make__icontains=make)
        model = self.request.GET.get("model_name", "")
        if model:
            object_list = object_list.filter(model_name__icontains=model)
        year = self.request.GET.get("year", "")
        if year:
            object_list = object_list.filter(year__year=model)
        return object_list


class DetailCarView(DetailView):
    model = CarModel


class UpdateCarView(UpdateView):
    model = CarModel
    fields = "__all__"
    success_url = "/"

    def get_form(self):
        """add date picker in forms"""
        from django.forms.widgets import SelectDateWidget

        form = super(UpdateCarView, self).get_form()
        form.fields["year"].widget = SelectDateWidget()
        return form


class DeleteCarView(DeleteView):
    model = CarModel
    fields = "__all__"
    success_url = "/"


@login_required
def BuyCarView(request, pk):
    if request.method == "POST":
        cardata = CarModel.objects.get(id=pk)
        orders = User.objects.filter(id=request.user.id).first()
        if not orders.orders:
            orders.orders = list(
                dict(make=cardata.make, id=cardata.id, model_name=cardata.model_name)
            )
        else:
            orders.orders.append(
                dict(make=cardata.make, id=cardata.id, model_name=cardata.model_name)
            )
        orders.save()
        CarModel.objects.filter(id=pk).update(sold=True)
        subject = f"Thank you for buy car {cardata.make},{cardata.model_name}"
        message = str(
            dict(
                orderid=cardata.id,
                model=cardata.model_name,
                make=cardata.make,
                seller=cardata.Seller_Info.username,
                seller_mobile=cardata.Seller_Info.phone_no,
                price=cardata.asking_price,
            )
        )
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            request.user.email,
        ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(
            request,
            "car sucessfully purchased and please check your inbox for extra details",
        )
        return redirect("detail", pk)
    else:
        cardata = CarModel.objects.get(id=pk)
        return render(request, "buy_confirm.html", {"data": cardata})


@login_required
def MakeAvailable(request, pk):
    CarModel.objects.filter(id=pk).update(sold=False)
    return redirect("/")
