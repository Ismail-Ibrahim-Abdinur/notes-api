from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes."
        },
        {
            "Endpoint": "/notes/<int:id>/",
            "method": "GET",
            "body": None,
            "description": "Returns a single object of note."
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": None,
            "description": "Creates a note."
        },
        {
            "Endpoint": "/notes/edit/<int:id>/",
            "method": "PUT",
            "body": None,
            "description": "Updates a single note."
        },
        {
            "Endpoint": "/notes/delete/<int:id>/",
            "method": "GET",
            "body": None,
            "description": "Deletes a single note."
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = serializers.NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, id):
    notes = Note.objects.get(id=id)
    serializer = serializers.NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body'],    
        user = data['user'],
        status = data['status'],
    )
    serializer = serializers.NoteSerializer(note)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, id):
    note = Note.objects.get(id=id)
    serializer = serializers.NoteSerializer(note, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response("Note was deleted")
