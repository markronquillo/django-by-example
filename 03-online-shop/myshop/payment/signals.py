from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order


def payment_notification(sender, **kwargs):
	# sender is an instance of PayPalIPN model
	ipn_obj = sender
	# we check if the payment status to make it sure that it is
	# equals to the completed status of django-paypal
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		order = get_object_or_404(Order, id=ipn_obj.invoice)
		order.paid = True
		order.save()
	valid_ipn_received.connect(payment_notification)


