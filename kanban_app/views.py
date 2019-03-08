from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Card
from .serializers import CardSerializer, AddCardSerializer


class CardsView(APIView):
    # permission_classes = (IsAuthenticated, )
    permission_classes = (AllowAny,)

    def get(self, request):
        status = request.GET.get('status')
        if status:
            cards = Card.objects.filter(status__iexact=status)
        else:
            cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class AddCardView(APIView):
    permission_classes = (IsAuthenticated, )
    # permission_classes = (AllowAny, )

    def post(self, request):
        # text = request.data.get('text')
        new_card = AddCardSerializer(data=request.data)
        if new_card.is_valid():
            new_card.save(creator=request.user)
            return Response({'state': 'Add'})
        return Response({'state': 'Error'})


class DeleteCardView(APIView):
    permission_classes = (IsAuthenticated, )
    # permission_classes = (AllowAny, )

    def get(self, request):
        card_id = request.GET.get('card_id')
        del_card = Card.objects.get(id=card_id)
        if del_card:
            del_card.delete()
            return Response({'state': 'Deleted'})
        return Response({'state': 'Delete Error'})
