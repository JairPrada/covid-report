from django.utils.deprecation import MiddlewareMixin

FRAME_ANCESTORS = "frame-ancestors 'self' https://*.vercel.app http://localhost:* http://127.0.0.1:*"


class FrameAncestorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = FRAME_ANCESTORS
        return response