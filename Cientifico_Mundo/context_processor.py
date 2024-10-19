def dados_usuario(request):
   return {
      'user': request.user
   }