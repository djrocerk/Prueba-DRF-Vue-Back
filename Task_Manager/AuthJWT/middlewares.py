from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class CustomResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Verificar si la respuesta es de tipo Response de DRF
        if isinstance(response, Response):
            
            # Excluimos las vistas de swagger
            if 'swagger' in request.path:
                return response

            # Excluimos las vistas de redoc
            if 'redoc' in request.path:
                return response
            
            # Verificar si la respuesta original contiene errores
            if response.status_code >= 400:
                # En caso de error, construir el nuevo formato de respuesta con la información del objeto
                formatted_data = {
                    'error': True,
                    'descripcion': response.data.get('detail', ''),
                    'objeto': {}
                }
            else:
                # En caso de éxito, colocar la respuesta original en el nuevo formato
                formatted_data = {
                    'error': False,
                    'descripcion': '',
                    'objeto': response.data
                }

            # Crear una nueva instancia de Response con el nuevo formato
            formatted_response = Response(formatted_data, status=response.status_code)

            # Configurar el renderizador JSON (ajusta esto según tus necesidades)
            renderer = JSONRenderer()
            formatted_response.accepted_renderer = renderer
            formatted_response.accepted_media_type = renderer.media_type
            formatted_response.renderer_context = {}

            # Renderizar la nueva respuesta antes de devolverla
            formatted_response.render()

            return formatted_response

        return response
