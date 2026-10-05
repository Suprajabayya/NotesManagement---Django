# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Note


# HOME
def home(request):
    return render(request, 'home.html')


# DISPLAY ALL NOTES
def notes(request):

    language = request.GET.get('language')

    if language:
        obj = Note.objects.filter(language=language)
    else:
        obj = Note.objects.all()

    return render(
        request,
        'notes.html',
        {'aa': obj}
    )


# ADD NOTE
def addnote(request):

    if request.method == 'POST':

        language = request.POST.get('language')
        topic = request.POST.get('topic')
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if not language or not topic or not question or not answer:

            messages.error(
                request,
                'Please fill all the fields.'
            )

            return render(request, 'addnote.html')

        Note.objects.create(
            language=language,
            topic=topic,
            question=question,
            answer=answer
        )

        messages.success(
            request,
            'Note added successfully!'
        )

        return redirect('notes')

    return render(request, 'addnote.html')


# VIEW ONE NOTE
def viewnote(request, id):

    obj = get_object_or_404(Note, id=id)

    return render(
        request,
        'viewnote.html',
        {'obj': obj}
    )


# UPDATE NOTE
def editnote(request, id):

    obj = get_object_or_404(Note, id=id)

    if request.method == 'POST':

        obj.language = request.POST.get('language')
        obj.topic = request.POST.get('topic')
        obj.question = request.POST.get('question')
        obj.answer = request.POST.get('answer')

        obj.save()

        messages.success(
            request,
            'Note updated successfully!'
        )

        return redirect('notes')

    return render(
        request,
        'editnote.html',
        {'obj': obj}
    )


# DELETE NOTE
def deletenote(request, id):

    obj = get_object_or_404(Note, id=id)

    obj.delete()

    messages.success(
        request,
        'Note deleted successfully!'
    )

    return redirect('notes')