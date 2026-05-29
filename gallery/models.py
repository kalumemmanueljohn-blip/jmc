from django.db import models
from django.utils.text import slugify

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL personnalisée")
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL personnalisée")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='gallery/', verbose_name="Image")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    taken_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de l'événement")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="À la une")
    
    # Comme le blog
    author = models.CharField(max_length=100, verbose_name="Auteur", default='Administrateur')
    views = models.IntegerField(default=0, verbose_name="Vues")
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['-taken_at', '-uploaded_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while GalleryImage.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class GalleryVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL personnalisée")
    description = models.TextField(blank=True, verbose_name="Description")
    video_url = models.URLField(blank=True, null=True, verbose_name="Lien YouTube/Vimeo")
    video_file = models.FileField(upload_to='gallery/videos/', blank=True, null=True, verbose_name="Fichier vidéo (MP4)")
    thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True, null=True, verbose_name="Miniature")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="À la une")
    
    # Comme le blog
    author = models.CharField(max_length=100, verbose_name="Auteur", default='Administrateur')
    views = models.IntegerField(default=0, verbose_name="Vues")
    
    class Meta:
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"
        ordering = ['-uploaded_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while GalleryVideo.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_video_id(self):
        """Extrait l'ID d'une vidéo YouTube"""
        if self.video_url:
            if 'youtu.be' in self.video_url:
                return self.video_url.split('/')[-1]
            elif 'youtube.com' in self.video_url:
                return self.video_url.split('v=')[-1].split('&')[0]
        return None
    
    def get_embed_url(self):
        """Retourne l'URL embed pour YouTube"""
        video_id = self.get_video_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
