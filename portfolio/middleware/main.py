from django.http import HttpResponseBadRequest


class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        data = None  # Initialize data variable

        if request.method == "POST":
            if "contact" in request.path:
                data = request.POST
            if not self.is_valid(data):
                return HttpResponseBadRequest("invalid data submitted")
        response = self.get_response(request)
        return response

    def is_valid(self, data):
        fields = ["name", "specialization", "phone"]
        for field in fields:
            if field not in data or not data[field]:
                return False

        return True
