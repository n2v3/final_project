from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
@api_view(["POST"])
@permission_classes([])
def accept_telegram_message(request):
    print(request.data)
    # Reply for message
    # chat_id = request.data['message']['chat']['id']
    # text = 'Are you still looking for a new job?'
    # send_message(text, chat_id)

    return Response({"status": "OK"})
