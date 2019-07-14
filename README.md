# INSTRUCCIONES PARA PROBAR EL DESARROLLO

Para poder ver el documento se debe comentariar la línea 22 de la vista (permission_classes = (IsAuthenticated,) para que no tenga en cuenta la seguridad. Adicionalmente, por cualquier nevegador Web se debe ir a la url http://127.0.0.1:8000/ticketpqr.

Para solicitar el Token en línea de comando: http http://localhost:8000/api-token-auth/ username=admin password=ecocapital123

También se puede solicitar el Token ingresando por el explorador Web a la url http http://localhost:8000/admin con las mismas credenciales.

Si se ingresa lo línea de comando con las url y el Token: http http://localhost:8000/ticketpqr/ 'Authorization: Token da6d2b4a3864ac24cc67b1802044c9c5c51a4548' muestra el binario del pdf.
