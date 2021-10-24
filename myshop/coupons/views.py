from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Coupon
from django.views.decorators.http import require_POST
from .forms import CouponApplyForm
from django.contrib import messages

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            messages.warning(request, 'The coupon you have entered does not exist!')
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')