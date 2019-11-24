from supplier.models import SupplierProfile, SupplierRating, FuelRequest, FuelUpdate, Offer
from buyer.models import FuelRequest
from django.contrib.auth.models import User


# overall_score = 0
# type_score = 0
# rating_score = 0
# quantity_score = 0


def recommend(fuel_type, amount, user_id, price):
    status = False
    suppliers = FuelUpdate.objects.filter(max_amount__lte=amount, min_amount__gte=amount, fuel_type__icontains=fuel_type)
    if suppliers.count() == 0:
        return status
    else:
        supplier_names = [supplier.supplier.name for supplier in suppliers]
        scores = []
        value = 0
        final = []
        current = 0

        for name in supplier_names:
            supplier_profile = SupplierProfile.objects.get(name=name)
            ratings = SupplierRating.objects.filter(supplier=supplier_profile)
            for rating in ratings:
                value += rating.rating
                scores.append(f'{rating.supplier.name_id} - {value}')
                value = 0

        for score in scores:
            data = score.split('-', 2)
            if data[1] > current:
                current = data[1]
                final.clear()
                final.append(score)

        best = final[0].split('-', 2)
        user = User.objects.get(id=best[0])
        supplier_user = SupplierProfile.objects.get(name=user)
        request_user = FuelRequest.objects.get(id=user_id)

        offer = Offer.objects.create(quantity=amount, supplier=supplier_user, request=request_user, price=price)

        return offer.id


