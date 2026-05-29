from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from .models import GalleryImage, GalleryVideo, GalleryCategory
from .forms import GalleryImageForm, GalleryVideoForm

def gallery(request):
    """Afficher toutes les photos et vidéos"""
    images = GalleryImage.objects.all().order_by('-taken_at', '-uploaded_at')
    videos = GalleryVideo.objects.all().order_by('-uploaded_at')
    
    context = {
        'images': images,
        'videos': videos,
    }
    return render(request, 'gallery/gallery.html', context)

def photo_detail(request, slug):
    """Afficher une photo en détail (comme blog_detail)"""
    photo = get_object_or_404(GalleryImage, slug=slug)
    photo.views += 1
    photo.save()
    
    context = {
        'photo': photo,
    }
    return render(request, 'gallery/photo_detail.html', context)

def video_detail(request, slug):
    """Afficher une vidéo en détail"""
    video = get_object_or_404(GalleryVideo, slug=slug)
    video.views += 1
    video.save()
    
    context = {
        'video': video,
    }
    return render(request, 'gallery/video_detail.html', context)

@staff_member_required
def add_photo(request):
    """Ajouter une photo - comme add_blog"""
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user.get_full_name() or request.user.username
            photo.save()
            messages.success(request, f'✅ Photo "{photo.title}" ajoutée avec succès !')
            return redirect('gallery')
        else:
            messages.error(request, f'❌ Erreur: {form.errors}')
    else:
        form = GalleryImageForm()
    
    return render(request, 'gallery/add_photo.html', {'form': form})

@staff_member_required
def add_video(request):
    """Ajouter une vidéo"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_url = request.POST.get('video_url')
        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')
        category_id = request.POST.get('category')
        
        if not video_url and not video_file:
            messages.error(request, "❌ Veuillez fournir un lien YouTube OU un fichier vidéo.")
            return redirect('add_video')
        
        category = None
        if category_id:
            category = GalleryCategory.objects.get(id=category_id)
        
        video = GalleryVideo(
            title=title,
            description=description,
            video_url=video_url,
            video_file=video_file,
            thumbnail=thumbnail,
            category=category,
            author=request.user.get_full_name() or request.user.username,
        )
        video.save()
        messages.success(request, f'✅ Vidéo "{video.title}" ajoutée avec succès !')
        return redirect('gallery')
    
    categories = GalleryCategory.objects.all()
    return render(request, 'gallery/add_video.html', {'categories': categories})

@staff_member_required
def delete_photo(request, slug):
    """Supprimer une photo (admin uniquement) - comme delete_blog"""
    photo = get_object_or_404(GalleryImage, slug=slug)
    title = photo.title
    photo.delete()
    messages.success(request, f'✅ Photo "{title}" supprimée avec succès !')
    return redirect('gallery')

@staff_member_required
def delete_video(request, slug):
    """Supprimer une vidéo (admin uniquement)"""
    video = get_object_or_404(GalleryVideo, slug=slug)
    title = video.title
    video.delete()
    messages.success(request, f'✅ Vidéo "{title}" supprimée avec succès !')
    return redirect('gallery')
